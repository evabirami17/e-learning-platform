from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'course_details.html')
def fc(request):
    return render(request,'freecourse.html')
def eb(request):
    return render(request,'Ebook.html')
def eb1(request):
    return render(request,'index.html')
def eb2(request):
    return render(request,'program_details.html')
def eb3(request):
    return render(request,'programminghub.html')
