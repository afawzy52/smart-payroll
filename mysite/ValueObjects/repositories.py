# Create a repository class to encapsulate the logic for accessing data.
from .models import business_type


class business_type_repo:
    def get_all_business_types():
        return business_type.objects.all()
        

get_all = business_type_repo().get_all_business_types()
print(get_all)
