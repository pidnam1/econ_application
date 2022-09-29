from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Final_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    TASKS = ['1', '2']
    SUB1TASKS = ['Econ1', 'Cook1', 'Sport1']
    SUB2TASKS = ['Econ2', 'Cook2', 'Sport2']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def make_field_one():
    return models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
    )

class Player(BasePlayer):
    gender = models.IntegerField()
    id_partnerf1 = models.IntegerField()
    id_partnerf2 = models.IntegerField()
    id_partnerf3 = models.IntegerField()
    id_partnerf4 = models.IntegerField()
    id_partnerm1 = models.IntegerField()
    id_partnerm2 = models.IntegerField()
    id_partnerm3 = models.IntegerField()
    id_partnerm4 = models.IntegerField()
    name_partnerf1 = models.StringField()
    name_partnerf2 = models.StringField()
    name_partnerf3 = models.StringField()
    name_partnerf4 = models.StringField()
    name_partnerm1 = models.StringField()
    name_partnerm2 = models.StringField()
    name_partnerm3 = models.StringField()
    name_partnerm4 = models.StringField()
    hintsecon_partnerf1 = models.IntegerField()
    hintsecon_partnerf2 = models.IntegerField()
    hintsecon_partnerf3 = models.IntegerField()
    hintsecon_partnerf4 = models.IntegerField()
    hintsecon_partnerm1 = models.IntegerField()
    hintsecon_partnerm2 = models.IntegerField()
    hintsecon_partnerm3 = models.IntegerField()
    hintsecon_partnerm4 = models.IntegerField()
    hintscook_partnerf1 = models.IntegerField()
    hintscook_partnerf2 = models.IntegerField()
    hintscook_partnerf3 = models.IntegerField()
    hintscook_partnerf4 = models.IntegerField()
    hintscook_partnerm1 = models.IntegerField()
    hintscook_partnerm2 = models.IntegerField()
    hintscook_partnerm3 = models.IntegerField()
    hintscook_partnerm4 = models.IntegerField()
    hintssport_partnerf1 = models.IntegerField()
    hintssport_partnerf2 = models.IntegerField()
    hintssport_partnerf3 = models.IntegerField()
    hintssport_partnerf4 = models.IntegerField()
    hintssport_partnerm1 = models.IntegerField()
    hintssport_partnerm2 = models.IntegerField()
    hintssport_partnerm3 = models.IntegerField()
    hintssport_partnerm4 = models.IntegerField()
    econhints1_partner1 = make_field_one()
    econhints1_partner2 = make_field_one()
    econhints1_partner3 = make_field_one()
    econhints1_partner4 = make_field_one()
    econhints2_partner1 = make_field_one()
    econhints2_partner2 = make_field_one()
    econhints2_partner3 = make_field_one()
    econhints2_partner4 = make_field_one()
    cookhints1_partner1 = make_field_one()
    cookhints1_partner2 = make_field_one()
    cookhints1_partner3 = make_field_one()
    cookhints1_partner4 = make_field_one()
    cookhints2_partner1 = make_field_one()
    cookhints2_partner2 = make_field_one()
    cookhints2_partner3 = make_field_one()
    cookhints2_partner4 = make_field_one()
    sporthints1_partner1 = make_field_one()
    sporthints1_partner2 = make_field_one()
    sporthints1_partner3 = make_field_one()
    sporthints1_partner4 = make_field_one()
    sporthints2_partner1 = make_field_one()
    sporthints2_partner2 = make_field_one()
    sporthints2_partner3 = make_field_one()
    sporthints2_partner4 = make_field_one()

