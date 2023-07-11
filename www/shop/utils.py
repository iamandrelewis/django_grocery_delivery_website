import uuid

def generate_product_id():
    code = str(uuid.uuid4().int)[:12]
    return code
