
from tortoise import fields
from tortoise.models import Model

class APIKey(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)
    key = fields.CharField(max_length=255, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