# FUNCTIONS
def creating_session(subsession: Subsession):
    session = subsession.session

    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.exclude = False
            p.participant.partner_exclude = []
            round_numbers = list(range(1, 3))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))
            sub_round_number1 = list(range(2, 5))
            random.shuffle(sub_round_number1)
            sub_round_number2 = list(range(6, 9))
            random.shuffle(sub_round_number2)
            round_number_1 = task_round['1']
            p.participant.task_roundsf = dict()
            if round_number_1 == 1:
                p.participant.task_roundsf.update({'1': 1})
                task_rounds_1_1 = dict(zip(C.SUB1TASKS, sub_round_number1))
                p.participant.task_roundsf.update(task_rounds_1_1)
            elif round_number_1 == 2:
                p.participant.task_roundsf.update({'1': 5})
                task_rounds_1_2 = dict(zip(C.SUB1TASKS, sub_round_number2))
                p.participant.task_roundsf.update(task_rounds_1_2)

            round_number_2 = task_round['2']
            if round_number_2 == 1:
                p.participant.task_roundsf.update({'2': 1})
                task_rounds_2_1 = dict(zip(C.SUB2TASKS, sub_round_number1))
                p.participant.task_roundsf.update(task_rounds_2_1)
            elif round_number_2 == 2:
                p.participant.task_roundsf.update({'2': 5})
                task_rounds_2_2 = dict(zip(C.SUB2TASKS, sub_round_number2))
                p.participant.task_roundsf.update(task_rounds_2_2)

def set_helped(player: Player):
    g = player.group
    my_previous_helped = []
    if player.participant.partnerm1 != 0:
        player.id_partnerm1 = player.participant.partnerm1
        partnerm1 = g.get_player_by_id(player.id_partnerm1)
        player.name_partnerm1 = partnerm1.participant.label
        my_previous_helped.append(partnerm1)
    if player.participant.partnerm2 != 0:
        player.id_partnerm2 = player.participant.partnerm2
        partnerm2 = g.get_player_by_id(player.id_partnerm2)
        player.name_partnerm2 = partnerm2.participant.label
        my_previous_helped.append(partnerm2)
    if player.participant.partnerm3 != 0:
        player.id_partnerm3 = player.participant.partnerm3
        partnerm3 = g.get_player_by_id(player.id_partnerm3)
        player.name_partnerm3 = partnerm3.participant.label
        my_previous_helped.append(partnerm3)
    if player.participant.partnerm4 != 0:
        player.id_partnerm4 = player.participant.partnerm4
        partnerm4 = g.get_player_by_id(player.id_partnerm4)
        player.name_partnerm4 = partnerm4.participant.label
        my_previous_helped.append(partnerm4)
    if player.participant.partnerf1 != 0:
        player.id_partnerf1 = player.participant.partnerf1
        partnerf1 = g.get_player_by_id(player.id_partnerf1)
        player.name_partnerf1 = partnerf1.participant.label
        my_previous_helped.append(partnerf1)
    if player.participant.partnerf2 != 0:
        player.id_partnerf2 = player.participant.partnerf2
        partnerf2 = g.get_player_by_id(player.id_partnerf2)
        player.name_partnerf2 = partnerf2.participant.label
        my_previous_helped.append(partnerf2)
    if player.participant.partnerf3 != 0:
        player.id_partnerf3 = player.participant.partnerf3
        partnerf3 = g.get_player_by_id(player.id_partnerf3)
        player.name_partnerf3 = partnerf3.participant.label
        my_previous_helped.append(partnerf3)
    if player.participant.partnerf4 != 0:
        player.id_partnerf4 = player.participant.partnerf4
        partnerf4 = g.get_player_by_id(player.id_partnerf4)
        player.name_partnerf4 = partnerf4.participant.label
        my_previous_helped.append(partnerf4)
    for partner in my_previous_helped:
        if partner.participant.exclude == True:
            if player.id_in_group in partner.participant.partner_exclude:
                my_previous_helped.remove(partner)
    return my_previous_helped

