from django.contrib import admin
from .models import (user_profile,profile_text,friends)


# Register your models here.


admin.site.register({user_profile,profile_text,friends})