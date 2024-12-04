from django.db import models
from django.utils.translation import gettext_lazy as _


class country(models.Model):
    country_name = models.CharField(max_length=100, default='Egypt')
    country_code = models.SmallIntegerField()
    country_phone_code = models.IntegerField()

    def __str__(self):
        return self.country_name


class city(models.Model):
    city_name = models.CharField(max_length=75)
    city_code = models.SmallIntegerField()
    country = models.ForeignKey(country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class address(models.Model):
    line1 = models.CharField(max_length=75)
    line2 = models.CharField(max_length=75)
    country = models.ForeignKey (country, on_delete=models.CASCADE)
    city = models.ForeignKey(city,on_delete=models.CASCADE)
    zipcode = models.SmallIntegerField(null=True)

    def __str__(self):
        lines = [self.line1]
        if self.line2:
            lines.append(self.line2)
        lines.append(f'{self.country},{self.city}, {self.zipcode}')
        return '\n'.join(lines)


class month(models.Model):
    month_id = models.SmallIntegerField()
    month_name_eng = models.CharField(max_length=10)
    month_name_ar = models.CharField(max_length=10)
    days_in_month = models.SmallIntegerField()



