from django.shortcuts import render, redirect
from faker import Faker
from .forms import VisitorForm
from .models import Visitor, Tours, Guides

# Create your views here.



# https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Georgia.svg/1920px-Georgia.svg.png
def home(request):
    return render(request, 'Home.html' )


def base(request):
    return render(request, 'Base.html')
def kaxeti(request):
    return render(request, 'Kaxeti.html')


def add_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            return redirect('Hello_Georgia:Home')
    else:
        form = VisitorForm()
        return render(request, 'add_visitor.html', {'form': form})
