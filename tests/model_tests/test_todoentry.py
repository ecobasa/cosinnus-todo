# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.encoding import force_text
from django.utils.timezone import now

from cosinnus.models import CosinnusGroup
from cosinnus_todo.models import TodoEntry


class TodoEntryTest(TestCase):
    todo_title = 'testtodo'

    def setUp(self):
        super(TodoEntryTest, self).setUp()
        self.group = CosinnusGroup.objects.create(name='testgroup')
        self.admin = User.objects.create_superuser(
            username='admin', email=None, password=None)
        self.todo = TodoEntry.objects.create(
            group=self.group, title=self.todo_title, creator=self.admin)

    def test_string_repr(self):
        """
        String representation should be the title
        """
        self.assertEqual(self.todo_title, force_text(self.todo))

    def test_save(self):
        """
        Should set completed on save if completed date is given
        """
        self.assertFalse(self.todo.is_completed)
        self.todo.completed_date = now()
        self.todo.save()
        self.assertTrue(self.todo.is_completed)
