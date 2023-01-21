from django.db import models

FLOAT_FIELD = models.FloatField(default=0, null=False)


# Create your models here.
class Foods(models.Model):
    name = models.CharField(max_length=200, null=False)
    type = models.CharField(max_length=200, null=False)
    calories = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.name


class Activities(models.Model):
    Activity_name = models.CharField(max_length=200, null=False)
    time_duration = models.IntegerField(null=False)
    calorie_burns = FLOAT_FIELD
