from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)