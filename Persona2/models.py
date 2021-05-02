from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Persona2'
    players_per_group = None
    num_rounds = 10
    stakes = c(100)  # amount of payoff for winning


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## Define variables to save

    # the player's choice
    Offer= models.IntegerField(min=0, max=100)
    # save if player won or lost
    is_winner = models.BooleanField()

    bot_strategy = models.StringField()
    # the bot's choice

    bot_side = models.StringField(choices=['Decline', 'Accept'])

    # Here, the player's role is always set to "Proposer"
    # Change this function to do otherwise
    def role(self):
        return 'Proposer'

    ## Define possible strategies used by the bot

    # Strategy: if the offer from the proposer is between a certain interval, it will randomly choose "accept" or
    #"decline" depending on the weights (the bigger offer, the bigger probability of accepting)

    def Strategy1(self):
        if self.Offer >= 0 and self.Offer <= 20:
            if str(random.choices(('Accept', 'Decline'), [0.3, 0.7])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'

        elif self.Offer >= 21 and self.Offer <= 34:

            if str(random.choices(('Accept', 'Decline'), [0.5, 0.5])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 35 and self.Offer <= 45:
            if str(random.choices(('Accept', 'Decline'), [0.8, 0.2])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 46 and self.Offer <= 56:
            if str(random.choices(('Accept', 'Decline'), [0.8, 0.2])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 57 and self.Offer <= 70:
            if str(random.choices(('Accept', 'Decline'), [0.8, 0.2])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 71 and self.Offer <= 80:
            if str(random.choices(('Accept', 'Decline'), [0.9, 0.1])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 81 and self.Offer <= 100:
            if str(random.choices(('Accept', 'Decline'), [1, 0])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'

        else:
            self.bot_side ='Decline'
        self.bot_strategy = "Weighted"
    def Strategy2(self):
        if self.Offer >= 0 and self.Offer <= 20:
            if str(random.choices(('Accept', 'Decline'), [0.3, 0.7])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'

        elif self.Offer >= 21 and self.Offer <= 34:

            if str(random.choices(('Accept', 'Decline'), [0.5, 0.5])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 35 and self.Offer <= 45:
            if str(random.choices(('Accept', 'Decline'), [0.8, 0.2])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 46 and self.Offer <= 56:
            if str(random.choices(('Accept', 'Decline'), [0.8, 0.2])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 57 and self.Offer <= 70:
            if str(random.choices(('Accept', 'Decline'), [0.8, 0.2])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 71 and self.Offer <= 80:
            if str(random.choices(('Accept', 'Decline'), [0.9, 0.1])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'
        elif self.Offer >= 81 and self.Offer <= 100:
            if str(random.choices(('Accept', 'Decline'), [1, 0])) == '[\'Accept\']':
                self.bot_side = 'Accept'
            else:
                self.bot_side = 'Decline'

        else:
            self.bot_side ='Decline'
        self.bot_strategy = "Weighted"

    def set_payoffs(self):
        if self.bot_side == 'Accept':
            self.is_winner = True
        else:
            self.is_winner = False

        # if player won, money money
        if self.is_winner:
            self.payoff = Constants.stakes - self.Offer
        # else, 0
        else:
            self.payoff = c(0)