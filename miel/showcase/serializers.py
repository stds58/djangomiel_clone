from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import CandidateCard, Office, Status, Experience, PersonalInfo, Course, Skill, CandidateCourse, \
    CandidateSkill

User = get_user_model()


class InvitationToOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('name',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


class ExperienceSerializer(serializers.ModelSerializer):
    date_start = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    date_end = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = Experience
        fields = (
            'workplace',
            'occupation',
            'date_start',
            'date_end',
        )


class PersonalInfoSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(PersonalInfo.Genders, source='get_gender_display')  # TODO чекнуть
    email = serializers.EmailField()
    contact_link = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = PersonalInfo
        fields = (
            'email',
            'phone',
            'contact_link',
            'first_name',
            'last_name',
            'middle_name',
            'city',
            'gender',
            'date_of_birth',
        )


class CourseSerializer(serializers.ModelSerializer):
    progress = serializers.IntegerField()

    class Meta:
        model = Course
        has_through_model = CandidateCourse
        fields = (
            'name',
            'progress',
        )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        has_through_model = CandidateSkill
        fields = ('name',)


class CandidateCardSerializer(WritableNestedModelSerializer):  # TODO
    invitation_to_office = InvitationToOfficeSerializer(allow_null=True, many=True, required=False)
    experience = ExperienceSerializer(many=True, required=False)
    personal_info = PersonalInfoSerializer()
    course = CourseSerializer(read_only=True, source='course_set', required=False)
    skills = SkillSerializer(read_only=True, source='skills_set', required=False)
    comment = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = CandidateCard
        fields = '__all__'
        read_only_fields = ('id',)

#  By default, relational fields that target a
#  ManyToManyField with a through model specified are set to read-only.
#
# If you explicitly specify a relational field
# pointing to a ManyToManyField with a through model,
# be sure to set read_only to True.
