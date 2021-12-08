from django import forms
from . import models
from bookingem.models import Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            "title",
            "description"
        ]
        widgets = {
            "title":forms.TextInput(attrs={"class": "form-control", "placeholder": "Title of the book"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", )

        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Comment..."})
        }