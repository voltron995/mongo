from django import forms
from django.contrib.auth.models import User
from .models import Comment, Entry, UserProfile


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        self.entry = kwargs.pop('entry')   # the blog entry instance
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=False):
        comment = super(CommentForm, self).save(commit=False)
        comment.entry = self.entry
        comment.save()
        return comment

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'body', 'author')

    def __init__(self, *args, **kwargs):
        self.entry = kwargs.pop('entry')   # the blog entry instance
        super(EntryForm, self).__init__(*args, **kwargs)

    def save(self, commit=False):
        entry = super(EntryForm, self).save(commit=False)
        entry.save()
        return entry