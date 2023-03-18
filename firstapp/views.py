from django.shortcuts import render,redirect
from .models import Employees
from django.contrib import messages
# Create your views here.

# edit employee data
def edit(request,id):
    if request.method == "POST":
       employee = Employees.objects.get(pk=id)
       employee.name = request.POST["name"]
       employee.designation = request.POST["designation"]
       employee.age = request.POST["age"]
       employee.gender = request.POST["gender"]
       employee.save()
       messages.success(request, "employee updated successfully")
       return redirect('grid')
    else:
        employee = Employees.objects.get(pk=id)
        gender = ["male","female"]
        return render(request, "edit.html",{"employee":employee,"gender":gender})
