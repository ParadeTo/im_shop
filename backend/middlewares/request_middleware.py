from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('request')
        return HttpResponse('a')