class HtmxLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Toute redirection pendant une requête HTMX (boosted) doit forcer
        # un vrai changement de page navigateur, pas un swap AJAX sur #main-content
        if request.headers.get('HX-Request') == 'true' and response.status_code in (301, 302):
            response['HX-Redirect'] = response.get('Location', '')

        return response