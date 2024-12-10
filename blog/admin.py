from django.contrib import admin
from .models import Author, Post, Editorial

# Registrar modelos en el panel de administración
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Editorial)
