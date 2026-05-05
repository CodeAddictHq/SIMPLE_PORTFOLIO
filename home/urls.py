from django.urls import path
from .views import Home, About, Contacts_v, RegiCon, SignUp, LogIn, LogOut



urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('about/', About.as_view(), name='about'),
  path('contacts/', Contacts_v.as_view(), name='contacts'),
  path('contacts/register/', RegiCon, name='register'),
  path('signup/', SignUp.as_view(), name='signup'),
  path('login/', LogIn.as_view(), name='login'),
  path('logout/', LogOut.as_view(), name='logout'),
  
]