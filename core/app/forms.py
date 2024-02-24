from django import forms
from .models import Post, Category, Author

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','author','category']


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'surname', 'sex', 'date_of_birth']

    
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']
