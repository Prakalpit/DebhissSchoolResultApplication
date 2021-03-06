from django.contrib.auth.forms import UserCreationForm
from  .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'