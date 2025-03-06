from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to pages/urls.py file for more pages.
"""


class MiscPagesView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )

        return context

class LibroListView(ListView):
    model = Libro
    template_name = 'core/libro_list.html'
    context_object_name = 'libros'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'core/libro_detail.html'
    context_object_name = 'libro'

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'descripcion', 'fecha_publicacion', 'autor', 'categoria']
    template_name = 'core/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'descripcion', 'fecha_publicacion', 'autor', 'categoria']
    template_name = 'core/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'core/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')
