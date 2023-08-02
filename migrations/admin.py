from django.contrib import admin
from .models import Blog,Contacts,Footer
# Register your models here.

admin.site.site_header = "Blog Application"
admin.site.site_title = "Blog Application"
admin.site.index_title = "Welcome to Blog Application Admin Panel"

class BlogAdmin(admin.ModelAdmin):
    list_display = ("id",'title', 'subheading', 'description')
    fields = ("title",)
    list_editable = ("title","subheading",)
    search_fields = ("title",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contacts)
admin.site.register(Footer)