from django import forms
from django.forms import Textarea

from . import models
from bookingem.models import Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            "title",
            "description"
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows':5})