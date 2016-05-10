from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from mastery_app.request_api import get_champ_img, link_summoner
from users.forms import SingUpForm


def index(request):
    home_nav = True
    msg_err = ""
    msg_success = ""
    singup = SingUpForm()

    if request.GET.get('summoner', None):
        msg_err = "SummonerName dosent exist"

    if request.GET.get('success', None):
        msg_success = "Registration success, please login."

    if request.user.is_authenticated():
        return redirect('/menu')

    if request.method == 'POST':
        if 'login' in request.POST:
            user = request.POST['user_log']
            password = request.POST['pass_log']
            user_auth = authenticate(username=user, password=password)
            if user_auth is not None:
                if user_auth.is_active:
                    login(request, user_auth)
                    return redirect('/menu')
                else:
                    msg_err = "The password is valid, but the account has been disabled!"
            else:
                msg_err = "The username and password were incorrect."

        if 'signup' in request.POST:
            singup = SingUpForm(request.POST)
            if singup.is_valid():
                check_form = singup.save(commit=False)
                summoner_name = request.POST['summoner_name']
                server = request.POST['server']
                data_summoner = link_summoner(summoner_name, server)
                if not data_summoner:
                    return redirect('/?summoner=False')
                else:
                    check_form.avatar = data_summoner['avatar']
                    check_form.status = True
                    check_form.password = make_password(request.POST['password'], salt=None, hasher='default')
                    check_form.save()
                    return redirect('/?success=True')
            else:
                print singup.errors
                msg_err = singup.errors

    ctx = {
        'singup':singup,
        'home_nav':home_nav,
        'champ_ob':get_champ_img(),
        'msg_err':msg_err,
        'msg_success':msg_success,
    }

    return render(request, "index.html", ctx)
