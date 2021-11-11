from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from characters.models import Character, City, PowersCharacter, Universe
from django.db.models import Count
from django.db.models import Q

# Create your views here.


def list(request):
    querySet = request.GET.get("search")
    list2= Universe.objects.all()

    if querySet:
        list = Character.objects.all().filter(name__contains=querySet)
        return render(request, 'characters/index.html', {"list": list,"list2":list2})
    else:
        list = Character.objects.all()
        return render(request, 'characters/index.html', {"list": list,"list2":list2})


def list_universes(request):
    list2=Universe.objects.all()
    return render(request,'characters/prueba.html',{"list2":list2})

def filter_by_universe(request,id):
    list=Character.objects.filter(universe=id)
    list2=Universe.objects.all()
    return render(request, 'characters/index.html', {"list": list,"list2":list2})

def save(request):
    if request.method == "GET":
        list = Universe.objects.all()
        list2 = City.objects.all()
        return render(request, 'characters/save.html',{"list":list,"list2":list2})
    name_ = request.POST["name"]
    description_ = request.POST["description"]
    city_id_ = request.POST["city_id"]
    universe_id_ = request.POST["universe_id"]
    file = request.FILES["file"]

    character = Character(name=name_, description=description_,
                          city_id=city_id_, universe_id=universe_id_, path=file)
    character.save()

    return redirect("characters:list_characters")

def detail(request, id):
    list=Character.objects.all().filter(id__contains=id)
    return render(request, 'characters/detail.html',{"list":list})


# Taller consultas:

def puntouno(request):
    ch = Character.objects.select_related('city')
    html = ""
    for character in ch:
        html = html + character.name + character.city.name+"<br>"
        # print(character.name)
    return HttpResponse(html)


def puntodos(request):
    result = (Character.objects
              .values('city','city__name')
              .annotate(dcount=Count('city'))
              .order_by())
    print(str(result))
    html = result
    return HttpResponse(html)


def puntotres(request):
    ch = PowersCharacter.objects.select_related('character', 'character__city')
    html = ""
    for character in ch:
        html = html + character.character.name+" |"+character.power.name + \
            str(character.level)+"  |" + character.character.city.name+"<br>"
        # print(character.name)
    return HttpResponse(html)


def puntocinco(request):
    ch = Character.objects.filter(name__contains="u")
    html = ""
    for character in ch:
        html = html + character.name+"<br>"
        # print(character.name)
    return HttpResponse(html)


def puntoseis(request):
    criterion1 = Q(power=1)
    criterion2 = Q(power=3)
    ch = PowersCharacter.objects.filter(criterion1 & criterion2)
    html=""
    for character in ch:
        html=html + str(character)+" |"+"<br>"
        # print(character.name)
    return HttpResponse(html)


def puntosiete(request):
    ch=PowersCharacter.objects.select_related('character').filter(
        Q(power__name__contains='Super fuerza') | Q(power__name__contains='Volar') | Q(power__name__contains='Telequinesis'))
    html=""
    for character in ch:
        html=html + character.character.name+" |"+character.power.name+"<br>"
        # print(character.name)
    return HttpResponse(html)

def puntoocho(request):
    ch = Character.objects.filter(Q(birthdate__range=('2010-01-01','2020-01-01')))
    html = ""
    for character in ch:
        html = html + character.name + " | " + str(character.birthdate) +"<br>"
    return HttpResponse(html)

def puntonueve(request):
    ch = Character.objects.filter(birthdate__lt = '2011-01-01')
    html=""
    for character in ch:
        html=html + character.name + " | " + str(character.birthdate)+"<br>"
    return HttpResponse(html)

def puntodiez(request):
    ch = PowersCharacter.objects.select_related('character').filter(~Q(power__name='Volar'))
    html = ""
    for character in ch:
        html = html + character.character.name + " |" + character.power.name + "<br>"
    return HttpResponse(html)
