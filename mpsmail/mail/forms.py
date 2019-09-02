from django import forms
from .models import Sentmail

class CreatemailForm(forms.ModelForm):
	class Meta:
		model=Sentmail
		fields=['msg','sub']
		labels = {
            "sub":"Subject",
            "msg":"Message"
        }
		widgets={
			'sub':forms.TextInput(attrs={'class':"form-control"})
			#'msg':forms.Textarea(attrs={'cols':"50"})
}

