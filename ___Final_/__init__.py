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
        blank=True
    )

class Player(BasePlayer):
    wtp = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']], initial = 0,
        label='Would you be willing to use part of your payment to do so?',
        widget=widgets.RadioSelect,
    )
    partner4 = models.BooleanField(blank=True)
    partner7 = models.BooleanField(blank=True)
    partner1 = models.BooleanField(blank=True)
    partner5 = models.BooleanField(blank=True)
    wtp_howmuch1 =  models.IntegerField(
        label='', initial=0,
        min=0, max=200,
    )
    wtp_howmuch2 =  models.IntegerField(
        label='', initial=0,
        min=0, max=200,
    )
    wtp_howmuch3 =  models.IntegerField(
        label='', initial=0,
        min=0, max=200,
    )
    wtp_howmuch4 =  models.IntegerField(
        label='', initial=0,
        min=0, max=200,
    )
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

def set_helped(player: Player):
    g = player.group
    my_previous_helped = []
    if player.participant.partnerm1 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerm1))
    if player.participant.partnerm2 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerm2))
    if player.participant.partnerm3 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerm3))
    if player.participant.partnerm4 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerm4))
    if player.participant.partnerf1 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerf1))
    if player.participant.partnerf2 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerf2))
    if player.participant.partnerf3 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerf3))
    if player.participant.partnerf4 != 0:
        my_previous_helped.append(g.get_player_by_id(player.participant.partnerf4))
    for partner in my_previous_helped:
        if partner.participant.exclude == True:
            if player.id_in_group in partner.participant.partner_exclude:
                my_previous_helped.remove(partner)
    return my_previous_helped

def set_hints_given(player:Player,partner):
    partner.participant.hints_given_econ = 0
    partner.participant.hints_given_cook = 0
    partner.participant.hints_given_sport = 0
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
    partner.participant.econ_hint_used = 0
    partner.participant.cook_hint_used = 0
    partner.participant.sport_hint_used = 0
    if partner.id_in_group == player.participant.partner1:
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner1
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner1
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner1
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner2:
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner2
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner2
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner2
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner3:
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner3
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner3
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner3
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner4:
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner4
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner4
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner4
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner5:
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner5
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner5
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner5
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner6:
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner6
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner6
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner6
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner7:
        partner.participant.econ_hint_used = partner.participant.econ_hint_requests_partner7
        partner.participant.cook_hint_used = partner.participant.cook_hint_requests_partner7
        partner.participant.sport_hint_used = partner.participant.sport_hint_requests_partner7
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]
    elif partner.id_in_group == player.participant.partner8:
        partner.participant.econ_hint_used = partner.participant.econ_hint_used_partner8
        partner.participant.cook_hint_used = partner.participant.cook_hint_used_partner8
        partner.participant.sport_hint_used = partner.participant.sport_hint_used_partner8
        return [partner.participant.econ_hint_used,partner.participant.cook_hint_used,partner.participant.sport_hint_used]



# PAGES
class WTP_YesNo(Page):
    form_model = 'player'
    form_fields = ['wtp']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        arr = [player.participant.partner4, player.participant.partner7, player.participant.partner1, player.participant.partner5]
        string_arr = ['partner4', 'partner7', 'partner1', 'partner5']
        final = {}
        input = []
        for i, j in zip(arr, string_arr):
            if i != 0:
                input.append(g.get_player_by_id(i).participant.label)
        final = dict(input=input)
        return final

class WTP_Who(Page):
    form_model = 'player'
    form_fields = ['partner4','partner7','partner1','partner5']
    @staticmethod
    def is_displayed(player: Player):
        return player.wtp == 1 and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        arr = [player.participant.partner4, player.participant.partner7, player.participant.partner1,
               player.participant.partner5]
        string_arr = ['partner4', 'partner7', 'partner1', 'partner5']
        labels = []
        for i, j in zip(arr, string_arr):
            if i != 0:
                labels.append(dict(name=j, label=g.get_player_by_id(i).participant.label))
        return dict(labels=labels)

