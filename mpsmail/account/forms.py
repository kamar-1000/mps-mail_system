from django import forms
from .models import Profile
class LoginForm(forms.Form):
	email=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Enter your mps email ID"}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter your password"}))
	def clean_email(self):
		email=self.cleaned_data['email']
		if not email.endswith('@mps.edu'):
			print("ValidationError")
			raise forms.ValidationError('Entered email address is not an mps email id')
		return email
class SignupForm(forms.ModelForm):
	class Meta:
		model=Profile
		exclude=['user','email','pic']
		widgets={
				'tel':forms.TextInput(attrs={'class':"form-control",'placeholder':"Enter you phone number"}),
				'security':forms.TextInput(attrs={'class':"form-control",'placeholder':"Enter your security question this helps to reset your password"})
		}
		labels = {
        "tel": "Phone no.",
        "security":"Security Question"
    }
