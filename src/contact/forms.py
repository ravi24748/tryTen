from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'special'}))
	email = forms.EmailField(required=True)
	comment= forms.CharField(required=True, widget=forms.TextInput(attrs={'size': '40'}))