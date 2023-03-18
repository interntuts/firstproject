from django.shortcuts import render,redirect
from .models import Employees
from django.contrib import messages
# Create your views here.

# add employee data
def add(request):
    if request.method == "POST":
        try:
            form_data = {
            "name": request.POST["name"], 
            "designation": request.POST["designation"], 
            "age": request.POST["age"], 
            "gender": request.POST["gender"], 
            }
            employee = Employees(**form_data)
            employee.save()
            messages.success(request, "Employee added successfully")
        except Exception as e:
            messages.error(request, e)

    return render(request, 'add.html')
