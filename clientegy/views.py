from django.shortcuts import render, redirect
from clientegy.models import Developer,Client,Project,PSRecord,Final_bid
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
                dev_id=userd.dev_id
                return redirect(f"/view_all_projects_dev/{dev_id}/")
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

def finalized_project(request,client_id):
    particualarClientproj= Project.objects.filter(client_id=client_id)
    return render(request,'client_finalized_projects.html',{'client_id': client_id,'posts':particualarClientproj})

def project_view_client(request,projectAndUser):
    client_id,projectid=projectAndUser.split('&')
    projectobj=Project.objects.get(project_id=int(projectid))
    bidderListObj= PSRecord.objects.filter(project_id=projectid)
    return render(request,'view_single_project_client.html',{'project':projectobj,'client_id':client_id,'bidders':bidderListObj,'projectid':projectid})

def confirmation(request,projectAndUser):
    dev_id,project_id,client_id=projectAndUser.split('&')
    dev_Obj=Developer.objects.get(dev_id=dev_id)
    projectobj=Project.objects.get(project_id=int(project_id))
    client_Obj = Client.objects.get(client_id = client_id)
    bidderObj= PSRecord.objects.get(dev_id=dev_id , project_id=project_id)
    print(bidderObj.bid_price)
    return render(request,'selected_freelancer_client.html',{'project':projectobj,'client':client_Obj,'bidder':bidderObj,'dev':dev_Obj,'projectid':project_id})

def bill_final(request,projectAndUser):
    client_id,dev_id,project_id = projectAndUser.split('&')
    BidObj = PSRecord.objects.get(dev_id=dev_id , project_id=project_id)
    clientObj = Client.objects.get(client_id = client_id)
    devObj = Developer.objects.get( dev_id = dev_id)
    projectObj = Project.objects.get( project_id = project_id)
    bid_price = BidObj.bid_price
    devObj.dev_selected_flag = True
    projectObj.proj_selected_flag = True
    Final_bid.objects.create(dev_id=dev_id, client_id= client_id, bid_price=bid_price, project_id=project_id)
    return render(request,'bill_final.html',{'client':clientObj,'dev':devObj,'project':projectObj,'bid_price':bid_price})


def project_delete(request,projectAndUser):
    client_id,projectid=projectAndUser.split('&')
    projectobj=Project.objects.get(project_id=int(projectid))
    projectobj.delete()
    return redirect(f'/client_posted_projects/{client_id}/')

def dev_posted_projects(request,dev_id):
    devobj=Developer.objects.get(dev_id=dev_id)
    domain=devobj.service
    projectListObj=Project.objects.filter(domain=domain)
    return render(request,'view_all_projects.html',{'projects':projectListObj,'dev_id':dev_id})
    
def project_view_dev(request,projectAndUser):
    if request.method=='POST':
        dev_id,project_id,client_id=projectAndUser.split('&')
        dev_name=Developer.objects.get(dev_id=dev_id).name
        bid_price=request.POST['price']
        PSRecord.objects.create(dev_id=dev_id,client_id=client_id,bid_price=bid_price,project_id=project_id,dev_name=dev_name)
        return redirect(f'/view_project_dev/{dev_id}&{project_id}')
    dev_id,projectid=projectAndUser.split('&')
    projectobj=Project.objects.get(project_id=int(projectid))
    clientObj=Client.objects.get(client_id=projectobj.client_id)
    bidderListObj= PSRecord.objects.filter(project_id=projectid)
    return render(request,'view_single_project_dev.html',{'project':projectobj,'dev_id':dev_id,'client':clientObj,'bidders':bidderListObj,'projectid':projectid})


def applied_projects(request,dev_id):
    listOfAppliedProjects= PSRecord.objects.filter(dev_id=dev_id)
    NameAndPrice=[]
    for i in listOfAppliedProjects:
        lis=[]
        name=Project.objects.get(client_id=i.client_id,project_id=i.project_id).title
        print(name)
        lis.append(name)
        lis.append(i.bid_price)
        lis.append(i.dev_id)
        lis.append(i.project_id)
        NameAndPrice.append(lis)
    return render(request,'applied_projects_dev.html',{'appliedProjects':NameAndPrice,'dev_id':dev_id})

def self_dev_profile(request,dev_id):
    user=Developer.objects.get(dev_id=dev_id)
    return render(request,'self_profile_freelancer.html',{'user':user,'dev_id':dev_id})

def self_client_profile(request, client_id):
    user=Client.objects.get(client_id = client_id)
    return render( request,'self_profile_client.html',{'user':user,'client_id':client_id})

def edit_profile_client(request,client_id):
    user=Client.objects.get(client_id=client_id)
    if request.method=='POST':
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.ph_no=request.POST['phoneNo']
        user.age=request.POST['age']
        user.pass_client=request.POST['password']
        user.save()
        return redirect(f'/self_profile_client/{client_id}/')
    return render(request,'edit_profile_client.html',{'user':user,'client_id':client_id})

def edit_profile_dev(request,dev_id):
    user=Developer.objects.get(dev_id=dev_id)
    if request.method=='POST':
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.ph_no=request.POST['phoneNo']
        user.age=request.POST['age']
        user.pass_dev=request.POST['password']
        user.exp = request.POST['experience']
        user.service= request.POST['service']
        user.cost = request.POST['cost']
        user.save()
        return redirect(f'/self_profile_dev/{dev_id}/')
    return render(request,'edit_profile_dev.html',{'user':user,"dev_id":dev_id})
