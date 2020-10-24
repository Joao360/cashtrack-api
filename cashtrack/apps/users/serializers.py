from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User
from .authentication import token_expire_handler, expires_in


class UserSerializer(serializers.HyperlinkedModelSerializer):
    money_deposits = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="moneydeposit-detail"
    )
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()
    token_expires_in = serializers.SerializerMethodField()

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        is_expired, token = token_expire_handler(token)
        return token.key

    def get_token_expires_in(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        is_expired, token = token_expire_handler(token)
        return expires_in(token)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "money_deposits",
            "token",
            "token_expires_in",
        ]


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
