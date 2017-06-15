from django.shortcuts import render

def hello(request):
    context = {}
    return render(request,'index.html',context)
