from django.urls import path

from blog.views import (
    BlogCategoryCreateAPIView,
    BlogCategoryDestroyAPIView,
    BlogCategoryDetailAPIView,
    BlogCategoryListAPIView,
    BlogCategroyUpdateAPIView,
    BlogPostCreateAPIView,
    BlogPostDestroyAPIView,
    BlogPostDetailAPIView,
    BlogPostListAPIView,
    BlogPostUpdateAPIView,
    CommentCreateAPIView,
    CommentDestroyAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
    CommentUpdateAPIView,
    TagCreateAPIView,
    TagDestroyAPIView,
    TagDetailAPIView,
    TagListAPIView,
    TagUpdateAPIView,
)

urlpatterns = [
    path("categories/", BlogCategoryListAPIView.as_view(), name="blogcategory-list"),
    path(
        "categories/create/",
        BlogCategoryCreateAPIView.as_view(),
        name="blogcategory-create",
    ),
    path(
        "categories/<int:id>/",
        BlogCategoryDetailAPIView.as_view(),
        name="blogcategory-detail",
    ),
    path(
        "categories/<int:id>/update/",
        BlogCategroyUpdateAPIView.as_view(),
        name="blogcategory-update",
    ),
    path(
        "categories/<int:id>/delete/",
        BlogCategoryDestroyAPIView.as_view(),
        name="blogcategory-delete",
    ),
    path("posts/", BlogPostListAPIView.as_view(), name="blogpost-list"),
    path("posts/create/", BlogPostCreateAPIView.as_view(), name="blogpost-create"),
    path("posts/<int:id>/", BlogPostDetailAPIView.as_view(), name="blogpost-detail"),
    path(
        "posts/<int:id>/update/",
        BlogPostUpdateAPIView.as_view(),
        name="blogpost-update",
    ),
    path(
        "posts/<int:id>/delete/",
        BlogPostDestroyAPIView.as_view(),
        name="blogpost-delete",
    ),
    path("tags/", TagListAPIView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateAPIView.as_view(), name="tag-create"),
    path("tags/<int:id>/", TagDetailAPIView.as_view(), name="tag-detail"),
    path("tags/<int:id>/update/", TagUpdateAPIView.as_view(), name="tag-update"),
    path("tags/<int:id>/delete/", TagDestroyAPIView.as_view(), name="tag-delete"),
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
    path("comments/create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("comments/<int:id>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    path(
        "comments/<int:id>/update/",
        CommentUpdateAPIView.as_view(),
        name="comment-update",
    ),
    path(
        "comments/<int:id>/delete/",
        CommentDestroyAPIView.as_view(),
        name="comment-delete",
    ),
]
