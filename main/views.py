from django.shortcuts import render
from .forms import formLogin
from django.http import HttpResponse
 
def index(request):
    form_login = formLogin(auto_id=False)
    return render(request, 'main/home_page.html', {'form_login':form_login})

def verify_login(request):
    if 'email' in request.POST:
        message = 'You searched for: %r' % request.POST['email' ]
        message += "and: " + request.POST['password'] 
        return HttpResponse(message)


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