def set_hints_given(player:Player,partner):
    if partner.id_in_group == player.participant.partnerm1:
        partner.participant.hints_given_econ = player.participant.MP1hints_given_econ
        partner.participant.hints_given_cook = player.participant.MP1hints_given_cook
        partner.participant.hints_given_sport = player.participant.MP1hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerm2:
        partner.participant.hints_given_econ = player.participant.MP2hints_given_econ
        partner.participant.hints_given_cook = player.participant.MP2hints_given_cook
        partner.participant.hints_given_sport = player.participant.MP2hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerm3:
        partner.participant.hints_given_econ = player.participant.MR1hints_given_econ
        partner.participant.hints_given_cook = player.participant.MR1hints_given_cook
        partner.participant.hints_given_sport = player.participant.MR1hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerm4:
        partner.participant.hints_given_econ = player.participant.MR2hints_given_econ
        partner.participant.hints_given_cook = player.participant.MR2hints_given_cook
        partner.participant.hints_given_sport = player.participant.MR2hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerf1:
        partner.participant.hints_given_econ = player.participant.WP1hints_given_econ
        partner.participant.hints_given_cook = player.participant.WP1hints_given_cook
        partner.participant.hints_given_sport = player.participant.WP1hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerf2:
        partner.participant.hints_given_econ = player.participant.WP2hints_given_econ
        partner.participant.hints_given_cook = player.participant.WP2hints_given_cook
        partner.participant.hints_given_sport = player.participant.WP2hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerf3:
        partner.participant.hints_given_econ = player.participant.WR1hints_given_econ
        partner.participant.hints_given_cook = player.participant.WR1hints_given_cook
        partner.participant.hints_given_sport = player.participant.WR1hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]
    elif partner.id_in_group == player.participant.partnerf4:
        partner.participant.hints_given_econ = player.participant.WR2hints_given_econ
        partner.participant.hints_given_cook = player.participant.WR2hints_given_cook
        partner.participant.hints_given_sport = player.participant.WR2hints_given_sport
        return [partner.participant.hints_given_econ,partner.participant.hints_given_cook,partner.participant.hints_given_sport]

def set_hints_used(player:Player,partner):
    if player.id_in_group == partner.participant.partner1:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner1
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner1
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner1
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner1
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner1
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner1
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner1
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner2:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner2
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner2
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner2
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner2
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner2
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner2
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner2
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner3:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner3
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner3
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner3
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner3
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner3
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner3
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner3
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner4:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner4
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner4
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner4
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner4
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner4
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner4
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner4
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner5:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner5
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner5
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner5
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner5
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner5
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner5
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner5
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner6:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner6
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner6
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner6
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner6
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner6
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner6
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner6
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner7:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner7
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner7
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner7
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner7
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner7
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner7
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner7
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif player.id_in_group == partner.participant.partner8:
        if partner.id_in_group == player.participant.partnerm1:
            player.hintsecon_partnerm1 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerm1 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerm1 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerm2:
            player.hintsecon_partnerm2 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerm2 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerm2 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerm3:
            player.hintsecon_partnerm3 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerm3 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerm3 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerm4:
            player.hintsecon_partnerm4 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerm4 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerm4 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerf1:
            player.hintsecon_partnerf1 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerf1 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerf1 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerf2:
            player.hintsecon_partnerf2 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerf2 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerf2 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerf3:
            player.hintsecon_partnerf3 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerf3 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerf3 = partner.participant.sport_hint_requests_partner8
        elif partner.id_in_group == player.participant.partnerf4:
            player.hintsecon_partnerf4 = partner.participant.econ_hint_requests_partner8
            player.hintscook_partnerf4 = partner.participant.cook_hint_requests_partner8
            player.hintssport_partnerf4 = partner.participant.sport_hint_requests_partner8
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner8
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner8
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner8
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]

