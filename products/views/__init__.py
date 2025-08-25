from .product_create import ProductCreateAPIView
from .product_destroy import ProductDestroyAPIView
from .product_detail import ProductDetailAPIView
from .product_list import ProductListAPIView
from .product_update import ProductUpdateAPIView
from .productcat_create import ProductCategoryCreateAPIView
from .productcat_destroy import ProductCategoryDestroyAPIView
from .productcat_detail import ProductCategoryDetailAPIView
from .productcat_list import ProductCategoryListAPIView
from .productcat_update import ProductCategoryUpdateAPIView
from .productvar_create import ProductVariantCreateAPIView
from .productvar_destroy import ProductVariantDestroyAPiView
from .productvar_detail import ProductVarinatDetailAPIView
from .productvar_list import ProductVariantListAPIView
from .productvar_update import ProductVariantUpdateAPIView

__all__ = [
    "ProductCategoryCreateAPIView",
    "ProductCategoryDestroyAPIView",
    "ProductCategoryDetailAPIView",
    "ProductCategoryListAPIView",
    "ProductCategoryUpdateAPIView",
    "ProductCreateAPIView",
    "ProductDestroyAPIView",
    "ProductDetailAPIView",
    "ProductListAPIView",
    "ProductUpdateAPIView",
    "ProductVariantCreateAPIView",
    "ProductVariantDestroyAPiView",
    "ProductVariantListAPIView",
    "ProductVariantUpdateAPIView",
    "ProductVarinatDetailAPIView",
]
