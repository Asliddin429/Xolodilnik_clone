from django.urls import path

from users.views import (
    LoginUserView,
    LogoutUserView,
    ProfessionCreateAPIView,
    ProfessionDestroyAPIView,
    ProfessionDetailAPIView,
    ProfessionListAPIView,
    ProfessionUpdateAPIView,
    ProfileUpdateView,
    RegisterUserView,
    UserDetailAPIView,
    UserListAPIView,
    UserProfileAPIViewByHand,
)

urlpatterns = [
    # Templates
    path("template/register/", RegisterUserView.as_view(), name="register-template"),
    path("template/login/", LoginUserView.as_view(), name="login-template"),
    path("template/logout/", LogoutUserView.as_view(), name="logout-template"),
    path("template/profile/", ProfileUpdateView.as_view(), name="profile-template"),
    # APIs
    path("api/user-profile/", UserProfileAPIViewByHand.as_view(), name="user-profile"),
    path("api/user-detail/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("api/user-list/", UserListAPIView.as_view(), name="user-list"),
    path(
        "api/profession-create/",
        ProfessionCreateAPIView.as_view(),
        name="profession-create",
    ),
    path(
        "api/profession-detail/<int:pk>/",
        ProfessionDetailAPIView.as_view(),
        name="profession-detail",
    ),
    path(
        "api/profession-list/", ProfessionListAPIView.as_view(), name="profession-list"
    ),
    path(
        "api/profession-update/<int:pk>/",
        ProfessionUpdateAPIView.as_view(),
        name="profession-update",
    ),
    path(
        "api/profession-destroy/<int:pk>/",
        ProfessionDestroyAPIView.as_view(),
        name="profession-destroy",
    ),
]
