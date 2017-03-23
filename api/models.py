# coding: utf-8

from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    created_by = models.ForeignKey(
        User,
        verbose_name='Created by',
        related_name='task_created',
        blank=True
    )

    assigned = models.ForeignKey(
        User,
        verbose_name='assigned',
        related_name='tasks',
        blank=True,
        null=True
    )

    done = models.BooleanField(
        verbose_name="Is done?",
        default=False
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


class Notification(models.Model):
    class Meta:
        verbose_name_plural = "Notifications"

    sender = models.ForeignKey(
        User,
        verbose_name='Sender',
        related_name='notification_sent'
    )

    receiver = models.ForeignKey(
        User,
        verbose_name='Receiver',
        related_name='notifications_received'
    )

    published_date = models.DateField(
        verbose_name='Published date'
    )

    modification_date = models.DateField(
        verbose_name='Modification Date',
        blank=True,
        null=True
    )

    status = models.IntegerField(
        verbose_name='Status',
        default=1
    )

    is_read = models.BooleanField(
        verbose_name='Is read',
        default=0
    )

    target_type = models.CharField(
        verbose_name='Target type',
        max_length=50
    )

    target_id = models.PositiveIntegerField(
        verbose_name='Target ID'
    )

    target_intention = models.CharField(
        verbose_name='Target intention',
        max_length=50
    )

    title = models.CharField(
        verbose_name='Title',
        max_length=255
    )

    text = models.TextField(
        verbose_name='Text',
    )


# Receivers
@receiver(post_save, sender=Task, dispatch_uid="task_saved")
def task_saved(sender, instance, created, *args, **kwargs):
    # If the user creating the task is not the one assigned
    if created and instance.assigned is not None and instance.assigned is not instance.created_by:
        Notification.objects.create(
            sender=instance.created_by,
            receiver=instance.assigned,
            published_date=instance.creation_date,
            target_type="task",
            target_id=instance.id,
            target_intention="create",
            title='You have been assigned to "%s"' % instance.name,
            text=instance.description
        )
    
