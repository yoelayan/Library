"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from web_project.views import SystemView
from .views import MiscPagesView
from . import views

def misc_page(template_name, name):
    return MiscPagesView.as_view(template_name=template_name, name=name)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
    path("pages/misc/error/", misc_page("pages_misc_error.html", "pages-misc-error")),
    path("pages/misc/under_maintenance/", misc_page("pages_misc_under_maintenance.html", "pages-misc-under-maintenance")),
    path("pages/misc/comingsoon/", misc_page("pages_misc_comingsoon.html", "pages-misc-comingsoon")),
    path("pages/misc/not_authorized/", misc_page("pages_misc_not_authorized.html", "pages-misc-not-authorized")),
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro_detail'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete'),
]

handler404 = SystemView.as_view(template_name="pages_misc_error.html", status=404)
handler403 = SystemView.as_view(template_name="pages_misc_not_authorized.html", status=403)
handler400 = SystemView.as_view(template_name="pages_misc_error.html", status=400)
handler500 = SystemView.as_view(template_name="pages_misc_error.html", status=500)
