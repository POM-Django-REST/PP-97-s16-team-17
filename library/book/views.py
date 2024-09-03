from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required(login_url='/login/')
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})

@login_required(login_url='/login/')
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})

@login_required(login_url='/login/')
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})