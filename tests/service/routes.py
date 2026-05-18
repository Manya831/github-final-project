products = []

def read_product(product_id):
    return {"id": product_id, "name": "Laptop"}

def update_product(product_id, data):
    return {"id": product_id, **data}

def delete_product(product_id):
    return True

def list_products():
    return products

def find_by_name(name):
    return [p for p in products if p.get("name") == name]

def find_by_category(category):
    return [p for p in products if p.get("category") == category]

def find_by_availability(status):
    return [p for p in products if p.get("available") == status]
