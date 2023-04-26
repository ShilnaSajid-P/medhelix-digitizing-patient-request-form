from django import forms
from.models import Userr
from django.contrib.auth.models import User
from datetime import date



from django import forms
from django.contrib.auth.models import User

from django import forms

from django import forms

class Userform(forms.Form):
    image_file = forms.ImageField(required=False)
    image_data = forms.CharField(widget=forms.HiddenInput(), required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    serial_no = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('image_file') and not cleaned_data.get('image_data'):
            raise forms.ValidationError('Please select an image file or enter image data.')
        return cleaned_data
                
class ImageSearchForm(forms.Form):
    serial_no = forms.CharField(max_length=20, required=True)
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))