from django.urls import path, include
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='registro'),
	path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
	path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
	path('password-success', views.password_success, name='password-success'),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='profile'),
	path('<int:pk>/profile-edition/', EditProfilePageView.as_view(), name='profile-edition'),
	path('createProfilePage/', CreateProfilePage.as_view(), name='createProfilePage'),
]