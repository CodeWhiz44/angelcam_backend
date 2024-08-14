import os
import json
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CameraSerializer, RecordingSerializer, LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid()

        username = request.data['full_name']
        email = request.data['email']
        token = request.data['personal_token']

        response = requests.get(
            url='https://api.angelcam.com/v1/me',
            headers={
                'Authorization': f'PersonalAccessToken {token}'
            }
        )
        
        data = response.json()
        if response.status_code == 200 and username == f'{data["first_name"]} {data["last_name"]}' and email == data['email']:
            return Response({'status': 200})
        else:
            return Response(data)

class CameraListView(APIView):
    def get(self, request):
        auth = request.headers['Authorization']
        token = auth.split()[1]
        
        headers = {
            'Authorization': f'PersonalAccessToken {token}'
        }
        response = requests.get('https://api.angelcam.com/v1/shared-cameras', headers=headers)
        data = response.json()

        # serializer = CameraSerializer(data=data, many=True)
        # return Response(serializer.data)
        return Response(data)

class RecordingListView(APIView):
    def get(self, request, camera_id):
        headers = {
            'Authorization' : 'Bearer'
        }
        response = requests.get(f'https://api.angelcam.com/cameras/{camera_id}/recordings', headers=headers)
        data = response.json()
        serializer = RecordingSerializer(data=data, many=True)
        return Response(serializer.data)
    
class SharedRecordingView(APIView):
    def get(self, request, camera_id):
        auth = request.headers['Authorization']
        token = auth.split()[1]
        
        headers = {
            'Authorization': f'PersonalAccessToken {token}'
        }
        response = requests.get(f'https://api.angelcam.com/v1/shared-cameras/{camera_id}/recording', headers=headers)
        data = response.json()

        return Response(data)
    
class RecordingTimelineView(APIView):
    def get(self, request, camera_id):
        auth = request.headers['Authorization']
        token = auth.split()[1]

        startTime = request.GET.get('start')
        endTime = request.GET.get('end')
        
        headers = {
            'Authorization': f'PersonalAccessToken {token}'
        }
        params = {
            'start': startTime,
            'end': endTime
        }
        response = requests.get(f'https://api.angelcam.com/v1/shared-cameras/{camera_id}/recording/timeline', headers=headers, params=params)
        data = response.json()

        return Response(data)
    
class RecordingStreamView(APIView):
    def get(self, request, camera_id):
        auth = request.headers['Authorization']
        token = auth.split()[1]

        startTime = request.GET.get('start')
        
        headers = {
            'Authorization': f'PersonalAccessToken {token}'
        }
        params = {
            'start': startTime,
        }
        response = requests.get(f'https://api.angelcam.com/v1/shared-cameras/{camera_id}/recording/stream', headers=headers, params=params)
        data = response.json()

        return Response(data)
    
    