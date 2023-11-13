from django.db import models

class OrderQuery(models.Model):
    user_id = models.CharField(max_length=50, default='Shopper')
    user_query = models.TextField(default='', max_length=500)
    expert_answer = models.TextField(default='', max_length=1000)

class OrderDetails(models.Model):
    user_id = models.CharField(max_length=50, default='Shopper')