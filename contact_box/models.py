from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, null=True)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.SmallIntegerField()
    apartment_number = models.SmallIntegerField(null=True)


class Phone(models.Model):
    type = (
        (1, "prywatny"),
        (2, "służbowy"),
        (3, "domowy"),
        (4, "inny"),
    )
    phone_number = models.IntegerField()
    phone_type = models.SmallIntegerField(choices=type, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        phone_type = ""
        if self.phone_type:
            phone_type += f", numer {self.get_phone_type_display()}"
        return f"{self.phone_number} {phone_type}"

class Email(models.Model):
    type = (
        (1, "prywatny"),
        (2, "służbowy"),
        (3, "inny"),
    )
    email = models.EmailField(max_length=64)
    email_type = models.SmallIntegerField(choices=type, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        email_type = ""
        if self.email_type:
            email_type += f", e-mail {self.get_email_type_display()}"
        return f"{self.email} {email_type}"

class Groups(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)
