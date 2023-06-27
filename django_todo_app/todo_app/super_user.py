from django.shortcuts import redirect
from django.urls import reverse

class SuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(reverse('user_login')):
            next_url = request.path
            login_url = reverse('user_login')
            redirect_url = f'{login_url}?next={next_url}'
            return redirect(redirect_url)
        return self.get_response(request)
