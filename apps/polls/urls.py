from . import views
from django.urls import path

app_name = "polls"
urlpatterns = [
    path('', views.index, name='polls-index'),
    path('<int:question_id>/', views.detail, name='poll-question'),
]
