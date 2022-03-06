from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'tag', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tag'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username',
                'id': 'elder'
            }),
            # 'author': forms.Select(attrs={
            #     'class': 'form-control',
            # }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Body'
            }),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'tag', 'body']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
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