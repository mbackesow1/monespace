# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include  # add this
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from core import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    #path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("monespace/", include("apps.home.urls"))
    #path('monespace/', include('monespace.urls')),# UI Kits Html files
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
