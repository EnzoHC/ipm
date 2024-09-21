from rest_framework import serializers
from ipm.models import UsersApi


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersApi
        fields = "__all__"
