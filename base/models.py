from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userTime(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    middle_initial = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    monday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    monday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    monday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    monday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    tuesday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    tuesday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    tuesday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    tuesday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    wednesday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    wednesday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    wednesday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    wednesday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    thursday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    thursday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    thursday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    thursday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    friday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    friday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    friday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    friday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    saturday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    saturday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    saturday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    saturday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    sunday_morning_time_in = models.CharField(max_length=100, blank=True, null=True)
    sunday_morning_time_out = models.CharField(max_length=100, blank=True, null=True)
    sunday_afternoon_time_in = models.CharField(max_length=100, blank=True, null=True)
    sunday_afternoon_time_out = models.CharField(max_length=100, blank=True, null=True)
    monday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_in_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_out_morning_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_in_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_out_afternoon_overload_undergrad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    monday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    tuesday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    wednesday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    thursday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    friday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    saturday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_in_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_out_morning_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_in_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)
    sunday_time_out_afternoon_overload_grad = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.user.username

