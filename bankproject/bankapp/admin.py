from django.contrib import admin
from .models import login,register,Branches,District
# Register your models here.
admin.site.register(login)

class BranchesAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Branches,BranchesAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(District,DistrictAdmin)