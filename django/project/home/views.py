from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('this is homepage')
    return render(request,'index.html')

def about(request):
    # return HttpResponse('this is about page')
    return render(request,'about.html')

def services(request):
    # return HttpResponse('this is services page')
    return render(request,'services.html')

def userRegisteration(request):
    # return HttpResponse('this is contact page')
    return render(request,'userRegisteration.html')

def userLogin(request):
    return render(request,'userLogin.html')