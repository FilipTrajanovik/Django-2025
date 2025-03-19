from django.db import models
from django.contrib.auth.models import User


# Create your models here.





class ContactInformation(models.Model):
    street = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    telephone_number = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.street} - {self.number} - {self.telephone_number} - {self.email}'


class Product(models.Model):
    PRODUCT_TYPE = [
        ("food", "храна"),
        ("drink", "пијалок"),
        ("bakery", "пекара"),
        ("cosmetics", "козметика"),
        ("hygiene", "хигиена")
    ]
    name = models.CharField(max_length=50, null=False, blank=False)
    home = models.BooleanField(default=False)
    code = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPE, null=False, blank=False)

    def __str__(self):
        return f'{self.name} '


class Market(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    contact_info = models.ForeignKey(ContactInformation, on_delete=models.CASCADE, null=False, blank=False)
    open_date = models.DateField(null=False, blank=False)
    number_of_market = models.IntegerField(null=False, blank=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    working_hours_from = models.TimeField(null=False, blank=False)
    working_hours_to = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'

class Employee(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    embg = models.CharField(max_length=50, null=False, blank=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    paycheck = models.IntegerField(null=False, blank=False)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.surname}'


class MarketProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)