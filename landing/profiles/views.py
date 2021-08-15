from django.contrib.auth.views import LoginView


from .forms import LoginForm

class LoginForms(LoginView):
    from_class = LoginForm
    template_name = "profiles/login.html"

    def get_success_url(self):
        return print('work')

