from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Final_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    wtp = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='Would you be willing to use part of your payment to do so?',
        widget=widgets.RadioSelect,
    )
    wtp_who = models.StringField(
        label='Please choose the helper that you don\'t want to find out about your hints.',
        widget=widgets.RadioSelect,
    )
    wtp_howmuch =  models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10']],
        label='I would like to pay ____ $ NOT to communicate the hints I took to helper Y.',
        widget=widgets.RadioSelectHorizontal,
    )

def wtp_who_choices(player):
    g = player.group
    partner4 = g.get_player_by_id(player.participant.partner4)
    partner7 = g.get_player_by_id(player.participant.partner7)
    partner1 = g.get_player_by_id(player.participant.partner1)
    partner5 = g.get_player_by_id(player.participant.partner5)
    choices = [partner4.participant.label,partner7.participant.label,partner1.participant.label,partner5.participant.label]
    return choices

def set_helped(player: Player):
    g = player.group
    my_previous_helped = [g.get_player_by_id(player.participant.partnerm1),
    g.get_player_by_id(player.participant.partnerm2),
    g.get_player_by_id(player.participant.partnerm3),
    g.get_player_by_id(player.participant.partnerm4),
    g.get_player_by_id(player.participant.partnerf1),
    g.get_player_by_id(player.participant.partnerf2),
    g.get_player_by_id(player.participant.partnerf3),
    g.get_player_by_id(player.participant.partnerf4)]
    for partner in my_previous_helped:
        if partner.participant.exclude == True:
            if partner.participant.partner_exclude == player.id_in_group:
                thislist.remove(partner)
        else:
            continue

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
    def vars_for_template(player: Player):
        g = player.group
        ##only grab if they have partner, otherwise just skip it
        partner4 = g.get_player_by_id(player.participant.partner4)
        partner7 = g.get_player_by_id(player.participant.partner7)
        partner1 = g.get_player_by_id(player.participant.partner1)
        partner5 = g.get_player_by_id(player.participant.partner5)
        return dict(partner4=partner4.participant.label, partner7=partner7.participant.label, partner1=partner1.participant.label, partner5=partner5.participant.label)

class WTP_Who(Page):
    form_model = 'player'
    form_fields = ['wtp_who']
    @staticmethod
    def is_displayed(player: Player):
        return player.wtp == 1

class WTP_HowMuch(Page):
    form_model = 'player'
    form_fields = ['wtp_howmuch']
    @staticmethod
    def is_displayed(player: Player):
        return player.wtp == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        num = list(range(1,11))
        random.shuffle(num)
        random1 = num.copy()
        player.participant.random = random1[0]

#
class WTP_Results1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.participant.random < player.wtp_howmuch)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.exclude = True
        if player.wtp_who == 0:
            player.participant.partner_exclude = player.participant.partner4
        elif player.wtp_who == 1:
            player.participant.partner_exclude = player.participant.partner7
        elif player.wtp_who == 2:
            player.participant.partner_exclude = player.participant.partner1
        elif player.wtp_who == 3:
            player.participant.partner_exclude = player.participant.partner5


##make sure this works for no partner as well
class WTP_Results2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.wtp == 1) and (player.participant.random >= player.wtp_howmuch)

class FinalTable(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        my_previous_helped = set_helped(player)
        hints_given = [set_hints_given(player,partner) for partner in my_previous_helped]
        hints_used = [set_hints_used(player,partner) for partner in my_previous_helped]
        return dict(my_previous_partners=my_previous_helped,hints_given=hints_given,hints_used=hints_used)

page_sequence = [WTP_YesNo, WTP_Who, WTP_HowMuch, WTP_Results1, WTP_Results2, FinalTable]
