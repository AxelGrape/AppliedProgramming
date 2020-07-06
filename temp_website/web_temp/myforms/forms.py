from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

class ContactForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'body',
            Submit('submit', 'Submit', css_class='btn-sucess')


        )
