from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):  
    use_in_migrations = True

    def _create_user(self, email, student_number, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not student_number:
            raise ValueError('The given student number must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,student_number=student_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, student_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, student_number, password, **extra_fields)

    def create_superuser(self, email, student_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, student_number, password, **extra_fields)