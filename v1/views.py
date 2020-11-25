from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from v1.services.connect import connect

# Create your views here.

class echoTest(APIView):
    """
    echo test
    """
    def get(self, request):
        return Response({ 'echo': 'test' })

class echoPostTest(APIView):
    """
    echo post test
    """
    def post(self, request):
        return Response({ 'echo': 'test' })

class testMySQL(APIView):
    """
    mysql test
    """
    def get(self, request):
        conn = connect()
        result = conn.execQuery('SELECT * FROM `users`')
        return Response(result);