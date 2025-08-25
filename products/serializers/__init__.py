from .product_create import ProductCreateSerializer
from .product_destroy import ProductDestroySerializer
from .product_detail import ProductDetailSerializer
from .product_list import ProductListSerializer
from .product_update import ProductUpdateSerializer
from .productcat_create import ProductCategoryCreateSerializer
from .productcat_destroy import ProductCategoryDestroySerializer
from .productcat_detail import ProductCategoryDetailSerializer
from .productcat_list import ProductCategoryListSerializer
from .productcat_update import ProductCategoryUpdateSerializer
from .productvar_create import ProductVariantCreateSerializer
from .productvar_destroy import ProductVariantDestroySerializer
from .productvar_detail import ProductVariantDetailSerializer
from .productvar_list import ProductVariantListSerializer
from .productvar_update import ProductVariantUpdateSerializer

__all__ = [
    "ProductCategoryCreateSerializer",
    "ProductCategoryDestroySerializer",
    "ProductCategoryDetailSerializer",
    "ProductCategoryListSerializer",
    "ProductCategoryUpdateSerializer",
    "ProductCreateSerializer",
    "ProductDestroySerializer",
    "ProductDetailSerializer",
    "ProductListSerializer",
    "ProductUpdateSerializer",
    "ProductVariantCreateSerializer",
    "ProductVariantDestroySerializer",
    "ProductVariantDetailSerializer",
    "ProductVariantListSerializer",
    "ProductVariantUpdateSerializer",
]
