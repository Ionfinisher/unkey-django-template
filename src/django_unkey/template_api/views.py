from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.key_verification import verify_api_key
import os


class PublicView(APIView):
    def get(self, request):
        return Response({'message': 'Heeyaaa!! Touchdown to the public endpoint!!'})


class ProtectedView(APIView):
    def get(self, request):
        api_key = request.headers.get('Authorization')

        # Use the service for verification.
        # Example verification logic.
        if not api_key or not verify_api_key(api_key, permission='call-protected-route'):
            return Response({'detail': 'Invalid or missing API Key'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'message': 'Woohoo!! Touchdown to the protected endpoint!!'})
