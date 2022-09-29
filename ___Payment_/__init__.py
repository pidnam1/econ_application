from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = '___Payment_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    total_pay0 = models.IntegerField()
    testing_pay0 = models.IntegerField()
    helping_pay0 = models.IntegerField()
    wtp_pay0 = models.IntegerField()
    game_pay0 = models.IntegerField()
    guess_bonus_pay0 = models.IntegerField()

# PAGES
class Congratulations(Page):
    form_model = 'player'

class Payment(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.participant.total_payment = 300
        player.total_pay0 = player.participant.total_payment

        testing_pay = list(player.participant.payoff_tt.values())
        random.shuffle(testing_pay)
        player.participant.total_payment += testing_pay[0]
        player.testing_pay0 = testing_pay[0]

        #add all helpers
        #for all players
        #if your id is in the players payoff_helped and they are your 2 or 4 partner
        #add that value to your payoff_help with key of which partner
        helping_pay = list(player.participant.payoff_help.values())
        random.shuffle(helping_pay)
        player.participant.total_payment += helping_pay[0]
        player.helping_pay0 = helping_pay[0]

        #subtract wtp_payment
        player.wtp_pay0 = 0-player.participant.wtp_payment
        player.participant.total_payment += player.wtp_pay0

        #add amount game
        player.participant.total_payment += player.participant.game_payoff
        player.game_pay0 = player.participant.game_payoff

        #add bonus payoff
        player.participant.total_payment += player.participant.guess_bonus_payoff
        player.guess_bonus_pay0 = player.participant.guess_bonus_payoff

        return dict(testing_pay0=player.testing_pay0, helping_pay0=player.helping_pay0, guess_bonus_pay0=player.participant.guess_bonus_payoff, wtp_pay0=player.wtp_pay0, amount_game_pay0=player.participant.game_payoff, total_payment0=player.participant.total_payment)


page_sequence = [Congratulations, Payment]
