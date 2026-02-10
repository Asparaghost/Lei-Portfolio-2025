from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.signing import BadSignature
from django.core import signing
from .models import *

# Create your views here.
def index(request): 
    informations = Information.objects.all() 
    experiences = Experience.objects.all() 
    context = {
        'informations':informations,
        'experiences':experiences
    }
    return render(request, "portfolio25/index.html", context)


def projects(request): 
    projects = Project.objects.all() 
    context = {
        'projects':projects
    }
    return render(request, "portfolio25/projects.html", context)

@xframe_options_exempt
def proj_info(request, proj_hash):
    try:
        proj_id = signing.loads(proj_hash)
        project = Project.objects.get(proj_id=proj_id)
    except (BadSignature, Project.DoesNotExist):
        return HttpResponse("Invalid project link", status=404)

    context = {
        'project': project,
    }
    return render(request, "portfolio25/details.html", context)