from rest_framework import generics, permissions, status
from .serializers import ArticleGetSerializer, ArticlePostSerializer, CategorySerializer, TagSerializer, \
    CommentSerializer, SubContentSerializer, SubContentImageSerializer, MiniSubContentSerializer, MiniSubContentImageSerializer
from ..models import Article, Category, Tag, Comment, SubContent, SubContentImage
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q


class ArticleListCreateApiView(generics.ListCreateAPIView):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        q_condition = Q()
        tag_condition = Q()
        cat_condition = Q()
        if q:
            q_condition = Q(title__icontains=q)
        if tag:
            tag_condition = Q(tag__title__exact=tag)
        if cat:
            cat_condition = Q(category__title__exact=cat)
        qs = qs.filter(q_condition, tag_condition, cat_condition)
        return qs


class CategoryListCreateApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateApiView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentListCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class SubContentListCreateApiView(generics.ListCreateAPIView):
    queryset = SubContent.objects.all()

    def get_queryset(self, *args, **kwargs):
        sb = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            sb = sb.filter(article_id=article_id)
            return sb
        return []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MiniSubContentSerializer
        return SubContentSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx



class SubContentImageListCreateApiView(generics.ListCreateAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializer

class ArticleRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer



class CategoryRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class TagRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]


class CommentRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class SubContentRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubContent.objects.all()
    serializer_class = SubContentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class SubContentImageRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializer
    permission_classes = [IsOwnerOrReadOnly]