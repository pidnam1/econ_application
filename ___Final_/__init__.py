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
    pass

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

class FinalTable(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        my_previous_helped = [g.get_player_by_id(player.participant.partnerm1),
        g.get_player_by_id(player.participant.partnerm2),
        g.get_player_by_id(player.participant.partnerm3),
        g.get_player_by_id(player.participant.partnerm4),
        g.get_player_by_id(player.participant.partnerf1),
        g.get_player_by_id(player.participant.partnerf2),
        g.get_player_by_id(player.participant.partnerf3),
        g.get_player_by_id(player.participant.partnerf4)]
        hints_given = [set_hints_given(player,partner) for partner in my_previous_helped]
        hints_used = [set_hints_used(player,partner) for partner in my_previous_helped]
        return dict(my_previous_partners=my_previous_helped,hints_given=hints_given,hints_used=hints_used)

page_sequence = [FinalTable]
