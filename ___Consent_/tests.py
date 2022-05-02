from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):



    def play_round(self):
        #original_genders_list = [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        genders_list = [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
        ###change for diff tests
        PLAYERS = ['Shan Aman Rana', 'Alexia Delfino', 'Shamyla Chaudry', 'Ahsan Pasha',
                   'Shanzay Tariq', 'Izzah Kashif', 'Rohma Nasim', 'Hamna Tariq', 'Essa Kurd', 'Hammad Qayyum',
                   'Muhammad Pervaiz', 'Ayesha Hassan', 'Faizan Aziz', 'Assad Mustafa', 'Maheen Alvi',
                   'Hasan Akmal', 'Tamoor Salman', 'Khawaja Kashif', 'Haris Zahid', 'Khadija Aslam',
                   'Hamza Riaz']
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