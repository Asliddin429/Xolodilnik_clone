from django.urls import path

from common.views import (
    SponsorCreateAPIView,
    SponsorDestroyAPIView,
    SponsorDetailAPIView,
    SponsorListAPIView,
    SponsorUpdateAPIView,
)

urlpatterns = [
    path("sponsors/", SponsorListAPIView.as_view(), name="sponsor-list"),
    path("sponsors/create/", SponsorCreateAPIView.as_view(), name="sponsor-create"),
    path("sponsors/<int:id>/", SponsorDetailAPIView.as_view(), name="sponsor-detail"),
    path(
        "sponsors/<int:id>/update/",
        SponsorUpdateAPIView.as_view(),
        name="sponsor-update",
    ),
    path(
        "sponsors/<int:id>/delete/",
        SponsorDestroyAPIView.as_view(),
        name="sponsor-delete",
    ),
]
