from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserModel
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def AddRecords(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Added Successfully !')
            form = UserForm()
    else:
        form = UserForm()
    context = {
        'form':form
    }
    return render(request,'add.html',context)

def ShowRecords(request):
    userdata = UserModel.objects.all()
    context = {
        'userdata':userdata
    }
    return render(request,'show.html',context)

def UpdateRecords(request,id):
    if request.method == "POST":
        userdata = UserModel.objects.get(pk=id)
        data = UserForm(request.POST,instance=userdata)
        if data.is_valid():
            data.save()
            messages.success(request,'Data Update Successfully !')
    else:
        userdata = UserModel.objects.get(pk=id)
        data = UserForm(instance=userdata)
    context = {
        'data':data
    }
    return render(request,'update.html',context)

def DeleteRecords(request,id):
    if request.method == "POST":
        userdata = UserModel.objects.get(pk=id)
        userdata.delete()
        return HttpResponseRedirect('/show/')
    else:
        return render(request,'show.html')
