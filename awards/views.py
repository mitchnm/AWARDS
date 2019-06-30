from django.shortcuts import render, redirect
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def profile(request, id):
  project = Project.objects.filter(user_id=id)
  current_user = request.user
  user = User.objects.get(id=id)
  try:
      profile1 = Profile.objects.get(name=id)
  except ObjectDoesNotExist:
      return render(request,'profile.html')
  return render(request, 'profile.html', {"image": image, "user": user, "profile1": profile1})
