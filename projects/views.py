from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def all_projects(request):
    projects = Project.objects
    return render(request, 'projects/allprojects.html', {'projects': projects})


def details(request, blog_id):
    project = get_object_or_404(Project, pk=blog_id)
    return render(request, 'projects/project.html', {'project': project})
