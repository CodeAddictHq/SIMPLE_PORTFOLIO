from django.urls import path
from .views import Projects, SpecificProject, AddComment, DeleteComment, EditComment
urlpatterns = [
  path('', Projects.as_view(), name='projects_all'),
  path('<str:slug>/', SpecificProject.as_view(), name='specific_project'),
  path('<str:slug>/addcomment/', AddComment, name='add_comment'),
  path('<str:slug>/comment/<int:id>/delete', DeleteComment, name='add_comment'),
  path('<str:slug>/comment/<int:id>/edit', EditComment, name='add_comment'),
]