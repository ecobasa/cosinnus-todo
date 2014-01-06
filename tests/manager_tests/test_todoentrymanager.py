# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

from cosinnus.models import CosinnusGroup
from cosinnus_todo.managers import TodoEntryManager
from cosinnus_todo.models import TodoEntry


class TodoEntryManagerTest(TestCase):

    def setUp(self):
        super(TodoEntryManagerTest, self).setUp()
        self.group = CosinnusGroup.objects.create(name='testgroup')
        self.admin = User.objects.create_superuser(
            username='admin', email=None, password=None)
        self.todo = TodoEntry.objects.create(
            group=self.group, title='testtodo', created_by=self.admin)

    def test_tags(self):
        tags = ['foo', 'bar']
        for tag in tags:
            self.todo.tags.add(tag)
        manager = TodoEntryManager()
        self.assertEqual(manager.tags(), tags)