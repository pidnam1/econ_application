from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Preferences_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PLAYERS = ['Safi Ullah Khan','Muhammad Yousaf Khan','Abdul Nasir Khan','Arooj Khalid',
    'Zarak Naseer Baloch','Jannat Rashid','Shahid Ullah Khan','Saif Ur Rehman Kukuria',
    'Ali Hasnain','Muhammad Talha Wattoo','Shumaila Javaid','Shoaib Ullah','Rumaiza Mazhar',
    'Gul E Zahra Abbasi','Naveed Khan','Mahjabeen Sughra','Areesha Sohail','Sufyan Ali',
    'Hassan Umer','Ali Waqas','Sania Ehsan','Wareesha Ehsan','Muhammad Kashif Khan',
    'Muhammad Waqar','Umer Farooq','Zain U Din','Shahar Bano','Areesha Zahra Abbasi','Samiullah',
    'Rai Ahmad Khan','Rana Muhammad Imran','Amna Bibi','Tuba Naeem','Moazzam Asadullah',
    'Muhammad Musa Sulehria','Noor ul Huda Awan','Umme Aqeel']
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
        label=label, blank=True,
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
    f21_1_2 = make_field1('')
    f22_1_2 = make_field1('')
    f23_1_2 = make_field1('')
    f24_1_2 = make_field1('')
    f25_1_2 = make_field1('')
    f26_1_2 = make_field1('')
    f27_1_2 = make_field1('')
    f28_1_2 = make_field1('')
    f29_1_2 = make_field1('')
    f30_1_2 = make_field1('')
    f31_1_2 = make_field1('')
    f32_1_2 = make_field1('')
    f33_1_2 = make_field1('')
    f34_1_2 = make_field1('')
    f35_1_2 = make_field1('')
    f36_1_2 = make_field1('')
    f37_1_2 = make_field1('')
    f1_2_2 = make_field2('')
    f2_2_2 = make_field2('')
    f3_2_2 = make_field2('')
    f4_2_2 = make_field2('')
    f5_2_2 = make_field2('')
    f6_2_2 = make_field2('')
    f7_2_2 = make_field2('')
    f8_2_2 = make_field2('')
    f9_2_2 = make_field2('')
    f10_2_2 = make_field2('')
    f1_3_2 = make_field3('')
    f2_3_2 = make_field3('')
    f3_3_2 = make_field3('')
    f4_3_2 = make_field3('')
    f5_3_2 = make_field3('')
    f6_3_2 = make_field3('')
    f7_3_2 = make_field3('')
    f8_3_2 = make_field3('')
    f9_3_2 = make_field3('')
    f10_3_2 = make_field3('')

class Pref_Helper(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1','f15_1_1',
        'f16_1_1','f17_1_1','f18_1_1','f19_1_1','f20_1_1','f21_1_1','f22_1_1','f23_1_1',
        'f24_1_1','f25_1_1','f26_1_1','f27_1_1','f28_1_1','f29_1_1','f30_1_1','f31_1_1',
        'f32_1_1','f33_1_1','f34_1_1','f35_1_1','f36_1_1','f37_1_1']
        return form_fields
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        form_fields = ['f1_1_1','f2_1_1','f3_1_1','f4_1_1','f5_1_1','f6_1_1','f7_1_1',
        'f8_1_1','f9_1_1','f10_1_1','f11_1_1','f12_1_1','f13_1_1','f14_1_1','f15_1_1',
        'f16_1_1','f17_1_1','f18_1_1','f19_1_1','f20_1_1','f21_1_1','f22_1_1','f23_1_1',
        'f24_1_1','f25_1_1','f26_1_1','f27_1_1','f28_1_1','f29_1_1','f30_1_1','f31_1_1',
        'f32_1_1','f33_1_1','f34_1_1','f35_1_1','f36_1_1','f37_1_1']
        player.participant.form_fields_pref = form_fields[:]
        #randomizing list
        session = player.session
        random_players = session.active_players
        random.shuffle(random_players)
        player.participant.players = []
        for current_player in random_players:
            if current_player != player.id_in_group:
                c = g.get_player_by_id(current_player)
                player.participant.players.append(c.participant.label)
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
        player.f35_1_1, player.f36_1_1, player.f37_1_1]
        player.participant.name_list = []
        """
        ranking_order={}
        for i in range(len(rank_list)):
            if rank_list[i]!="No rank"":
                ranking_order[rank_list[i]]=player.participant.players[i]
        sorted_ranking_order = {key: val for key, val in sorted(ranking_order.items(), key = lambda ele: ele[0])}
        """
        ranking_order = dict(zip(rank_list, player.participant.players))
        sorted_ranking_order = {key: val for key, val in sorted(ranking_order.items(), key = lambda ele: ele[0])}
        sorted_ranking_order1 = {key: val for key, val in sorted(ranking_order.items(), key = lambda ele: ele[0])}
        for rank in sorted_ranking_order.keys():
            if rank == 'No rank':
                sorted_ranking_order1.pop(rank)
        player.participant.name_list = list(sorted_ranking_order1.values())

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
    form_fields = ['f1_2_1','f2_2_1','f3_2_1','f4_2_1','f5_2_1','f6_2_1','f7_2_1',
    'f8_2_1','f9_2_1','f10_2_1']
    @staticmethod
    def vars_for_template(player: Player):
        player_why = ["1. " + player.participant.name_list[0], "2. " + player.participant.name_list[1], "3. " + player.participant.name_list[2],
        "4. " + player.participant.name_list[3], "5. " + player.participant.name_list[4], "6. " + player.participant.name_list[5],
        "7. " + player.participant.name_list[6], "8. " + player.participant.name_list[7], "9. " + player.participant.name_list[8],
        "10. " + player.participant.name_list[9]]
        return dict(player_why = player_why)

