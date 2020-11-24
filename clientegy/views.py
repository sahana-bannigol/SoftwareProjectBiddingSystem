from django.shortcuts import render
from clientegy.models import Developer,Client


# Create your views here.
def home(request) :
    return render(request, "home.html")

def client_registration(request):
    return render(request,"client_registration.html")

def freelancer_registration(request):
    return render(request,"freelancer_registration.html")

def login(request):
    valid=True
    if request.method=="POST":
        email=request.POST['email']
        try:
            Developer.objects.get(email=email)
        except Developer.DoesNotExist as e:
            try:
                Client.objects.get(email=email)
            except Client.DoesNotExist as e:
                print("Not exists")
                valid=False
            
    return render(request,"login.html",{'valid':valid})