from . import views
from django.urls import path

app_name = "polls"
urlpatterns = [
    path('', views.index, name='polls-index')
]
