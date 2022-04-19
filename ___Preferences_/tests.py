from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random
class PlayerBot(Bot):
    def play_round(self):
        PLAYERS = ['Shan Aman Rana', 'Alexia Delfino', 'Shamyla Chaudry', 'Ahsan Pasha',
                   'Shanzay Tariq', 'Izzah Kashif', 'Rohma Nasim', 'Hamna Tariq', 'Essa Kurd', 'Hammad Qayyum',
                   'Muhammad Pervaiz', 'Ayesha Hassan', 'Faizan Aziz', 'Assad Mustafa', 'Maheen Alvi',
                   'Hasan Akmal', 'Tamoor Salman', 'Khawaja Kashif', 'Haris Zahid', 'Khadija Aslam',
                   'Hamza Riaz']

        #reason_choices = ["1. A close friend", "2. Male", "3. Female", "4. Has a high GPA",
         #          "5. Is older than me", "6. Is  younger than me", "7. Is from my ‘zaat’",
        #           "8. Is not from my \‘zaat\’", "9. Other"]

        reason_choices = ["1. A close friend", "2. Male", "3. Female", "4. Has a high GPA",
    "5. Is older than me", "6. Is  younger than me", "7. Is from my ‘zaat’",
    "8. Is not from my \‘zaat\’"]
        helper_form_fields = ['f1_1_1', 'f2_1_1', 'f3_1_1', 'f4_1_1', 'f5_1_1', 'f6_1_1', 'f7_1_1',
                       'f8_1_1', 'f9_1_1', 'f10_1_1', 'f11_1_1', 'f12_1_1', 'f13_1_1', 'f14_1_1', 'f15_1_1',
                       'f16_1_1', 'f17_1_1', 'f18_1_1', 'f19_1_1', 'f20_1_1', 'f1_2_1', 'f2_2_1', 'f3_2_1',
                       'f4_2_1', 'f5_2_1', 'f6_2_1', 'f7_2_1', 'f8_2_1', 'f9_2_1', 'f10_2_1', 'f11_2_1',
                       'f12_2_1', 'f13_2_1', 'f14_2_1', 'f15_2_1', 'f16_2_1', 'f17_2_1', 'f18_2_1', 'f19_2_1',
                       'f20_2_1']
        id = self.player.id_in_group - 1 ##-1 just to fit the format of the rest of the code
        random_list = list(range(0, len(PLAYERS)))
        random_list.remove(id)
        random.shuffle(random_list)
        # try:
        #     random_list.remove(id)
        # except:
        #     pass

        x = {}
        for i in range(20):
            x[helper_form_fields[i]] = PLAYERS[random_list[i]]
        for i in range(20, 40):
            x[helper_form_fields[i]] = random.choice(reason_choices)

        yield Pref_Helper, x

        tester_form_fields = ['f1_1_2', 'f2_1_2', 'f3_1_2', 'f4_1_2', 'f5_1_2', 'f6_1_2', 'f7_1_2',
                       'f8_1_2', 'f9_1_2', 'f10_1_2', 'f11_1_2', 'f12_1_2', 'f13_1_2', 'f14_1_2', 'f15_1_2',
                       'f16_1_2', 'f17_1_2', 'f18_1_2', 'f19_1_2', 'f20_1_2', 'f1_2_2', 'f2_2_2', 'f3_2_2',
                       'f4_2_2', 'f5_2_2', 'f6_2_2', 'f7_2_2', 'f8_2_2', 'f9_2_2', 'f10_2_2', 'f11_2_2',
                       'f12_2_2', 'f13_2_2', 'f14_2_2', 'f15_2_2', 'f16_2_2', 'f17_2_2', 'f18_2_2', 'f19_2_2',
                       'f20_2_2']
        random.shuffle(random_list)
        y = {}
        for i in range(20):
            y[tester_form_fields[i]] = PLAYERS[random_list[i]]
        for i in range(20, 40):
            y[tester_form_fields[i]] = random.choice(reason_choices)

        yield Pref_TT, y
