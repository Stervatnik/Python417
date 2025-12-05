from email.policy import default

from django.db import models
from users.models import Profile



class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    featured_image = models.ImageField(upload_to="projects/%Y/%m/%d/", blank=True, verbose_name='Рекомендуемое изображение', default="default.jpg")
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Теги')
    vote_total = models.IntegerField(default=0, verbose_name='Общее количество голосов')
    vote_ratio = models.IntegerField(default=0, verbose_name='Соотношение голосов')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-vote_ratio', '-vote_total', 'title']


    def reviews(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_votes = reviews.count()

        ratio = up_votes / total_votes * 100
        self.vote_total = total_votes
        self.vote_ratio = ratio

        self.save()


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Положительная оценка'),
        ('down', 'Отрицательная оценка'),
    )


    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Владелец')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    body = models.TextField(null=True, blank=True, verbose_name='Описание')
    value = models.CharField(max_length=20, choices=VOTE_TYPE, verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        unique_together = [['owner', 'project']]