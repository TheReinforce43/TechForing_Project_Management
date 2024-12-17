from django.contrib.auth.base_user import BaseUserManager 


class UserManager(BaseUserManager):


    def create_user(self,email,Username,password=None,**extra_fields):

        if not email:
            raise ValueError("Email must be provided")
        

        email= self.normalize_email(email)

        user = self.model(email=email,Username=Username,**extra_fields)
        if password:
            user.set_password(password)
        else:
            raise ValueError("Password must be provided")
        
        user.save(using=self._db)

        return user 
    

    def create_superuser(self,email,Username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self.create_user(email, Username,password,**extra_fields)