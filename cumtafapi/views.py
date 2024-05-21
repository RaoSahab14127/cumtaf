from django.shortcuts import render

def add_user(request):
    hammad = '<b>Hammad</b>'
    return render(request, 'cumtafapi/adduser.html', {'data': hammad})
