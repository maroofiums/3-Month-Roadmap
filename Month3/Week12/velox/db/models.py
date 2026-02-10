class Field:
    def __init__(self, type="TEXT"):
        self.type = type

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value.type

        attrs["_fields"] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    pass
