from django.urls import path
from . import views

app_name = 'useraccount'

urlpatterns = [
    path('top/',views.TopView.as_view(),name='top' ),
    path('registration/',views.RegistrationView.as_view(),name='registration' ),
    path('login/',views.MyLoginView.as_view(),name='login' ),
    path('logout/',views.MyLogoutView.as_view(),name='logout' ),
    path('user/',views.MyUserView.as_view(),name='user' ),
]
