from django.db import models

# Create your models here.

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_title = models.CharField(max_length=30)
    ticket_description = models.TextField()
    ticket_state = models.IntegerField(default=0)
    user_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=30)
