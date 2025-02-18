from rest_framework import serializers
from django.apps import apps

class MovieSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = apps.get_model('movies.Movie')
        fields = '__all__'
