from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, ensure_csrf_cookie


@requires_csrf_token
def login_view(request):
  # username = request.POST["username"]
  user_or_mail = request.POST["email"]
  password = request.POST["password"]
  print(request.body)
  username = ""

  if user_or_mail.find("@") == -1:
    username =  User.objects.get(username=user_or_mail).username
  else:
    username =  User.objects.get(email=user_or_mail).username

  user =  authenticate(request, password=password, username=username)
  print(user)
 
  # Check if a user is verified and authenticated
  if user is not None:
    # Use the returned user object in login()
    login(request, user)
  
    return JsonResponse({"login": "success",
                          "username": username,
                          "email": user.email})
  else:
    return JsonResponse({"login": "failed"})

@csrf_exempt
def sign_up(request):
    print(request.POST)   
    if request.method == "POST":
      username = request.POST["username"]
      email = request.POST["email"]
      password = request.POST["password"]

      user = User.objects.create_user(username=f"{username}",
                                  email=f"{email}",
                                  password=f"{password}")
      user.save()
      login(request, user)
      return JsonResponse({"signup": "success",
                           "login": "success",
                           "username": user.username,
                           "email": user.email})
    else:
      return JsonResponse({"signup": "failed"})



@login_required
@requires_csrf_token
def logout_view(request):
  username = request.POST["username"]
  logout(request)
  try:
    user = User.objects.get(username=username)
    user.is_active = False
    user.save()
    return JsonResponse({"logout": "success"})
  except: 
    return JsonResponse({"logout": "failed"})
  


@login_required
@requires_csrf_token
def delete_view(request):
  try:
    email = request.POST["email"]
    user = User.objects.get(email=email)
    user.delete()
  except:
    return JsonResponse({"delete": "failed"})
  return JsonResponse({"delete": "success"})

@login_required
@requires_csrf_token
def update_view(request):
  username = request.POST["username"]
  password = request.POST["password"]
  email = request.POST["email"]

  try:
    user = User.objects.get(email=email)
    user.username = username
    user.password = password
    user.save()
  except:
    return JsonResponse({"update": "failed"})