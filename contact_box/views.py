from django.shortcuts import render, redirect
from django.views import View
from .models import *
# Create your views here.


class NewPerson(View):
    def get(self, request):
        return render(request, "contact_box/add_new_person.html")

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        description = request.POST.get("description")
        new_person = Person.objects.create(name=name, surname=surname, description=description)
        id = new_person.id
        return redirect("/show/%s" % id)


def show_person(request, id):
    person = Person.objects.get(pk=id)
    phone_numbers = person.phone_set.all()
    email_addresses = person.email_set.all()
    ctx = {
       "person" : Person.objects.get(pk=id),
        "phone_numbers" : phone_numbers,
        "email_addresses" : email_addresses,
    }
    return render(request, "contact_box/show_person.html", ctx)


def show_all_contacts(request):
    ctx = {
        "contacts" : Person.objects.all().order_by("name", "surname")
    }
    return render(request, "contact_box/show_all_contacts.html", ctx)


class EditPerson(View):
    def get(self, request, id):
        ctx = {
            "person" : Person.objects.get(pk=id)
        }
        return render(request, "contact_box/edit_person.html", ctx)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.name = request.POST.get("name")
        person.surname = request.POST.get("surname")
        person.description = request.POST.get("description")
        person.save()
        return redirect("/show/%s" % id)


class DeletePerson(View):
    def get(self, request, id):
        ctx = {
            "person": Person.objects.get(pk=id)
        }
        return render(request, "contact_box/delete_person.html", ctx)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        if request.POST.get('delete') == "tak":
            person.delete()
        return redirect("/")


class AddAddress(View):
    def get(self, request, id):
        return render(request, "contact_box/add_address.html")

    def post(self, request, id):
        city = request.POST.get("city")
        street = request.POST.get("street")
        house_number = request.POST.get("house_number")
        apartment_number = request.POST.get("apartment_number")
        address = Address.objects.create(city=city, street=street, house_number=house_number, apartment_number=apartment_number)
        person = Person.objects.get(pk=id)
        person.address = address
        person.save()
        return redirect("/show/%s" % id)

class AddPhoneNumber(View):
    def get(self, request, id):
        return render(request, "contact_box/add_phone.html")

    def post(self, request, id):
        phone_number = request.POST.get("phone_number")
        phone_type = request.POST.get("phone_type")
        person = Person.objects.get(pk=id)
        Phone.objects.create(phone_number=phone_number, phone_type=phone_type, person=person)
        return redirect("/show/%s" % id)

class AddEmail(View):
    def get(self, request, id):
        return render(request, "contact_box/add_email.html")

    def post(self, request, id):
        email = request.POST.get("email")
        email_type = request.POST.get("email_type")
        person = Person.objects.get(pk=id)
        Email.objects.create(email=email, email_type=email_type, person=person)
        return redirect("/show/%s" % id)
