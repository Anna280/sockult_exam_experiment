from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'consentform'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
    choices=[
        [1, 'Yes'],
        [2, 'No'],
    ]
)
    personal_ID = models.IntegerField()
    Age = models.IntegerField()
    Gender = models.IntegerField( choices=[
        [1, 'Female'],
        [2, 'Male'],
        [3, 'Other'],
        [4, 'Prefer not to say'],
    ]
)

