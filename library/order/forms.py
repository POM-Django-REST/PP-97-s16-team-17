from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'user', 'plated_end_at']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'plated_end_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }