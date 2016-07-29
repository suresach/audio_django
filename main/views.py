from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

def index(request):
	return render(request, 'main/home_page.html')

def search_form(request):
    return render(request, 'main/search_form.html')

def search(request):
    if 'q' in request.POST:
        message = 'You searched for: %r' % request.POST['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sub = (cd['subject'])
            return render(request, 'main/thank.html', {'sub': sub})
    else:
        form = ContactForm()
    return render(request, 'main/contact_form.html', {'form': form})

