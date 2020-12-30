from django.urls import path
from . import views 

urlpatterns = [
    path('signup/',views.signup,name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('<id>/update',views.updateprofile,name='update'),
    path('create/',views.create_post,name='create'),
    path('home/',views.home,name='home'),
]
