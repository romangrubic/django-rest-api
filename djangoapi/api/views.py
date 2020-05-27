from .models import Python, JavaScript, HTML
from rest_framework import viewsets, permissions
from .serializers import  PythonSerializer, JavaScriptSerializer, HTMLSerializer
from django.shortcuts import render


class PythonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows only GET request for Python
    """
    queryset = Python.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PythonSerializer


class JavaScriptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows only GET for JavaScript
    """
    queryset = JavaScript.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = JavaScriptSerializer


class HTMLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows only GET for HTML
    """
    queryset = HTML.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HTMLSerializer


def index(request):
    """Return the index.html file"""
    return render(request, "index.html")


def documentation(request):
    """Return the documentatin.html file"""
    return render(request, "documentation.html")
