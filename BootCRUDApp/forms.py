from .models import sellModel
from django import forms


class sellForm(forms.ModelForm):
    class Meta:
        model = sellModel
        fields = '__all__'

        labels = {
            'picture': "Image Url",
        }
