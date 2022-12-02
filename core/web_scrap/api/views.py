from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

class WebScraperAPI(APIView):

    def post(self, request, *args, **kwargs):
        print(kwargs)

        return Response('200')

    def get(self, request):


        return Response('asdasd')