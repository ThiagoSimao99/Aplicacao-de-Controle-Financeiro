from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    """View de login com suporte a 'lembrar usuário' via cookie."""
    template_name = 'financeiro/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    
    def get_initial(self):
        """Pré-preenche o username se existir no cookie."""
        initial = super().get_initial()
        remembered_username = self.request.COOKIES.get('remembered_username', '')
        if remembered_username:
            initial['username'] = remembered_username
        return initial
    
    def form_valid(self, form):
        """Processa login e gerencia cookie de 'lembrar usuário'."""
        response = super().form_valid(form)
        
        remember_me = form.cleaned_data.get('remember_me', False)
        if remember_me:
            # Salva username no cookie por 30 dias
            response.set_cookie(
                'remembered_username',
                form.cleaned_data['username'],
                max_age=30 * 24 * 60 * 60,  # 30 dias
                httponly=True,
                samesite='Lax'
            )
        else:
            # Remove o cookie se existir
            response.delete_cookie('remembered_username')
        
        return response


class RegisterView(CreateView):
    """View de cadastro de novos usuários."""
    template_name = 'financeiro/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        """Redireciona usuários já autenticados."""
        if request.user.is_authenticated:
            return redirect('grupo-list')
        return super().dispatch(request, *args, **kwargs)


def logout_view(request):
    """View de logout que mantém o cookie de 'lembrar usuário'."""
    logout(request)
    return redirect('login')
