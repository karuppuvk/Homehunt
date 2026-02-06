from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Property(models.Model):

    class PropertyType(models.TextChoices):
        HOME = "home", "Home"
        APARTMENT = "apartment", "Apartment"

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        db_index=True,
    )
    size = models.PositiveIntegerField(help_text="Size in square feet")
    image = models.ImageField(upload_to="properties/", blank=True, null=True)
    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.HOME,
        db_index=True,
    )
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-time_added"]

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "property")

    def __str__(self):
        return f"{self.user.username} - {self.property.name}"
