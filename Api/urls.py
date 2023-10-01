from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,sendPasswordResetEmailView,PasswordResetView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register' ),
    path('login/', UserLoginView.as_view(),name='login' ),
    path('profile/', UserProfileView.as_view(),name='profile' ),
    path('changepassword/', UserChangePasswordView.as_view(),name='change_password' ),
    path('password-reset-send-email/', sendPasswordResetEmailView.as_view(),name='password-reset-send-email'),
    path('password-reset/<uid>/<token>/', PasswordResetView.as_view(),name='password-reset'),
]