from django.contrib import admin
from characters.models import Character
from characters.models import Universe

# Register your models here.
@admin.register(Character)
@admin.register(Universe)


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    list_display_links = ('id',)

class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    list_display_links = ('id',)
