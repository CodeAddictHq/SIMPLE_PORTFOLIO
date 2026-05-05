from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views import View 
from .models import Contacts

class Home(View):
  def get(self, request):
    return render(request, 'home.html')

class About(View):
  def get(self, request):
    return render(request, 'about.html')

class Contacts_v(View):
  def get(self, request):
    return render(request, 'contacts.html')



class SignUp(View):
  def get(self, request):
    return render(request, 'signup.html')



  def post(self, request):
    username = request.POST.get("username").strip()
    email = request.POST.get("email")
    password = request.POST.get("confirm_password")
    try:
      user = User.objects.create_user(username=username, password=password, email=email)
      login(request, user)
      return redirect('home')
      
    except IntegrityError:
      messages.error(request, "username already exists")
      return redirect('signup')
      
      


class LogIn(View):
  def get(self, request):
    return render(request, 'login.html')
  def post(self, request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('home')
    except User.DoesNotExist:
      messages.error(request, "user not found")
      return redirect('login')



class LogOut(View):
  def get(self, request):
    return render(request, 'logout.html')
  def post(self, request):
    username = request.user.username
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user :
      logout(request)
      return redirect("home")
    else:
      messages.error(request, "Password DoesNotExist")
      return redirect("logout")
      
from django.contrib.auth.decorators import login_required
@login_required



def RegiCon(request):
  if request.method =="GET":
    username = request.user.username
    print(username)
    return render(request, 'contacts_form.html', {'user':username})
  if request.method =="POST":
    user = request.user
    text = request.POST.get("message")
    link = request.POST.get("link")
    Contacts.objects.create(user=user,message=text, link=link)
    return redirect('contacts')
  