from django.contrib import admin
from .models import Python, JavaScript, HTML, GIT


# Register your models here.
admin.site.register(Python)
admin.site.register(JavaScript)
admin.site.register(HTML)
admin.site.register(GIT)
