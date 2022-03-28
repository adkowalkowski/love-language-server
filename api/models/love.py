from django.db import models
from django.contrib.auth import get_user_model

class Love(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    
    class LoveLanguages(models.TextChoices):
        ACTS_OF_SERVICE = 'Acts of Service'
        RECEIVING_GIFTS = 'Receiving Gifts'
        QUALITY_TIME = 'Quality Time'
        WORDS_OF_AFFIRMATION = 'Words of Affirmation'
        PHYSICAL_TOUCH = 'Physical Touch'
    
    one = models.CharField(max_length=20, choices=LoveLanguages.choices)
    two = models.CharField(max_length=20, choices=LoveLanguages.choices)
    three = models.CharField(max_length=20, choices=LoveLanguages.choices)
    four = models.CharField(max_length=20, choices=LoveLanguages.choices)
    five = models.CharField(max_length=20, choices=LoveLanguages.choices)    

