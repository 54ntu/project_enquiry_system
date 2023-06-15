from django.contrib import admin
from app_courses.models import courseModel 

# Register your models here.
class courseModelAdmin(admin.ModelAdmin):
    list_display=("course_name","course_code")
    list_filter=("course_name","course_code")
    search_fields= ("course_name","course_code")

admin.site.register(courseModel,courseModelAdmin)



# customizing admin panel title and name

admin.site.site_header = "student Enquiry system"
admin.site.site_title = "SES"
admin.site.index_title = "admin panel"