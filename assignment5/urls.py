from django.urls import path
from puzzle import views

urlpatterns = [
    path('', views.puzzle_view, name='puzzle'),
]
