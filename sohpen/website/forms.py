from django import forms
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Your Name',
        }))

    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Your subject',
        }))

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Your Message',
        }))


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


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'id': 'password',
            'placeholder': 'Old Password'

        }))
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'id': 'password',
            'placeholder': 'New Password'

        }))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'id': 'password',
            'placeholder': 'Re-type Password'

        }))

    def clean_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if new_password != confirm_password:
            raise forms.ValidationError("Your passwords do not match")

        return confirm_password


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
            'event_date',
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
            self.fields['parent'].queryset = Menu.objects.filter(
                deleted_at=None)


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


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = [
            'photo',
            'caption',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = [
            'file',
            'name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First Name'})
        self.fields['middle_name'].widget.attrs.update(
            {'placeholder': 'Middle Name (optional)'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last Name'})
        self.fields['fathers_name'].widget.attrs.update(
            {'placeholder': 'Fathers Name'})
        self.fields['dob'].widget.attrs.update(
            {'placeholder': 'Date of Birth (YYYY-MM-DD)'})
        self.fields['permanent_address'].widget.attrs.update(
            {'placeholder': 'Permanent Address'})
        self.fields['mailing_address'].widget.attrs.update(
            {'placeholder': 'Mailing Address'})

        self.fields['degree_1'].widget.attrs.update({'placeholder': 'Degree'})
        self.fields['major_1'].widget.attrs.update({'placeholder': 'Major'})
        self.fields['institution_1'].widget.attrs.update(
            {'placeholder': 'Institution'})
        self.fields['year_1'].widget.attrs.update(
            {'placeholder': 'Year (YYYY)'})

        self.fields['degree_2'].widget.attrs.update(
            {'placeholder': 'Degree (optional)'})
        self.fields['major_2'].widget.attrs.update(
            {'placeholder': 'Major (optional)'})
        self.fields['institution_2'].widget.attrs.update(
            {'placeholder': 'Institution (optional)'})
        self.fields['year_2'].widget.attrs.update(
            {'placeholder': 'Year (YYYY) (optional)'})

        self.fields['degree_3'].widget.attrs.update(
            {'placeholder': 'Degree (optional)'})
        self.fields['major_3'].widget.attrs.update(
            {'placeholder': 'Major (optional)'})
        self.fields['institution_3'].widget.attrs.update(
            {'placeholder': 'Institution (optional)'})
        self.fields['year_3'].widget.attrs.update(
            {'placeholder': 'Year (YYYY) (optional)'})

        self.fields['degree_4'].widget.attrs.update(
            {'placeholder': 'Degree (optional)'})
        self.fields['major_4'].widget.attrs.update(
            {'placeholder': 'Major (optional)'})
        self.fields['institution_4'].widget.attrs.update(
            {'placeholder': 'Institution (optional)'})
        self.fields['year_4'].widget.attrs.update(
            {'placeholder': 'Year (YYYY) (optional)'})

        self.fields['from_1'].widget.attrs.update(
            {'placeholder': 'From (YYYY-MM-DD)'})
        self.fields['to_1'].widget.attrs.update(
            {'placeholder': 'To (YYYY-MM-DD)'})
        self.fields['organization_1'].widget.attrs.update(
            {'placeholder': 'Organization'})
        self.fields['description_of_work_1'].widget.attrs.update(
            {'placeholder': 'About Work'})

        self.fields['from_2'].widget.attrs.update(
            {'placeholder': 'From (YYYY-MM-DD) (optional)'})
        self.fields['to_2'].widget.attrs.update(
            {'placeholder': 'To (YYYY-MM-DD) (optional)'})
        self.fields['organization_2'].widget.attrs.update(
            {'placeholder': 'Organization (optional)'})
        self.fields['description_of_work_2'].widget.attrs.update(
            {'placeholder': 'About Work (optional)'})

        self.fields['from_3'].widget.attrs.update(
            {'placeholder': 'From (YYYY-MM-DD) (optional)'})
        self.fields['to_3'].widget.attrs.update(
            {'placeholder': 'To (YYYY-MM-DD) (optional)'})
        self.fields['organization_3'].widget.attrs.update(
            {'placeholder': 'Organization (optional)'})
        self.fields['description_of_work_3'].widget.attrs.update(
            {'placeholder': 'About Work (optional)'})

        self.fields['from_4'].widget.attrs.update(
            {'placeholder': 'From (YYYY-MM-DD) (optional)'})
        self.fields['to_4'].widget.attrs.update(
            {'placeholder': 'To (YYYY-MM-DD) (optional)'})
        self.fields['organization_4'].widget.attrs.update(
            {'placeholder': 'Organization (optional)'})
        self.fields['description_of_work_4'].widget.attrs.update(
            {'placeholder': 'About Work (optional)'})

        self.fields['from_5'].widget.attrs.update(
            {'placeholder': 'From (YYYY-MM-DD) (optional)'})
        self.fields['to_5'].widget.attrs.update(
            {'placeholder': 'To (YYYY-MM-DD) (optional)'})
        self.fields['organization_5'].widget.attrs.update(
            {'placeholder': 'Organization (optional)'})
        self.fields['description_of_work_5'].widget.attrs.update(
            {'placeholder': 'About Work (optional)'})

        self.fields['membership_of_any_other'].widget.attrs.update(
            {'placeholder': 'Membership of any other Engineering/Professional Society (optional)'})

        self.fields['present_position'].widget.attrs.update(
            {'placeholder': 'Present Position (optional)'})
        self.fields['employeer'].widget.attrs.update(
            {'placeholder': 'Employeer (optional)'})
        self.fields['office_address'].widget.attrs.update(
            {'placeholder': 'Office Address (optional)'})

        self.fields['recommenders_name'].widget.attrs.update(
            {'placeholder': 'Recommenders Name (optional)'})
        self.fields['membership_no'].widget.attrs.update(
            {'placeholder': 'Membership No (optional)'})
        self.fields['membership_status'].widget.attrs.update(
            {'placeholder': 'Membership Status (optional)'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Office Address (optional)'})
