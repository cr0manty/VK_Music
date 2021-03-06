from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.db.models import Q

from api.serializers import StandardResultsSetPagination
from core.views import AmountModelViewSet
from .serializers import SongListSerializer
from songs.models import Song

from api.models import IsFriend
from core.models import Log, VKAuthMixin
from songs.tasks import get_user_songs


class SearchSongsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = SongListSerializer

    def get_query(self):
        search = self.request.GET.get('search', '')

        if search:
            yesterday = timezone.now() - timezone.timedelta(days=1)
            return Q(Q(artist__istartswith=search) | Q(
                title__istartswith=search)) & Q(Q(updated_at__gte=yesterday) | Q(ignore_time=True))
        return Q()

    def get_queryset(self):
        return Song.objects.filter(self.get_query())


class FriendsSongsView(SearchSongsView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsFriend)

    def get_query(self):
        user_id = self.kwargs.get('id')
        query = super().get_query()

        if user_id:
            query &= Q(users__id=user_id)
        return query


class RemoveSongFromUser(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, song_id):
        try:
            song = Song.objects.get(song_id=song_id, users=request.user)
            song.ignore_user(request.user)
            return Response(status=201)
        except Song.DoesNotExist:
            return Response(status=404)


class AddSongFromUser(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, song_id):
        try:
            song = Song.objects.get(song_id=song_id)
            if request.user in song.users.all():
                return Response(status=409)
            song.users.add(request.user)
            return Response(status=201)
        except Song.DoesNotExist:
            return Response(status=404)


class UserSongListAPIView(AmountModelViewSet, VKAuthMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Song.objects.all().order_by('song_id')
    serializer_class = SongListSerializer
    pagination_class = StandardResultsSetPagination

    def get_filter_query(self):
        song_id = self.request.GET.get('song_id', None)
        yesterday = timezone.now() - timezone.timedelta(days=1)
        query = Q(users=self.request.user) & Q(Q(updated_at__gte=yesterday) | Q(ignore_time=True))

        if song_id is not None:
            return query & Q(song_id=song_id)
        return query

    def create(self, request, *args, **kwargs):
        user = request.user
        try:
            self.try_auth(request.POST, user.vk_login, token=user.auth_token)
            if self.captcha_url:
                return Response({'url': self.captcha_url, 'sid': self.captcha_sid}, status=302)

            get_user_songs(user)
            return Response('Success', status=201)
        except Exception as e:
            err_text = 'Cant connect to vk server'
            Log.objects.create(exception=str(e), additional_text=err_text, from_user=user.username)
            return Response(err_text, status=400)


class AddNewLinkSongs(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Song.objects.all().order_by('song_id')
    serializer_class = SongListSerializer
