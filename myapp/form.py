from django.forms import ModelForm
from .models import Orders

class CreateOrder(ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'skinstyle', 'size', 'units', 'description', 'urgency']