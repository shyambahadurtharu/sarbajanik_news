from django.contrib import admin
from content.models import News, Category, Organization, Contact
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name",]
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=["title","sub_description","description","picture","category","news_postion","province","status",]
    exclude = ('view_count',) 
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display=["org_name","logo","address","contact","email","facebook","twiter","instagram","linkdin","youtube"]
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["name","email","subject","message"]
    
    def has_add_permission(self, request):
        # Return True to allow adding objects, False to deny
        return False  # Deny adding objects

    def has_delete_permission(self, request, obj=None):
        # Return True to allow deleting objects, False to deny
        return False  # Deny deleting objects