from django.urls import path

from .views import HomePageView, TodoListView, CreateTodoView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todos/', TodoListView.as_view(), name='todos'),
    path('create/', CreateTodoView.as_view(), name='create')
]
