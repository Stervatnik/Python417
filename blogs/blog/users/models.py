from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True, verbose_name="Имя")
    email = models.EmailField(max_length=500, blank=True)
    username = models.CharField(max_length=200, blank=True, verbose_name="Имя пользователя")
    short_intro = models.CharField(max_length=200, blank=True,verbose_name="Краткое описание")
    bio = models.TextField( blank=True, verbose_name="Биография")
    profile_image = models.ImageField(upload_to='profiles/', default="profiles/default.jpg", blank=True, verbose_name="Изображение профиля")
    social_github = models.CharField(max_length=200, blank=True)
    social_youtube = models.CharField(max_length=200, blank=True)
    social_website = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"




class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, verbose_name="Владелец")
    name = models.CharField(max_length=200, blank=True, verbose_name='Название')
    description = models.TextField( blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Умение'
        verbose_name_plural = 'Умения'



class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Отправитель")
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='messages', verbose_name="Получатель")
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Имя")
    email = models.EmailField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True, verbose_name='Предмет')
    body = models.TextField(verbose_name='Описание')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['is_read', '-created']