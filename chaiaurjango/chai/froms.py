from django import forms
from .models import CHAIVARIETY

class chaivarietyform(forms.Form):
  chai_variety = forms.ModelChoiceField(queryset=CHAIVARIETY.objects.all(), label="select chai variety")