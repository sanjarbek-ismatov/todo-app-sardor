from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import ToDo


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class TodoListView(ListView):
    model = ToDo
    template_name = 'todos.html'


class CreateTodoView(CreateView):
    template_name = 'create.html'
    model = ToDo
    fields = ['title', 'text']
