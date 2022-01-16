from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class User(AbstractUser):
	email = models.EmailField(max_length=255, unique=True)
	
	is_principal=models.BooleanField(default=False)
	is_responsable=models.BooleanField(default=False)
	is_collab=models.BooleanField(default=True)
	is_client=models.BooleanField(default=False)
	
