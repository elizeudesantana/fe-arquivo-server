from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import logging

log = logging.getLogger(__name__)

class HealthcheckAPIView(APIView):

    def get(self, request, format=None):
        database_healthy = True
        cursor = none
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT 1;')
        except Exception as Err:
            database_healthy = False
            log.exception(err)
        finally:
            if cursor is not None:
                cursor.close()
        data={
            'database'= database_healthy
        }
        return Response(data)