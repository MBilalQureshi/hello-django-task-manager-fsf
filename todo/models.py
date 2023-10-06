from django.db import models

# Create your models here.
class Item(models.Model):
    # To prevent the creation of todo items without a name. The null equals false attribute here
    # prevents items from being created without a name programmatically
    # and blank equals false will make the field required on forms.
    # This way we're certain that a todo item can't be created without a name
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)