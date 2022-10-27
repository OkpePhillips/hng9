from rest_framework import serializers
from .models import MyDetail

class MyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDetail
        fields = ('slackUsername', 'backend', 'age', 'bio',)