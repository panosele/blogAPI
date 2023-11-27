from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request):
  # username = request.POST["username"]
  email = request.POST["email"]
  password = request.POST["password"]

  user =  authenticate(request, password=password, email=email)
  print(user)
 
  # Check if a user is verified and authenticated
  if user is not None:
    # Use the returned user object in login()
    login(request, user)
    
    # Redirect to home page after logging in
    return JsonResponse({"login": "success"})
  else:
    return JsonResponse({"login": "failed"})

@csrf_exempt
def sign_up(request):   
  print(request.POST)
  if request.method == "POST":
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]

    print(username, email, password)
    print(request.POST)
 
    user = User.objects.create_user(username=f"{username}",
                                email=f"{email}",
                                password=f"{password}")
    
    user.save()
    return JsonResponse({"signup": "success"})
  else:
    return JsonResponse({"signup": "failed"})

def logout_view(request):
  # ... Other logic
  logout(request)
  return JsonResponse({"logout": "success"})