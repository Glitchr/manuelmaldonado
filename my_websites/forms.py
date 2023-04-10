from django import forms
from hcaptcha_field import hCaptchaField


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=200)
    message = forms.CharField(widget=forms.Textarea, required=True)
    hcaptcha = hCaptchaField()
