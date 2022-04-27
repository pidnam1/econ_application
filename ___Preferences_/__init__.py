from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Preferences_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PLAYERS = ['Shan Aman Rana','Alexia Delfino','Shamyla Chaudry','Ahsan Pasha',
    'Shanzay Tariq','Izzah Kashif','Rohma Nasim','Hamna Tariq','Essa Kurd','Hammad Qayyum',
    'Muhammad Pervaiz','Ayesha Hassan','Faizan Aziz','Assad Mustafa','Maheen Alvi',
    'Hasan Akmal','Tamoor Salman','Khawaja Kashif','Haris Zahid','Khadija Aslam',
    'Hamza Riaz']
    RANKINGS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    TOP5 = [1,2,3,4,5]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def make_field1(label):
    return models.StringField(
        choices=C.PLAYERS,
        label=label, initial = 0,
    )

def make_field2(label):
    return models.StringField(
        choices=["1. A close friend", "2. Male", "3. Female", "4. Has a high GPA",
        "5. Is older than me", "6. Is  younger than me", "7. Is from my 'zaat'",
        "8. Is not from my 'zaat'", "9. Other"],
        label=label, initial = "None"
    )

def make_field3(label):
    return models.StringField(
        label=label, blank=True, initial = 0,
    )

class Player(BasePlayer):
    f1_1_1 = make_field1('')
    f2_1_1 = make_field1('')
    f3_1_1 = make_field1('')
    f4_1_1 = make_field1('')
    f5_1_1 = make_field1('')
    f6_1_1 = make_field1('')
    f7_1_1 = make_field1('')
    f8_1_1 = make_field1('')
    f9_1_1 = make_field1('')
    f10_1_1 = make_field1('')
    f11_1_1 = make_field1('')
    f12_1_1 = make_field1('')
    f13_1_1 = make_field1('')
    f14_1_1 = make_field1('')
    f15_1_1 = make_field1('')
    f16_1_1 = make_field1('')
    f17_1_1 = make_field1('')
    f18_1_1 = make_field1('')
    f19_1_1 = make_field1('')
    f20_1_1 = make_field1('')
    f1_2_1 = make_field2('')
    f2_2_1 = make_field2('')
    f3_2_1 = make_field2('')
    f4_2_1 = make_field2('')
    f5_2_1 = make_field2('')
    f1_3_1 = make_field3('')
    f2_3_1 = make_field3('')
    f3_3_1 = make_field3('')
    f4_3_1 = make_field3('')
    f5_3_1 = make_field3('')
    f1_1_2 = make_field1('')
    f2_1_2 = make_field1('')
    f3_1_2 = make_field1('')
    f4_1_2 = make_field1('')
    f5_1_2 = make_field1('')
    f6_1_2 = make_field1('')
    f7_1_2 = make_field1('')
    f8_1_2 = make_field1('')
    f9_1_2 = make_field1('')
    f10_1_2 = make_field1('')
    f11_1_2 = make_field1('')
    f12_1_2 = make_field1('')
    f13_1_2 = make_field1('')
    f14_1_2 = make_field1('')
    f15_1_2 = make_field1('')
    f16_1_2 = make_field1('')
    f17_1_2 = make_field1('')
    f18_1_2 = make_field1('')
    f19_1_2 = make_field1('')
    f20_1_2 = make_field1('')
    f1_2_2 = make_field2('')
    f2_2_2 = make_field2('')
    f3_2_2 = make_field2('')
    f4_2_2 = make_field2('')
    f5_2_2 = make_field2('')
    f1_3_2 = make_field3('')
    f2_3_2 = make_field3('')
    f3_3_2 = make_field3('')
    f4_3_2 = make_field3('')
    f5_3_2 = make_field3('')

# def creating_session(subsession: Subsession):
#     if subsession.round_number == 1:
#         for p in subsession.get_players():
#             if (p.id_in_group == 2) or (p.id_in_group == 3) or (p.id_in_group == 4) or (p.id_in_group == 9) or (p.id_in_group == 12) or (p.id_in_group == 17):
#                 p.participant.gender = 0 #female
#             elif (p.id_in_group == 1) or (p.id_in_group == 5) or (p.id_in_group == 6) or (p.id_in_group == 7) or (p.id_in_group == 8) or (p.id_in_group == 10) or (p.id_in_group == 11) or (p.id_in_group == 13) or (p.id_in_group == 14) or (p.id_in_group == 15) or (p.id_in_group == 16) or (p.id_in_group == 18):
#                 p.participant.gender = 1 #male


