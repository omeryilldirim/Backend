from faker import Faker
from .models import Category, Post
from django.contrib.auth.models import User

def run():
    fake = Faker(['tr-TR'])
    categories = ('Gezi', 'Yemek', 'Spor', 'Ekonomi')

    for category in categories:
        new_category = Category.objects.create(name=category)
        for _ in range(50):
            Post.objects.create(
                title = fake.sentence(),
                content = fake.text(),
                category = new_category,
                user = User.objects.first()
            )

    print('Finished')
    