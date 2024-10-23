from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "index.html", {"Name": "Muhammad Ali Murtaza"});


def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    return render(request, "result.html", {"result": val1 + val2})
