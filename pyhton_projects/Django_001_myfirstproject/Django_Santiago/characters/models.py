from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        db_table = "cities"


class Universe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    foundation = models.DateTimeField()

    class Meta:
        db_table = "universes"


class Power(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "powers"


class Character(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    path = models.FileField(upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateTimeField()

    class Meta:
        db_table = "characters"


class PowersCharacter(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    power = models.ForeignKey(Power, on_delete=models.CASCADE)
    level = models.FloatField()

    class Meta:
        db_table = "powers_character"
