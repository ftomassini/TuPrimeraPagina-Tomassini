from django.urls import path
from . import views  # Importamos las vistas definidas en `views.py`

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('add_author/', views.add_author, name='add_author'),  # Formulario para agregar autores
    path('add_post/', views.add_post, name='add_post'),  # Formulario para agregar publicaciones
    path('search_posts/', views.search_posts, name='search_posts'),  # Página de búsqueda
    path('add_editorial/', views.add_editorial, name='add_editorial'),
]
