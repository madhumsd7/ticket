from django.db import models
import uuid

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    mobile_no = models.CharField(max_length = 30)


    def __str__(self):
        return self.name

class Agent(models.Model):
    ROLE_CHOICES = (
               ('SUPERVISOR','SUPERVISOR'),
               ('ACCOUNT MANAGER','ACCOUNT MANAGER'), 
        )

    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    mobile_no = models.CharField(max_length = 30)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    def __str__(self):
        return self.name



class Ticket(models.Model):
    PRIORITY_CHOICES = (
               ('HIGH','HIGH'),
               ('MEDIUM','MEDIUM'),
               ('LOW','LOW'),   
        )
    CREATED_CHOICES = (
               ('MADHU','MADHU'),
               ('JAGADEESH','JAGADEESH'),
               ('PRABHU','PRABHU'),   
        )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('user',on_delete=models.PROTECT)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    link = models.CharField(max_length = 20)
    description = models.TextField(max_length=50)
    assinged_to = models.ForeignKey('Agent',on_delete=models.PROTECT)
    history = models.CharField(max_length = 20)
    created_by =  models.CharField(max_length=10, choices=CREATED_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name