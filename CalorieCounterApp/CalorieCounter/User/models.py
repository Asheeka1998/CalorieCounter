import os

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    mail_id = models.CharField(max_length=200, null=False)


# Create your models here.
class UserNewActivity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Activity_name = models.CharField(max_length=20, null=False)
    time_duration = models.TimeField()
    calorie_burns = models.FloatField()
    Status = models.CharField(max_length=10, null=False)


# Create your models here.
class UserNewItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Item_name = models.CharField(max_length=20, null=False)
    calorie = models.FloatField()
    Status = models.CharField(max_length=20, null=False)


# Create your models here.
class FoodConsumption(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_food = models.CharField(max_length=20, null=False)
    today_date = models.DateField()
    quantity_consumed = models.FloatField(default=0)
    calorie_count = models.CharField(max_length=20, default=0, null=True, blank=True)


class ActivityPerformed(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    today_date = models.DateField()
    selected_activity = models.CharField(max_length=200, null=False)
    time_spent = models.CharField(max_length=200, default=0, null=True, blank=True)
    calorie_burn = models.CharField(max_length=200, default=0, null=True, blank=True)

    # def save(self, *args, **kwargs):  # new
    #     if self.selected_food is not None:
    #         self.amount = (self.selected_food.calories / self.selected_food.quantity_consumed)
    #         self.calorie_count = self.amount * self.quantity
    #         self.total_calorie = self.calorie_count + self.total_calorie
    #         calories = userProfile.objects.filter(person_of=self.user_profile).last()
    #         PostFood.objects.create(profile=calories, food=self.selected_food, calorie_amount=self.calorie_count,
    #                                 amount=self.quantity_consumed)
    #         self.selected_food = None
    #         super(userProfile, self).save(*args, **kwargs)
    #
    #     else:
    #         super(userProfile, self).save(*args, **kwargs)
    #
    # def __str__(self):
    #     return str(self.profile_name.username)
