from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project, Comment
class Projects(View):
  def get(self, request):
    cat = request.GET.get("type")
    projects = None
    if not cat:
      return render(request, 'projects.html')
    elif cat:
      projects = Project.objects.filter(language=cat)
      return render(request, 'projects.html', {'projects':projects})

class SpecificProject(View):
  def get(self, request, slug):
    project = Project.objects.get(slug=slug)
    comments = Comment.objects.filter(project=project)
    print(comments)
    return render(request, 'specific_project.html', {'project':project, 'comments':comments})


@login_required

def AddComment(request, slug):
  if request.method =="GET":
    username = request.user.username
    project = Project.objects.get(slug=slug)
    return render(request, 'add_comment.html', {'username':username,'project':project})
  elif request.method == "POST":
    body = request.POST.get("body")
    author = request.user
    project_slug = request.POST.get("slug")
    project = Project.objects.get(slug=slug)
    Comment.objects.create(body=body, author=author, project=project)
    messages.success(request, "Comment added go back and reload")
    return redirect('specific_project', slug=slug)


def DeleteComment(request, slug, id):
  if request.method =="GET":
    comment = Comment.objects.get(id=id)
    username = request.user.username
    return render(request, 'deletecomment.html', {'username':username, 'comment':comment})
  elif request.method == "POST":
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('specific_project', slug=slug)



def EditComment(request, slug, id):
  if request.method =="GET":
    comment = Comment.objects.get(id=id)
    username = request.user.username
    return render(request, 'editcomment.html', {'username':username, 'comment':comment})
  elif request.method == "POST":
    body = request.POST.get("body")
    comment = Comment.objects.get(id=id)
    comment.body = body
    comment.save()
    return redirect('specific_project', slug=slug)


    