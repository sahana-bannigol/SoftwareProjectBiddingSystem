"""swpbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientegy.views import home,client_registration,freelancer_registration,login,post_project,posted_project,project_view_client,project_delete,dev_posted_projects,project_view_dev,applied_projects,self_dev_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('client_registration/',client_registration),
    path('freelancer_registration/',freelancer_registration),
    path('login/',login),
    path('client_post_project/<int:client_id>/',post_project),
    path('client_posted_projects/<int:client_id>/',posted_project),
    path('viewproject_client/<str:projectAndUser>/',project_view_client),#views details of the posted project of the client
    path('delete_project/<str:projectAndUser>/',project_delete),
    path('view_all_projects_dev/<int:dev_id>/',dev_posted_projects),
    path('view_project_dev/<str:projectAndUser>/',project_view_dev),
    path('applied_projects/<int:dev_id>/',applied_projects),
    path('self_profile_dev/<int:dev_id>/',self_dev_profile)
    
    
]
