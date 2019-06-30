from django.shortcuts import render, redirect
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, ProjectForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    project = Project.objects.all()
    profile1 = Profile.objects.all()
    return render(request, 'index.html', {"project": project, "profile1": profile1})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    project = Project.objects.filter(user_id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
        profile1 = Profile.objects.get(name=id)
    except ObjectDoesNotExist:
        return render(request, 'profile.html')
    return render(request, 'profile.html', {"project": project, "user": user, "profile1": profile1})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.name_id = current_user.id
            profile.save()
        return render(request, 'profile.html')

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form, "user": current_user})


@login_required(login_url='/accounts/login/')
def new_project(request, id):
    current_user = request.user
    if request.method == 'POST':
        print('noo')
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('welcome')

    else:
        form = ProjectForm()
        print('xyz')
    return render(request, 'project.html', {"form": form, 'user': current_user})
