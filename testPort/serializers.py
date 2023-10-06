from rest_framework import serializers
from testPort.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','profile_image']
        # profile_image = serializers.ImageField(required=False)
    def validate(self, data):
        errors = {}
        for field in ['username', 'email', 'password','profile_image']:
            if not data.get(field):
                errors[field] = [f'This field is required.']

        if errors:
            raise serializers.ValidationError(errors)

        return data

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     user = UserProfile.objects.create(**validated_data)

    #     if password:
    #         user.set_password(password)
    #         user.save()

    #     return user

    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError('Username and password are required.')

        return data 