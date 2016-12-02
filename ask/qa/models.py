# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        '''метод возвращающий последние добавленные вопросы'''
        return self.order_by('-id')

    def popular(self):
        '''метод возвращающий вопросы﻿ отсортированные по рейтингу'''
        return self.order_by('-rating')

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=48)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class Session(models.Model):
    key = models.CharField(max_length=512, unique=True)
    user = models.ForeignKey(User)
    expires = models.DateField()

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'

    def __str__(self):
        return '{} until-> {}'.format(self.user, self.expires)

class Question (models.Model):
    title = models.CharField(max_length=127)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="authors")
    likes = models.ManyToManyField(User, related_name="likes")
    objects = QuestionManager()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def get_absolute_url(self):
        return "/question/%i/" % self.id

    def __str__(self):
        return '{} -> {}'.format(self.author, self.title)

class Answer  (models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return '{} Answer -> {}'.format(self.author, self.question.title)

