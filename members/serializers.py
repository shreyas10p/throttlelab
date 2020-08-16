from rest_framework import serializers
from .models import User, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityPeriod
        fields = ['start_time','end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(read_only=True,many=True,source='activityperiod_set')
    class Meta:
        model = User
        fields = ['id','real_name','tz','activity_periods']