class Pref_Helper_Other(Page):
    form_model = 'player'
    form_fields = ['f1_3_1','f2_3_1','f3_3_1','f4_3_1','f5_3_1','f6_3_1','f7_3_1',
    'f8_3_1','f9_3_1','f10_3_1']
    @staticmethod
    def vars_for_template(player: Player):
        players_other = []
        if player.f1_2_1 == "9. Other":
            player1 = [player.participant.name_list[0]]
            players_other = players_other + player1
        if player.f2_2_1 == "9. Other":
            player2 = [player.participant.name_list[1]]
            players_other = players_other + player2
        if player.f3_2_1 == "9. Other":
            player3 = [player.participant.name_list[2]]
            players_other = players_other + player3
        if player.f4_2_1 == "9. Other":
            player4 = [player.participant.name_list[3]]
            players_other = players_other + player4
        if player.f5_2_1 == "9. Other":
            player5 = [player.participant.name_list[4]]
            players_other = players_other + player5
        if player.f6_2_1 == "9. Other":
            player6 = [player.participant.name_list[5]]
            players_other = players_other + player6
        if player.f7_2_1 == "9. Other":
            player7 = [player.participant.name_list[6]]
            players_other = players_other + player7
        if player.f8_2_1 == "9. Other":
            player8 = [player.participant.name_list[7]]
            players_other = players_other + player8
        if player.f9_2_1 == "9. Other":
            player9 = [player.participant.name_list[8]]
            players_other = players_other + player9
        if player.f10_2_1 == "9. Other":
            player10 = [player.participant.name_list[9]]
            players_other = players_other + player10
        return dict(players_other = players_other)
    @staticmethod
    def is_displayed(player: Player):
        return (player.f1_2_1 == "9. Other") or (player.f2_2_1 == "9. Other") or (player.f3_2_1 == "9. Other") or (player.f4_2_1 == "9. Other") or (player.f5_2_1 == "9. Other") or (player.f6_2_1 == "9. Other") or (player.f7_2_1 == "9. Other") or (player.f8_2_1 == "9. Other") or (player.f9_2_1 == "9. Other") or (player.f10_2_1 == "9. Other")

