from django import forms

class formLogin(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
     'placeholder':'Email'}),label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
     'placeholder':'Password'}),label='')
    # widgets = {'password': forms.PasswordInput(),}
    