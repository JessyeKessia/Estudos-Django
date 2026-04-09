from django import forms
from .models import Autor, Editora, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__' 
        widgets = {
            'publicacao': forms.DateInput(attrs={'type': 'date'}),
        }