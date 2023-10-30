from django.db import models

class OrderQuery(models.Model):
    user_id = models.CharField(max_length=50, default='HappyUser')
    user_query = models.TextField(default='', max_length=1000)
    expert_answer = models.TextField(default='')