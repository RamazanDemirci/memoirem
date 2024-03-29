from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

import django_js_reverse.views


urlpatterns = [
    path("", lambda request: redirect("/memories/")),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("memories/", include("memories.urls"), name="memories"),
]
