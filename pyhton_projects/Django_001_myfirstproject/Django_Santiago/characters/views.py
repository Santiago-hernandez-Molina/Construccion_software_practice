from django.shortcuts import redirect, render
from django.http import HttpResponse
from characters.models import Character

# Create your views here.


def list(request):
    list = Character.objects.all()
    return render(request, 'characters/index.html', {"list": list})


def save(request):
    if request.method == "GET":
        return render(request, 'characters/save.html')
    name_ = request.POST["name"]
    description_ = request.POST["description"]
    city_id_ = request.POST["city_id"]
    universe_id_ = request.POST["universe_id"]
    file = request.FILES["file"]

    character = Character(name=name_, description=description_,
                          city_id=city_id_, universe_id=universe_id_, path=file)
    character.save()

    return redirect("characters:list_characters")


def detail(request):
    return render(request, 'characters/detail.html')
