from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery_poc.celery import *


class SubmitTaskView(APIView):
    def post(self, request, *args, **kwargs):
        print_json.delay(request.data)
        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)

class SubmitFeedView(APIView):
    def post(self, request, *args, **kwargs):
        print_json_for_feed.delay(request.data)
        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)

class SubmitWebhookTaskView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'status': 'success', 'retval': {"yes": 1}})
    
class SubmitToFanoutQueueView(APIView):
    def post(self, request, *args, **kwargs):
        print_json.apply_async(
            args=[request.data],
            queue="fanout_queue"
        )
        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)

class SubmitToBroadCastQueueView(APIView):
    def post(self, request, *args, **kwargs):
        print_json.apply_async(
            args=[request.data],
            queue="broadcast_queue"
        )
        return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
