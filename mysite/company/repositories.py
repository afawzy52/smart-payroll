# Create a repository class to encapsulate the logic for accessing data.
from .models import company


class CompanyRepo:
    @staticmethod
    def get_company(com_id):
        return company.objects.get(pk=com_id)

    @staticmethod
    def get_all_companies():
        return company.objects.all()
    




