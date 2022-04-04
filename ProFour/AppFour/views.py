from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    help_dict={'insert_here':"Help is on the way from views.py"}
    return render(request,'AppFour\help.html',context=help_dict)
