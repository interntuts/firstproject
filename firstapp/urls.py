from django.urls import path
from . import views

urlpatterns = [
    path('',views.grid,name="grid"),
    path('add',views.add,name="add"),
    path('delete/<id>',views.delete,name="delete"),
    path('edit/<id>',views.edit,name="edit"),
]