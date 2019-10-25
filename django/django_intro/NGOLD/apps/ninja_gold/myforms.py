from django import forms

class farmForm(forms.Form):
    building = forms.CharField(widget = forms.HiddenInput(), initial='farm')

class caveForm(forms.Form):
    building = forms.CharField(widget = forms.HiddenInput(), initial='cave')

class houseForm(forms.Form):
    building = forms.CharField(widget = forms.HiddenInput(), initial='house')

class casinoForm(forms.Form):
    building = forms.CharField(widget = forms.HiddenInput(), initial='casino')
