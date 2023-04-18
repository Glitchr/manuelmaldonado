from django import forms
from hcaptcha_field import hCaptchaField


class ContactForm(forms.Form):                                                                                               
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=200)
    message = forms.CharField(widget=forms.Textarea, required=True)
    hcaptcha = hCaptchaField(label='')

    hcaptcha.widget.attrs.update({'class': 'border-0 text-center form-shadow', 'style': 'padding: 0; width: 0;'})
    email.widget.attrs.update({'class': 'form-shadow'})
    subject.widget.attrs.update({'class': 'form-shadow'})
    message.widget.attrs.update({'class': 'form-shadow'})