from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model =Person
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.RadioSelect(attrs={"class": "form-select"}),
            "profile_picture": forms.ClearableFileInput(attrs={"class":"form-control"}),

        }