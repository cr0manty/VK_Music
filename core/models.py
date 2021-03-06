from django.db import models
from vk_api import VkApi


class Log(models.Model):
    from_user = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    exception = models.TextField(blank=True, null=True)
    additional_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.from_user, self.created_at)


class RQLog(models.Model):
    from_user = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_exception = models.BooleanField(default=False)
    exception_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.from_user, self.created_at)


class TelegramBotLogs(models.Model):
    LOG_TYPE = (
        (0, 'Error'),
        (1, 'Not Sended'),
        (2, 'Not Found'),
        (3, 'Success')
    )

    chat_id = models.IntegerField(blank=True)
    group = models.BooleanField(default=False)
    log_type = models.IntegerField(choices=LOG_TYPE, default=0)
    content = models.TextField(blank=True, null=True)
    exception = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_kwargs(message, e='', log_type=0):
        return {
            'chat_id': message.chat.id,
            'group': message.chat.type == 'group',
            'log_type': log_type,
            'content': message.text,
            'exception': e,
            'user_id': message.from_user.id,
            'username': message.from_user.username,
            'language': message.json['from'].get('language_code')
        }

    def __str__(self):
        return '{} ({})'.format(self.username or '', self.created_at)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Telegram Bot Log'
        verbose_name_plural = 'Telegram Bot Logs'


class VKAuthMixin(object):
    captcha_key = None
    captcha_url = None
    captcha_sid = None

    def captcha_handler(self, captcha):
        if self.captcha_key and self.captcha_sid:
            captcha.sid = self.captcha_sid
            self.captcha_sid = None
            return captcha.try_again(self.captcha_key)
        else:
            self.captcha_url, self.captcha_sid = captcha.get_url(), captcha.sid

    def try_auth(self, post, username, password=None, token=None, reauth=True):
        try:
            if not password and not token:
                raise ValueError

            self.captcha_key = post.get('captcha')
            self.captcha_sid = post.get('sid')

            if token:
                vk_session = VkApi(login=username, config_filename='config.json', token=token,
                                   captcha_handler=self.captcha_handler)
            else:
                vk_session = VkApi(login=username, config_filename='config.json', password=password,
                                   captcha_handler=self.captcha_handler)
            vk_session.auth(token_only=token is not None, reauth=reauth)
            return vk_session
        except Exception as e:
            Log.objects.create(exception=e, additional_text=username)
            return None


class TelegramLogs(models.Model):
    chat_id = models.IntegerField()
    is_group = models.BooleanField(default=False)
    user_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=16, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_object(message):
        is_group = message.chat.type == 'group'
        try:
            TelegramLogs.objects.get(chat_id=message.chat.id, user_id=message.from_user.id,
                                     is_group=is_group)
        except TelegramLogs.DoesNotExist:
            TelegramLogs.objects.create(chat_id=message.chat.id, user_id=message.from_user.id,
                                        username=message.from_user.username, is_group=is_group,
                                        language=message.from_user.language_code)
