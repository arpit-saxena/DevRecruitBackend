from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.text import slugify
import hash_info

from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    def signup(self, request, user):
        pass

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.slug = slugify("%s %s" %(user.first_name, user.last_name))
        if commit:
            user.save()
            user.my_hash = hash_info.USER.encode(user.id)
            user.save()
        else:
            user.save(commit=False)
        return user

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        exclude = ('date_joined', 'username', )

class UserSignupForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=13)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.email = self.cleaned_data['email']
        user.slug = slugify("%s %s" % (user.first_name, user.last_name))
        user.save()
        user.my_hash = hash_info.USER.encode(user.id)
        user.save()
        return user

    class Meta(forms.Form):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        exclude = (
            'date_joined',
            'username',
            'my_hash',
            'slug'
            )

class CustomUserChangeForm(UserChangeForm):
    def save(self, commit=True):
        user = super(CustomUserChangeForm, self).save(commit=False)
        user.slug = slugify("%s %s" % (user.first_name, user.last_name))
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        exclude = (
            'date_joined', 
            'username',
            'my_hash',
            'slug'
            )
        