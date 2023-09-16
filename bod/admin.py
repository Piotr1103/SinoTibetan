from django.contrib import admin
from .models import word

# Register your models here.
class wordAdmin(admin.ModelAdmin):
	list_display = ['id', 'bod', 'han', 'category', 'transliteration', 'pronunciation', 'explanation']

admin.site.register(word, wordAdmin)