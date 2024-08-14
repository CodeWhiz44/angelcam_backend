from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    token = serializers.CharField()

class CameraSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()

class RecordingSerializer(serializers.Serializer):
    id = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()