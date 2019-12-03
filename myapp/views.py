from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Base.html")

def Child1(request):
    return render(request,"Child1.html")

def Child2(request):
    return render(request,"Child2.html")

def Form_demo(request):
    print(request.GET.get("firstname"))
    print(request.GET.get("textdata"))
    print(request.GET.get("textdata").count(" ")+1)
    #print(request.POST.get("firstname"))
    return render(request,"form_demo.html")