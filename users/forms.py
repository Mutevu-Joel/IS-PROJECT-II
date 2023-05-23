from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Child, Parent
from .models import Profile
from .models import Vaccine


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['vaccine_id', 'mode_of_admission', 'batch_no', 'vaccine_quantity', 'expiry_date']
        widgets = {

            'expiry_date': DateInput(),

        }


class ChildForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['parent_id','mobile_no','surname','other_name','sex','dob','village','ward','pre_condition']
        widgets = {

            'dob': DateInput(),

        }


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['child_registration_no','clinic_no','weight','height','parent_id','vaccine_id','dose_no','comment','immunized_at',
                  'return_date']
        widgets = {
            'immunized_at': DateInput(),
            'parent_id': forms.TextInput,

            'return_date': DateInput()
        }
