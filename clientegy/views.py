from django.shortcuts import render, redirect
from clientegy.models import Developer,Client,Project
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

def post_project(request,client_id):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        domain = request.POST['domain']
        experience_level = request.POST['experience']
        description = request.POST['description']
        range_price = request.POST['cost']
        Project.objects.create(title = project_name,domain =domain, lvl_exp = experience_level, description = description, price_range = range_price,client_id=client_id)
    return render(request,"client_post_project.html",{'client_id': client_id})

def login(request):
    valid=True
    check_password = True
    if request.method=="POST":
        email=request.POST['email']
        entered_password = request.POST['password']
        try:
            userd = Developer.objects.get(email=email)
            if userd.pass_dev == entered_password:
                return render(request, "view_all_projects.html")
            else:
                check_password = False
                return render(request,"login.html",{'check_password':check_password})
                
        except Developer.DoesNotExist as e:
            try:
                userc = Client.objects.get(email=email)
                if userc.pass_client == entered_password:
                    client_id=userc.client_id
                    return redirect(f'/client_post_project/{client_id}/')
                else:
                    check_password = False
                    return render(request,"login.html",{'check_password':check_password})
                    
            except Client.DoesNotExist as e:
                print("Not exists")
                valid=False
            
    return render(request,"login.html",{'valid':valid})


def posted_project(request,client_id):
    particualarClientproj= Project.objects.filter(client_id=client_id)
    return render(request,'client_posted_projects.html',{'client_id': client_id,'posts':particualarClientproj})

def project_view_client(request,projectAndUser):
    client_id,projectid=projectAndUser.split('&')
    projectobj=Project.objects.get(project_id=int(projectid))
    return render(request,'view_single_project_client.html',{'project':projectobj,'client_id':client_id})

def project_delete(request,projectAndUser):
    client_id,projectid=projectAndUser.split('&')
    projectobj=Project.objects.get(project_id=int(projectid))
    projectobj.delete()
    return redirect(f'/client_posted_projects/{client_id}/')
    
