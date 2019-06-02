from django.db import models


class UserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})
