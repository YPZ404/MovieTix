from django.db import models
from datetime import datetime


# Staff Model
class Staff(models.Model):
    staff_id = models.IntegerField()
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=0)  # level 0: normal 1:manager
    phone = models.IntegerField()
    email = models.CharField(max_length=40)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'staff_id': self.staff_id, 'password': self.password, 'name': self.name, 'level': self.level,
                'phone': self.phone, 'email': self.email, 'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "Staff"
