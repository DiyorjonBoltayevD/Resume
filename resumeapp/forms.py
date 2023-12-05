from django.forms import ModelForm, TextInput, Textarea

from resumeapp.models import ContactModelMessage


class ContactForm(ModelForm):
    class Meta:
        model = ContactModelMessage
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Your name'
            }),
            'email': TextInput(attrs={
                'email': 'inpt',
                'placeholder': 'Your email',
            }),

            'subject': TextInput(attrs={
                'subject': 'inpt',
                'placeholder': 'Subject'

            }),
            'message': Textarea(attrs={
                'message': 'inpt',
                'placeholder': 'Message'
            }),
            'rows': '7',
            'cols': '30',

        }
