from django.forms import ModelForm
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['city']


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'cities']


# maybe name this User_Edit_Form
class EditProfileForm(UserChangeForm):
    # to hide the password related information from edit page
    password = None

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
        )
