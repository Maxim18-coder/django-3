from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
     id = models.AutoField(PrymaryKey = True) # реализуйте модель
     model = models.CharField(max_length=30)
     year = models.PositiveIntegerField()
     color = models.CharField(max_length=50)
     mileage = models.PositiveIntegerField()
     volume = models.DecimalField(max_digits=4, decimal_places=1)
     body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
     drive_unit = models.CharField(max_length=20, choises=DRIVE_UNIT_CHOICES)
     gearbox = models.CharField(max_length=20, choises=GEARBOX_CHOICES)
     fuel_type = models.CharField(max_length=20, choises=FUEL_TYPE_CHOICES)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to='images/')


def __str__(self):
    return f"{self.model} ({self.year})"

class Sale(models.Model):
      id = models.AutoField(PrymaryKey = True) # реализуйте модель
      client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='sales')
      car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='sales')
      created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"Sale of {self.car.model} to {self.client} on {self.created_at}"