class Pref_TT(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['f1_1_2','f2_1_2','f3_1_2','f4_1_2','f5_1_2','f6_1_2','f7_1_2',
        'f8_1_2','f9_1_2','f10_1_2','f11_1_2','f12_1_2','f13_1_2','f14_1_2','f15_1_2',
        'f16_1_2','f17_1_2','f18_1_2','f19_1_2','f20_1_2','f21_1_2','f22_1_2','f23_1_2',
        'f24_1_2','f25_1_2','f26_1_2','f27_1_2','f28_1_2','f29_1_2','f30_1_2','f31_1_2',
        'f32_1_2','f33_1_2','f34_1_2','f35_1_2','f36_1_2','f37_1_2']
        return form_fields
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        form_fields = ['f1_1_2','f2_1_2','f3_1_2','f4_1_2','f5_1_2','f6_1_2','f7_1_2',
        'f8_1_2','f9_1_2','f10_1_2','f11_1_2','f12_1_2','f13_1_2','f14_1_2','f15_1_2',
        'f16_1_2','f17_1_2','f18_1_2','f19_1_2','f20_1_2','f21_1_2','f22_1_2','f23_1_2',
        'f24_1_2','f25_1_2','f26_1_2','f27_1_2','f28_1_2','f29_1_2','f30_1_2','f31_1_2',
        'f32_1_2','f33_1_2','f34_1_2','f35_1_2','f36_1_2','f37_1_2']
        player.participant.form_fields_pref2 = form_fields[:]
        return dict(players=player.participant.players)
    @staticmethod
    def error_message(player: Player, values):
        choices = []
        for field in player.participant.form_fields_pref2:
            choices += [values[field]]
        if len(set(choices)) != 11:
            return "You must choose exactly 10 ranks. You cannot choose the same rank for two people."
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        rank_list = [player.f1_1_2, player.f2_1_2, player.f3_1_2, player.f4_1_2,
        player.f5_1_2, player.f6_1_2, player.f7_1_2, player.f8_1_2, player.f9_1_2,
        player.f10_1_2, player.f11_1_2, player.f12_1_2, player.f13_1_2, player.f14_1_2,
        player.f15_1_2, player.f16_1_2, player.f17_1_2, player.f18_1_2, player.f19_1_2,
        player.f20_1_2, player.f21_1_2, player.f22_1_2, player.f23_1_2, player.f24_1_2,
        player.f25_1_2, player.f26_1_2, player.f27_1_2, player.f28_1_2, player.f29_1_2,
        player.f30_1_2, player.f31_1_2, player.f32_1_2, player.f33_1_2, player.f34_1_2,
        player.f35_1_2, player.f36_1_2, player.f37_1_2]
        player.participant.name_list1 = []
        ranking_order = dict(zip(rank_list, player.participant.players))
        sorted_ranking_order = {key: val for key, val in sorted(ranking_order.items(), key = lambda ele: ele[0])}
        sorted_ranking_order1 = {key: val for key, val in sorted(ranking_order.items(), key = lambda ele: ele[0])}
        for rank in sorted_ranking_order.keys():
            if rank == 'No rank':
                sorted_ranking_order1.pop(rank)
        player.participant.name_list1 = list(sorted_ranking_order1.values())

        id_list = []
        id_list_female = []
        id_list_male = []
        group = player.group
        for name in player.participant.name_list1:
            for p in group.get_players():

                ##subtly eliminates ones who did not show up from matching algorithm
                if p.participant.label == name:
                    id_list.append(p.id_in_group)
                    if p.participant.gender == 0: #female
                        id_list_female.append(p.id_in_group)
                    else: #male
                        id_list_male.append(p.id_in_group)
        player.participant.pref_tt = dict(zip(C.RANKINGS,id_list))
        player.participant.pref_tt_female = dict()
        player.participant.pref_tt_male = dict()
        for key, value in player.participant.pref_tt.items():
            if value in id_list_female:
                player.participant.pref_tt_female.update({key:value})
            elif value in id_list_male:
                player.participant.pref_tt_male.update({key:value})

class Pref_TT_Why(Page):
    form_model = 'player'
    form_fields = ['f1_2_2','f2_2_2','f3_2_2','f4_2_2','f5_2_2','f6_2_2','f7_2_2',
    'f8_2_2','f9_2_2','f10_2_2']
    @staticmethod
    def vars_for_template(player: Player):
        player_why = ["1. " + player.participant.name_list1[0], "2. " + player.participant.name_list1[1], "3. " + player.participant.name_list1[2],
        "4. " + player.participant.name_list1[3], "5. " + player.participant.name_list1[4], "6. " + player.participant.name_list1[5],
        "7. " + player.participant.name_list1[6], "8. " + player.participant.name_list1[7], "9. " + player.participant.name_list1[8],
        "10. " + player.participant.name_list1[9]]
        return dict(player_why = player_why)

class Pref_TT_Other(Page):
    form_model = 'player'
    form_fields = ['f1_3_2','f2_3_2','f3_3_2','f4_3_2','f5_3_2','f6_3_2','f7_3_2',
    'f8_3_2','f9_3_2','f10_3_2']
    @staticmethod
    def vars_for_template(player: Player):
        players_other = []
        if player.f1_2_2 == "9. Other":
            player1 = [player.participant.name_list1[0]]
            players_other = players_other + player1
        if player.f2_2_2 == "9. Other":
            player2 = [player.participant.name_list1[1]]
            players_other = players_other + player2
        if player.f3_2_2 == "9. Other":
            player3 = [player.participant.name_list1[2]]
            players_other = players_other + player3
        if player.f4_2_2 == "9. Other":
            player4 = [player.participant.name_list1[3]]
            players_other = players_other + player4
        if player.f5_2_2 == "9. Other":
            player5 = [player.participant.name_list1[4]]
            players_other = players_other + player5
        if player.f6_2_2 == "9. Other":
            player6 = [player.participant.name_list1[5]]
            players_other = players_other + player6
        if player.f7_2_2 == "9. Other":
            player7 = [player.participant.name_list1[6]]
            players_other = players_other + player7
        if player.f8_2_2 == "9. Other":
            player8 = [player.participant.name_list1[7]]
            players_other = players_other + player8
        if player.f9_2_2 == "9. Other":
            player9 = [player.participant.name_list1[8]]
            players_other = players_other + player9
        if player.f10_2_2 == "9. Other":
            player10 = [player.participant.name_list1[9]]
            players_other = players_other + player10
        return dict(players_other = players_other)
    @staticmethod
    def is_displayed(player: Player):
        return (player.f1_2_2 == "9. Other") or (player.f2_2_2 == "9. Other") or (player.f3_2_2 == "9. Other") or (player.f4_2_2 == "9. Other") or (player.f5_2_2 == "9. Other") or (player.f6_2_2 == "9. Other") or (player.f7_2_2 == "9. Other") or (player.f8_2_2 == "9. Other") or (player.f9_2_2 == "9. Other") or (player.f10_2_2 == "9. Other")

page_sequence = [Pref_Helper, Pref_Helper_Why, Pref_Helper_Other, Pref_TT, Pref_TT_Why, Pref_TT_Other]
