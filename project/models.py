from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
  title = models.CharField(max_length=50)
  detail = models.TextField()
  code = models.TextField()
  github_link = models.TextField(blank=True)
  lang_choices = [
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('comb', 'Combined'),
    ('oth', 'Other'),
  ]
  language = models.CharField(max_length=10, choices=lang_choices)
  slug = models.SlugField(unique=True, null=True)
  def __str__(self):
    return self.title
  
  
class Comment(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()