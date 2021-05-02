from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['consent','personal_ID']



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class AgeGender(Page):
    form_model = 'player'
    form_fields = ['Age', 'Gender']


page_sequence = [
    MyPage,
    AgeGender,
]
