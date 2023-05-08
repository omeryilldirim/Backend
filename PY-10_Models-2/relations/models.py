from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return f'{self.username} - {self.password} - {self.email}'
    

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField()
    picture = models.ImageField(upload_to='profile/', default='', null=True, blank=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    '''
    on_delete properties:
    CASCADE: Delete the related data when the object is deleted.
    PROTECT: Prevent deletion of the related object by raising ProtectedError, a subclass of django.db.IntegrityError.
    SET_NULL: Set the ForeignKey null; this is only possible if null is True.
    SET_DEFAULT: Set the ForeignKey to its default value; a default for the ForeignKey must be set.
    SET(): Set the ForeignKey to the value passed to SET(), or if a callable is passed in, the result of calling it. In most cases, passing a callable will be necessary to avoid executing queries at the time your models.py is imported:
    DO_NOTHING: Take no action. If your database backend enforces referential integrity, this will cause an IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.

    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
    '''

COUNTRIES=(
    ('TR', 'Turkey'),
    ('US', 'United States'),
    ('GB', 'United Kingdom'),
    ('DE', 'Germany'),
    ('SE', 'Sweden'),
)

# ManyToOne() == ForeignKey()
class Address(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    country = models.CharField(max_length=50, choices=COUNTRIES)
    phone = models.CharField(max_length=16)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.address} - {self.country} - {self.phone}'
    
class Product(models.Model):
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    accoutn = models.ManyToManyField(Account, verbose_name='Accounts')

    def __str__(self):
        return f'{self.brand} - {self.product}'