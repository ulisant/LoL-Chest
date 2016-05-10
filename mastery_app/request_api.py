import urllib2
import json
from random import randint

#Yor api key
api_riot = "66369ede-8538-4fe9-94ab-16981b0059ab"

def get_champ_img():


    uri = "https://global.api.pvp.net/api/lol/static-data/lan/v1.2/champion?champData=blurb&api_key="+ api_riot

    serialized_data = urllib2.urlopen(uri).read()

    data = json.loads(serialized_data)
    get_total_champ = len(data['data'])-1
    random_champ_num = randint(0,get_total_champ)
    get_vule_ran = data['data'].values()[random_champ_num]
    champ_ob = get_vule_ran['key']

    return champ_ob

def link_summoner(summoner_name, server):

    uri = "https://lan.api.pvp.net/api/lol/" + server + "/v1.4/summoner/by-name/" + summoner_name  + "?api_key=" + api_riot

    try:
        serialized_data = urllib2.urlopen(uri).read()
        data = json.loads(serialized_data)

        summoner =  data[summoner_name]['name']
        uri_profile_icon = "http://ddragon.leagueoflegends.com/cdn/6.9.1/img/profileicon/" + str(data[summoner_name]['profileIconId']) + ".png"

        data = {'summoner_name':summoner, 'avatar':uri_profile_icon}

        return data

    except urllib2.HTTPError as e:

        return False

def get_all_champs():


    uri = "https://global.api.pvp.net/api/lol/static-data/lan/v1.2/champion?champData=blurb&api_key="+ api_riot

    serialized_data = urllib2.urlopen(uri).read()

    data = json.loads(serialized_data)
    get_champs = data['data']

    return get_champs
