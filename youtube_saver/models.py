from django.db import models


class YoutubePosts(models.Model):
    slug = models.SlugField(blank=True, null=True)
    uploader = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=511, blank=True, null=True)
    creator = models.CharField(max_length=511, blank=True, null=True)
    alt_title = models.CharField(max_length=511, blank=True, null=True)
    duration = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    image = models.TextField(blank=True, null=True)
    artist = models.CharField(max_length=511, blank=True, null=True)
    track = models.CharField(max_length=511, blank=True, null=True)
    album = models.CharField(max_length=511, blank=True, null=True)
    webpage_url = models.URLField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title or super().__str__()

    class Meta:
        verbose_name = 'YoutubePost'
        verbose_name_plural = 'YoutubePosts'
