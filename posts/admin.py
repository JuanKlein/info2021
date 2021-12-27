from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
	readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
	readonly_fields=('created','updated')
	list_display = ('titulo', 'autor', 'created')
	list_filter = ('created', 'catergorias')
	search_fields=('autor',)
	

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)