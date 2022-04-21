from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = '___Round1_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    TASKS = ['1', '2']
    SUB1TASKS = ['Econ1', 'Cook1', 'Sport1']
    SUB2TASKS = ['Econ2', 'Cook2', 'Sport2']
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    econhints1_partner1 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints1_partner2 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints1_partner3 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints1_partner4 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints2_partner1 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints2_partner2 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints2_partner3 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econhints2_partner4 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints1_partner1 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints1_partner2 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints1_partner3 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints1_partner4 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints2_partner1 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints2_partner2 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints2_partner3 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookhints2_partner4 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints1_partner1 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints1_partner2 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints1_partner3 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints1_partner4 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints2_partner1 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints2_partner2 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints2_partner3 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    sporthints2_partner4 = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults1_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults1_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults1_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults1_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults2_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults2_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults2_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults2_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults1_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults1_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults1_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults1_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults2_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults2_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults2_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults2_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults1_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults1_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults1_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults1_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults2_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults2_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults2_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults2_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults01_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults01_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults01_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults01_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults02_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults02_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults02_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    econresults02_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults01_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults01_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults01_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults01_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults02_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults02_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults02_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    cookresults02_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults01_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults01_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults01_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults01_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults02_partner1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults02_partner2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults02_partner3 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )
    sportresults02_partner4 = models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    session = subsession.session
    session.arrived_ids = set()
    session.wait_for_ids = set()

    if subsession.round_number == 1:
        for p in subsession.get_players():
            initialize_variables(subsession)
            round_numbers = list(range(1, 3))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))
            sub_round_number1 = list(range(2, 5))
            random.shuffle(sub_round_number1)
            sub_round_number2 = list(range(6, 9))
            random.shuffle(sub_round_number2)
            round_number_1 = task_round['1']
            p.participant.task_rounds1 = dict()
            if round_number_1 == 1:
                p.participant.task_rounds1.update({'1': 1})
                task_rounds_1_1 = dict(zip(C.SUB1TASKS, sub_round_number1))
                p.participant.task_rounds1.update(task_rounds_1_1)
            elif round_number_1 == 2:
                p.participant.task_rounds1.update({'1': 5})
                task_rounds_1_2 = dict(zip(C.SUB1TASKS, sub_round_number2))
                p.participant.task_rounds1.update(task_rounds_1_2)

            round_number_2 = task_round['2']
            if round_number_2 == 1:
                p.participant.task_rounds1.update({'2': 1})
                task_rounds_2_1 = dict(zip(C.SUB2TASKS, sub_round_number1))
                p.participant.task_rounds1.update(task_rounds_2_1)
            elif round_number_2 == 2:
                p.participant.task_rounds1.update({'2': 5})
                task_rounds_2_2 = dict(zip(C.SUB2TASKS, sub_round_number2))
                p.participant.task_rounds1.update(task_rounds_2_2)


