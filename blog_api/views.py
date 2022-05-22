from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from blog.models import Note
from . import serializers, filters


class NoteListCreateAPIView(APIView):

    def get(self, request: Request):
        objects = Note.objects.all()
        serializer = serializers.NoteSerializer(
            instance=objects,
            many=True,
            )
        return Response(data=serializer.data)

    def post(self, request: Request):
        serializer = serializers.NoteSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PublicNotListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializers_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)  # author=self.request.user, public=True

    def filter_queryset(self, queryset):
        return filters.note_filter_by_author_id(
            queryset,
            author_id=self.request.query_params.get('author_id', None)
        )
