from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tag'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Body'
            }),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'body']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tag'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Body'
            }),
        }