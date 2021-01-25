from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from p_lib.models import Book, Author
from p_lib.forms import BookForm
from django.urls import reverse_lazy

# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'base.html'


class BooksList(ListView):
    model = Book

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        # search
        if get_params.get('q'):
            qs = qs.filter(title__icontains=get_params.get('q'))

        return qs


class AuthorsList(ListView):
    model = Author

class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author


class ContactsView(TemplateView):

    template_name = 'contacts.html'


class BookEdit(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_lib:index')
    template_name = 'book_edit.html'
