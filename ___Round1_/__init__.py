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


def make_field_one():
    return models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

def make_field_two():
    return models.StringField(
        choices=[[0, '0'], [1, '1'],
                 [2, '2'], [3, '3'], [4, '4']],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
class Player(BasePlayer):
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
    econresults1_partner1 = make_field_two()
    econresults1_partner2 = make_field_two()
    econresults1_partner3 = make_field_two()
    econresults1_partner4 = make_field_two()
    econresults2_partner1 = make_field_two()
    econresults2_partner2 = make_field_two()
    econresults2_partner3 = make_field_two()
    econresults2_partner4 = make_field_two()
    cookresults1_partner1 = make_field_two()
    cookresults1_partner2 = make_field_two()
    cookresults1_partner3 = make_field_two()
    cookresults1_partner4 = make_field_two()
    cookresults2_partner1 = make_field_two()
    cookresults2_partner2 = make_field_two()
    cookresults2_partner3 = make_field_two()
    cookresults2_partner4 = make_field_two()
    sportresults1_partner1 = make_field_two()
    sportresults1_partner2 = make_field_two()
    sportresults1_partner3 = make_field_two()
    sportresults1_partner4 = make_field_two()
    sportresults2_partner1 = make_field_two()
    sportresults2_partner2 = make_field_two()
    sportresults2_partner3 = make_field_two()
    sportresults2_partner4 = make_field_two()
    econresults01_partner1 = make_field_two()
    econresults01_partner2 = make_field_two()
    econresults01_partner3 = make_field_two()
    econresults01_partner4 = make_field_two()
    econresults02_partner1 = make_field_two()
    econresults02_partner2 = make_field_two()
    econresults02_partner3 = make_field_two()
    econresults02_partner4 = make_field_two()
    cookresults01_partner1 = make_field_two()
    cookresults01_partner2 = make_field_two()
    cookresults01_partner3 = make_field_two()
    cookresults01_partner4 = make_field_two()
    cookresults02_partner1 = make_field_two()
    cookresults02_partner2 = make_field_two()
    cookresults02_partner3 = make_field_two()
    cookresults02_partner4 = make_field_two()
    sportresults01_partner1 = make_field_two()
    sportresults01_partner2 = make_field_two()
    sportresults01_partner3 = make_field_two()
    sportresults01_partner4 = make_field_two()
    sportresults02_partner1 = make_field_two()
    sportresults02_partner2 = make_field_two()
    sportresults02_partner3 = make_field_two()
    sportresults02_partner4 = make_field_two()



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
        p.participant.helpers_dict = dict(pf = [], pm = [], rf = [], rm = [])
        ##p.participant.pref_helpers =[]
        ##p.participant.pref_female_helpers = []
        ##p.participant.pref_male_helpers = []

        p.participant.tts = []
        p.participant.female_tts = []
        p.participant.male_tts = []
        p.participant.assigned_helpers = []

        p.participant.count_participant = 0
##### Functions for helper implementation, related to participants

def is_helping(player: Player, id):
    for i in player.participant.helpers_dict.values():
        if id in i:
            return True
    return False

def can_help_male(player:Player):
    return len(player.participant.male_tts) < 4

def can_help_female(player:Player):
    return len(player.participant.female_tts) < 4

def can_help_player_preferred(player:Player, gender):
    if gender == 0:
        return len(player.participant.female_tts) < 2
    else:
        return len(player.participant.male_tts) < 2
def can_help_player_random(player:Player, gender):
    if gender == 0:
        return len(player.participant.female_tts) < 4
    else:
        return len(player.participant.male_tts) < 4

def add_test_taker(helper:Player, test_taker:Player):
    if test_taker.participant.gender == 0:
        helper.participant.female_tts.append(test_taker.id_in_group)
    else:
        helper.participant.male_tts.append(test_taker.id_in_group)

def assign_helper(player:Player, helper:Player, round):
    if helper.participant.gender == 0 and round == "preferred":
        player.participant.helpers_dict["pf"].append(helper.id_in_group)
    elif helper.participant.gender == 0 and round == "random":
        player.participant.helpers_dict["rf"].append(helper.id_in_group)
    elif helper.participant.gender == 1 and round == "preferred":
        player.participant.helpers_dict["pm"].append(helper.id_in_group)
    else:
        player.participant.helpers_dict["rm"].append(helper.id_in_group)

def set_helpers_new(subsession: Subsession):
    session = subsession.session
    g = subsession.get_groups()[0]

    #randomizing list
    random_players = session.active_players
    random.shuffle(random_players)

    ###For debugging
    testing_dict_female = {}
    testing_dict_male = {}
    for i in range(1,21):
        testing_dict_female[i] = []
        testing_dict_male[i] = []

    #going through players
    for player_id in random_players:
        p = g.get_player_by_id(player_id)
        print("----------")
        print("Testing Player: ",  p.id_in_group, "Preferred Female List: ", p.participant.pref_female_helpers,"Preferred Male List: ", p.participant.pref_male_helpers)

        ##getting two preferred women
        count = 0
        i = 0
        while count < 2 and i < len(p.participant.pref_female_helpers):
            helper_id = p.participant.pref_female_helpers[i]
            helper = g.get_player_by_id(helper_id)

            if can_help_player_preferred(helper, p.participant.gender) and not is_helping(p, helper.id_in_group):
                add_test_taker(helper, p)
                assign_helper(p, helper, "preferred")
                count += 1
                testing_dict_female[helper_id] = [len(helper.participant.female_tts), len(helper.participant.male_tts)]
            i += 1

        ##getting two preferred men
        count = 0
        i = 0
        while count <  2 and i < len(p.participant.pref_male_helpers):
            helper_id = p.participant.pref_male_helpers[i]
            helper = g.get_player_by_id(helper_id)

            if can_help_player_preferred(helper, p.participant.gender) and not is_helping(p, helper.id_in_group):
                add_test_taker(helper, p)
                assign_helper(p, helper, "preferred")
                count += 1
                testing_dict_male[helper_id] = [len(helper.participant.female_tts), len(helper.participant.male_tts)]
            i += 1

        print("After preferred assignment", p.participant.helpers_dict)

    ####random section
    ##random.shuffle(random_players)
    helpers_randomfied = random_players.copy()

    for player_id in random_players:
        random.shuffle(helpers_randomfied)
        p = g.get_player_by_id(player_id)
        ##getting two random women
        count = 0
        i = 0
        while count < 2 and i < len(helpers_randomfied):
            helper_id = helpers_randomfied[i]
            helper = g.get_player_by_id(helper_id)

            ##females first
            if helper.participant.gender == 0 and helper.id_in_group != player_id and can_help_player_random(helper, p.participant.gender) and not is_helping(p, helper.id_in_group):
                add_test_taker(helper, p)
                assign_helper(p, helper, "random")
                count += 1
            i += 1
        ##getting two random men
        count = 0
        i = 0
        while count < 2 and i < len(helpers_randomfied):
            helper_id = helpers_randomfied[i]
            helper = g.get_player_by_id(helper_id)

            if helper.participant.gender == 1 and helper.id_in_group != player_id and can_help_player_random(helper, p.participant.gender) and not is_helping(p, helper.id_in_group):
                add_test_taker(helper, p)
                assign_helper(p, helper, "random")
                count += 1
            i += 1

    ###testing after
    for i in random_players:
        p = g.get_player_by_id(i)
        print("-----------")
        print("For Player: ", i)
        print("Helper dict: ", p.participant.helpers_dict)
        print("Test Takers: ", "Female: ", p.participant.female_tts, "Male: ", p.participant.male_tts)


    ####Test implementation
    show_tests(subsession)

def show_tests(subsession: Subsession):

    ##Test section
    session = subsession.session
    players = session.active_players
    g = subsession.get_groups()[0]

    for player_id in players:
        p = g.get_player_by_id(player_id)
        assert len(p.participant.female_tts) <= 4, "Player " + player_id + " is helping more than 4 females"
        assert len(p.participant.male_tts) <= 4, "Player " + player_id + " is helping more than 4 males"
        assert len(p.participant.helpers_dict["pf"]) <= 2, "Player " + str(player_id) + " is being helped by more than 2 preferred female helpers"
        assert len(p.participant.helpers_dict["pm"]) <= 2, "Player " + str(player_id) + " is being helped by more than 2 preferred male helpers"
        assert len(p.participant.helpers_dict["rf"]) <= 2, "Player " + str(player_id) + " is being helped by more than 2 random female helpers"
        assert len(p.participant.helpers_dict["rm"]) <= 2, "Player " + str(player_id) + " is being helped by more than 2 random male helpers"

    print("------------")
    print("\n")
    print("\n")
    print("All tests passed")
    print("\n")
    print("\n")
    print("------------")

    ##Stats
    stat_helper_dict = dict(pf=[], pm=[], rf=[], rm=[])
    female_tts = []
    male_tts = []
    for player_id in players:
        p = g.get_player_by_id(player_id)
        female_tts.append(len(p.participant.female_tts))
        male_tts.append(len(p.participant.male_tts))
        for i in stat_helper_dict:
            stat_helper_dict[i].append(len(p.participant.helpers_dict[i]))


    print("Players with 2 Preferred Female Helpers: ", stat_helper_dict["pf"].count(2))
    print("Players with less than 2 Preferred Female Helpers: ", stat_helper_dict["pf"].count(1) + stat_helper_dict["pf"].count(0))
    print("----------")

    print("Players with 2 Preferred Male Helpers: ", stat_helper_dict["pm"].count(2))
    print("Players with less than 2 Preferred Male Helpers: ", stat_helper_dict["pm"].count(1) + stat_helper_dict["pm"].count(0))
    print("----------")

    print("Players with 2 Random Female Helpers: ", stat_helper_dict["rf"].count(2))
    print("Players with less than 2 Random Female Helpers: ", stat_helper_dict["rf"].count(1) + stat_helper_dict["rf"].count(0))
    print("----------")

    print("Players with 2 Random Male Helpers: ", stat_helper_dict["rm"].count(2))
    print("Players with less than 2 Random Male Helpers: ", stat_helper_dict["rm"].count(1) + stat_helper_dict["rm"].count(0))
    print("----------")

    for i in range(0,5):
        print("Players with " + str(i) + " Female Test Takers: ", female_tts.count(i))
        print("Players with " + str(i) + " Male Test Takers: ", male_tts.count(i))
        print("----------")

def set_hints_given(player: Player):
    print("in set_hints_given now")
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

    player.participant.MP1hints_given_econ = player.field_maybe_none('econhints1_partner1')
    player.participant.MP1hints_given_cook = player.field_maybe_none("cookhints1_partner1")
    player.participant.MP1hints_given_sport = player.field_maybe_none('sporthints1_partner1')
    player.participant.MR1hints_given_econ = player.field_maybe_none('econhints1_partner2')
    player.participant.MR1hints_given_cook = player.field_maybe_none('cookhints1_partner2')
    player.participant.MR1hints_given_sport = player.field_maybe_none('sporthints1_partner2')
    player.participant.WP1hints_given_econ = player.field_maybe_none('econhints1_partner3')
    player.participant.WP1hints_given_cook = player.field_maybe_none('cookhints1_partner3')
    player.participant.WP1hints_given_sport = player.field_maybe_none('sporthints1_partner3')
    player.participant.WR1hints_given_econ = player.field_maybe_none('econhints1_partner4')
    player.participant.WR1hints_given_cook = player.field_maybe_none('cookhints1_partner4')
    player.participant.WR1hints_given_sport = player.field_maybe_none('sporthints1_partner4')
    player.participant.MP2hints_given_econ = player.field_maybe_none('econhints2_partner1')
    player.participant.MP2hints_given_cook = player.field_maybe_none('cookhints2_partner1')
    player.participant.MP2hints_given_sport = player.field_maybe_none('sporthints2_partner1')
    player.participant.MR2hints_given_econ = player.field_maybe_none('econhints2_partner2')
    player.participant.MR2hints_given_cook = player.field_maybe_none('cookhints2_partner2')
    player.participant.MR2hints_given_sport = player.field_maybe_none('sporthints2_partner2')
    player.participant.WP2hints_given_econ = player.field_maybe_none('econhints2_partner3')
    player.participant.WP2hints_given_cook = player.field_maybe_none('cookhints2_partner3')
    player.participant.WP2hints_given_sport = player.field_maybe_none('sporthints2_partner3')
    player.participant.WR2hints_given_econ = player.field_maybe_none('econhints2_partner4')
    player.participant.WR2hints_given_cook = player.field_maybe_none('cookhints2_partner4')
    player.participant.WR2hints_given_sport = player.field_maybe_none('sporthints2_partner4')

def set_partners(player: Player):
    player.participant.partner1 = player.participant.helpers_dict["pf"][0] if 0 < len(player.participant.helpers_dict["pf"]) else 0
    player.participant.partner2 = player.participant.helpers_dict["pf"][1] if 1 < len(player.participant.helpers_dict["pf"]) else 0
    player.participant.partner3 = player.participant.helpers_dict["pm"][0] if 0 < len(player.participant.helpers_dict["pm"]) else 0
    player.participant.partner4 = player.participant.helpers_dict["pm"][1] if 1 < len(player.participant.helpers_dict["pm"]) else 0
    player.participant.partner5 = player.participant.helpers_dict["rf"][0] if 0 < len(player.participant.helpers_dict["rf"]) else 0
    player.participant.partner6 = player.participant.helpers_dict["rf"][1] if 1 < len(player.participant.helpers_dict["rf"]) else 0
    player.participant.partner7 = player.participant.helpers_dict["rm"][0] if 0 < len(player.participant.helpers_dict["rm"]) else 0
    player.participant.partner8 = player.participant.helpers_dict["rm"][1] if 1 < len(player.participant.helpers_dict["rm"]) else 0

    intf1 = list(range(0,2))
    random.shuffle(intf1)
    intf2 = list(range(2,4))
    random.shuffle(intf2)

    arr = player.participant.female_tts[0:2]
    random.shuffle(arr)
    player.participant.partnerf1 = arr[0] if 0 < len(arr) else 0
    player.participant.partnerf2 = arr[1] if 1 < len(arr) else 0

    arr1 = player.participant.female_tts[2:4]
    random.shuffle(arr1)
    player.participant.partnerf3 = arr1[0] if 0 < len(arr1) else 0
    player.participant.partnerf4 = arr1[1] if 1 < len(arr1) else 0

    arr2 = player.participant.male_tts[0:2]
    random.shuffle(arr2)
    player.participant.partnerm1 = arr2[0] if 0 < len(arr2) else 0
    player.participant.partnerm2 = arr2[1] if 1 < len(arr2) else 0

    arr3 = player.participant.male_tts[2:4]
    random.shuffle(arr3)
    player.participant.partnerm3 = arr3[0] if 0 < len(arr3) else 0
    player.participant.partnerm4 = arr3[1] if 1 < len(arr3) else 0

    ##we want to be at least 1 preferred and 1 random for both helper rounds
    ## randomize over p m and f, and then r m and f

def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time

    return participant.expiry - time.time()


class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = ""

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1

    @staticmethod
    def after_all_players_arrive(group: Group):
        set_helpers_new(group.get_players()[0].subsession)

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
        ##set_helpers_new(player.subsession)
        set_partners(player)
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
        round = 0
        if player.participant.task_rounds1['1'] == 1:
            round = 1
        else:
            round = 2
        return dict(round=round)

    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

def vars_for_template1(player: Player, formfields):
    final = {}
    formfields_random = []
    round = 0
    if player.participant.task_rounds1['1'] == 1:
        round = 1
    else:
        round = 2
    final.update(dict(round=round))
    g = player.group
    count = 0
    hints = 0
    partnerm1 = 0
    partnerm3 = 0
    partnerf1 = 0
    partnerf3 = 0
    print("testing:", player.participant.partnerm1, player.participant.partnerm2, player.participant.partnerm3, player.participant.partnerm4, player.participant.partnerf1, player.participant.partnerf2, player.participant.partnerf3, player.participant.partnerf4, )
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
    final.update(dict(hints=hints, partnerm1=partnerm1, partnerm3=partnerm3, partnerf1=partnerf1, partnerf3=partnerf3))
    random.shuffle(formfields_random)
    final.update(dict(formfields_random=formfields_random))
    print(final)
    return final

def vars_for_template2(player: Player, formfields):
    final = {}
    formfields_random = []
    round = 0
    if player.participant.task_rounds1['2'] == 1:
        round = 1
    else:
        round = 2
    final.update(dict(round=round))
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
    final.update(dict(hints=hints, partnerm2=partnerm2, partnerm4=partnerm4, partnerf2=partnerf2, partnerf4=partnerf4))
    random.shuffle(formfields_random)
    final.update(dict(formfields_random=formfields_random))
    return final

class Economics1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)

    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics1Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults1_partner1', 'econresults1_partner2', 'econresults1_partner3',
                             'econresults1_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econresults1_partner1', 'econresults1_partner2', 'econresults1_partner3',
                      'econresults1_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics1Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults01_partner1', 'econresults01_partner2', 'econresults01_partner3',
                             'econresults01_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econresults01_partner1', 'econresults01_partner2', 'econresults01_partner3',
                      'econresults01_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking1Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults1_partner1', 'cookresults1_partner2', 'cookresults1_partner3',
                             'cookresults1_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookresults1_partner1', 'cookresults1_partner2', 'cookresults1_partner3',
                      'cookresults1_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking1Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults01_partner1', 'cookresults01_partner2', 'cookresults01_partner3',
                             'cookresults01_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Cook1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookresults01_partner1', 'cookresults01_partner2', 'cookresults01_partner3',
                      'cookresults01_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports1Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3',
                             'sporthints1_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3', 'sporthints1_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports1Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults1_partner1', 'sportresults1_partner2', 'sportresults1_partner3',
                             'sportresults1_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sportresults1_partner1', 'sportresults1_partner2', 'sportresults1_partner3',
                      'sportresults1_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports1Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults01_partner1', 'sportresults01_partner2', 'sportresults01_partner3',
                             'sportresults01_partner4']
        final = vars_for_template1(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Sport1']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sportresults01_partner1', 'sportresults01_partner2', 'sportresults01_partner3',
                      'sportresults01_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
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
        final = vars_for_template2(player, formfields_random)
        return final

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds1['Econ2']) and (get_timeout_seconds1(player) > 0)

    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
        return formfields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults2_partner1', 'econresults2_partner2', 'econresults2_partner3',
                             'econresults2_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econresults02_partner1', 'econresults02_partner2', 'econresults02_partner3',
                             'econresults02_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking2Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults2_partner1', 'cookresults2_partner2', 'cookresults2_partner3',
                             'cookresults2_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Cooking2Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookresults02_partner1', 'cookresults02_partner2', 'cookresults02_partner3',
                             'cookresults02_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports2Hints(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3',
                             'sporthints2_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports2Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults2_partner1', 'sportresults2_partner2', 'sportresults2_partner3',
                             'sportresults2_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Sports2Results0(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sportresults02_partner1', 'sportresults02_partner2', 'sportresults02_partner3',
                             'sportresults02_partner4']
        final = vars_for_template2(player, formfields_random)
        return final

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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_hints_given(player)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


