from .profession_create import ProfessionCreateAPIView
from .profession_destroy import ProfessionDestroyAPIView
from .profession_detail import ProfessionDetailAPIView
from .profession_list import ProfessionListAPIView
from .profession_update import ProfessionUpdateAPIView
from .template_view import (
    LoginUserView,
    LogoutUserView,
    ProfileUpdateView,
    RegisterUserView,
)
from .user_detail import UserDetailAPIView
from .user_list import UserListAPIView
from .user_profile import UserProfileAPIViewByHand

__all__ = [
    "LoginUserView",
    "LogoutUserView",
    "ProfessionCreateAPIView",
    "ProfessionDestroyAPIView",
    "ProfessionDetailAPIView",
    "ProfessionListAPIView",
    "ProfessionUpdateAPIView",
    "ProfileUpdateView",
    "RegisterUserView",
    "UserDetailAPIView",
    "UserListAPIView",
    "UserProfileAPIViewByHand",
]
