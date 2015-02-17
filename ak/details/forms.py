from django import forms

from details.models import Detail

class DetailsForm(forms.ModelForm):

	class Meta:
		model = Detail
		field = ['name', 'phone', 'email']
		