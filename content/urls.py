from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.Search.as_view(), name='search'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('create/blog/', views.BlogCreateView.as_view(), name='blog_create'),
    path('create/blog_category/', views.BlogCategoryCreateView.as_view(), name='blog_category_create'),
    path('blog/<int:pk>/', views.BlogArchiveByCategoryPK.as_view(), name='blog_archive_by_category_pk'),
    path('blog/<str:slug>/', views.BlogSingle.as_view(), name='blog_single'),
    path('create/video_cast_category/', views.VideocastCategoryCreateView.as_view(), name='video_cast_category_create'),
    path('video_cast/', views.Videocast.as_view(), name='video_cast'),
    path('create/video_cast/', views.VideocastCreateView.as_view(), name='video_cast_create'),
    path('video_cast/<int:pk>/', views.VideocastArchiveByCategoryPK.as_view(), name='video_cast_archive_by_category_pk'),
    path('video_cast/<str:slug>/', views.VideocastSingle.as_view(), name='video_cast_single'),
    path('create/podcast_category/', views.PodcastCategoryCreateView.as_view(), name='podcast_category_create'),
    path('podcast/', views.Podcast.as_view(), name='podcast'),
    path('create/podcast/', views.PodcastCreateView.as_view(), name='podcast_create'),
    path('podcast/<int:pk>/', views.PodArchiveByCategoryPK.as_view(), name='podcast_archive_by_category_pk'),
    path('podcast/<str:slug>/', views.PodSingle.as_view(), name='podcast_single'),
    path('create/skill/', views.SkillCreateView.as_view(), name='skill_create'),
]
