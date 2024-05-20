from django.shortcuts import render
from django.http import HttpResponse
from content.models import News,Organization
# Create your views here.

def home(request):
    data= News.objects.filter(news_postion="first").filter(status="public").order_by("-id").first()
    second_data= News.objects.filter(news_postion="second").filter(status="public").order_by("-id").first()
    third_data= News.objects.filter(news_postion="third").filter(status="public").order_by("-id").first()
    fourth_data= News.objects.filter(news_postion="forth").filter(status="public").order_by("-id").first()
    org = Organization.objects.order_by('-id').first()
    
    context={
        "data":data,
        "org":org,
        "second_data":second_data,
        "third_data": third_data,
        "fourth_data": fourth_data
    }
    return render(request,"index.html", context)

def contact(request):
    org = Organization.objects.order_by('-id').first()
    
    context={
       
        "org":org
    }
    return render(request, "contact.html",context)