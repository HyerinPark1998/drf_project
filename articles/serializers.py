from rest_framework import serializers
from articles.models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Comment
        fields = ('user', 'content', 'created_at', 'updated_at',)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image')


class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return obj.comment_set.count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content',
                  'image', 'updated_at', 'likes_count', 'comment_count',)
