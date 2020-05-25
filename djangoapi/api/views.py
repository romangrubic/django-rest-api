from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewd or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# # Make a get request to get the latest position of the international space station from the opennotify api.
# response = requests.get("https://django-api-romangrubic.herokuapp.com/users/1")
# # Print the status code of the response.
# data = response.json()
# print(type(data))
# print(data)