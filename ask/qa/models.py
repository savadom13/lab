# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class QuestionManager (models.Manager):
    def new(self):
        '''метод возвращающий последние добавленные вопросы'''
        return self.order_by('-id')

    def popular(self):
        '''метод возвращающий вопросы﻿ отсортированные по рейтингу'''
        return self.order_by('-rating')

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
        return self.title

class Answer  (models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return '{} Answer on {}'.format(self.author, self.question.title)

