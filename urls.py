from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request): return HttpResponse("Transport Manager en ligne — ça marche ✅")

urlpatterns = [path("admin/", admin.site.urls), path("", home)]
