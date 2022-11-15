from django.shortcuts import render
import DeliveryFood.models as mod
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import AdressForm

# Create your views here.

def test_link(request):
    return render(request, 'test.html')

@csrf_exempt
def signUp_link(request):
    if request.method == "GET":
        return render(request, 'signUp.html')
    elif request.method == "POST":
        return render(request, 'test.html')
        username = request.POST["name"]
        first_name = request.POST["first_name"]
        second_name = request.POST["second_name"]
        email = request.POST["email"]
        password = request.POST["pass"]
        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=second_name, password=password, email=email)
        user.save()
        return redirect('signIn')

@csrf_exempt
def signIn_link(request):
    if request.method == "GET":
        return render(request, "signIn.html", {"sucess" : 1})
    if request.method == "POST":
         username = request.POST["your_name"]
         password = request.POST["your_pass"]
         user = authenticate(username=username, password=password)
         if user is None:
             return render(request, "signIn.html", {"sucess" : 0})
         else:
             login(request, user)
             return redirect('/')

def index(request):
    category_list = mod.Categories.objects.all()
    food_list = mod.Foods.objects.all()
    return render(request, 'index.html', {"cat_list":category_list, "food_list":food_list})

def changeAdress(request):
    form = AdressForm()
    return render(request, 'AdresForm.html', {"form":form})

def logoutUser(request):
    logout(request)
    return redirect('/')

def checkusername(request):
    result = {'code': 1, "content": ""}
    # получить запрос
    username = request.GET.get("username")
    # Определить, существует ли пользователь
    user = User.objects.filter(username=username).first()
    if user:
        ## существовать
        result = {'code': -1, "content": "Имя пользователя уже существует"}
    else:
        result = {'code': 1, "content": "Имя пользователя не существует"}
    return JsonResponse(result)

def checkmail(request):
    result = {'code': 1, "content": ""}
    # получить запрос
    email = request.GET.get("email")
    print(email)
    # Определить, существует ли пользователь
    user = User.objects.filter(email__exact=email).first()
    if user:
        ## существовать
        result = {'code': -1, "content": "Пользователь с такой почтой существует"}
    else:
        result = {'code': 1, "content": "Пользователь с такой почтой не существует"}
    return JsonResponse(result)

