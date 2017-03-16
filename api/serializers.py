from rest_framework import serializers

from api import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import re
from django.core import exceptions


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active'
        )
        read_only_fields = (
            'id',
            'is_active',
            'email'
        )


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )
        read_only_fields = (
            'id',
            'username'
        )


class AuthCustomTokenSerializer(serializers.Serializer):
    login = serializers.CharField()

    password = serializers.CharField()

    def validate_email(self, email):
        if len(email) > 6:
            if re.match(
                    '[A-Za-z0-1\.-]+'
                    '@[A-Za-z0-1\.-]+'
                    '\.[A-Za-z0-1]{2,4}',
                    email
            ):
                return 1
        return 0

    def validate(self, attrs):
        email_or_username = attrs.get('login')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if self.validate_email(email_or_username):
                email_exist = User.objects.filter(
                    email=email_or_username,
                )

                if not email_exist.count():
                    # Email is not use
                    msg = "This email doesn't have account"
                    raise exceptions.ValidationError(msg)

                email_or_username = email_exist[0].username
            else:
                user_exist = User.objects.filter(
                    username=email_or_username
                ).count()

                if not user_exist:
                    # User doesn't exist
                    msg = "This username doesn't have account"
                    raise exceptions.ValidationError(msg)

            user = authenticate(
                username=email_or_username,
                password=password
            )

            if user:
                if not user.is_active:
                    # User is inactive
                    msg = "This user is inactive"
                    raise exceptions.ValidationError(msg)
            else:
                # Bad password
                msg = "Bad password"
                raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


class KanboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Kanboard
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Column
        fields = '__all__'


class AccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Access
        fields = ('right', 'user', 'project')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'right')

    right = serializers.SerializerMethodField()

    def get_right(self, obj):
        return models.Access.objects.get(
            project=obj,
            user=self.context['request'].user
        ).right

    def create(self, validated_data):
        instance = super(ProjectSerializer, self).create(validated_data)

        models.Access.objects.create(
            user=self.context['request'].user,
            project=instance,
            right='ADMIN'
        )

        return instance


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Label
        fields = '__all__'


class BaseLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Label
        fields = ('name', 'color')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = '__all__'

    labels = BaseLabelSerializer(many=True, read_only=True)

    assigned = UserSerializer(read_only=True)
    assigned_id = serializers.PrimaryKeyRelatedField(
        queryset=models.User.objects.all(), source='user', write_only=True)

    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Project.objects.all(), source='project', write_only=True)


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.File
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'
