from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def rannum(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 0
    request.session['rannum'] = get_random_string(length=5, allowed_chars='0123456789')
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/rannum')


