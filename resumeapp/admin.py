from django.contrib import admin

from resumeapp.models import *


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'phone']
    list_display_links = ['name', 'email', 'country']


@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created']
    list_display_links = ['title']


@admin.register(ServisModel)
class ServisAdmin(admin.ModelAdmin):
    list_display = ['icon', 'profession']
    list_display_links = ['icon']


@admin.register(Myskills)
class MyskillsAdmin(admin.ModelAdmin):
    list_display = ['skil_name', 'percent']
    list_display_links = ['skil_name']


@admin.register(OurProjects)
class OurProjects(admin.ModelAdmin):
    list_display = ['direction', 'direction']
    list_display_links = ['direction']


@admin.register(Ourblog)
class OurProjects(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_display_links = ['created']


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'telegram', 'created']
    list_display_links = ['name', 'telegram']


@admin.register(ContactModelMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created']
    list_display_links = ['name', 'email']
