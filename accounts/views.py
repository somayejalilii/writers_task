from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here

@csrf_exempt
def create_profile(request):

    try:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        profile = Profile()

        profile.first_name = first_name
        profile.last_name = last_name
        profile.password = password
        profile.phone = phone
        profile.address = address
        profile.save()

        return HttpResponse("200 OK")

    except:
        return HttpResponse("NOT OK")

@csrf_exempt
def update_profile(request):
    try:
        profile = Profile
        id = request.POST.get('id')
        password = request.Post.get('password')
        phone = request.Post.get('phone')
        address = request.Post.get('address')

        profile.objects.filter(id=id).update(phone=phone, password=password, address=address)
        return HttpResponse("200 OK")

    except:
        return HttpResponse("Not Ok")






