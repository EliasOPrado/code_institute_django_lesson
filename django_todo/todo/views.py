from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.


def get_todo_list(request):
    results = Items.objects.all()
    return render(request, "todo_list.html", {'item':results})

