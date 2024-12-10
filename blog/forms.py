from django import forms
from .models import Author, Post, Editorial

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'