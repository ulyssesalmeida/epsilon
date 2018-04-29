from django import forms

class PipForm(forms.Form):
    title = forms.CharField()
    orgUnit = forms.CharField()
    client = forms.CharField()
    justification = forms.CharField(widget=forms.Textarea)
    objectives = forms.CharField(widget=forms.Textarea)
    cost_estimates = forms.CharField()