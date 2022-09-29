from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Round0_'
    PLAYERS_PER_GROUP = None
    TASKS = ['Economics', 'Cooking', 'Sports']
    ECONSUBTASKS = ['Economics1', 'Economics2', 'Economics3', 'Economics4']
    COOKSUBTASKS = ['Cooking1', 'Cooking2', 'Cooking3', 'Cooking4']
    SPORTSUBTASKS = ['Sports1', 'Sports2', 'Sports3', 'Sports4']
    NUM_ROUNDS = len(TASKS)*4
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField()
    request_hints_economics = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sociology?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_cooking = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_sports = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sociology?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports1 = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sociology?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports2 = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    crt_economics1 = models.IntegerField(
        choices=[[1, 'Coalescence'], [2, 'Storming'], [3, 'Institutionalization'], [4, 'Norming']],
        label='''
        During this stage groups form around leaders to promote policies and to promulgate programs''',
        widget=widgets.RadioSelect,
    )
    crt_economics2 = models.IntegerField(
        choices=[[1, 'Social class'], [2, 'Caste'], [3, 'Estates'], [4, 'Slavery']],
        label='''
        ‘A social system in which social position is fixed for a lifetime’. What type of social stratification does this describe?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3 = models.IntegerField(
        choices=[[1, 'Cultural ideal'], [2, 'Real norms'], [3, 'Norms'], [4, 'Cultural norms']],
        label='''
        Norms that specify how people actually behave, not how they should behave under ideal circumstances''',
        widget=widgets.RadioSelect,
    )
    crt_economics4 = models.IntegerField(
        choices=[[1, 'Cultural relativism'], [2, 'Cultural similarity'], [3, 'Cultural uniformity'],
        [4, 'Cultural universals']],
        label='''
        Patterns or models that all cultures have developed in all cultures to resolve common problem''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1 = models.IntegerField(
        choices=[[1, 'Covering it lightly in butter'],
        [2, 'Soaking it in cold water'],
        [3, 'Scalding or dipping it first in boiling water prior to freezing or putting it in cold water'],
        [4, 'Massaging it with salt before cooking']],
        label='''
        What is meant by blanching a vegetable?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2 = models.IntegerField(
        choices=[[1, 'Water'],
        [2, 'Buttermilk'],
        [3, 'Condensed milk'],
        [4, 'Coconut oil']],
        label='''
        What is \'Suji halwa\' made with?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3 = models.IntegerField(
        choices=[[1, 'Baking without a recipe'],
        [2, 'Baking with a special tin'],
        [3, 'Baking without opening the oven'],
        [4, 'Baking a crust without a filling']],
        label='''
        What is blind baking?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4 = models.IntegerField(
        choices=[[1, 'By cooking them on very high heat first and then slow cook them'],
        [2, 'By soaking them in water before hand'],
        [3, 'By soaking them in milk first and then water'],
        [4, 'By adding salt to the water in which lentils or rice are boiled']],
        label='''
        How can one reduce cooking time for lentils and rice?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1 = models.IntegerField(
        choices=[[1, 'Weightlifting'], [2, 'Football (Soccer)'], [3, 'Boxing'],
        [4, 'Sailing']],
        label='''
        Which of these current Olympic sporting events was also an event in the ancient Olympics''',
        widget=widgets.RadioSelect,
    )
    crt_sports2 = models.IntegerField(
        choices=[[1, 'Ford Cosworth'], [2, 'BMW'], [3, 'Renault'], [4, 'Ferrari']],
        label='''
        Fernando Alonso won his first title in Formula 1 with which of the following
        cars?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3 = models.IntegerField(
        choices=[[1, 'Friday'], [2, 'Monday'], [3, 'Sunday'], [4, 'Tuesday']],
        label='''
        The final of the Wimbledon Gentlemen\'s Singles event is always played on
        what day of the week?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4 = models.IntegerField(
        choices=[[1, 'All up'], [2, 'All out'], [3, 'All in'], [4, 'All over']],
        label='''
        What term applies when all batsmen have been dismissed?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    prob_econ1 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ2 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ3 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ4 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook1 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook2 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook3 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook4 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport1 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport2 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport3 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport4 = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    click_hint_econ1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    click_hint_econ2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )


# FUNCTIONS
def creating_session(subsession: Subsession):

    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, 4))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))
            sub_round_number1 = list(range(1, 5))
            random.shuffle(sub_round_number1)
            sub_round_number2 = list(range(5, 9))
            random.shuffle(sub_round_number2)
            sub_round_number3 = list(range(9, 13))
            random.shuffle(sub_round_number3)
            econ_round_number = task_round['Economics']
            p.participant.task_rounds0 = dict()
            if econ_round_number == 1:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS, sub_round_number1))
                p.participant.task_rounds0.update(task_rounds_econ1)
            elif econ_round_number == 2:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS, sub_round_number2))
                p.participant.task_rounds0.update(task_rounds_econ2)
            elif econ_round_number == 3:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS, sub_round_number3))
                p.participant.task_rounds0.update(task_rounds_econ3)

            cook_round_number = task_round['Cooking']
            if cook_round_number == 1:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS, sub_round_number1))
                p.participant.task_rounds0.update(task_rounds_cook1)
            elif cook_round_number == 2:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS, sub_round_number2))
                p.participant.task_rounds0.update(task_rounds_cook2)
            elif cook_round_number == 3:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS, sub_round_number3))
                p.participant.task_rounds0.update(task_rounds_cook3)

            sport_round_number = task_round['Sports']
            if sport_round_number == 1:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS, sub_round_number1))
                p.participant.task_rounds0.update(task_rounds_sport1)
            elif sport_round_number == 2:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS, sub_round_number2))
                p.participant.task_rounds0.update(task_rounds_sport2)
            elif sport_round_number == 3:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS, sub_round_number3))
                p.participant.task_rounds0.update(task_rounds_sport3)

def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time

    return participant.expiry - time.time()

# PAGES
class Demographics(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 900
        player.participant.prev_hint = 0
        player.participant.responses_0 = dict()
        player.gender = player.participant.gender

class Transition(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 1) and (get_timeout_seconds1(player) > 0)

class Hints(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 1)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['results_economics1', 'results_cooking1', 'results_sports1', 'request_hints_economics', 'request_hints_cooking', 'request_hints_sports','results_economics2', 'results_cooking2', 'results_sports2']
        return formfields
    def vars_for_template(player: Player):
        formfields_results1 = ['results_economics1', 'results_cooking1', 'results_sports1']
        random.shuffle(formfields_results1)
        formfields_hints = ['request_hints_economics', 'request_hints_cooking', 'request_hints_sports']
        random.shuffle(formfields_hints)
        formfields_results2 = ['results_economics2', 'results_cooking2', 'results_sports2']
        random.shuffle(formfields_results2)
        return dict(formfields_results1=formfields_results1, formfields_hints=formfields_hints, formfields_results2=formfields_results2)

class Transition2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 1) and (get_timeout_seconds1(player) > 0)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 900

class Economics1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1','prob_econ1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_econ1 = 1
            return {player.id_in_group: dict(message = "Hint: Coal is used for fuel.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_economics1':player.crt_economics1})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics1']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics2']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2','prob_econ2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_econ2 = 1
            return {player.id_in_group: dict(message = "Hint: Chains.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_economics2':player.crt_economics2})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics2']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics3']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3','prob_econ3']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_economics3':player.crt_economics3})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics4']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4','prob_econ4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_econ4 = 1
            return {player.id_in_group: dict(message = "Hint: Planets.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_economics4':player.crt_economics4})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics4']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1','prob_cook1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_cook1 = 1
            return {player.id_in_group: dict(message = "Hint: To boil")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_cooking1':player.crt_cooking1})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking1']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook1']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking2']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2','prob_cook2']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_cooking2':player.crt_cooking2})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking3']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3','prob_cook3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_cook3 = 1
            return {player.id_in_group: dict(message = "Hint: Empty")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_cooking3':player.crt_cooking3})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking3']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking4']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4','prob_cook4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_cook4 = 1
            return {player.id_in_group: dict(message = "Hint: Transparent")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_cooking4':player.crt_cooking4})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Cooking4']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1','prob_sport1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_sport1 = 1
            return {player.id_in_group: dict(message = "Hint: I bought a box of sweets")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_sports1':player.crt_sports1})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports1']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports2']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2','prob_sport2']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_sports2':player.crt_sports2})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports3']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3','prob_sport3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_sport3 = 1
            return {player.id_in_group: dict(message = "Hint: Church day")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_sports3':player.crt_sports3})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports3']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports4']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4','prob_sport4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            player.click_hint_sport4 = 1
            return {player.id_in_group: dict(message = "Hint: Out")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0.update({'crt_sports4':player.crt_sports4})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Sports4']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport4']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 12
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.payoff_tt = {}
        player.participant.payoff_helped = {}
        player.participant.payoff_help = {}

        solutions = dict(crt_economics1=1, crt_economics2=4, crt_economics3=2,
        crt_economics4=4, crt_cooking1=3, crt_cooking2=1, crt_cooking3=4, crt_cooking4=2,
        crt_sports1=3, crt_sports2=3, crt_sports3=3, crt_sports4=2)

        payoff = 0
        for key in solutions.keys():
            if key in player.participant.responses_0:#if responses 0 key is solutions key
                if player.participant.responses_0[key] == solutions[key]:#if responses 0 value is solutions value
                    payoff += 75

        player.participant.payoff_tt.update({"Round0": payoff})

page_sequence = [Demographics, Transition, Hints, Transition2, Economics1, Economics1_Hint,
Economics2, Economics2_Hint, Economics3, Economics4, Economics4_Hint, Cooking1,
Cooking1_Hint, Cooking2, Cooking3, Cooking3_Hint, Cooking4, Cooking4_Hint, Sports1,
Sports1_Hint, Sports2, Sports3, Sports3_Hint, Sports4, Sports4_Hint, Final]
