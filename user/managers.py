from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        # if not email:
        #     raise ValueError('The Email must be set')
        # email = self.normalize_email(email)
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(password, **extra_fields)
