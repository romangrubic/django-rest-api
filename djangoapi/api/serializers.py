from django.contrib.auth.models import User, Group
from .models import Python, JavaScript
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']
        read_only_Fields = ('id', 'url',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']
        read_only_Fields = ('id', 'url',)


class PythonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Python
        fields = ['id', 'url', 'question', 'answer', 'link', 'question_created']
        read_only_Fields = ('id', 'url',)


class JavaScriptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JavaScript
        fields = ['id', 'url', 'question', 'answer', 'link', 'question_created']
        read_only_Fields = ('id', 'url')