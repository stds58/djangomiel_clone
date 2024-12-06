from rest_framework import serializers

from .models import PersonalInfo


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'city')
