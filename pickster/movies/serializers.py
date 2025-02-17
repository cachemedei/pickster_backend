from rest_framework import serializers
from django.apps import apps

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('movies.Movie')
        fields = '__all__'