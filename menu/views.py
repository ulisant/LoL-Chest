from django.shortcuts import render
from mastery_app.request_api import get_all_champs

def Menu(request):
    login_nav = True
    ctx = {
        'login_nav':login_nav,
        'get_champs':get_all_champs()
    }

    return render(request, "menu.html", ctx)