def set_mismatch(player:Player,partner):
    mismatch_econ = 0
    mismatch_cook = 0
    mismatch_sport = 0
    if (partner.participant.hints_given_econ is not None) and (partner.participant.econ_hint_used is not None):
        mismatch_econ = int(partner.participant.hints_given_econ) - int(partner.participant.econ_hint_used)
    if (partner.participant.hints_given_cook is not None) and (partner.participant.cook_hint_used is not None):
        mismatch_cook = int(partner.participant.hints_given_cook) - int(partner.participant.cook_hint_used)
    if (partner.participant.hints_given_sport is not None) and (partner.participant.sport_hint_used is not None):
        mismatch_sport = int(partner.participant.hints_given_sport) - int(partner.participant.sport_hint_used)

    if mismatch_econ > 0:
        partner.participant.mismatch_econ = "+" + str(mismatch_econ)
    elif mismatch_econ <= 0:
        partner.participant.mismatch_econ = mismatch_econ
    else:
        partner.participant.mismatch_econ = "None"

    if mismatch_cook > 0:
        partner.participant.mismatch_cook = "+" + str(mismatch_cook)
    elif mismatch_cook <= 0:
        partner.participant.mismatch_cook = mismatch_cook
    else:
        partner.participant.mismatch_cook = "None"

    if mismatch_sport > 0:
        partner.participant.mismatch_sport = "+" + str(mismatch_sport)
    elif mismatch_sport <= 0:
        partner.participant.mismatch_sport = mismatch_sport
    else:
        partner.participant.mismatch_sport = "None"

    return [partner.participant.mismatch_econ,partner.participant.mismatch_cook,partner.participant.mismatch_sport]


# PAGES
class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = "Please be patient with your fellow classmates. WHILE YOU WAIT, YOU CAN PLAY THE GAME ON THE PAPER THAT IS ON YOUR DESK. PLEASE DO NOT TALK TO ANYONE."

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1

