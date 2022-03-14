from rest_framework import serializers
from .models import UserManger


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=4, write_only=True)
    class Meta:
        model = UserManger
        fields = ['email', 'user_name', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManger
        fields = ('id', 'user_name', 'email', 'first_name', 'last_name')