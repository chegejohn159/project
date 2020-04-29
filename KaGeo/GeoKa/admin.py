from django.contrib import admin
from .models import user,Movie,MainCharacter
# Register your models here.

admin.site.register(user)
admin.site.register(Movie)
admin.site.register(MainCharacter)
