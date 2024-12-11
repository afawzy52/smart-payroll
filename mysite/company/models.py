import uuid
from django.core.serializers import serialize
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ValueObjects.models import country, city, business_type
from django.utils.translation import gettext_lazy as _
from .choices import business_type_category






# Create your models here.
class company(models.Model):
    class OwnershipChoices(models.TextChoices):
        private = 'Private', _('Private')
        public = 'Public', _('Public')
        corporation = 'Corporation', _('Corporation')
        limited = 'Limited', _('Limited')
        partnership = 'Partnership', _('Partnership')
        nonprofit  = 'Nonprofit ', _('Nonprofit ')

    manager_incharge = models.ForeignKey(User,on_delete=models.CASCADE)
    com_id = models.AutoField(primary_key=True)
    com_slug = models.UUIDField(default=uuid.uuid4, db_index=True)
    com_name = models.CharField(max_length=200, null=True)
    com_short_name = models.CharField(max_length=100, null=True)
    com_address = models.CharField(max_length=250, null= True)
    country = models.ForeignKey(country, on_delete=models.CASCADE, default=1)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    phone = models.CharField(max_length=17, null=True)
    legal_form = models.CharField(max_length= 35, choices=OwnershipChoices, null=True)
    business_type = models.CharField(max_length= 150, choices= business_type_category, null=True)
    com_email = models.EmailField(max_length=254, null=True)
    owner_name = models.CharField(max_length=250, null=True)
    tax_office = models.CharField(max_length=150, null=True)
    tax_no = models.IntegerField(null=True)
    soc_in_office = models.CharField(max_length=150, null=True)
    soc_in_no = models.IntegerField(null=True)
    website = models.URLField(max_length=350 ,null=True)
    created_at = models.DateTimeField(datetime.now(), auto_now=True)

    def __str__(self):
        Name= self.com_name
        if self.com_short_name:
            Name = self.com_short_name
        return Name


    def __unicode__(self):
        return unicode(self.user)