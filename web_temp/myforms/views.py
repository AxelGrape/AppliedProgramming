from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
import sys
sys.path.insert(1, '../parser/')
from interface_module import parse_file_string

# Create your views here.

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            body = form.cleaned_data['body']
            return HttpResponse(f'<p>{parse_file_string(body)}</p><br><a href="http://127.0.0.1:8000/">Gå tillbaka</a>')


    form = ContactForm()
    return render(request, 'forms.html', {'form': form})

def result(request):
    return HttpResponse('<h1>Hello</h1>')
