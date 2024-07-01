from django.test import TestCase

# Create your tests here.
from .models import Visitor

data = Visitor.objects()
print(data)