class WTP_HowMuch(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.wtp == 1 and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        labels = []
        master = {}
        g = player.group
        if player.field_maybe_none('partner4') != None:
            partner4 = g.get_player_by_id(player.participant.partner4)
            master.update(dict(partner4=partner4))
            labels.append(dict(name='wtp_howmuch1', label=partner4.participant.label))
        if player.field_maybe_none('partner7') != None:
            partner7 = g.get_player_by_id(player.participant.partner7)
            master.update(dict(partner7=partner7))
            labels.append(dict(name='wtp_howmuch2', label=partner7.participant.label))
        if player.field_maybe_none('partner1') != None:
            partner1 = g.get_player_by_id(player.participant.partner1)
            master.update(dict(partner1=partner1))
            labels.append(dict(name='wtp_howmuch3', label=partner1.participant.label))
        if player.field_maybe_none('partner5') != None:
            partner5 = g.get_player_by_id(player.participant.partner5)
            master.update(dict(partner5=partner5))
            labels.append(dict(name='wtp_howmuch4', label=partner5.participant.label))
        master.update(dict(labels=labels))
        return master
    @staticmethod
    def get_form_fields(player: Player):
        formfields = []
        if player.field_maybe_none('partner4') != None:
            formfields.append('wtp_howmuch1')
        if player.field_maybe_none('partner7') != None:
            formfields.append('wtp_howmuch2')
        if player.field_maybe_none('partner1') != None:
            formfields.append('wtp_howmuch3')
        if player.field_maybe_none('partner5') != None:
            formfields.append('wtp_howmuch4')
        return formfields
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        num = list(range(1,201))
        random.shuffle(num)
        random1 = num.copy()
        player.participant.random1 = random1[0]
        player.participant.random2 = random1[1]
        player.participant.random3 = random1[2]
        player.participant.random4 = random1[3]

class WTP_Results1_1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner4') != None) and (player.participant.random1 < player.wtp_howmuch1) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner4 = g.get_player_by_id(player.participant.partner4)
        return dict(partner4=partner4.participant.label)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.exclude = True
        player.participant.partner_exclude.append(player.participant.partner4)

class WTP_Results2_1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner4') != None) and (player.participant.random1 >= player.wtp_howmuch1) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner4 = g.get_player_by_id(player.participant.partner4)
        return dict(partner4=partner4.participant.label)

class WTP_Results1_2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner7') != None) and (player.participant.random2 < player.wtp_howmuch2) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner7 = g.get_player_by_id(player.participant.partner7)
        return dict(partner7=partner7.participant.label)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.exclude = True
        player.participant.partner_exclude.append(player.participant.partner7)

class WTP_Results2_2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner7') != None) and (player.participant.random2 >= player.wtp_howmuch2) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner7 = g.get_player_by_id(player.participant.partner7)
        return dict(partner7=partner7.participant.label)

class WTP_Results1_3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner1') != None) and (player.participant.random3 < player.wtp_howmuch3) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner1 = g.get_player_by_id(player.participant.partner1)
        return dict(partner1=partner1.participant.label)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.exclude = True
        player.participant.partner_exclude.append(player.participant.partner1)

class WTP_Results2_3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner1') != None) and (player.participant.random3 >= player.wtp_howmuch3) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner1 = g.get_player_by_id(player.participant.partner1)
        return dict(partner1=partner1.participant.label)

class WTP_Results1_4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner5') != None) and (player.participant.random4 < player.wtp_howmuch4) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner5 = g.get_player_by_id(player.participant.partner5)
        return dict(partner5=partner5.participant.label)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.exclude = True
        player.participant.partner_exclude.append(player.participant.partner5)

class WTP_Results2_4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.field_maybe_none('partner5') != None) and (player.participant.random4 >= player.wtp_howmuch4) and player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner5 = g.get_player_by_id(player.participant.partner5)
        return dict(partner5=partner5.participant.label)

