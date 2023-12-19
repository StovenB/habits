from django.urls import path

from . import views
from .views import get_latest_habit

app_name = 'habits'
urlpatterns = [
    path('', views.index, name='index'),
    path('latest-habit/', get_latest_habit, name='latest_habit'),
    path('<int:habit_id>/', views.detail, name='detail'),
    path('<int:habit_id>/complete/', views.complete, name='complete'),
]
