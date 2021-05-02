from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['about_you']

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    form_model = 'player'


page_sequence = [
    MyPage,
]
