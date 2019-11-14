from django.contrib import admin
from .models import ImageUploadModel

# Register your models here.
class image_upload_Admin(admin.ModelAdmin):
    list_display = ('description', 'document','uploaded_at')
    list_fillter = ['uploaded_at']
    search_fields = ['document']

admin.site.register(ImageUploadModel, image_upload_Admin)
