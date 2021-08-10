from django.urls import path
from . import views

app_name = 'accounts'
# unique name for the app so same names for paht, don't crash our program
urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
