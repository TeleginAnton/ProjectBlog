from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.NoteListCreateAPIView.as_view()),
    path('notes/public/', views.PublicNotListAPIView.as_view()),
]
