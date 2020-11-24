from django.contrib import admin
from clientegy.models import Developer, Client, Project, PSRecord, Final_bid
# Register your models here.
admin.site.register(Developer)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(PSRecord)
admin.site.register(Final_bid)