from django.db import models

# https://docs.djangoproject.com/en/4.2/topics/db/models/
class Student(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # Kayıt yapıldığı anki zamanı otomatik yaz.
    updated = models.DateTimeField(auto_now=True) # Kayıt güncellendiği anki zamanı otomatik yaz.

    def __str__(self): # Kayıt yazdır.
        return f'{self.first_name} {self.last_name} # {self.number}'
    
    class Meta: # Default özellikleri değiştir.
        # https://docs.djangoproject.com/en/4.2/ref/models/options/
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        ordering = ["-number"] # Ters sıralama için (DESC) sutun isminin başına - konur.