from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, \
    DetailView, DeleteView, CreateView
from django.views.generic.edit import FormMixin

from . import models, forms
from bookingem.forms import CommentForm

class BookListView(ListView):
    template_name = "book/book_list.html"
    queryset = models.Books.objects.all()

    def get_queryset(self):
        return models.Books.objects.all()

class BookCreateView(CreateView):
    template_name = "book/book_create.html"
    form_class = forms.BookForm
    success_url = "/"
    queryset = models.Books.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)

class BookDetailView(FormMixin, DetailView):
    template_name = "book/book_detail.html"
    form_class = CommentForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)


    def get_success_url(self):
        return reverse_lazy("book-detail", kwargs={"pk": self.get_object().id})


class BookUpdateView(UpdateView):
    template_name = "book/book_create.html"
    form_class = forms.BookForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("book:book-list")

class BookDeleteView(DeleteView):
    template_name = "book/book_delete.html"

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=id_)

    def get_success_url(self):
        return reverse("book:book-list")

