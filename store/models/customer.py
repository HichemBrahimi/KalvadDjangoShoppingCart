from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
