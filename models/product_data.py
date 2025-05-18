from typing import List, Dict

products: List[Dict] = [
    {"id": 1, "name": "Televisor", "price": 250.99, "stock": 10, "available": True},
    {"id": 2, "name": "Bocina Estéreo", "price": 100.00, "stock": 0, "available": False},
    {"id": 3, "name": "Luces LED", "price": 29.99, "stock": 5, "available": True},
]

def update_product_stock(product: Dict, quantity: int) -> Dict:
    """Actualizar el stock y la disponibilidad del producto."""
    product['stock'] += quantity
    if product['stock'] < 0:
        product['stock'] = 0
    product['available'] = product['stock'] > 0
    return product
