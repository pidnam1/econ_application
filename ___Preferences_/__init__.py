from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Preferences_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    RANKINGS = [1,2,3,4,5,6,7,8,9,10,'No rank']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def make_field1(label):
    return models.StringField(
        choices=C.RANKINGS,
        label=label, initial = "No rank",
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
        label=label,
    )


class Player(BasePlayer):
    gender = models.IntegerField()
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
    f21_1_1 = make_field1('')
    f22_1_1 = make_field1('')
    f23_1_1 = make_field1('')
    f24_1_1 = make_field1('')
    f25_1_1 = make_field1('')
    f26_1_1 = make_field1('')
    f27_1_1 = make_field1('')
    f28_1_1 = make_field1('')
    f29_1_1 = make_field1('')
    f30_1_1 = make_field1('')
    f31_1_1 = make_field1('')
    f32_1_1 = make_field1('')
    f33_1_1 = make_field1('')
    f34_1_1 = make_field1('')
    f35_1_1 = make_field1('')
    f36_1_1 = make_field1('')
    f37_1_1 = make_field1('')
    f38_1_1 = make_field1('')
    f39_1_1 = make_field1('')
    f40_1_1 = make_field1('')
    f1_2_1 = make_field2('')
    f2_2_1 = make_field2('')
    f3_2_1 = make_field2('')
    f4_2_1 = make_field2('')
    f5_2_1 = make_field2('')
    f6_2_1 = make_field2('')
    f7_2_1 = make_field2('')
    f8_2_1 = make_field2('')
    f9_2_1 = make_field2('')
    f10_2_1 = make_field2('')
    f1_3_1 = make_field3('')
    f2_3_1 = make_field3('')
    f3_3_1 = make_field3('')
    f4_3_1 = make_field3('')
    f5_3_1 = make_field3('')
    f6_3_1 = make_field3('')
    f7_3_1 = make_field3('')
    f8_3_1 = make_field3('')
    f9_3_1 = make_field3('')
    f10_3_1 = make_field3('')

class Transition(Page):
    form_model = 'player'
    @staticmethod
    def before_next_page(player: Player,timeout_happened):
        #randomizing list
        session = player.session
        g = player.group
        random_players = session.active_players
        random.shuffle(random_players)
        player.participant.players = []
        for current_player in random_players:
            if current_player != player.id_in_group:
                c = g.get_player_by_id(current_player)
                player.participant.players.append(c.participant.label)
        print(player.participant.players)
        player.gender = player.participant.gender

class Pref_Helper(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        session = player.session
        form_fields_all = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1','f15_1_1',
        'f16_1_1','f17_1_1','f18_1_1','f19_1_1','f20_1_1','f21_1_1','f22_1_1','f23_1_1',
        'f24_1_1','f25_1_1','f26_1_1','f27_1_1','f28_1_1','f29_1_1','f30_1_1','f31_1_1',
        'f32_1_1','f33_1_1','f34_1_1','f35_1_1','f36_1_1','f37_1_1','f38_1_1','f39_1_1',
        'f40_1_1']
        form_fields = form_fields_all[:session.count - 1]
        return form_fields
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        session = player.session
        form_fields = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1','f15_1_1',
        'f16_1_1','f17_1_1','f18_1_1','f19_1_1','f20_1_1','f21_1_1','f22_1_1','f23_1_1',
        'f24_1_1','f25_1_1','f26_1_1','f27_1_1','f28_1_1','f29_1_1','f30_1_1','f31_1_1',
        'f32_1_1','f33_1_1','f34_1_1','f35_1_1','f36_1_1','f37_1_1','f38_1_1','f39_1_1',
        'f40_1_1']
        player.participant.form_fields_pref = form_fields[:session.count - 1]
        return dict(players=player.participant.players)
    @staticmethod
    def error_message(player: Player, values):
        choices = []
        for field in player.participant.form_fields_pref:
            choices += [values[field]]
        if len(set(choices)) != 11:
            return "You must choose exactly 10 ranks. You cannot choose the same rank for two people."
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        #SET THESE WHEN SETTING THE NAMES OF THE PLAYERS

        #change this and the player names list in Consent's tests.py for testing
        rank_list = [player.f1_1_1, player.f2_1_1, player.f3_1_1, player.f4_1_1,
        player.f5_1_1, player.f6_1_1, player.f7_1_1, player.f8_1_1, player.f9_1_1,
        player.f10_1_1, player.f11_1_1, player.f12_1_1, player.f13_1_1, player.f14_1_1,
        player.f15_1_1, player.f16_1_1, player.f17_1_1, player.f18_1_1, player.f19_1_1,
        player.f20_1_1, player.f21_1_1, player.f22_1_1, player.f23_1_1, player.f24_1_1,
        player.f25_1_1, player.f26_1_1, player.f27_1_1, player.f28_1_1, player.f29_1_1,
        player.f30_1_1, player.f31_1_1, player.f32_1_1, player.f33_1_1, player.f34_1_1,
        player.f35_1_1, player.f36_1_1, player.f37_1_1, player.f38_1_1, player.f39_1_1,
        player.f40_1_1]
        player.participant.name_list = []
        ranking_order={}
        for i in range(len(rank_list)):
            if rank_list[i]!="No rank":
                ranking_order[rank_list[i]]=player.participant.players[i]
        sorted_ranking_order = {key: val for key, val in sorted(ranking_order.items(),key=lambda ele: int(ele[0]))}
        player.participant.name_list = list(sorted_ranking_order.values())

        id_list = []
        id_list_female = []
        id_list_male = []
        group = player.group
        for name in player.participant.name_list:
            for p in group.get_players():
                print(p.participant.label, name)
                if p.participant.label == name:
                    id_list.append(p.id_in_group)
                    if p.participant.gender == 0: #female
                        id_list_female.append(p.id_in_group)
                    else: #male
                        id_list_male.append(p.id_in_group)

        print("id list", id_list)
        player.participant.pref_helpers = id_list
        player.participant.pref_female_helpers = []
        player.participant.pref_male_helpers = []
        for value in player.participant.pref_helpers:
            if value in id_list_female:
                player.participant.pref_female_helpers.append(value)
            elif value in id_list_male:
                player.participant.pref_male_helpers.append(value)

