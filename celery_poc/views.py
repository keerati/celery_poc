from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery_poc.celery import print_json


class SubmitTaskView(APIView):
    def post(self, request, *args, **kwargs):
        print_json.delay(request.data)
        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
