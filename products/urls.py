from django.urls import path

from products.views import (
    ProductCategoryCreateAPIView,
    ProductCategoryDestroyAPIView,
    ProductCategoryDetailAPIView,
    ProductCategoryListAPIView,
    ProductCategoryUpdateAPIView,
    ProductCreateAPIView,
    ProductDestroyAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
    ProductUpdateAPIView,
    ProductVariantCreateAPIView,
    ProductVariantDestroyAPiView,
    ProductVariantListAPIView,
    ProductVariantUpdateAPIView,
    ProductVarinatDetailAPIView,
)

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("products/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("products/<int:id>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path(
        "products/<int:id>/update/",
        ProductUpdateAPIView.as_view(),
        name="product-update",
    ),
    path(
        "products/<int:id>/delete/",
        ProductDestroyAPIView.as_view(),
        name="product-delete",
    ),
    path(
        "productcategories/",
        ProductCategoryListAPIView.as_view(),
        name="productcategory-list",
    ),
    path(
        "productcategories/create/",
        ProductCategoryCreateAPIView.as_view(),
        name="productcategory-create",
    ),
    path(
        "productcategories/<int:id>/",
        ProductCategoryDetailAPIView.as_view(),
        name="productcategory-detail",
    ),
    path(
        "productcategories/<int:id>/update/",
        ProductCategoryUpdateAPIView.as_view(),
        name="productcategory-update",
    ),
    path(
        "productcategories/<int:id>/delete/",
        ProductCategoryDestroyAPIView.as_view(),
        name="productcategory-delete",
    ),
    path(
        "productvariants/",
        ProductVariantListAPIView.as_view(),
        name="productvariant-list",
    ),
    path(
        "productvariants/create/",
        ProductVariantCreateAPIView.as_view(),
        name="productvariant-create",
    ),
    path(
        "productvariants/<int:id>/",
        ProductVarinatDetailAPIView.as_view(),
        name="productvariant-detail",
    ),
    path(
        "productvariants/<int:id>/update/",
        ProductVariantUpdateAPIView.as_view(),
        name="productvariant-update",
    ),
    path(
        "productvariants/<int:id>/delete/",
        ProductVariantDestroyAPiView.as_view(),
        name="productvariant-delete",
    ),
]
