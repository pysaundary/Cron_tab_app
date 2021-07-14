from rest_framework import serializers,fields
from .models import Students,subject_choices

class StudentSerializer(serializers.ModelSerializer):

    profile_pic_url= serializers.SerializerMethodField()
    subject=fields.MultipleChoiceField(choices=subject_choices)
    class Meta:
        model=Students
        fields=['id','name','sex','profile_pic_url','is_active','subject']
    def get_profile_pic_url(self, student):
        request = self.context.get('request')
        profile_pic_url = student.profile_pic.url
        print(profile_pic_url)
        return request.build_absolute_uri(profile_pic_url)
