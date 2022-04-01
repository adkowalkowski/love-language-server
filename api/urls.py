from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.loves import LovesView, LoveView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('love-languages/', LovesView.as_view(), name='love-languages'),
    path('love-languages/<str:variable_email>', LoveView.as_view(), name='love-languages')
]