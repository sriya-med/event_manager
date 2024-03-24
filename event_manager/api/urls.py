from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("event/<int:event_id>", views.event_detail, name="event_detail"),
    path('event/create/', views.event_create, name='event_create'),
]