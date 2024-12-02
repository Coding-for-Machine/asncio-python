from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    street = fields.CharField(max_length=255, null=True)
    city = fields.CharField(max_length=100, null=True)

    class Meta:
        table = "users"
     # to_dict metodini yaratish
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "street": self.street,
            "city": self.city
        }