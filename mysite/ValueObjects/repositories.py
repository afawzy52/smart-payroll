# Create a repository class to encapsulate the logic for accessing data.

from .models import country, city

def cityToConutry (country_id):
    return city.objects.filter(country_id=country_id)

  
        


