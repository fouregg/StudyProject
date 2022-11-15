from django import forms

class AdressForm(forms.Form):
    street = forms.CharField(label="Ваша улица", max_length=50)
    build = forms.CharField(label="Ведите Ваш дом", max_length=7)
    flat = forms.IntegerField(label="Введите квартиру или офис")
