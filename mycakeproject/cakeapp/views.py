from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from cakeapp.models import City, Town, Cake


# Create your views here.
def allCake(request, c_slug=None):
    c_page = None
    products = None
    if c_slug is not None:
        c_page = get_object_or_404(Cake, name=c_slug)
        products = Cake.objects.all().filter(name=c_page)
    else:
        products = Cake.objects.all().filter(name=True)

    return render(request, "category.html")


def cities(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'cities.html', context)


def towns(request):
    city = request.GET.get('city')
    towns = Town.objects.filter(city=city)
    context = {'towns': towns}
    return render(request, 'partials/towns.html', context)


def thankyou(request):
    return render(request,"thanks.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
