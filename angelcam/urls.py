from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('cameras', views.CameraListView.as_view()),
    path('cameras/<str:camera_id>/recordings', views.RecordingListView.as_view()),
    path('shared-cameras/<str:camera_id>/recording', views.SharedRecordingView.as_view()),
    path('shared-cameras/<str:camera_id>/recording/stream', views.RecordingStreamView.as_view()),
    path('shared-cameras/<str:camera_id>/recording/timeline', views.RecordingTimelineView.as_view()),
]