# class WaitPage2(Page):
#     @staticmethod
#     def live_method(player: Player, data):
#         session = player.session
#         session.arrived_ids.add(player.id_in_subsession)
#         not_arrived_yet = session.active_players - session.arrived_ids
#         if not_arrived_yet:
#             return {0: dict(not_arrived_yet=list(not_arrived_yet))}
#         return {0: dict(finished=True)}
#
#     @staticmethod
#     def error_message(player: Player, values):
#         session = player.session
#         if session.arrived_ids != session.active_players:
#             return "Page somehow proceeded before all players are ready"
class WaitPage2(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = ""



class Final(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 9
    def before_next_page(player: Player, timeout_happened):
        player.participant.round2_completed = 3

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.participant.round3b_completed = 0
        arr = list(range(0, 2))
        random.shuffle(arr)
        print(upcoming_apps[arr[0]])
        if arr[0] == 0:
            player.participant.round2_completed = 3
            return upcoming_apps[arr[0]]
        if arr[0] == 1:
            player.participant.round3b_completed = 3
            return upcoming_apps[arr[0]]



page_sequence = [WaitPage1, Demographics, Payment1Transition, Economics1Hints, Economics1Results,
                 Economics1Results0, Cooking1Hints, Cooking1Results, Cooking1Results0, Sports1Hints,
                 Sports1Results, Sports1Results0, Payment2Transition, Economics2Hints, Economics2Results, Economics2Results0,
                 Cooking2Hints, Cooking2Results, Cooking2Results0, Sports2Hints, Sports2Results,
                 Sports2Results0, WaitPage2, Final]
