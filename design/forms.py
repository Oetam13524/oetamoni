from django import forms
from . models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Name",
            "user_email": "Email",
            "text": "Comment"
        }


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']