from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,FormView
from django.views.generic.base import TemplateView,View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegistrationForm, LoginForm

class TopView(TemplateView):
    template_name = 'top.html'
    

class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm


class MyLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    
    #ログイン維持するかのチェックボックス追加
    def form_valid(self,form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1000000)
        return super.form_valid(form)
    

class MyLogoutView(LogoutView):
    pass

#もう一つのログイン実装方法
# class MyLoginView(FormView):
#     template_name = 'login.html'
#     form_class = LoginForm
    
#     def post(self, request, *args, **kwargs):
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password = password)
#         next_url = request.POST['next']
#         if user is not None and user.is_active:
#             login(request,user)
            
#         #ユーザーページ->ログイン画面と遷移していたときトップに戻さず直接ユーザーページに飛ばしてあげる
#         if next_url:
#             return redirect(next_url)
#         return redirect('useraccount:top')

# class MyLogoutView(View):
    
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('useraccount:login')
    

class MyUserView(TemplateView):
    template_name = 'user.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)