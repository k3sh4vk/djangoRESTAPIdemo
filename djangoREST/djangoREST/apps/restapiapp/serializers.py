from rest_framework import serializers
from .models import webUsers

class webUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = webUsers
        fields = "__all__"