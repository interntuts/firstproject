from django.shortcuts import render,redirect
from .models import Employees
from django.contrib import messages
# Create your views here.

#fetch employee all data
def grid(request):
    employees = Employees.objects.all()
    return render(request, 'grid.html',{"employees":employees})

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

# delete employee
def delete(request,id):
    employee = Employees.objects.get(pk=id)
    if employee:
        delete = employee.delete()
        messages.success(request, "Employee deleted successfully")
        return redirect('grid')
    
    messages.error(request, "Unable to delete")
    return redirect('grid')
