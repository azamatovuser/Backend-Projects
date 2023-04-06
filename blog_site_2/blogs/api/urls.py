from django.urls import path
from .views import ArticleListCreateApiView, CategoryListCreateApiView, TagListCreateApiView, \
    CommentListCreateApiView, SubContentImageListCreateApiView, SubContentListCreateApiView, \
    ArticleRUDApiView, CategoryRUDApiView, TagRUDApiView, CommentRUDApiView, SubContentRUDApiView, \
    SubContentImageRUDApiView


urlpatterns = [
    path('article/', ArticleListCreateApiView.as_view()),
    path('article_rud/<int:pk>/', ArticleRUDApiView.as_view()),
    path('category/', CategoryListCreateApiView.as_view()),
    path('category_rud/<int:pk>/', CategoryRUDApiView.as_view()),
    path('tag/', TagListCreateApiView.as_view()),
    path('tag_rud/<int:pk>/', TagRUDApiView.as_view()),
    path('article/<int:article_id>/comment/', CommentListCreateApiView.as_view()),
    path('comment_rud/<int:pk>/', CommentRUDApiView.as_view()),
    path('article/<int:article_id>/subcontent/', SubContentListCreateApiView.as_view()),
    path('subcontent_rud/<int:pk>/', SubContentRUDApiView.as_view()),
    path('article/<int:article_id>/subcontent_image/', SubContentImageListCreateApiView.as_view()),
    path('subcontent_image_rud/<int:pk>/', SubContentImageRUDApiView.as_view()),
]