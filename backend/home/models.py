from django.conf import settings
from django.db import models


class Home(models.Model):
    "Generated Model"
    user = models.ManyToManyField(
        "users.User",
        related_name="home_user",
    )
