from django.contrib import admin
from .models import Note


@admin.register(Note)  # связываем админку с моделью
class NoteAdmin(admin.ModelAdmin):
    pass
