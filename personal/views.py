from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html',{})

def conservation(request):
    return render(request,'personal/conservation.html',{})

def personalityquiz(request):
    return render(request,'personal/personalityquiz.html',{})
