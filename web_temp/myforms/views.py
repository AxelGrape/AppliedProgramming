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

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.content_type)

        #Check if the uploaded files is .pas file
        if(uploaded_file.content_type == "text/x-pascal"):
            return HttpResponse(f'<p>{parse_file_string(handle_uploaded_file(uploaded_file))}</p><br><a href="http://127.0.0.1:8000/">Go Back</a>')
        else:
            return HttpResponse(f'<p>Only pascal files are accepted</p><br><a href="http://127.0.0.1:8000/">Go back</a>')

    return render(request, 'upload.html')

def handle_uploaded_file(f):
    message = b''
    for chunk in f.chunks():
        message += chunk
    print(message.decode("utf-8"))
    return message.decode("utf-8")
