from django.shortcuts import render
from django.http import HttpResponse
from AppFour.models import Topic,Webpage,AccessRecord
# Create your views here.
def index(request):
    webpage_list=AccessRecord.objects.order_by('date')
    my_dict={'Access_Record':webpage_list}
    help_dict={'insert_here':"Help is on the way from views.py"}
    return render(request,'AppFour\help.html',context=my_dict)
