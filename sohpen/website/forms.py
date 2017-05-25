from django import forms
from .models import *

from ckeditor.widgets import CKEditorWidget


class LogInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'id': 'username',
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'id': 'password',

        }))


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = [
            'title',
            'slug',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'title',
            'slug',
            'photo',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = [
            'title',
            'url',
            'priority',
            'active',
            'parent',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SliderForm(forms.ModelForm):

    class Meta:
        model = Slider
        fields = [
            'photo',
            'label',
            'active',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
