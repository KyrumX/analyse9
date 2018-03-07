from django.db import models

# Create your models here.

class Browsers(models.Model):
    browser_type = models.CharField(primary_key=True, max_length=10000)
    amount = models.IntegerField()

    @staticmethod
    def check_if_browser_exists(browser):
        return Browsers.objects.filter(browser_type=browser).exists()

    @staticmethod
    def increment_existing(browser):
        object = Browsers.objects.get(browser_type=browser)
        object.amount += 1
        object.save()

    @staticmethod
    def create_new_entry(browser):
        object = Browsers(browser_type=browser, amount=1)
        object.save()

    @staticmethod
    def get_all_objects():
        return Browsers.objects.all()

class Colors(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    color = models.CharField(max_length=7)

    @staticmethod
    def save_color_entry(name, address, color):
        object = Colors(name=name, address=address, color=color)
        object.save()

    @staticmethod
    def get_ten_random():
        return Colors.objects.all().order_by('?')[:10]