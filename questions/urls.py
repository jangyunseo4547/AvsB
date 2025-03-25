from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    # comment create
    path('<int:question_id>/comments/create/', views.comment_create, name='comment_create'),
    path('random/', views.random_link, name = 'random_link'),

]