from django.shortcuts import redirect, render
from .models import CaseStudy, Category
# Create your views here.


def list(request):
    list = Category.objects.all()
    return render(request, 'solutions/index.html', {"list": list})


def saveCategory(request):
    if request.method == "GET":
        list = Category.objects.all()
        return render(request, 'solutions/save.html', {"list": list})
    name_ = request.POST["name"]
    description_ = request.POST["description"]
    file = request.FILES["file"]

    category = Category(name=name_, description=description_, video=file)
    category.save()

    return redirect("solutions:list")

def detail(request,id):
    item=Category.objects.get(pk=id)
    list=CaseStudy.objects.filter(category=id)
    return render(request,'solutions/detail.html',{"item":item,"list":list})
