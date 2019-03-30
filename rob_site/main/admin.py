
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial, cars
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]}),
        ("links", {'fields' : ['tutorial_links']}),
        ("songs", {'fields' : ['tutorial_song']})
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(cars)

