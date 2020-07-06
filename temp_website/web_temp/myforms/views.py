from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
import sys
sys.path.insert(1, '../../parser/')
from interface_module import parse_file_string

# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            body = form.cleaned_data['body']

            parse_file_string(body)

    form = ContactForm()
    return render(request, 'forms.html', {'form': form})
