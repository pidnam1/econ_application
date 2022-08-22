from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random
class PlayerBot(Bot):
    def play_round(self):
        PLAYERS = ['Nida Naz', 'Kavish Hassan', 'Amna Noor','Amina Ejaz','Sarah Asif',
    'Lalarukh Schkoh', 'Khadija Idress', 'Madiha', 'Abdul Rehman', 'Barkat', 'Shahmeer',
    'Sadam', 'Ibrahim', 'Taha', 'Shamyla Chaudry']
        #reason_choices = ["1. A close friend", "2. Male", "3. Female", "4. Has a high GPA",
         #          "5. Is older than me", "6. Is  younger than me", "7. Is from my ‘zaat’",
        #           "8. Is not from my \‘zaat\’", "9. Other"]


        helper_form_fields = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1']

        id = self.player.id_in_group - 1 ##-1 just to fit the format of the rest of the code
        random_list = list(range(0, len(PLAYERS)))
        random_list.remove(id)
        random.shuffle(random_list)
        # try:
        #     random_list.remove(id)
        # except:
        #     pass

        x = {}

        for i in range(14):
            x[helper_form_fields[i]] = PLAYERS[random_list[i]]

        yield Pref_Helper, x

        ###Pref Helper_Why Testing

        z = {}
        helper_why_form_fields = ['f1_2_1', 'f2_2_1', 'f3_2_1', 'f4_2_1', 'f5_2_1']
        reason_choices = ["1. A close friend", "2. Male", "3. Female", "4. Has a high GPA",
        "5. Is older than me", "6. Is  younger than me", "7. Is from my 'zaat'",
        "8. Is not from my 'zaat'"]
        for i in helper_why_form_fields:
            z[i] = reason_choices[random.randint(0, 7)]

        yield Pref_Helper_Why, z

        ###Choosing TT
        tester_form_fields = ['f1_1_2','f2_1_2','f3_1_2','f4_1_2','f5_1_2','f6_1_2','f7_1_2',
        'f8_1_2','f9_1_2','f10_1_2','f11_1_2','f12_1_2','f13_1_2','f14_1_2']
        random.shuffle(random_list)
        y = {}
        for i in range(14):
            y[tester_form_fields[i]] = PLAYERS[random_list[i]]

        yield Pref_TT, y

        a = {}
        tester_why_form_fields = ['f1_2_2','f2_2_2','f3_2_2','f4_2_2','f5_2_2']
        reason_choices = ["1. A close friend", "2. Male", "3. Female", "4. Has a high GPA",
        "5. Is older than me", "6. Is  younger than me", "7. Is from my 'zaat'",
        "8. Is not from my 'zaat'"]

        for i in tester_why_form_fields:
            a[i] = reason_choices[random.randint(0, 7)]
        yield Pref_TT_Why, a
