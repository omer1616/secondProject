from django.forms import ModelForm, TextInput, FileInput
from .models import Company, Person


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        widgets = {'image': FileInput(
            attrs={'form-label-margin-bottom': '.5rem;', 'class': 'form-control form-control-lg', 'required': False}
        )}


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"