from django.shortcuts import render, redirect
from mastery_app.request_api import get_champ_img, link_summoner
from .forms import ExtraDataForm

def ExtraData(request):
    home_nav = True
    msg_err = ""
    extra_data_form = ExtraDataForm()

    if request.user.status:
        return redirect('/menu')

    if request.GET.get('summoner', None):
        msg_err = "SummonerName dosent exist"


    if request.method == 'POST':
        extra_data_form = ExtraDataForm(request.POST)
        if extra_data_form.is_valid():
            check_form = extra_data_form.save(commit = False)
            summoner_name = request.POST['summoner_name']
            server = request.POST['server']
            data_summoner = link_summoner(summoner_name, server)
            if not data_summoner:
                return redirect('/users/extra-data?summoner=False')
            else:
                request.user.avatar = data_summoner['avatar']
                request.user.summoner_name = data_summoner['summoner_name']
                request.user.server = server
                request.user.status = True
                request.user.save()
                return redirect('/')
        else:
            msg_err = extra_data_form.errors

    ctx = {
        'msg_err':msg_err,
        'home_nav':home_nav,
        'champ_ob':get_champ_img(),
        'extra_data_form':extra_data_form,
    }

    return render(request, "extra_data.html", ctx)
