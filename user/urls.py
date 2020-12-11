from django.urls import path
from . import views 

urlpatterns = [
    path('signup/',views.signup,name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('success/',views.success,name='success'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('update/',views.updateprofile,name='update'),
]
