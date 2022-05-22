from rest_framework import serializers

from blog.models import Note

# def note_to_json(note):
#     return {
#         'id': note.id,
#         'title': note.title,
#         'message': note.message,
#         'public': note.public,
#         'date_public': note.date_public,
#         'update': note.update,
#     }


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('author',)
