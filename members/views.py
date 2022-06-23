from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from club.models import Profile

# Create your views here.
class CreateProfilePage(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = 'registration/createprofile.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
	model = Profile
	template_name = 'registration/profile_editon.html'
	fields = ['bio', 'profileImage', 'ciudad', 'redes']
	success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/profile.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
		context["page_user"] = page_user
		return context

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('password_success')

def password_success(request):
	return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user
