from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} profile'

class Premium(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    charge = models.IntegerField(default=100)
    # respmsg = models.TextField()
    # mid = models.TextField()
    # txnid = models.TextField()
    # banktxnid = models.IntegerField(max_length=100)
    # txndate = models.CharField(max_length=100)
    # bankname = models.CharField(max_length=100)
    # paymentmode = models.CharField(max_length=100)
    # status = models.CharField(max_length=100)
    # gatewayname = models.CharField(max_length=100)
    

    def __str__(self):
        return f'{self.user.username} is a premium user'

class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}'s message"
