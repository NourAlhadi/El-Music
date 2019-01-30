from django.shortcuts import redirect
from django.urls import resolve


class DenyLoggedInLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if str(request.user) != 'AnonymousUser':
            current_url = resolve(request.path_info).url_name
            current_url = str(current_url)
            if current_url == 'login' or current_url == 'signup':
                return redirect('main:index')

        response = self.get_response(request)
        return response

