from rest_framework import serializers
from ..models import Article, Category, Tag, Comment, SubContent, SubContentImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MiniSubContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = '__all__'


class MiniSubContentSerializer(serializers.ModelSerializer):
    subcontentimage = MiniSubContentImageSerializer(read_only=True, many=True)
    class Meta:
        model = SubContent
        fields = ['id', 'description2', 'subcontentimage']


class ArticleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    subcontent = MiniSubContentSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'description', 'image', 'category', 'tags', 'subcontent', 'created_date']


class ArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'article': {'required': False}
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        message = validated_data.get('message')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, message=message)
        return instance


class SubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = '__all__'
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_date):
        article_id = self.context['article_id']
        description2 = validated_data.get('description2')
        instance = SubContent.objects.create(article_id=article_id, description2=description2)
        return instance



class SubContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = '__all__'