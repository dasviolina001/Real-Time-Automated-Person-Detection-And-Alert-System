from django.contrib import admin
from .models import Person, LiveFaceGuard #Alert
import subprocess
import os
from django.http import HttpResponse
from django.urls import path

class LiveFaceGuardAdmin(admin.ModelAdmin):
    change_list_template = "admin/live_face_guard/change_list.html"  # Ensure this template is used

    def has_add_permission(self, request):
        return False  # Disable the "Add" option

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('detect/', self.detect_faces, name='detect_faces'),
        ]
        return custom_urls + urls

    def detect_faces(self, request):
        try:
            # Path to your 'run_detection.py' file inside the Django folder
            detection_script_path = os.path.join(os.getcwd(), 'run_detection.py')  # Modify path if needed
            subprocess.run(["python", detection_script_path], check=True)  # Run the detection script
            return HttpResponse("Detection started successfully!", content_type="text/plain")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Error: {e}", content_type="text/plain")

# Register the LiveFaceGuard model with its custom admin
admin.site.register(LiveFaceGuard, LiveFaceGuardAdmin)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'details')  # Display name and details in the admin list view

#@admin.register(Alert)
#class AlertAdmin(admin.ModelAdmin):
    #list_display = ('person', 'location', 'timestamp', 'is_sent')
    #list_filter = ('is_sent', 'timestamp')

    #def has_add_permission(self, request):
        # This completely removes the +Add button
        #return False
