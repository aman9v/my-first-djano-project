from django import forms
# from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,	ButtonHolder, Submit
from django.contrib.auth.forms import UserCreationForm


# class UserRegistrationForm(forms.ModelForm):
# 	Password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
# 	Password2 = forms.CharField(widget=forms.PasswordInput, label="Password(again)")

# 	class Meta:
# 		model = get_user_model()
# 		fields = ['username','email',]


class UserRegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password1',
			'password2',
			ButtonHolder(
				Submit('register', 'Register', css_class='btn-primary')
			)
		)

