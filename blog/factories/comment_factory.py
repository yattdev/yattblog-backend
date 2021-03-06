#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker

from blog.models.comment_models import Comment

from .article_factory import ArticleFactory

# Creat fake object
fake = Faker()


class CommentFactory(factory.django.DjangoModelFactory):
    """Factory class for blog:Comment models"""
    class Meta:
        model = Comment
        django_get_or_create = ('comment', )

    name = factory.LazyFunction(fake.unique.name)
    email = factory.LazyFunction(fake.email)
    comment = factory.LazyFunction(fake.unique.text)
    article = factory.SubFactory(ArticleFactory, comments=[])