class Pref_Helper_Why(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        session = player.session
        form_fields_all = ['f1_2_1','f2_2_1','f3_2_1','f4_2_1','f5_2_1','f6_2_1','f7_2_1','f8_2_1','f9_2_1','f10_2_1']
        form_fields = form_fields_all[:session.count - 1]
        return form_fields
    @staticmethod
    def vars_for_template(player: Player):
        player_why = ["1. " + player.participant.name_list[0], "2. " + player.participant.name_list[1], "3. " + player.participant.name_list[2],
        "4. " + player.participant.name_list[3], "5. " + player.participant.name_list[4], "6. " + player.participant.name_list[5],
        "7. " + player.participant.name_list[6], "8. " + player.participant.name_list[7], "9. " + player.participant.name_list[8],
        "10. " + player.participant.name_list[9]]
        return dict(player_why = player_why)

def vars_for_template1(player: Player):
    players_other = []
    formfields = []
    if player.f1_2_1 == "9. Other":
        player1 = [player.participant.name_list[0]]
        players_other = players_other + player1
        formfields.append('f1_3_1')
    if player.f2_2_1 == "9. Other":
        player2 = [player.participant.name_list[1]]
        players_other = players_other + player2
        formfields.append('f2_3_1')
    if player.f3_2_1 == "9. Other":
        player3 = [player.participant.name_list[2]]
        players_other = players_other + player3
        formfields.append('f3_3_1')
    if player.f4_2_1 == "9. Other":
        player4 = [player.participant.name_list[3]]
        players_other = players_other + player4
        formfields.append('f4_3_1')
    if player.f5_2_1 == "9. Other":
        player5 = [player.participant.name_list[4]]
        players_other = players_other + player5
        formfields.append('f5_3_1')
    if player.f6_2_1 == "9. Other":
        player6 = [player.participant.name_list[5]]
        players_other = players_other + player6
        formfields.append('f6_3_1')
    if player.f7_2_1 == "9. Other":
        player7 = [player.participant.name_list[6]]
        players_other = players_other + player7
        formfields.append('f7_3_1')
    if player.f8_2_1 == "9. Other":
        player8 = [player.participant.name_list[7]]
        players_other = players_other + player8
        formfields.append('f8_3_1')
    if player.f9_2_1 == "9. Other":
        player9 = [player.participant.name_list[8]]
        players_other = players_other + player9
        formfields.append('f9_3_1')
    if player.f10_2_1 == "9. Other":
        player10 = [player.participant.name_list[9]]
        players_other = players_other + player10
        formfields.append('f10_3_1')
    return [players_other, formfields]

class Pref_Helper_Other(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        formfields = vars_for_template1(player)[1]
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        players_other = vars_for_template1(player)[0]
        return dict(players_other = players_other)
    @staticmethod
    def is_displayed(player: Player):
        return (player.f1_2_1 == "9. Other") or (player.f2_2_1 == "9. Other") or (player.f3_2_1 == "9. Other") or (player.f4_2_1 == "9. Other") or (player.f5_2_1 == "9. Other") or (player.f6_2_1 == "9. Other") or (player.f7_2_1 == "9. Other") or (player.f8_2_1 == "9. Other") or (player.f9_2_1 == "9. Other") or (player.f10_2_1 == "9. Other")

page_sequence = [Transition, Pref_Helper, Pref_Helper_Why, Pref_Helper_Other]
