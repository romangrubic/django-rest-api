from .models import Python, JavaScript, HTML, GIT
from rest_framework import serializers


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


class HTMLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HTML
        fields = ['id', 'url', 'question', 'answer', 'link', 'question_created']
        read_only_Fields = ('id', 'url')


class GITSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GIT
        fields = ['id', 'url', 'question', 'answer', 'link', 'question_created']
        read_only_Fields = ('id', 'url')