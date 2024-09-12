from django.forms import ModelForm
from .models import Notes

class notecreationform(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
