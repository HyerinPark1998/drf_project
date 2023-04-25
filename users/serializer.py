from rest_framework import serializers
from users.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from articles.serializers import ArticleSerializer


class UserProfileSerializers(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    article_set = ArticleSerializer(many=True)
    like_articles = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'followings', 'followers',
                  'article_set', "like_articles")


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token
