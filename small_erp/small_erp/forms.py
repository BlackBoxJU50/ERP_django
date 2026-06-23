from django import forms

class usersForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()


class InventoryForm(forms.Form):
    name = forms.CharField(label='Item name', max_length=255, required=True)
    quantity = forms.IntegerField(label='Quantity', min_value=0, required=True)
    price = forms.DecimalField(label='Price (USD)', max_digits=10, decimal_places=2, min_value=0, required=True)
    