class FinalTable(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        my_previous_helped = set_helped(player)
        hints_given = [set_hints_given(player,partner) for partner in my_previous_helped]
        hints_used = [set_hints_used(player,partner) for partner in my_previous_helped]
        mismatch = [set_mismatch(player,partner) for partner in my_previous_helped]
        return dict(my_previous_partners=my_previous_helped,hints_given=hints_given,hints_used=hints_used,mismatch=mismatch)

def vars_for_template1(player: Player, formfields):
    final = {}
    formfields_random = []
    g = player.group
    display = True
    count = 0
    hints = 0
    partnerm1 = 0
    partnerm3 = 0
    partnerf1 = 0
    partnerf3 = 0
    if player.participant.partnerm1 != 0:
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        final.update(dict(partner1_label='{}?'.format(partnerm1.participant.label)))
        formfields_random.append(formfields[0])
        count+=1
    if player.participant.partnerm3 != 0:
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        final.update(dict(partner2_label='{}?'.format(partnerm3.participant.label)))
        formfields_random.append(formfields[1])
        count+=1
    if player.participant.partnerf1 != 0:
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        final.update(dict(partner3_label='{}?'.format(partnerf1.participant.label)))
        formfields_random.append(formfields[2])
        count+=1
    if player.participant.partnerf3 != 0:
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        final.update(dict(partner4_label='{}?'.format(partnerf3.participant.label)))
        formfields_random.append(formfields[3])
        count+=1
    if count == 1:
        hints = 2
    elif count == 2:
        hints = 5
    elif count == 3:
        hints = 7
    elif count == 4:
        hints = 10
    elif count == 0:
        hints = 0
        display = False
    final.update(dict(hints=hints, display=display, partnerm1=partnerm1, partnerm3=partnerm3, partnerf1=partnerf1, partnerf3=partnerf3))
    random.shuffle(formfields_random)
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

def vars_for_template2(player: Player, formfields):
    final = {}
    formfields_random = []
    g = player.group
    display = True
    count = 0
    hints = 0
    partnerm2 = 0
    partnerm4 = 0
    partnerf2 = 0
    partnerf4 = 0
    if player.participant.partnerm2 != 0:
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        final.update(dict(partner1_label='{}?'.format(partnerm2.participant.label)))
        formfields_random.append(formfields[0])
        count+=1
    if player.participant.partnerm4 != 0:
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        final.update(dict(partner2_label='{}?'.format(partnerm4.participant.label)))
        formfields_random.append(formfields[1])
        count+=1
    if player.participant.partnerf2 != 0:
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        final.update(dict(partner3_label='{}?'.format(partnerf2.participant.label)))
        formfields_random.append(formfields[2])
        count+=1
    if player.participant.partnerf4 != 0:
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        final.update(dict(partner4_label='{}?'.format(partnerf4.participant.label)))
        formfields_random.append(formfields[3])
        count+=1
    if count == 1:
        hints = 2
    elif count == 2:
        hints = 5
    elif count == 3:
        hints = 7
    elif count == 4:
        hints = 10
    elif count == 0:
        hints = 0
        display = False
    final.update(dict(hints=hints, display=display, partnerm2=partnerm2, partnerm4=partnerm4, partnerf2=partnerf2, partnerf4=partnerf4))
    random.shuffle(formfields_random)
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

class Economics1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        hints = vars_for_template1(player, formfields_random)[1]
        final["hints"] = hints
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        formfields_random = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        return (player.round_number == participant.task_roundsf['Econ1']) and (final["display"])

    @staticmethod
    def get_form_fields(player: Player):
        formfields_random = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        formfields = final["formfields_random"]
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        hints = vars_for_template1(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class Cooking1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        hints = vars_for_template1(player, formfields_random)[1]
        final["hints"] = hints
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        formfields_random = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        return (player.round_number == participant.task_roundsf['Cook1']) and (final["display"])

    @staticmethod
    def get_form_fields(player: Player):
        formfields_random = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        formfields = final["formfields_random"]
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        hints = vars_for_template1(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class Sports1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3',
                             'sporthints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        hints = vars_for_template1(player, formfields_random)[1]
        final["hints"] = hints
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        formfields_random = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3',
                             'sporthints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        return (player.round_number == participant.task_roundsf['Sport1']) and (final["display"])

    @staticmethod
    def get_form_fields(player: Player):
        formfields_random = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3', 'sporthints1_partner4']
        final = vars_for_template1(player, formfields_random)[0]
        formfields = final["formfields_random"]
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3',
                             'sporthints1_partner4']
        hints = vars_for_template1(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class Economics2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        hints = vars_for_template2(player, formfields_random)[1]
        final["hints"] = hints
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        formfields_random = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        return (player.round_number == participant.task_roundsf['Econ2']) and (final["display"])

    @staticmethod
    def get_form_fields(player: Player):
        formfields_random = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        formfields = final["formfields_random"]
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        hints = vars_for_template2(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class Cooking2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        hints = vars_for_template2(player, formfields_random)[1]
        final["hints"] = hints
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        formfields_random = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        return (player.round_number == participant.task_roundsf['Cook2']) and (final["display"])

    @staticmethod
    def get_form_fields(player: Player):
        formfields_random = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        formfields = final["formfields_random"]
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        hints = vars_for_template2(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class Sports2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3',
                             'sporthints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        hints = vars_for_template2(player, formfields_random)[1]
        final["hints"] = hints
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        formfields_random = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3',
                             'sporthints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        return (player.round_number == participant.task_roundsf['Sport2']) and (final["display"])

    @staticmethod
    def get_form_fields(player: Player):
        formfields_random = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3', 'sporthints2_partner4']
        final = vars_for_template2(player, formfields_random)[0]
        formfields = final["formfields_random"]
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3',
                             'sporthints2_partner4']
        hints = vars_for_template2(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"


page_sequence = [WaitPage1, FinalTable, Economics1Hints, Economics2Hints, Cooking1Hints,
Cooking2Hints, Sports1Hints, Sports2Hints]
