from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
    d={'movies':[
        {'name1':'Kal Ho Na Ho','year1':2001,'director1':'yash chopra','rating1':7,'genre1':'drama'},
        {'name2':'Dilwale','year2':2014,'director2':'Farah khan','rating2':5,'genre2':'action'},
        {'name3':'Om shanti om','year3':2003,'director3':'gauri khan','rating3':9,'genre3':'history'},
        {'name4':'Main hoon na','year4':1999,'director4':'sunil chopra','rating4':8,'genre4':'war'},
        {'name5':'Jawan','year5':2023,'director5':'atlee','rating5':10,'genre5':'comedy'}
    ]}
    return render(request,'joy.html',d)