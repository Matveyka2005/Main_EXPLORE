from django.http import JsonResponse


class Process500:
    def __init__(self, get_respnse):
        self._get_response = get_respnse

    def __call__(self, request):
        return self._get_response(request)
    
    def process_excaption(self, request, exception):
        return JsonResponse({
                "success": False,
                "errorMassage": str(exception)
                
                })
