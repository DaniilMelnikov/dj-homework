from django.contrib import admin
from .models import Phone
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Phone, PostAdmin)