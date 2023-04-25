from django.urls import path
from articles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(),
         name='articledetail_view'),
    path('<int:article_id>/comment/',
         views.CommentView.as_view(), name='comment_view'),
    path('<int:article_id>/comment/<int:comment_id>/',
         views.CommentDetailView.as_view(), name='commentdetail_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='like_view'),
    path('feed/', views.FeedView.as_view(), name='feed_view')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
