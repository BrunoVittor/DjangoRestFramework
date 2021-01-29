from app.models import Todo
from rest_framework import serializers

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'created_at']
