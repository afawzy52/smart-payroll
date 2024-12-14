# Create a repository class to encapsulate the logic for accessing data.
from .models import company


class CompanyRepo:

    @staticmethod
    def get(pk):
        return company.objects.get(pk=pk)

    @staticmethod
    def get_all():
        return company.objects.all()
    
    @staticmethod
    def save_comapny(self, *args, **kwargs):
        super(company,self).save(*args, **kwargs)
        