def initialize_variables(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.p_helping = dict(pftt1=0, pftt2=0, pmtt1=0, pmtt2=0, rftt1=0, rftt2=0, rmtt1=0, rmtt2=0)

        int = list(range(1, 21))
        random.shuffle(int)
        p.participant.pref_helper = {int[0]: 1, int[1]: 2, int[2]: 3, int[3]: 4, int[4]: 5,
                                     int[5]: 6, int[6]: 7, int[7]: 8, int[8]: 9, int[9]: 10, int[10]: 11, int[11]: 12,
                                     int[12]: 13, int[13]: 14, int[14]: 15, int[15]: 16, int[16]: 17, int[17]: 18,
                                     int[18]: 19, int[19]: 20}
        p.participant.pref_helper_female = {int[0]: 1, int[1]: 2, int[3]: 4, int[4]: 5,
                                            int[7]: 8, int[10]: 11, int[11]: 12, int[12]: 13, int[13]: 14, int[14]: 15,
                                            int[15]: 16}
        p.participant.pref_helper_male = {int[2]: 3, int[5]: 6, int[6]: 7, int[8]: 9,
                                          int[9]: 10, int[16]: 17, int[17]: 18, int[18]: 19, int[19]: 20}

        p.participant.partner1 = 0
        p.participant.partner2 = 0
        p.participant.partner3 = 0
        p.participant.partner4 = 0
        p.participant.partner5 = 0
        p.participant.partner6 = 0
        p.participant.partner7 = 0
        p.participant.partner8 = 0

        p.participant.partnerf1 = 0
        p.participant.partnerf2 = 0
        p.participant.partnerf3 = 0
        p.participant.partnerf4 = 0
        p.participant.partnerm1 = 0
        p.participant.partnerm2 = 0
        p.participant.partnerm3 = 0
        p.participant.partnerm4 = 0

        p.participant.count_participant = 0


def set_players(subsession: Subsession):
    upper = session.count + 1
    int = list(range(1, upper))
    random.shuffle(int)
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            for i in range(len(int)):
                if p.id_in_group == i + 1:
                    p.participant.true_id = int[i]


def set_helpers(subsession: Subsession):
    session = subsession.session
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            for key in p.participant.pref_helper:
                if p.participant.gender == 0:  # female
                    if (key in p.participant.pref_helper_female) and (
                            p.participant.pref_helper_female[key] != p.id_in_group) and (p.participant.partner1 == 0):
                        helper1_id = p.participant.pref_helper_female[key]
                        helper1 = g.get_player_by_id(helper1_id)
                        if helper1.participant.p_helping['pftt1'] == 0:
                            helper1.participant.partnerf1 = p.id_in_group
                            p.participant.partner1 = helper1_id
                            helper1.participant.p_helping['pftt1'] = p.id_in_group
                        elif helper1.participant.p_helping['pftt2'] == 0:
                            helper1.participant.partnerf2 = p.id_in_group
                            p.participant.partner1 = helper1_id
                            helper1.participant.p_helping['pftt2'] = p.id_in_group
                    elif (key in p.participant.pref_helper_female) and (
                            p.participant.pref_helper_female[key] != p.id_in_group) and (
                            p.participant.pref_helper_female[key] != p.participant.partner1) and (
                            p.participant.partner2 == 0):
                        helper2_id = p.participant.pref_helper_female[key]
                        helper2 = g.get_player_by_id(helper2_id)
                        if helper2.participant.p_helping['pftt1'] == 0:
                            helper2.participant.partnerf1 = p.id_in_group
                            p.participant.partner2 = helper2_id
                            helper2.participant.p_helping['pftt1'] = p.id_in_group
                        elif helper2.participant.p_helping['pftt2'] == 0:
                            helper2.participant.partnerf2 = p.id_in_group
                            p.participant.partner2 = helper2_id
                            helper2.participant.p_helping['pftt2'] = p.id_in_group
                    elif (key in p.participant.pref_helper_male) and (p.participant.partner3 == 0):
                        helper3_id = p.participant.pref_helper_male[key]
                        helper3 = g.get_player_by_id(helper3_id)
                        if helper3.participant.p_helping['pftt1'] == 0:
                            helper3.participant.partnerf1 = p.id_in_group
                            p.participant.partner3 = helper3_id
                            helper3.participant.p_helping['pftt1'] = p.id_in_group
                        elif helper3.participant.p_helping['pftt2'] == 0:
                            helper3.participant.partnerf2 = p.id_in_group
                            p.participant.partner3 = helper3_id
                            helper3.participant.p_helping['pftt2'] = p.id_in_group
                    elif (key in p.participant.pref_helper_male) and (
                            p.participant.pref_helper_male[key] != p.participant.partner3) and (
                            p.participant.partner4 == 0):
                        helper4_id = p.participant.pref_helper_male[key]
                        helper4 = g.get_player_by_id(helper4_id)
                        if helper4.participant.p_helping['pftt1'] == 0:
                            helper4.participant.partnerf1 = p.id_in_group
                            p.participant.partner4 = helper4_id
                            helper4.participant.p_helping['pftt1'] = p.id_in_group
                        elif helper4.participant.p_helping['pftt2'] == 0:
                            helper4.participant.partnerf2 = p.id_in_group
                            p.participant.partner4 = helper4_id
                            helper4.participant.p_helping['pftt2'] = p.id_in_group
                else:  # male
                    if (key in p.participant.pref_helper_female) and (p.participant.partner1 == 0):
                        helper1_id = p.participant.pref_helper_female[key]
                        helper1 = g.get_player_by_id(helper1_id)
                        if helper1.participant.p_helping['pmtt1'] == 0:
                            helper1.participant.partnerm1 = p.id_in_group
                            p.participant.partner1 = helper1_id
                            helper1.participant.p_helping['pmtt1'] = p.id_in_group
                        elif helper1.participant.p_helping['pmtt2'] == 0:
                            helper1.participant.partnerm2 = p.id_in_group
                            p.participant.partner1 = helper1_id
                            helper1.participant.p_helping['pmtt2'] = p.id_in_group
                    elif (key in p.participant.pref_helper_female) and (
                            p.participant.pref_helper_female[key] != p.participant.partner1) and (
                            p.participant.partner2 == 0):
                        helper2_id = p.participant.pref_helper_female[key]
                        helper2 = g.get_player_by_id(helper2_id)
                        if helper2.participant.p_helping['pmtt1'] == 0:
                            helper2.participant.partnerm1 = p.id_in_group
                            p.participant.partner2 = helper2_id
                            helper2.participant.p_helping['pmtt1'] = p.id_in_group
                        elif helper2.participant.p_helping['pmtt2'] == 0:
                            helper2.participant.partnerm2 = p.id_in_group
                            p.participant.partner2 = helper2_id
                            helper2.participant.p_helping['pmtt2'] = p.id_in_group
                    elif (key in p.participant.pref_helper_male) and (
                            p.participant.pref_helper_male[key] != p.id_in_group) and (p.participant.partner3 == 0):
                        helper3_id = p.participant.pref_helper_male[key]
                        helper3 = g.get_player_by_id(helper3_id)
                        if helper3.participant.p_helping['pmtt1'] == 0:
                            helper3.participant.partnerm1 = p.id_in_group
                            p.participant.partner3 = helper3_id
                            helper3.participant.p_helping['pmtt1'] = p.id_in_group
                        elif helper3.participant.p_helping['pmtt2'] == 0:
                            helper3.participant.partnerm2 = p.id_in_group
                            p.participant.partner3 = helper3_id
                            helper3.participant.p_helping['pmtt2'] = p.id_in_group
                    elif (key in p.participant.pref_helper_male) and (
                            p.participant.pref_helper_male[key] != p.id_in_group) and (
                            p.participant.pref_helper_male[key] != p.participant.partner3) and (
                            p.participant.partner4 == 0):
                        helper4_id = p.participant.pref_helper_male[key]
                        helper4 = g.get_player_by_id(helper4_id)
                        if helper4.participant.p_helping['pmtt1'] == 0:
                            helper4.participant.partnerm1 = p.id_in_group
                            p.participant.partner4 = helper4_id
                            helper4.participant.p_helping['pmtt1'] = p.id_in_group
                        elif helper4.participant.p_helping['pmtt2'] == 0:
                            helper4.participant.partnerm2 = p.id_in_group
                            p.participant.partner4 = helper4_id
                            helper4.participant.p_helping['pmtt2'] = p.id_in_group
            if (p.participant.partner1 == 0) | (p.participant.partner2 == 0) | (p.participant.partner3 == 0) | (
                    p.participant.partner4 == 0):
                set_exceptions(subsession)
            if (p.participant.partner1 == 0) | (p.participant.partner2 == 0) | (p.participant.partner3 == 0) | (
                    p.participant.partner4 == 0):
                set_exceptions2(subsession)
            set_randoms(subsession)
            if (p.participant.partner5 == 0) | (p.participant.partner6 == 0) | (p.participant.partner7 == 0) | (
                    p.participant.partner8 == 0):
                set_exceptions_randoms(subsession)
    session = subsession.session
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            print(p.participant.p_helping)
            if (p.participant.partner1 == 0) | (p.participant.partner2 == 0) | (p.participant.partner3 == 0) | (
                    p.participant.partner4 == 0):
                print("something is wrong with exceptions")
                print("partner1 = ")
                print(p.participant.partner1)
                print("partner2 = ")
                print(p.participant.partner2)
                print("partner3 = ")
                print(p.participant.partner3)
                print("partner4 = ")
                print(p.participant.partner4)
            if (p.participant.partner5 == 0) | (p.participant.partner6 == 0) | (p.participant.partner7 == 0) | (
                    p.participant.partner8 == 0):
                print(p.id_in_group)
                print("something is wrong with randoms")
                print("partner5 = ")
                print(p.participant.partner5)
                print("partner6 = ")
                print(p.participant.partner6)
                print("partner7 = ")
                print(p.participant.partner7)
                print("partner8 = ")
                print(p.participant.partner8)
            if (p.participant.partnerf1 == 0) | (p.participant.partnerf2 == 0) | (p.participant.partnerf3 == 0) | (
                    p.participant.partnerf4 == 0):
                print("something is wrong with female assignment")
                print("partnerf1 = ")
                print(p.participant.partnerf1)
                print("partnerf2 = ")
                print(p.participant.partnerf2)
                print("partnerf3 = ")
                print(p.participant.partnerf3)
                print("partnerf4 = ")
                print(p.participant.partnerf4)
            if (p.participant.partnerm1 == 0) | (p.participant.partnerm2 == 0) | (p.participant.partnerm3 == 0) | (
                    p.participant.partnerm4 == 0):
                print("something is wrong with male assignment")
                print("partnerm1 = ")
                print(p.participant.partnerm1)
                print("partnerm2 = ")
                print(p.participant.partnerm2)
                print("partnerm3 = ")
                print(p.participant.partnerm3)
                print("partnerm4 = ")
                print(p.participant.partnerm4)


def set_exceptions(subsession: Subsession):
    # catch exceptions and make random if needed
    session = subsession.session
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            if p.participant.gender == 0:  # female
                if p.participant.partner1 == 0:
                    upper = session.count + 1
                    int1 = list(range(1, upper))
                    random.shuffle(int1)
                    for i in range(len(int1)):
                        if (int1[i] != p.id_in_group) and (int1[i] != p.participant.partner2) and (
                                int1[i] != p.participant.partner3) and (int1[i] != p.participant.partner4):
                            helper1_id = int1[i]
                            helper1 = g.get_player_by_id(helper1_id)
                            if helper1.participant.p_helping['pftt1'] == 0:
                                helper1.participant.partnerf1 = p.id_in_group
                                p.participant.partner1 = helper1_id
                                helper1.participant.p_helping['pftt1'] = p.id_in_group
                                break
                            elif helper1.participant.p_helping['pftt2'] == 0:
                                helper1.participant.partnerf2 = p.id_in_group
                                p.participant.partner1 = helper1_id
                                helper1.participant.p_helping['pftt2'] = p.id_in_group
                                break
                if p.participant.partner2 == 0:
                    upper = session.count + 1
                    int2 = list(range(1, upper))
                    random.shuffle(int2)
                    for j in range(len(int2)):
                        if (int2[j] != p.id_in_group) and (int2[j] != p.participant.partner1) and (
                                int2[j] != p.participant.partner3) and (int2[j] != p.participant.partner4):
                            helper2_id = int2[j]
                            helper2 = g.get_player_by_id(helper2_id)
                            if helper2.participant.p_helping['pftt1'] == 0:
                                helper2.participant.partnerf1 = p.id_in_group
                                p.participant.partner2 = helper2_id
                                helper2.participant.p_helping['pftt1'] = p.id_in_group
                                break
                            elif helper2.participant.p_helping['pftt2'] == 0:
                                helper2.participant.partnerf2 = p.id_in_group
                                p.participant.partner2 = helper2_id
                                helper2.participant.p_helping['pftt2'] = p.id_in_group
                                break
                if p.participant.partner3 == 0:
                    upper = session.count + 1
                    int3 = list(range(1, upper))
                    random.shuffle(int3)
                    for k in range(len(int3)):
                        if (int3[k] != p.id_in_group) and (int3[k] != p.participant.partner1) and (
                                int3[k] != p.participant.partner2) and (int3[k] != p.participant.partner4):
                            helper3_id = int3[k]
                            helper3 = g.get_player_by_id(helper3_id)
                            if helper3.participant.p_helping['pftt1'] == 0:
                                helper3.participant.partnerf1 = p.id_in_group
                                p.participant.partner3 = helper3_id
                                helper3.participant.p_helping['pftt1'] = p.id_in_group
                                break
                            elif helper3.participant.p_helping['pftt2'] == 0:
                                helper3.participant.partnerf2 = p.id_in_group
                                p.participant.partner3 = helper3_id
                                helper3.participant.p_helping['pftt2'] = p.id_in_group
                                break
                if p.participant.partner4 == 0:
                    upper = session.count + 1
                    int4 = list(range(1, upper))
                    random.shuffle(int4)
                    for l in range(len(int4)):
                        if (int4[l] != p.id_in_group) and (int4[l] != p.participant.partner1) and (
                                int4[l] != p.participant.partner2) and (int4[l] != p.participant.partner3):
                            helper4_id = int4[l]
                            helper4 = g.get_player_by_id(helper4_id)
                            if helper4.participant.p_helping['pftt1'] == 0:
                                helper4.participant.partnerf1 = p.id_in_group
                                p.participant.partner4 = helper4_id
                                helper4.participant.p_helping['pftt1'] = p.id_in_group
                                break
                            elif helper4.participant.p_helping['pftt2'] == 0:
                                helper4.participant.partnerf2 = p.id_in_group
                                p.participant.partner4 = helper4_id
                                helper4.participant.p_helping['pftt2'] = p.id_in_group
                                break
            else:
                if p.participant.partner1 == 0:
                    upper = session.count + 1
                    int1 = list(range(1, upper))
                    random.shuffle(int1)
                    for i in range(len(int1)):
                        if (int1[i] != p.id_in_group) and (int1[i] != p.participant.partner2) and (
                                int1[i] != p.participant.partner3) and (int1[i] != p.participant.partner4):
                            helper1_id = int1[i]
                            helper1 = g.get_player_by_id(helper1_id)
                            if helper1.participant.p_helping['pmtt1'] == 0:
                                helper1.participant.partnerm1 = p.id_in_group
                                p.participant.partner1 = helper1_id
                                helper1.participant.p_helping['pmtt1'] = p.id_in_group
                                break
                            elif helper1.participant.p_helping['pmtt2'] == 0:
                                helper1.participant.partnerm2 = p.id_in_group
                                p.participant.partner1 = helper1_id
                                helper1.participant.p_helping['pmtt2'] = p.id_in_group
                                break
                if p.participant.partner2 == 0:
                    upper = session.count + 1
                    int2 = list(range(1, upper))
                    random.shuffle(int2)
                    for j in range(len(int2)):
                        if (int2[j] != p.id_in_group) and (int2[j] != p.participant.partner1) and (
                                int2[j] != p.participant.partner3) and (int2[j] != p.participant.partner4):
                            helper2_id = int2[j]
                            helper2 = g.get_player_by_id(helper2_id)
                            if helper2.participant.p_helping['pmtt1'] == 0:
                                helper2.participant.partnerm1 = p.id_in_group
                                p.participant.partner2 = helper2_id
                                helper2.participant.p_helping['pmtt1'] = p.id_in_group
                                break
                            elif helper2.participant.p_helping['pmtt2'] == 0:
                                helper2.participant.partnerm2 = p.id_in_group
                                p.participant.partner2 = helper2_id
                                helper2.participant.p_helping['pmtt2'] = p.id_in_group
                                break
                if p.participant.partner3 == 0:
                    upper = session.count + 1
                    int3 = list(range(1, upper))
                    random.shuffle(int3)
                    for k in range(len(int3)):
                        if (int3[k] != p.id_in_group) and (int3[k] != p.participant.partner1) and (
                                int3[k] != p.participant.partner2) and (int3[k] != p.participant.partner4):
                            helper3_id = int3[k]
                            helper3 = g.get_player_by_id(helper3_id)
                            if helper3.participant.p_helping['pmtt1'] == 0:
                                helper3.participant.partnerm1 = p.id_in_group
                                p.participant.partner3 = helper3_id
                                helper3.participant.p_helping['pmtt1'] = p.id_in_group
                                break
                            elif helper3.participant.p_helping['pmtt2'] == 0:
                                helper3.participant.partnerm2 = p.id_in_group
                                p.participant.partner3 = helper3_id
                                helper3.participant.p_helping['pmtt2'] = p.id_in_group
                                break
                if p.participant.partner4 == 0:
                    upper = session.count + 1
                    int4 = list(range(1, upper))
                    random.shuffle(int4)
                    for l in range(len(int4)):
                        if (int4[l] != p.id_in_group) and (int4[l] != p.participant.partner1) and (
                                int4[l] != p.participant.partner2) and (int4[l] != p.participant.partner3):
                            helper4_id = int4[l]
                            helper4 = g.get_player_by_id(helper4_id)
                            if helper4.participant.p_helping['pmtt1'] == 0:
                                helper4.participant.partnerm1 = p.id_in_group
                                p.participant.partner4 = helper4_id
                                helper4.participant.p_helping['pmtt1'] = p.id_in_group
                                break
                            elif helper4.participant.p_helping['pmtt2'] == 0:
                                helper4.participant.partnerm2 = p.id_in_group
                                p.participant.partner4 = helper4_id
                                helper4.participant.p_helping['pmtt2'] = p.id_in_group
                                break


def set_exceptions2(subsession: Subsession):
    # catch exceptions that go awol
    session = subsession.session
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            if p.participant.gender == 0:  # female
                if p.participant.partner1 == 0:
                    upper = session.count + 1
                    int1 = list(range(1, upper))
                    random.shuffle(int1)
                    for i in range(len(int1)):
                        if (int1[i] != p.id_in_group) and (int1[i] != p.participant.partner2) and (
                                int1[i] != p.participant.partner3) and (int1[i] != p.participant.partner4):
                            helper1_id = int1[i]
                            helper1 = g.get_player_by_id(helper1_id)
                            old_player_id = helper1.participant.p_helping['pftt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper1.participant.partnerf1 = p.id_in_group
                            p.participant.partner1 = helper1_id
                            helper1.participant.p_helping['pftt1'] = p.id_in_group
                            int1_1 = list(range(1, 19))
                            random.shuffle(int1_1)
                            for i1 in range(len(int1_1)):
                                helper_new_id = int1_1[i1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pftt1'] == 0:
                                    helper_new.participant.partnerf1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper1_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper1_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper1_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper1_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pftt2'] == 0:
                                    helper_new.participant.partnerf2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper1_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper1_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper1_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper1_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner2 == 0:
                    upper = session.count + 1
                    int2 = list(range(1, upper))
                    random.shuffle(int2)
                    for j in range(len(int2)):
                        if (int2[j] != p.id_in_group) and (int2[j] != p.participant.partner1) and (
                                int2[j] != p.participant.partner3) and (int2[j] != p.participant.partner4):
                            helper2_id = int2[j]
                            helper2 = g.get_player_by_id(helper2_id)
                            old_player_id = helper2.participant.p_helping['pftt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper2.participant.partnerf1 = p.id_in_group
                            p.participant.partner2 = helper2_id
                            helper2.participant.p_helping['pftt1'] = p.id_in_group
                            upper = session.count + 1
                            int2_1 = list(range(1, upper))
                            random.shuffle(int2_1)
                            for j1 in range(len(int2_1)):
                                helper_new_id = int2_1[j1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pftt1'] == 0:
                                    helper_new.participant.partnerf1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper2_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper2_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper2_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper2_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pftt2'] == 0:
                                    helper_new.participant.partnerf2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper2_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper2_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper2_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper2_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner3 == 0:
                    upper = session.count + 1
                    int3 = list(range(1, upper))
                    random.shuffle(int3)
                    for k in range(len(int3)):
                        if (int3[k] != p.id_in_group) and (int3[k] != p.participant.partner1) and (
                                int3[k] != p.participant.partner2) and (int3[k] != p.participant.partner4):
                            helper3_id = int3[k]
                            helper3 = g.get_player_by_id(helper3_id)
                            old_player_id = helper3.participant.p_helping['pftt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper3.participant.partnerf1 = p.id_in_group
                            p.participant.partner3 = helper3_id
                            helper3.participant.p_helping['pftt1'] = p.id_in_group
                            upper = session.count + 1
                            int3_1 = list(range(1, upper))
                            random.shuffle(int3_1)
                            for k1 in range(len(int3_1)):
                                helper_new_id = int3_1[k1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pftt1'] == 0:
                                    helper_new.participant.partnerf1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper3_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper3_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper3_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper3_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pftt2'] == 0:
                                    helper_new.participant.partnerf2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper3_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper3_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper3_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper3_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner4 == 0:
                    upper = session.count + 1
                    int4 = list(range(1, upper))
                    random.shuffle(int4)
                    for l in range(len(int4)):
                        if (int4[l] != p.id_in_group) and (int4[l] != p.participant.partner1) and (
                                int4[l] != p.participant.partner2) and (int4[l] != p.participant.partner3):
                            helper4_id = int4[l]
                            helper4 = g.get_player_by_id(helper4_id)
                            old_player_id = helper4.participant.p_helping['pftt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper4.participant.partnerf1 = p.id_in_group
                            p.participant.partner4 = helper4_id
                            helper4.participant.p_helping['pftt1'] = p.id_in_group
                            upper = session.count + 1
                            int4_1 = list(range(1, upper))
                            random.shuffle(int4_1)
                            for l1 in range(len(int4_1)):
                                helper_new_id = int4_1[l1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pftt1'] == 0:
                                    helper_new.participant.partnerf1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper4_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper4_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper4_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper4_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pftt2'] == 0:
                                    helper_new.participant.partnerf2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper4_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper4_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper4_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper4_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pftt2'] = old_player.id_in_group
                                    break
                            break
            else:
                if p.participant.partner1 == 0:
                    upper = session.count + 1
                    int1 = list(range(1, upper))
                    random.shuffle(int1)
                    for i in range(len(int1)):
                        if (int1[i] != p.id_in_group) and (int1[i] != p.participant.partner2) and (
                                int1[i] != p.participant.partner3) and (int1[i] != p.participant.partner4):
                            helper1_id = int1[i]
                            helper1 = g.get_player_by_id(helper1_id)
                            old_player_id = helper1.participant.p_helping['pmtt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper1.participant.partnerm1 = p.id_in_group
                            p.participant.partner1 = helper1_id
                            helper1.participant.p_helping['pmtt1'] = p.id_in_group
                            upper = session.count + 1
                            int1_1 = list(range(1, upper))
                            random.shuffle(int1_1)
                            for i1 in range(len(int1_1)):
                                helper_new_id = int1_1[i1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pmtt1'] == 0:
                                    helper_new.participant.partnerm1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper1_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper1_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper1_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper1_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pmtt2'] == 0:
                                    helper_new.participant.partnerm2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper1_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper1_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper1_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper1_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner2 == 0:
                    upper = session.count + 1
                    int2 = list(range(1, upper))
                    random.shuffle(int2)
                    for j in range(len(int2)):
                        if (int2[j] != p.id_in_group) and (int2[j] != p.participant.partner1) and (
                                int2[j] != p.participant.partner3) and (int2[j] != p.participant.partner4):
                            helper2_id = int2[j]
                            helper2 = g.get_player_by_id(helper2_id)
                            old_player_id = helper2.participant.p_helping['pmtt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper2.participant.partnerm1 = p.id_in_group
                            p.participant.partner2 = helper2_id
                            helper2.participant.p_helping['pmtt1'] = p.id_in_group
                            upper = session.count + 1
                            int2_1 = list(range(1, upper))
                            random.shuffle(int2_1)
                            for j1 in range(len(int2_1)):
                                helper_new_id = int2_1[j1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pmtt1'] == 0:
                                    helper_new.participant.partnerm1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper2_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper2_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper2_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper2_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pmtt2'] == 0:
                                    helper_new.participant.partnerm2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper2_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper2_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper2_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper2_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner3 == 0:
                    upper = session.count + 1
                    int3 = list(range(1, upper))
                    random.shuffle(int3)
                    for k in range(len(int3)):
                        if (int3[k] != p.id_in_group) and (int3[k] != p.participant.partner1) and (
                                int3[k] != p.participant.partner2) and (int3[k] != p.participant.partner4):
                            helper3_id = int3[k]
                            helper3 = g.get_player_by_id(helper3_id)
                            old_player_id = helper3.participant.p_helping['pmtt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper3.participant.partnerm1 = p.id_in_group
                            p.participant.partner3 = helper3_id
                            helper3.participant.p_helping['pmtt1'] = p.id_in_group
                            upper = session.count + 1
                            int3_1 = list(range(1, upper))
                            random.shuffle(int3_1)
                            for k1 in range(len(int3_1)):
                                helper_new_id = int3_1[k1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pmtt1'] == 0:
                                    helper_new.participant.partnerm1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper3_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper3_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper3_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper3_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pmtt2'] == 0:
                                    helper_new.participant.partnerm2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper3_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper3_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper3_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper3_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner4 == 0:
                    upper = session.count + 1
                    int4 = list(range(1, upper))
                    random.shuffle(int4)
                    for l in range(len(int4)):
                        if (int4[l] != p.id_in_group) and (int4[l] != p.participant.partner1) and (
                                int4[l] != p.participant.partner2) and (int4[l] != p.participant.partner3):
                            helper4_id = int4[l]
                            helper4 = g.get_player_by_id(helper4_id)
                            old_player_id = helper4.participant.p_helping['pmtt1']
                            old_player = g.get_player_by_id(old_player_id)
                            helper4.participant.partnerm1 = p.id_in_group
                            p.participant.partner4 = helper4_id
                            helper4.participant.p_helping['pmtt1'] = p.id_in_group
                            upper = session.count + 1
                            int4_1 = list(range(1, upper))
                            random.shuffle(int4_1)
                            for l1 in range(len(int4_1)):
                                helper_new_id = int4_1[l1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['pmtt1'] == 0:
                                    helper_new.participant.partnerm1 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper4_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper4_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper4_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper4_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['pmtt2'] == 0:
                                    helper_new.participant.partnerm2 = old_player.id_in_group
                                    if old_player.participant.partner1 == helper4_id:
                                        old_player.participant.partner1 = helper_new_id
                                    elif old_player.participant.partner2 == helper4_id:
                                        old_player.participant.partner2 = helper_new_id
                                    elif old_player.participant.partner3 == helper4_id:
                                        old_player.participant.partner3 = helper_new_id
                                    elif old_player.participant.partner4 == helper4_id:
                                        old_player.participant.partner4 = helper_new_id
                                    helper_new.participant.p_helping['pmtt2'] = old_player.id_in_group
                                    break
                            break


# set all randoms
# random helper2
def set_randoms(subsession: Subsession):
    session = subsession.session
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            if p.participant.gender == 0:  # female
                upper = session.count + 1
                int1 = list(range(1, upper))
                random.shuffle(int1)
                for i in range(len(int1)):
                    if (p.participant.partner5 == 0) and (int1[i] != p.id_in_group) and (
                            int1[i] != p.participant.partner1) and (int1[i] != p.participant.partner2) and (
                            int1[i] != p.participant.partner3) and (int1[i] != p.participant.partner4):
                        helper5_id = int1[i]
                        helper5 = g.get_player_by_id(helper5_id)
                        if helper5.participant.p_helping['rftt1'] == 0:
                            helper5.participant.partnerf3 = p.id_in_group
                            p.participant.partner5 = helper5_id
                            helper5.participant.p_helping['rftt1'] = p.id_in_group
                            break
                        elif helper5.participant.p_helping['rftt2'] == 0:
                            helper5.participant.partnerf4 = p.id_in_group
                            p.participant.partner5 = helper5_id
                            helper5.participant.p_helping['rftt2'] = p.id_in_group
                            break
                int2 = list(range(1, upper))
                random.shuffle(int2)
                for j in range(len(int2)):
                    if (p.participant.partner6 == 0) and (int2[j] != p.id_in_group) and (
                            int2[j] != p.participant.partner1) and (int2[j] != p.participant.partner2) and (
                            int2[j] != p.participant.partner3) and (int2[j] != p.participant.partner4) and (
                            int2[j] != p.participant.partner5):
                        helper6_id = int2[j]
                        helper6 = g.get_player_by_id(helper6_id)
                        if helper6.participant.p_helping['rftt1'] == 0:
                            helper6.participant.partnerf3 = p.id_in_group
                            p.participant.partner6 = helper6_id
                            helper6.participant.p_helping['rftt1'] = p.id_in_group
                            break
                        elif helper6.participant.p_helping['rftt2'] == 0:
                            helper6.participant.partnerf4 = p.id_in_group
                            p.participant.partner6 = helper6_id
                            helper6.participant.p_helping['rftt2'] = p.id_in_group
                            break
                int3 = list(range(1, upper))
                random.shuffle(int3)
                for k in range(len(int3)):
                    if (p.participant.partner7 == 0) and (int3[k] != p.id_in_group) and (
                            int3[k] != p.participant.partner1) and (int3[k] != p.participant.partner2) and (
                            int3[k] != p.participant.partner3) and (int3[k] != p.participant.partner4) and (
                            int3[k] != p.participant.partner5) and (int3[k] != p.participant.partner6):
                        helper7_id = int3[k]
                        helper7 = g.get_player_by_id(helper7_id)
                        if helper7.participant.p_helping['rftt1'] == 0:
                            helper7.participant.partnerf3 = p.id_in_group
                            p.participant.partner7 = helper7_id
                            helper7.participant.p_helping['rftt1'] = p.id_in_group
                            break
                        elif helper7.participant.p_helping['rftt2'] == 0:
                            helper7.participant.partnerf4 = p.id_in_group
                            p.participant.partner7 = helper7_id
                            helper7.participant.p_helping['rftt2'] = p.id_in_group
                            break
                int4 = list(range(1, upper))
                random.shuffle(int4)
                for l in range(len(int4)):
                    if (p.participant.partner8 == 0) and (int4[l] != p.id_in_group) and (
                            int4[l] != p.participant.partner1) and (int4[l] != p.participant.partner2) and (
                            int4[l] != p.participant.partner3) and (int4[l] != p.participant.partner4) and (
                            int4[l] != p.participant.partner5) and (int4[l] != p.participant.partner6) and (
                            int4[l] != p.participant.partner7):
                        helper8_id = int4[l]
                        helper8 = g.get_player_by_id(helper8_id)
                        if helper8.participant.p_helping['rftt1'] == 0:
                            helper8.participant.partnerf3 = p.id_in_group
                            p.participant.partner8 = helper8_id
                            helper8.participant.p_helping['rftt1'] = p.id_in_group
                            break
                        elif helper8.participant.p_helping['rftt2'] == 0:
                            helper8.participant.partnerf4 = p.id_in_group
                            p.participant.partner8 = helper8_id
                            helper8.participant.p_helping['rftt2'] = p.id_in_group
                            break
            else:  # male
                upper = session.count + 1
                int1 = list(range(1, upper))
                random.shuffle(int1)
                for i in range(len(int1)):
                    if (p.participant.partner5 == 0) and (int1[i] != p.id_in_group) and (
                            int1[i] != p.participant.partner1) and (int1[i] != p.participant.partner2) and (
                            int1[i] != p.participant.partner3) and (int1[i] != p.participant.partner4):
                        helper5_id = int1[i]
                        helper5 = g.get_player_by_id(helper5_id)
                        if helper5.participant.p_helping['rmtt1'] == 0:
                            helper5.participant.partnerm3 = p.id_in_group
                            p.participant.partner5 = helper5_id
                            helper5.participant.p_helping['rmtt1'] = p.id_in_group
                            break
                        elif helper5.participant.p_helping['rmtt2'] == 0:
                            helper5.participant.partnerm4 = p.id_in_group
                            p.participant.partner5 = helper5_id
                            helper5.participant.p_helping['rmtt2'] = p.id_in_group
                            break
                int2 = list(range(1, upper))
                random.shuffle(int2)
                for j in range(len(int2)):
                    if (p.participant.partner6 == 0) and (int2[j] != p.id_in_group) and (
                            int2[j] != p.participant.partner1) and (int2[j] != p.participant.partner2) and (
                            int2[j] != p.participant.partner3) and (int2[j] != p.participant.partner4) and (
                            int2[j] != p.participant.partner5):
                        helper6_id = int2[j]
                        helper6 = g.get_player_by_id(helper6_id)
                        if helper6.participant.p_helping['rmtt1'] == 0:
                            helper6.participant.partnerm3 = p.id_in_group
                            p.participant.partner6 = helper6_id
                            helper6.participant.p_helping['rmtt1'] = p.id_in_group
                            break
                        elif helper6.participant.p_helping['rmtt2'] == 0:
                            helper6.participant.partnerm4 = p.id_in_group
                            p.participant.partner6 = helper6_id
                            helper6.participant.p_helping['rmtt2'] = p.id_in_group
                            break
                int3 = list(range(1, upper))
                random.shuffle(int3)
                for k in range(len(int3)):
                    if (p.participant.partner7 == 0) and (int3[k] != p.id_in_group) and (
                            int3[k] != p.participant.partner1) and (int3[k] != p.participant.partner2) and (
                            int3[k] != p.participant.partner3) and (int3[k] != p.participant.partner4) and (
                            int3[k] != p.participant.partner5) and (int3[k] != p.participant.partner6):
                        helper7_id = int3[k]
                        helper7 = g.get_player_by_id(helper7_id)
                        if helper7.participant.p_helping['rmtt1'] == 0:
                            helper7.participant.partnerm3 = p.id_in_group
                            p.participant.partner7 = helper7_id
                            helper7.participant.p_helping['rmtt1'] = p.id_in_group
                            break
                        elif helper7.participant.p_helping['rmtt2'] == 0:
                            helper7.participant.partnerm4 = p.id_in_group
                            p.participant.partner7 = helper7_id
                            helper7.participant.p_helping['rmtt2'] = p.id_in_group
                            break
                int4 = list(range(1, upper))
                random.shuffle(int4)
                for l in range(len(int4)):
                    if (p.participant.partner8 == 0) and (int4[l] != p.id_in_group) and (
                            int4[l] != p.participant.partner1) and (int4[l] != p.participant.partner2) and (
                            int4[l] != p.participant.partner3) and (int4[l] != p.participant.partner4) and (
                            int4[l] != p.participant.partner5) and (int4[l] != p.participant.partner6) and (
                            int4[l] != p.participant.partner7):
                        helper8_id = int4[l]
                        helper8 = g.get_player_by_id(helper8_id)
                        if helper8.participant.p_helping['rmtt1'] == 0:
                            helper8.participant.partnerm3 = p.id_in_group
                            p.participant.partner8 = helper8_id
                            helper8.participant.p_helping['rmtt1'] = p.id_in_group
                            break
                        elif helper8.participant.p_helping['rmtt2'] == 0:
                            helper8.participant.partnerm4 = p.id_in_group
                            p.participant.partner8 = helper8_id
                            helper8.participant.p_helping['rmtt2'] = p.id_in_group
                            break


def set_exceptions_randoms(subsession: Subsession):
    # catch randoms that go awol
    session = subsession.session
    for g in subsession.get_groups():
        for player in session.active_players:
            p = g.get_player_by_id(player)
            if p.participant.gender == 0:  # female
                if p.participant.partner5 == 0:
                    upper = session.count + 1
                    int1 = list(range(1, upper))
                    random.shuffle(int1)
                    for i in range(len(int1)):
                        if (int1[i] != p.id_in_group) and (int1[i] != p.participant.partner1) and (
                                int1[i] != p.participant.partner2) and (int1[i] != p.participant.partner3) and (
                                int1[i] != p.participant.partner4) and (int1[i] != p.participant.partner6) and (
                                int1[i] != p.participant.partner7) and (int1[i] != p.participant.partner8):
                            helper5_id = int1[i]
                            helper5 = g.get_player_by_id(helper5_id)
                            old_player_id = helper5.participant.p_helping['rftt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper5.participant.partnerf4 = p.id_in_group
                            p.participant.partner5 = helper5_id
                            helper5.participant.p_helping['rftt2'] = p.id_in_group
                            upper = session.count + 1
                            int1_1 = list(range(1, upper))
                            random.shuffle(int1_1)
                            for i1 in range(len(int1_1)):
                                helper_new_id = int1_1[i1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rftt1'] == 0:
                                    helper_new.participant.partnerf3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper5_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper5_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper5_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper5_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rftt2'] == 0:
                                    helper_new.participant.partnerf4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper5_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper5_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper5_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper5_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner6 == 0:
                    upper = session.count + 1
                    int2 = list(range(1, upper))
                    random.shuffle(int2)
                    for j in range(len(int2)):
                        if (int2[j] != p.id_in_group) and (int2[j] != p.participant.partner1) and (
                                int2[j] != p.participant.partner2) and (int2[j] != p.participant.partner3) and (
                                int2[j] != p.participant.partner4) and (int2[j] != p.participant.partner5) and (
                                int2[j] != p.participant.partner7) and (int2[j] != p.participant.partner8):
                            helper6_id = int2[j]
                            helper6 = g.get_player_by_id(helper6_id)
                            old_player_id = helper6.participant.p_helping['rftt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper6.participant.partnerf4 = p.id_in_group
                            p.participant.partner6 = helper6_id
                            helper6.participant.p_helping['rftt2'] = p.id_in_group
                            upper = session.count + 1
                            int2_1 = list(range(1, upper))
                            random.shuffle(int2_1)
                            for j1 in range(len(int2_1)):
                                helper_new_id = int2_1[j1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rftt1'] == 0:
                                    helper_new.participant.partnerf3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper6_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper6_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper6_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper6_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rftt2'] == 0:
                                    helper_new.participant.partnerf4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper6_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper6_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper6_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper6_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner7 == 0:
                    upper = session.count + 1
                    int3 = list(range(1, upper))
                    random.shuffle(int3)
                    for k in range(len(int3)):
                        if (int3[k] != p.id_in_group) and (int3[k] != p.participant.partner1) and (
                                int3[k] != p.participant.partner2) and (int3[k] != p.participant.partner3) and (
                                int3[k] != p.participant.partner4) and (int3[k] != p.participant.partner5) and (
                                int3[k] != p.participant.partner6) and (int3[k] != p.participant.partner8):
                            helper7_id = int3[k]
                            helper7 = g.get_player_by_id(helper7_id)
                            old_player_id = helper7.participant.p_helping['rftt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper7.participant.partnerf4 = p.id_in_group
                            p.participant.partner7 = helper7_id
                            helper7.participant.p_helping['rftt2'] = p.id_in_group
                            upper = session.count + 1
                            int3_1 = list(range(1, upper))
                            random.shuffle(int3_1)
                            for k1 in range(len(int3_1)):
                                helper_new_id = int3_1[k1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rftt1'] == 0:
                                    helper_new.participant.partnerf3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper7_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper7_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper7_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper7_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rftt2'] == 0:
                                    helper_new.participant.partnerf4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper7_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper7_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper7_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper7_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner8 == 0:
                    upper = session.count + 1
                    int4 = list(range(1, upper))
                    random.shuffle(int4)
                    for l in range(len(int4)):
                        if (int4[l] != p.id_in_group) and (int4[l] != p.participant.partner1) and (
                                int4[l] != p.participant.partner2) and (int4[l] != p.participant.partner3) and (
                                int4[l] != p.participant.partner4) and (int4[l] != p.participant.partner5) and (
                                int4[l] != p.participant.partner6) and (int4[l] != p.participant.partner7):
                            helper8_id = int4[l]
                            helper8 = g.get_player_by_id(helper8_id)
                            old_player_id = helper8.participant.p_helping['rftt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper8.participant.partnerf4 = p.id_in_group
                            p.participant.partner8 = helper8_id
                            helper8.participant.p_helping['rftt2'] = p.id_in_group
                            upper = session.count + 1
                            int4_1 = list(range(1, upper))
                            random.shuffle(int4_1)
                            for l1 in range(len(int4_1)):
                                helper_new_id = int4_1[l1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rftt1'] == 0:
                                    helper_new.participant.partnerf3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper8_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper8_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper8_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper8_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rftt2'] == 0:
                                    helper_new.participant.partnerf4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper8_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper8_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper8_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper8_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rftt2'] = old_player.id_in_group
                                    break
                            break
            else:
                if p.participant.partner5 == 0:
                    upper = session.count + 1
                    int1 = list(range(1, upper))
                    random.shuffle(int1)
                    for i in range(len(int1)):
                        if (int1[i] != p.id_in_group) and (int1[i] != p.participant.partner1) and (
                                int1[i] != p.participant.partner2) and (int1[i] != p.participant.partner3) and (
                                int1[i] != p.participant.partner4) and (int1[i] != p.participant.partner6) and (
                                int1[i] != p.participant.partner7) and (int1[i] != p.participant.partner8):
                            helper5_id = int1[i]
                            helper5 = g.get_player_by_id(helper5_id)
                            old_player_id = helper5.participant.p_helping['rmtt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper5.participant.partnerm4 = p.id_in_group
                            p.participant.partner5 = helper5_id
                            helper5.participant.p_helping['rmtt2'] = p.id_in_group
                            upper = session.count + 1
                            int1_1 = list(range(1, upper))
                            random.shuffle(int1_1)
                            for i1 in range(len(int1_1)):
                                helper_new_id = int1_1[i1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rmtt1'] == 0:
                                    helper_new.participant.partnerm3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper5_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper5_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper5_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper5_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rmtt2'] == 0:
                                    helper_new.participant.partnerm4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper5_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper5_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper5_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper5_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner6 == 0:
                    upper = session.count + 1
                    int2 = list(range(1, upper))
                    random.shuffle(int2)
                    for j in range(len(int2)):
                        if (int2[j] != p.id_in_group) and (int2[j] != p.participant.partner1) and (
                                int2[j] != p.participant.partner2) and (int2[j] != p.participant.partner3) and (
                                int2[j] != p.participant.partner4) and (int2[j] != p.participant.partner5) and (
                                int2[j] != p.participant.partner7) and (int2[j] != p.participant.partner8):
                            helper6_id = int2[j]
                            helper6 = g.get_player_by_id(helper6_id)
                            old_player_id = helper6.participant.p_helping['rmtt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper6.participant.partnerm4 = p.id_in_group
                            p.participant.partner6 = helper6_id
                            helper6.participant.p_helping['rmtt2'] = p.id_in_group
                            upper = session.count + 1
                            int2_1 = list(range(1, upper))
                            random.shuffle(int2_1)
                            for j1 in range(len(int2_1)):
                                helper_new_id = int2_1[j1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rmtt1'] == 0:
                                    helper_new.participant.partnerm3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper6_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper6_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper6_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper6_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rmtt2'] == 0:
                                    helper_new.participant.partnerm4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper6_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper6_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper6_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper6_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner7 == 0:
                    upper = session.count + 1
                    int3 = list(range(1, upper))
                    random.shuffle(int3)
                    for k in range(len(int3)):
                        if (int3[k] != p.id_in_group) and (int3[k] != p.participant.partner1) and (
                                int3[k] != p.participant.partner2) and (int3[k] != p.participant.partner3) and (
                                int3[k] != p.participant.partner4) and (int3[k] != p.participant.partner5) and (
                                int3[k] != p.participant.partner6) and (int3[k] != p.participant.partner8):
                            helper7_id = int3[k]
                            helper7 = g.get_player_by_id(helper7_id)
                            old_player_id = helper7.participant.p_helping['rmtt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper7.participant.partnerm4 = p.id_in_group
                            p.participant.partner7 = helper7_id
                            helper7.participant.p_helping['rmtt2'] = p.id_in_group
                            upper = session.count + 1
                            int3_1 = list(range(1, upper))
                            random.shuffle(int3_1)
                            for k1 in range(len(int3_1)):
                                helper_new_id = int3_1[k1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rmtt1'] == 0:
                                    helper_new.participant.partnerm3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper7_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper7_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper7_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper7_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rmtt2'] == 0:
                                    helper_new.participant.partnerm4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper7_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper7_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper7_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper7_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt2'] = old_player.id_in_group
                                    break
                            break
                if p.participant.partner8 == 0:
                    upper = session.count + 1
                    int4 = list(range(1, upper))
                    random.shuffle(int4)
                    for l in range(len(int4)):
                        if (int4[l] != p.id_in_group) and (int4[l] != p.participant.partner1) and (
                                int4[l] != p.participant.partner2) and (int4[l] != p.participant.partner3) and (
                                int4[l] != p.participant.partner4) and (int4[l] != p.participant.partner5) and (
                                int4[l] != p.participant.partner6) and (int4[l] != p.participant.partner7):
                            helper8_id = int4[l]
                            helper8 = g.get_player_by_id(helper8_id)
                            old_player_id = helper8.participant.p_helping['rmtt2']
                            old_player = g.get_player_by_id(old_player_id)
                            helper8.participant.partnerm4 = p.id_in_group
                            p.participant.partner8 = helper8_id
                            helper8.participant.p_helping['rmtt2'] = p.id_in_group
                            upper = session.count + 1
                            int4_1 = list(range(1, upper))
                            random.shuffle(int4_1)
                            for l1 in range(len(int4_1)):
                                helper_new_id = int4_1[l1]
                                helper_new = g.get_player_by_id(helper_new_id)
                                if helper_new.participant.p_helping['rmtt1'] == 0:
                                    helper_new.participant.partnerm3 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper8_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper8_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper8_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper8_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt1'] = old_player.id_in_group
                                    break
                                elif helper_new.participant.p_helping['rmtt2'] == 0:
                                    helper_new.participant.partnerm4 = old_player.id_in_group
                                    if old_player.participant.partner5 == helper8_id:
                                        old_player.participant.partner5 = helper_new_id
                                    elif old_player.participant.partner6 == helper8_id:
                                        old_player.participant.partner6 = helper_new_id
                                    elif old_player.participant.partner7 == helper8_id:
                                        old_player.participant.partner7 = helper_new_id
                                    elif old_player.participant.partner8 == helper8_id:
                                        old_player.participant.partner8 = helper_new_id
                                    helper_new.participant.p_helping['rmtt2'] = old_player.id_in_group
                                    break
                            break


def set_hints_given(player: Player):
    player.participant.econ_hint_requests_partner1 = 0
    player.participant.econ_hint_requests_partner2 = 0
    player.participant.econ_hint_requests_partner3 = 0
    player.participant.econ_hint_requests_partner4 = 0
    player.participant.econ_hint_requests_partner5 = 0
    player.participant.econ_hint_requests_partner6 = 0
    player.participant.econ_hint_requests_partner7 = 0
    player.participant.econ_hint_requests_partner8 = 0
    player.participant.cook_hint_requests_partner1 = 0
    player.participant.cook_hint_requests_partner2 = 0
    player.participant.cook_hint_requests_partner3 = 0
    player.participant.cook_hint_requests_partner4 = 0
    player.participant.cook_hint_requests_partner5 = 0
    player.participant.cook_hint_requests_partner6 = 0
    player.participant.cook_hint_requests_partner7 = 0
    player.participant.cook_hint_requests_partner8 = 0
    player.participant.econ_hint_requests_partner1 = 0
    player.participant.sport_hint_requests_partner2 = 0
    player.participant.sport_hint_requests_partner3 = 0
    player.participant.sport_hint_requests_partner4 = 0
    player.participant.sport_hint_requests_partner5 = 0
    player.participant.sport_hint_requests_partner6 = 0
    player.participant.sport_hint_requests_partner7 = 0
    player.participant.sport_hint_requests_partner8 = 0

    player.participant.MP1hints_given_econ = player.econhints1_partner1
    player.participant.MP1hints_given_cook = player.cookhints1_partner1
    player.participant.MP1hints_given_sport = player.sporthints1_partner1
    player.participant.MR1hints_given_econ = player.econhints1_partner2
    player.participant.MR1hints_given_cook = player.cookhints1_partner2
    player.participant.MR1hints_given_sport = player.sporthints1_partner2
    player.participant.WP1hints_given_econ = player.econhints1_partner3
    player.participant.WP1hints_given_cook = player.cookhints1_partner3
    player.participant.WP1hints_given_sport = player.sporthints1_partner3
    player.participant.WR1hints_given_econ = player.econhints1_partner4
    player.participant.WR1hints_given_cook = player.cookhints1_partner4
    player.participant.WR1hints_given_sport = player.sporthints1_partner4
    player.participant.MP2hints_given_econ = player.econhints2_partner1
    player.participant.MP2hints_given_cook = player.cookhints2_partner1
    player.participant.MP2hints_given_sport = player.sporthints2_partner1
    player.participant.MR2hints_given_econ = player.econhints2_partner2
    player.participant.MR2hints_given_cook = player.cookhints2_partner2
    player.participant.MR2hints_given_sport = player.sporthints2_partner2
    player.participant.WP2hints_given_econ = player.econhints2_partner3
    player.participant.WP2hints_given_cook = player.cookhints2_partner3
    player.participant.WP2hints_given_sport = player.sporthints2_partner3
    player.participant.WR2hints_given_econ = player.econhints2_partner4
    player.participant.WR2hints_given_cook = player.cookhints2_partner4
    player.participant.WR2hints_given_sport = player.sporthints2_partner4


def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time

    return participant.expiry - time.time()


class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = ""

    @staticmethod
    def after_all_players_arrive(group: Group):
        set_players(group.get_players()[0].subsession)
        set_helpers(group.get_players()[0].subsession)
# PAGES
# class WaitPage1(Page):
#     @staticmethod
#     def live_method(player: Player, data):
#         set_players(player.subsession)
#         session = player.session
#         for p in session.active_players:
#             session.wait_for_ids.add(p)
#         session.arrived_ids.add(player.id_in_subsession)
#         not_arrived_yet = session.wait_for_ids - session.arrived_ids
#         print("Not arrived", not_arrived_yet)
#         if not_arrived_yet:
#             return {0: dict(not_arrived_yet=not_arrived_yet)}
#         return {0: dict(finished=True)}
#
#     @staticmethod
#     def error_message(player: Player, values):
#         session = player.session
#         if session.arrived_ids != session.wait_for_ids:
#             return "Page somehow proceeded before all players are ready"

class Demographics(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        set_helpers(player.subsession)
        return dict()

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200


class Payment1Transition(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(round=player.round_number)

    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?'.format(partnerm1.participant.label),
                    partner2_label='{}?'.format(partnerm3.participant.label),
                    partner3_label='{}?'.format(partnerf1.participant.label),
                    partner4_label='{}?'.format(partnerf3.participant.label), formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics1Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults1_partner1', 'econresults1_partner2', 'econresults1_partner3',
                             'econresults1_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm1.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm3.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf1.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf3.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econresults1_partner1', 'econresults1_partner2', 'econresults1_partner3',
                      'econresults1_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics1Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults01_partner1', 'econresults01_partner2', 'econresults01_partner3',
                             'econresults01_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm1.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm3.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf1.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf3.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econresults01_partner1', 'econresults01_partner2', 'econresults01_partner3',
                      'econresults01_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?'.format(partnerm1.participant.label),
                    partner2_label='{}?'.format(partnerm3.participant.label),
                    partner3_label='{}?'.format(partnerf1.participant.label),
                    partner4_label='{}?'.format(partnerf3.participant.label), formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking1Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults1_partner1', 'cookresults1_partner2', 'cookresults1_partner3',
                             'cookresults1_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm1.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm3.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf1.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf3.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookresults1_partner1', 'cookresults1_partner2', 'cookresults1_partner3',
                      'cookresults1_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking1Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults01_partner1', 'cookresults01_partner2', 'cookresults01_partner3',
                             'cookresults01_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm1.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm3.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf1.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf3.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookresults01_partner1', 'cookresults01_partner2', 'cookresults01_partner3',
                      'cookresults01_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3',
                             'sporthints1_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?'.format(partnerm1.participant.label),
                    partner2_label='{}?'.format(partnerm3.participant.label),
                    partner3_label='{}?'.format(partnerf1.participant.label),
                    partner4_label='{}?'.format(partnerf3.participant.label), formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3', 'sporthints1_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports1Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults1_partner1', 'sportresults1_partner2', 'sportresults1_partner3',
                             'sportresults1_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm1.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm3.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf1.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf3.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sportresults1_partner1', 'sportresults1_partner2', 'sportresults1_partner3',
                      'sportresults1_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports1Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults01_partner1', 'sportresults01_partner2', 'sportresults01_partner3',
                             'sportresults01_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm1.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm3.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf1.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf3.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sportresults01_partner1', 'sportresults01_partner2', 'sportresults01_partner3',
                      'sportresults01_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Payment2Transition(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def vars_for_template(player: Player):
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        return dict(round=round)

    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?'.format(partnerm2.participant.label),
                    partner2_label='{}?'.format(partnerm4.participant.label),
                    partner3_label='{}?'.format(partnerf2.participant.label),
                    partner4_label='{}?'.format(partnerf4.participant.label), formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults2_partner1', 'econresults2_partner2', 'econresults2_partner3',
                             'econresults2_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm2.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm4.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf2.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf4.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['econresults2_partner1', 'econresults2_partner2', 'econresults2_partner3',
                      'econresults2_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults02_partner1', 'econresults02_partner2', 'econresults02_partner3',
                             'econresults02_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm2.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm4.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf2.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf4.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['econresults02_partner1', 'econresults02_partner2', 'econresults02_partner3',
                      'econresults02_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?'.format(partnerm2.participant.label),
                    partner2_label='{}?'.format(partnerm4.participant.label),
                    partner3_label='{}?'.format(partnerf2.participant.label),
                    partner4_label='{}?'.format(partnerf4.participant.label), formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking2Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults2_partner1', 'cookresults2_partner2', 'cookresults2_partner3',
                             'cookresults2_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm2.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm4.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf2.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf4.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['cookresults2_partner1', 'cookresults2_partner2', 'cookresults2_partner3',
                      'cookresults2_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking2Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults02_partner1', 'cookresults02_partner2', 'cookresults02_partner3',
                             'cookresults02_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm2.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm4.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf2.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf4.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['cookresults02_partner1', 'cookresults02_partner2', 'cookresults02_partner3',
                      'cookresults02_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3',
                             'sporthints2_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?'.format(partnerm2.participant.label),
                    partner2_label='{}?'.format(partnerm4.participant.label),
                    partner3_label='{}?'.format(partnerf2.participant.label),
                    partner4_label='{}?'.format(partnerf4.participant.label), formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3', 'sporthints2_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports2Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults2_partner1', 'sportresults2_partner2', 'sportresults2_partner3',
                             'sportresults2_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm2.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm4.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf2.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf4.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['sportresults2_partner1', 'sportresults2_partner2', 'sportresults2_partner3',
                      'sportresults2_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports2Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults02_partner1', 'sportresults02_partner2', 'sportresults02_partner3',
                             'sportresults02_partner4']
        random.shuffle(formfields_random)
        round = 0
        if player.participant.task_rounds1['2'] == 1:
            round = 1
        else:
            round = 2
        g = player.group
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        return dict(round=round, partner1_label='{}?[Out of 4 questions]'.format(partnerm2.participant.label),
                    partner2_label='{}?[Out of 4 questions]'.format(partnerm4.participant.label),
                    partner3_label='{}?[Out of 4 questions]'.format(partnerf2.participant.label),
                    partner4_label='{}?[Out of 4 questions]'.format(partnerf4.participant.label),
                    formfields_random=formfields_random)

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['sportresults02_partner1', 'sportresults02_partner2', 'sportresults02_partner3',
                      'sportresults02_partner4']
        random.shuffle(formfields)
        return formfields

    set_hints_given(Player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class WaitPage2(Page):
    @staticmethod
    def live_method(player: Player, data):
        session = player.session
        session.arrived_ids.add(player.id_in_subsession)
        not_arrived_yet = session.active_players - session.arrived_ids
        if not_arrived_yet:
            return {0: dict(not_arrived_yet=list(not_arrived_yet))}
        return {0: dict(finished=True)}

    @staticmethod
    def error_message(player: Player, values):
        session = player.session
        if session.arrived_ids != session.active_players:
            return "Page somehow proceeded before all players are ready"


class Final(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 9

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.participant.round2_completed = 0
        player.participant.round3b_completed = 0
        int = list(range(0, 3))
        random.shuffle(int)
        for i in range(len(int)):
            if ('___Round2_' in upcoming_apps[int[i]]) and (player.participant.round2_completed == 0):
                player.participant.round2_completed = 3
                return upcoming_apps[int[i]]
            elif ('___Round3b_' in upcoming_apps[int[i]]) and (player.participant.round3b_completed == 0):
                player.participant.round3b_completed = 3
                return upcoming_apps[int[i]]


page_sequence = [WaitPage1, Demographics, Economics1Hints, Economics1Results,
                 Economics1Results0, Cooking1Hints, Cooking1Results, Cooking1Results0, Sports1Hints,
                 Sports1Results, Sports1Results0, Economics2Hints, Economics2Results, Economics2Results0,
                 Cooking2Hints, Cooking2Results, Cooking2Results0, Sports2Hints, Sports2Results,
                 Sports2Results0, WaitPage2, Final]
