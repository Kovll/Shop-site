from django.urls import path

from users.views import login, register, profile, logout_user

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

]
