from django.shortcuts import render

# Create your views here.
def grid():
    return render(request, 'grid.html')