from django.shortcuts import render
from faker import Faker

# Create your views here.

fake = Faker()

posts = [
    {"id": 1, "title": "Kahketi", 'description': fake.text(500)},
    {"id": 2, "title": "Imereti", 'description': fake.text(500)},
    {"id": 3, "title": "Guria", 'description': fake.text(500)}
]

#https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Georgia.svg/1920px-Georgia.svg.png
def home(request):
    return render(request, 'Home.html',{"posts": posts})

