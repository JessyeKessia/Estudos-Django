from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Autor, Editora, Livro
from ..blog.forms import AutorForm, EditoraForm, LivroForm

# --- CRUD AUTOR ---
class AutorListView(ListView): model = Autor
class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('autor_list')
class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('autor_list')
class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor_list')

# --- CRUD EDITORA ---
class EditoraListView(ListView): model = Editora
class EditoraCreateView(CreateView):
    model = Editora
    form_class = EditoraForm
    success_url = reverse_lazy('editora_list')
class EditoraUpdateView(UpdateView):
    model = Editora
    form_class = EditoraForm
    success_url = reverse_lazy('editora_list')
class EditoraDeleteView(DeleteView):
    model = Editora
    success_url = reverse_lazy('editora_list')

# --- CRUD LIVRO ---
class LivroListView(ListView): model = Livro
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('livro_list')
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('livro_list')
class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('livro_list')