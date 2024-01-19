from django.shortcuts import render,redirect
from .forms import Book
from .models import Books
from django.contrib import messages

# Create your views here.
def index(request):
    data=Books.objects.all()
    context={
        "data" : data,
     }
    return render(request,'index.html',context)
def add(request):
     form = Book(request.POST or None, request.FILES or None)
     if form.is_valid():
        form.save()
        return redirect('index')
     context = {
          'form': form,
     }
     messages.info(request," Hey! Book added sucessfully!")
     return render(request,'addbook.html',context)

def edit(request, id=None):
    edit_book = Books.objects.get(id=id)
    form = Book(request.POST or None, request.FILES or None, instance=edit_book)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    messages.warning(request," Hey! Book Details Edited sucessfully!")
    return render(request,'addbook.html',context)
 

def delete(request,id=None):
    datas = Books.objects.get(id=id)
    if request.method == "POST":
        datas.delete()
        return redirect('index')
    context = {
        'book': datas
    }
    messages.warning(request," Hey! Book deleted sucessfully!")
    return render(request, 'delete.html', context)

    
   