class Pref_Helper(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1','f15_1_1',
        'f16_1_1','f17_1_1','f18_1_1','f19_1_1','f20_1_1']
        return form_fields
    @staticmethod
    def vars_for_template(player: Player):
        form_fields = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1','f15_1_1',
        'f16_1_1','f17_1_1','f18_1_1','f19_1_1','f20_1_1']
        player.participant.form_fields_pref = form_fields[:]
        return
    @staticmethod
    def error_message(player: Player, values):
        choices = []
        for field in player.participant.form_fields_pref:
            choices += [values[field]]
        if len(set(choices)) != len(choices):
            return "You cannot choose the same person for two ranks"
        if player.participant.label in choices:
            return "DO NOT SELECT YOUR OWN NAME"
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        #SET THESE WHEN SETTING THE NAMES OF THE PLAYERS
        name_list = [player.f1_1_1, player.f2_1_1, player.f3_1_1, player.f4_1_1,
        player.f5_1_1, player.f6_1_1, player.f7_1_1, player.f8_1_1, player.f9_1_1,
        player.f10_1_1, player.f11_1_1, player.f12_1_1, player.f13_1_1, player.f14_1_1,
        player.f15_1_1, player.f16_1_1, player.f17_1_1, player.f18_1_1, player.f19_1_1,
        player.f20_1_1]
        id_list = []
        id_list_female = []
        id_list_male = []
        group = player.group
        for name in name_list:
            for p in group.get_players():
                if p.participant.label == name:
                    id_list.append(p.id_in_group)
                    if p.participant.gender == 0: #female
                        id_list_female.append(p.id_in_group)
                    else: #male
                        id_list_male.append(p.id_in_group)
        player.participant.pref_helper = dict(zip(C.RANKINGS,id_list))
        player.participant.pref_helper_female = dict()
        player.participant.pref_helper_male = dict()
        for key, value in player.participant.pref_helper.items():
            if value in id_list_female:
                player.participant.pref_helper_female.update({key:value})
            elif value in id_list_male:
                player.participant.pref_helper_male.update({key:value})

class Pref_Helper_Why(Page):
    form_model = 'player'
    form_fields = ['f1_2_1','f2_2_1','f3_2_1','f4_2_1','f5_2_1']
    @staticmethod
    def vars_for_template(player: Player):
        player_why = [player.f1_1_1, player.f2_1_1, player.f3_1_1, player.f4_1_1,
        player.f5_1_1]
        return dict(player_why = player_why)

class Pref_Helper_Other(Page):
    form_model = 'player'
    form_fields = ['f1_3_1','f2_3_1','f3_3_1','f4_3_1','f5_3_1']
    @staticmethod
    def vars_for_template(player: Player):
        players_other = []
        if player.f1_2_1 == "9. Other":
            player1 = [player.f1_1_1]
            players_other = players_other + player1
        if player.f2_2_1 == "9. Other":
            player2 = [player.f2_1_1]
            players_other = players_other + player2
        if player.f3_2_1 == "9. Other":
            player3 = [player.f3_1_1]
            players_other = players_other + player3
        if player.f4_2_1 == "9. Other":
            player4 = [player.f4_1_1]
            players_other = players_other + player4
        if player.f5_2_1 == "9. Other":
            player5 = [player.f5_1_1]
            players_other = players_other + player5
        return dict(players_other = players_other)
    @staticmethod
    def is_displayed(player: Player):
        return (player.f1_2_1 == "9. Other") or (player.f2_2_1 == "9. Other") or (player.f3_2_1 == "9. Other") or (player.f4_2_1 == "9. Other") or (player.f5_2_1 == "9. Other")

