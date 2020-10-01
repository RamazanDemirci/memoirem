from django.conf.urls import url
from memories import views

urlpatterns = [
    url(r'^api/matches$', views.memories),
]
