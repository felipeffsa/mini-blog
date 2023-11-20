from django.contrib.auth.middleware import AuthenticationMiddleware


class CustomUserMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        super().process_request(request)
        if hasattr(request, 'user'):
            request.usuario = request.user