class Pref_TT(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['f1_1_2','f2_1_2','f3_1_2','f4_1_2','f5_1_2','f6_1_2','f7_1_2',
        'f8_1_2','f9_1_2','f10_1_2','f11_1_2','f12_1_2','f13_1_2','f14_1_2','f15_1_2',
        'f16_1_2','f17_1_2','f18_1_2','f19_1_2','f20_1_2']
        return form_fields
    @staticmethod
    def vars_for_template(player: Player):
        form_fields = ['f1_1_2','f2_1_2','f3_1_2','f4_1_2','f5_1_2','f6_1_2','f7_1_2',
        'f8_1_2','f9_1_2','f10_1_2','f11_1_2','f12_1_2','f13_1_2','f14_1_2','f15_1_2',
        'f16_1_2','f17_1_2','f18_1_2','f19_1_2','f20_1_2']
        player.participant.form_fields_pref2 = form_fields[:20]
        return
    @staticmethod
    def error_message(player: Player, values):
        choices = []
        for field in player.participant.form_fields_pref2:
            choices += [values[field]]
        if len(set(choices)) != len(choices):
            return "You cannot choose the same person for two ranks"
        if player.participant.label in choices:
            return "DO NOT SELECT YOUR OWN NAME"
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        name_list = [player.f1_1_2, player.f2_1_2, player.f3_1_2, player.f4_1_2,
        player.f5_1_2, player.f6_1_2, player.f7_1_2, player.f8_1_2, player.f9_1_2,
        player.f10_1_2, player.f11_1_2, player.f12_1_2, player.f13_1_2, player.f14_1_2,
        player.f15_1_2, player.f16_1_2, player.f17_1_2, player.f18_1_2, player.f19_1_2,
        player.f20_1_2]
        id_list = []
        id_list_female = []
        id_list_male = []
        group = player.group
        for name in name_list:
            for p in group.get_players():
                if p.participant.label == name:
                    id_list.append(p.id_in_group)
                    if p.participant.gender == 0: #female
                        id_list_female.append(p.id_in_group)
                    else: #male
                        id_list_male.append(p.id_in_group)
        player.participant.pref_tt = dict(zip(C.RANKINGS,id_list))
        player.participant.pref_tt_female = dict()
        player.participant.pref_tt_male = dict()
        for key, value in player.participant.pref_helper.items():
            if value in id_list_female:
                player.participant.pref_tt_female.update({key:value})
            elif value in id_list_male:
                player.participant.pref_tt_male.update({key:value})

class Pref_TT_Why(Page):
    form_model = 'player'
    form_fields = ['f1_2_2','f2_2_2','f3_2_2','f4_2_2','f5_2_2']
    @staticmethod
    def vars_for_template(player: Player):
        player_why = [player.f1_1_2, player.f2_1_2, player.f3_1_2, player.f4_1_2,
        player.f5_1_2]
        return dict(player_why = player_why)

class Pref_TT_Other(Page):
    form_model = 'player'
    form_fields = ['f1_3_2','f2_3_2','f3_3_2','f4_3_2','f5_3_2']
    @staticmethod
    def vars_for_template(player: Player):
        players_other = []
        if player.f1_2_2 == "9. Other":
            player1 = [player.f1_1_2]
            players_other = players_other + player1
        if player.f2_2_2 == "9. Other":
            player2 = [player.f2_1_2]
            players_other = players_other + player2
        if player.f3_2_2 == "9. Other":
            player3 = [player.f3_1_2]
            players_other = players_other + player3
        if player.f4_2_2 == "9. Other":
            player4 = [player.f4_1_2]
            players_other = players_other + player4
        if player.f5_2_2 == "9. Other":
            player5 = [player.f5_1_2]
            players_other = players_other + player5
        return dict(players_other = players_other)
    @staticmethod
    def is_displayed(player: Player):
        return (player.f1_2_2 == "9. Other") or (player.f2_2_2 == "9. Other") or (player.f3_2_2 == "9. Other") or (player.f4_2_2 == "9. Other") or (player.f5_2_2 == "9. Other")

page_sequence = [Pref_Helper, Pref_Helper_Why, Pref_Helper_Other, Pref_TT, Pref_TT_Why, Pref_TT_Other]
