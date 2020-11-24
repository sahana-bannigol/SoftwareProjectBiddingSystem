from django.shortcuts import render, redirect
from clientegy.models import Developer,Client
from django.http import HttpResponse


# Create your views here.
def home(request) :
    return render(request, "home.html")

def client_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        ph_no = request.POST['phoneNo']
        password_client = request.POST['password']
        Client.objects.create(name=name , email = email, age= age, ph_no = ph_no, pass_client = password_client)
        print('Client User created successfully!') 
    return render(request,"client_registration.html")

def freelancer_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        ph_no = request.POST['phoneNo']
        password_dev = request.POST['password']
        experience = request.POST['experience']
        print(experience)
        domain = request.POST['service']
        print(domain)
        cost = request.POST['cost']
        print('Freelancer User created successfully!')
        Developer.objects.create(name = name, email = email, age = age, ph_no = ph_no, pass_dev = password_dev, exp = experience, service = domain, cost = cost)
    return render(request,"freelancer_registration.html")

def login(request):
    valid=True
    if request.method=="POST":
        email=request.POST['email']
        try:
            Developer.objects.get(email=email)
            return HttpResponse('Hi! you exist as a developer')
        except Developer.DoesNotExist as e:
            try:
                Client.objects.get(email=email)
                return HttpResponse('Hi! you exist as a client')
            except Client.DoesNotExist as e:
                print("Not exists")
                valid=False
            
    return render(request,"login.html",{'valid':valid})