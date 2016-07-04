from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# classes for creating, updating deleting a view.
from django.views.generic.edit import (CreateView, UpdateView, 
                                        DeleteView, FormView)
from .models import Book, Library
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


class BookList(ListView):
    context_object_name = 'Libraries'
    template_name = 'library_home.html'
    queryset = Library.objects.all() # same as writing model = Book

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['book_count'] = Book.objects.all().count()
        return context


# use createView class to create a new object
def new_book(request):
    if request.POST:
        lib_obj = get_object_or_404(Library, lib_type=request.POST['Lib_id'])
        Book.objects.create(title=request.POST['title'],
                            author=request.POST['author'],
                            description=request.POST['description'],
                            year_pub=request.POST['Year_pub'],
                            library=get_object_or_404(Library, pk=lib_obj.pk),
                            )
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'lib_books/new_book.html')


class BookDetail(DetailView):
    template_name = 'lib_books/book_detail.html'
    model = Book

# def book_detail(request, library_pk, book_pk):
#     book = get_object_or_404(Book, library_id=library_pk, pk=book_pk)
#     return render(request, 'lib_books/book_detail.html', {'book':book})

# class NewUserView(FormView):
#     template_name = 'new_registration.html'
#     form_class = UserRegistrationForm

#     # def get(self, request, *args, **kwargs):
#     #     form_class = self.get_form_class()
#     #     form = form_class(request.POST or None)
#     #     return render(request,'lib_books/new_registration.html', {'form':form})


# Had to move 'new_registration.html' inside the Library_proj/templates
# for it to work.
class NewUserView(CreateView):
    form_class = UserRegistrationForm
    model = User
    template_name = 'new_registration.html'



















    