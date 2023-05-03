from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Set Session Function
def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')

# Get Session Function
def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name': name})
    else:
        return HttpResponse("Your session is expired!")

# Delete Session Function
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')
