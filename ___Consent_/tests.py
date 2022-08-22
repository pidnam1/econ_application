from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        genders_list = [0,1,0,0,0,0,0,0,1,1,1,1,1,1,0]

        ###change for diff tests
        PLAYERS = ['Nida Naz', 'Kavish Hassan', 'Amna Noor','Amina Ejaz','Sarah Asif',
        'Lalarukh Schkoh', 'Khadija Idress', 'Madiha', 'Abdul Rehman', 'Barkat', 'Shahmeer',
        'Sadam', 'Ibrahim', 'Taha', 'Shamyla Chaudry']
        x = {}
        id = self.player.id_in_group - 1
        x["roll"] = id + 1
        x["esig"] = PLAYERS[id]
        self.player.participant.label = PLAYERS[id]
        self.player.participant.gender = genders_list[id]
        self.player.participant.roll_no = id + 1
        self.player.participant.count_participant = id+1
        x["agree"] = "I agree"
        yield Consent, x
