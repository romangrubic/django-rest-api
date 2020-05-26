from .models import Python, JavaScript
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