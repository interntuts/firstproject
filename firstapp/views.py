from django.shortcuts import render
from .models import Employees
# Create your views here.
def grid():
    employees = Employees.objects.all()
    return render(request, 'grid.html',{"employees":employees})