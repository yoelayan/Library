from django.urls import path
from .views import MiscPagesView
from . import views

urlpatterns = [
    path(
        "pages/misc/error/",
        MiscPagesView.as_view(template_name="pages_misc_error.html"),
        name="pages-misc-error",
    ),
    path(
        "pages/misc/under_maintenance/",
        MiscPagesView.as_view(template_name="pages_misc_under_maintenance.html"),
        name="pages-misc-under-maintenance",
    ),
    path(
        "pages/misc/comingsoon/",
        MiscPagesView.as_view(template_name="pages_misc_comingsoon.html"),
        name="pages-misc-comingsoon",
    ),
    path(
        "pages/misc/not_authorized/",
        MiscPagesView.as_view(template_name="pages_misc_not_authorized.html"),
        name="pages-misc-not-authorized",
    ),
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro_detail'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete'),
    ]
