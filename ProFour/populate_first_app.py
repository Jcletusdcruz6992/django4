import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProFour.settings')

import django
django.setup()

import random
from AppFour.models import Topic,Webpage,AccessRecord
from faker import Faker
fakegen=Faker()
topics=['News','Social','Marketplace','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.name()
        webpg=Webpage.objects.get_or_create(topic=add_topic(),name=fake_name,url=fake_url)[0]
        accRec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('population completed !')
