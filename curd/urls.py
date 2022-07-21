from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddRecords,name='addrecords'),
    path('show/',views.ShowRecords,name='showrecords'),
    path('update/<int:id>/',views.UpdateRecords,name='updaterecords'),
    path('<int:id>/',views.DeleteRecords,name='deleterecords')
]