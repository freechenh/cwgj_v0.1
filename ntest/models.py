from django.db import models

# Create your models here.



class case_eg(models.Model):
    case_id = models.AutoField(primary_key=True,null=False)
    url = models.CharField(max_length=100)
    case_name = models.CharField(max_length=50)
    header_parameter = models.TextField()
    content_parameter = models.TextField()
    tk_parameter = models.CharField(max_length=40)


    def __str__(self):
        return self.case_name


class Environment(models.Model):
    env_id = models.AutoField(primary_key=True,null=False)
    url = models.CharField(max_length=100)
    env_name = models.TextField()

    def __str__(self):
        return self.env_name

