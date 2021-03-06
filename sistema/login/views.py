from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from sistema import settings

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context ['title'] = "Iniciar Sesión"
        

        return context

class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy ('erp:dashboard') #ver que debería ir con LOGIN_REDIRECT_URL

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect (self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return HttpResponseRedirect (self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = "Iniciar Sesión"
        return context


#class LogoutFormView(LogoutView):
