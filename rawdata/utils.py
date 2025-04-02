import uuid

def gen_unique_code(model_class, field_name, length=5):
    for _ in range(100):
        code = uuid.uuid4().hex.upper()[:length]
        if not model_class.objects.filter(**{field_name: code}).exists():
            return code
    raise ValueError("Unable to generate unique UUID-based code.")