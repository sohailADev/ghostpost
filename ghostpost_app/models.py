from django.db import models

# Create your models here.
class BoastsRoastsModel(models.Model):
    
    isboast = models.BooleanField()
    post_body = models.CharField( max_length=280)
    post_upvote = models.IntegerField(default=0)
    post_downvote = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    s_key = models.CharField(max_length=10)
    # post_total = models.IntegerField()
    def __str__(self):
        return self.post_body   
    @property 
    def total(self):
        total =   self.post_upvote + self.post_downvote
        return total



