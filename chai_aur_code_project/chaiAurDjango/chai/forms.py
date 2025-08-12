from django import forms
from .models import ChaiVarity


class ChaiVarityForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label="Select chai variety")