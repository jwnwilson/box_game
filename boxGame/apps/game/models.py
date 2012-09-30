from django.db import models
 
class GameScores(models.Model):
    username = models.CharField(null=True, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    timepassed = models.FloatField()
    ip = models.IPAddressField()
