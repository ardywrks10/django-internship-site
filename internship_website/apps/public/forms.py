from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your comment...', 'rows': 4, 'class': 'form-control'}))