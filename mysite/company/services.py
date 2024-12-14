""" from .repository import CompanyRepo

class services:
    def update(*args, **kwargs):
        return CompanyRepo.save(*args, **kwargs)

    def get_all():
        return CompanyRepo.get_all() """
        

