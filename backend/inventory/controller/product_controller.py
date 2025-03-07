from django.http import JsonResponse
from ..services.product_service import get_all_products

def get_products(request):
    return JsonResponse(get_all_products(), safe=False)