class WaitPage(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = ""

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
        return dict(my_previous_partners=my_previous_helped,hints_given=hints_given,hints_used=hints_used)

def vars_for_template1(player: Player, formfields):
    final = {}
    formfields_random = formfields.copy()
    g = player.group
    count = 0
    hints = 0
    partnerm1 = 0
    partnerm3 = 0
    partnerf1 = 0
    partnerf3 = 0
    if player.participant.partnerm1 != 0:
        partnerm1 = g.get_player_by_id(player.participant.partnerm1)
        final.update(dict(partner1_label='{}?'.format(partnerm1.participant.label)))
        count+=1
    if player.participant.partnerm3 != 0:
        partnerm3 = g.get_player_by_id(player.participant.partnerm3)
        final.update(dict(partner2_label='{}?'.format(partnerm3.participant.label)))
        count+=1
    if player.participant.partnerf1 != 0:
        partnerf1 = g.get_player_by_id(player.participant.partnerf1)
        final.update(dict(partner3_label='{}?'.format(partnerf1.participant.label)))
        count+=1
    if player.participant.partnerf3 != 0:
        partnerf3 = g.get_player_by_id(player.participant.partnerf3)
        final.update(dict(partner4_label='{}?'.format(partnerf3.participant.label)))
        count+=1
    if count == 1:
        hints = 2
    elif count == 2:
        hints = 5
    elif count == 3:
        hints = 7
    elif count == 4:
        hints = 10
    final.update(dict(hints=hints, partnerm1=partnerm1, partnerm3=partnerm3, partnerf1=partnerf1, partnerf3=partnerf3))
    random.shuffle(formfields_random)
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

def vars_for_template2(player: Player, formfields):
    final = {}
    formfields_random = formfields.copy()
    g = player.group
    count = 0
    hints = 0
    partnerm2 = 0
    partnerm4 = 0
    partnerf2 = 0
    partnerf4 = 0
    if player.participant.partnerm2 != 0:
        partnerm2 = g.get_player_by_id(player.participant.partnerm2)
        final.update(dict(partner1_label='{}?'.format(partnerm2.participant.label)))
        count+=1
    if player.participant.partnerm4 != 0:
        partnerm4 = g.get_player_by_id(player.participant.partnerm4)
        final.update(dict(partner2_label='{}?'.format(partnerm4.participant.label)))
        count+=1
    if player.participant.partnerf2 != 0:
        partnerf2 = g.get_player_by_id(player.participant.partnerf2)
        final.update(dict(partner3_label='{}?'.format(partnerf2.participant.label)))
        count+=1
    if player.participant.partnerf4 != 0:
        partnerf4 = g.get_player_by_id(player.participant.partnerf4)
        final.update(dict(partner4_label='{}?'.format(partnerf4.participant.label)))
        count+=1
    if count == 1:
        hints = 2
    elif count == 2:
        hints = 5
    elif count == 3:
        hints = 7
    elif count == 4:
        hints = 10
    final.update(dict(hints=hints, partnerm2=partnerm2, partnerm4=partnerm4, partnerf2=partnerf2, partnerf4=partnerf4))
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
        return (player.round_number == participant.task_rounds1['Econ1'])

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
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
        return (player.round_number == participant.task_rounds1['Cook1'])

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
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
        return (player.round_number == participant.task_rounds1['Sport1'])

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3', 'sporthints1_partner4']
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3', 'sporthints1_partner4']
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
        return (player.round_number == participant.task_rounds1['Econ2'])

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
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
        return (player.round_number == participant.task_rounds1['Cook2'])

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        random.shuffle(formfields)
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
        return (player.round_number == participant.task_rounds1['Sport2'])

    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3', 'sporthints2_partner4']
        random.shuffle(formfields)
        return formfields

    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3', 'sporthints2_partner4']
        hints = vars_for_template1(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"


page_sequence = [WTP_YesNo, WTP_Who, WTP_HowMuch, WTP_Results1_1, WTP_Results2_1,
WTP_Results1_2, WTP_Results2_2, WTP_Results1_3, WTP_Results2_3, WTP_Results1_4,
WTP_Results2_4, WaitPage, FinalTable, Economics1Hints, Economics2Hints, Cooking1Hints, Cooking2Hints,
Sports1Hints, Sports2Hints]
