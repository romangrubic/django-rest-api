from django.contrib.auth.models import User, Group
from .models import Python, JavaScript
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, PythonSerializer, JavaScriptSerializer
from django.shortcuts import render


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewd or edited
    """
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GroupSerializer


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


def index(request):
    """Return the index.html file"""
    return render(request, "index.html")


def documentation(request):
    """Return the documentatin.html file"""
    return render(request, "documentation.html")
# # Make a get request to get the latest position of the international space station from the opennotify api.
# response = requests.get("https://django-api-romangrubic.herokuapp.com/users/1")
# # Print the status code of the response.
# data = response.json()
# print(type(data))
# print(data)