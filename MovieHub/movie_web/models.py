from django.db import models
from datetime import datetime

# Create your models here.

# Customer Model
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=100)
    password_salt = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.IntegerField()
    bank_card = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'username': self.username, 'password_hash': self.password_hash, 'password_salt': self.password_salt,
                'name': self.name, 'email': self.email, 'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'phone': self.phone, 'bank_card': self.bank_card,
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "Customer"


# Bank Card Model
