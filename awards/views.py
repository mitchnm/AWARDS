from django.shortcuts import render, redirect
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, ProjectForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AwardsMerch
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

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


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = User.objects.filter(
            username__icontains=search_term)
        profile1 = Profile.objects.all()
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "profile": searched_profiles, "profile1": profile1})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


class MerchList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_merch = AwardsMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
