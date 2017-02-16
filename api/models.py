# coding: utf-8

from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User


RIGHT_ACCESS = (
    ('READ_ONLY', 'Read-only'),
    ('EDIT', 'Edit'),
    ('MANAGE', 'Manage'),
    ('ADMIN', 'Administrateur'),
)


class Project(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'

    name = models.CharField(
        max_length=75,
        verbose_name="Name"
    )

    user = models.ManyToManyField(User, through='Access')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Access(models.Model):
    class Meta:
        verbose_name_plural = 'Access'

    user = models.ForeignKey(
        User,
        verbose_name="User",
        related_name="access"
    )

    project = models.ForeignKey(
        'Project',
        verbose_name="Project",
        related_name="access"
    )

    right = models.CharField(
        choices=RIGHT_ACCESS,
        verbose_name="Right access",
        max_length=50
    )


class Task(models.Model):
    class Meta:
        verbose_name_plural = 'Tasks'

    name = models.CharField(
        max_length=75,
        verbose_name="Name"
    )

    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )

    creation_date = models.DateTimeField(
        verbose_name="Creation date",
        auto_now_add=True,
        null=True
    )

    start_date = models.DateField(
        verbose_name="Start date",
        blank=True,
        null=True
    )

    end_date = models.DateField(
        verbose_name="End date",
        blank=True,
        null=True
    )

    priority = models.PositiveIntegerField(
        verbose_name="Priority",
        blank=True,
        null=True
    )

    labels = models.ManyToManyField(
        'Label',
        verbose_name='Labels',
        related_name='tasks',
        blank=True
    )

    project = models.ForeignKey(
        'Project',
        verbose_name="Project",
        related_name="tasks"
    )

    assigned = models.ForeignKey(
        User,
        verbose_name='assigned',
        related_name='tasks',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Label(models.Model):
    class Meta:
        verbose_name_plural = 'Labels'

    name = models.CharField(
        max_length=75,
        verbose_name="Name"
    )

    color = models.CharField(
        max_length=6,
        verbose_name="Color",
        default="FFFFFF"
    )

    project = models.ForeignKey(
        'Project',
        verbose_name="Project",
        related_name="labels"
    )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class File(models.Model):
    class Meta:
        verbose_name_plural = 'Files'

    name = models.CharField(
        max_length=75,
        verbose_name="Name"
    )

    file = models.FileField(
        verbose_name="File"
    )

    task = models.ForeignKey(
        'Task',
        verbose_name="Task",
        related_name="files"
    )

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'Comments'

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    content = models.TextField(
        verbose_name="Content"
    )

    task = models.ForeignKey(
        'Task',
        verbose_name="Task",
        related_name="comments"
    )

    author = models.ForeignKey(
        User,
        verbose_name="User"
    )

class Kanboard(models.Model):
    class Meta:
        verbose_name_plural = 'Kanboards'

    name = models.CharField(
        max_length=75,
        verbose_name="Name"
    )

    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True
    )

    creation_date = models.DateTimeField(
        verbose_name="Creation date",
        auto_now_add=True,
        null=True
    )

    project = models.ForeignKey(
        Project,
        verbose_name='Project',
        related_name='kanboards'
    )

    def __unicode__(self):
        return self.name


class Column(models.Model):
    class Meta:
        verbose_name_plural = 'Columns'

    name = models.CharField(
        max_length=75,
        verbose_name="Name"
    )

    color = models.CharField(
        max_length=6,
        verbose_name="Color",
        default="FFFFFF"
    )

    labels = models.ManyToManyField(
        Label,
        verbose_name='labels',
        related_name='columns'
    )

    def __unicode__(self):
        return self.name
