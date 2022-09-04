from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'

class SignUp(TemplateView):
    template_name = 'signup.html'

class SignIn(TemplateView):
    template_name = 'signin.html'

class AboutUs(TemplateView):
    template_name = 'about-us.html'