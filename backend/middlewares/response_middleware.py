from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class ResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        print('response')
        return response