from django.db import models

# Create your models here.
class Anchor(models.Model):
    #头像链接
    head_img_src = models.CharField(max_length = 200)
    #主播名
    name = models.CharField(max_length = 100)
    #id
    id = models.CharField(max_length = 20,primary_key=True)
    #content
    content = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.name

    class Mate:
        ordering = ['-date_time']
