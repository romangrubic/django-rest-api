"""djangoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from djangoapi.api import views
from djangoapi.api.views import index, documentation

router = routers.DefaultRouter()
router.register(r'python', views.PythonViewSet)
router.register(r'javascript', views.JavaScriptViewSet)
router.register(r'html', views.HTMLViewSet)
router.register(r'git', views.GITViewSet)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^documentation/', documentation, name='documentation'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
