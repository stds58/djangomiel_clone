import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import PersonalInfo, CandidateCard


# class CandidateCardModel:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# class PersonalInfoSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField()

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"






# def encode():
#     model = CandidateCardModel('Semen', 'Firsov')
#     model_sr = PersonalInfoSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"first_name":"Semen","last_name":"Firsov"}')
#     data = JSONParser().parse(stream)
#     serializer = PersonalInfoSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
