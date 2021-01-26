from django import forms
from .models import Comment, Post


class CommentCreateForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'textarea'})
        }


class PostCreateForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = '__all__'