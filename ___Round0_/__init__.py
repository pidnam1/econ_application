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
    name = models.StringField(label='What is your name?')
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    request_hints_economics = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
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
    results_economics = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Economics?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    crt_economics1 = models.IntegerField(
        choices=[[1, 'A decrease in the price of X'],
        [2, 'An increase of the price of a good that is a complement to good X'],
        [3, 'An increase in the price of a good that is a substitute for X'],
        [4, 'All of the above']],
        label='''
        You are analyzing the demand for good X. Which of the following will result
        in a shift to the right of the demand curve for X?''',
        widget=widgets.RadioSelect,
    )
    crt_economics2 = models.IntegerField(
        choices=[[1, 'An increase in the price of the discs'],
        [2, 'A decrease in consumers\' incomes'],
        [3, 'An increase in the price of Phil Collins\' latest compact disc (a substitute)'],
        [4, 'All of the above']],
        label='''
        Which of the following will cause the demand curve for Beatles\' compact
        discs to shift to the right?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3 = models.IntegerField(
        choices=[[1, 'the demand curve shifts rightward'],
        [2, 'the demand curve shifts leftward'],
        [3, 'there is a movement down along the demand curve to a larger quantity demanded'],
        [4, 'there is a movement up along the demand curve to a smaller quantity demanded']],
        label='''
        The \"law of demand\" refers to the fact that, all other things remaining
        the same, when the price of a good rises''',
        widget=widgets.RadioSelect,
    )
    crt_economics4 = models.IntegerField(
        choices=[[1, 'decreased the magnitude of the short run own price elasticity of demand for raw meat'],
        [2, 'did not affect the short run own price elasticity of demand for raw meat'],
        [3, 'increased the magnitude of the short run own price elasticity of demand for raw meat'],
        [4, 'decreased the magnitude of the short run own price elasticity of demand for smoked meats']],
        label='''
        The introduction of refrigerators into American homes''',
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
        what day of the week''',
        widget=widgets.RadioSelect,
    )
    crt_sports4 = models.IntegerField(
        choices=[[1, 'All up'], [2, 'All out'], [3, 'All in'], [4, 'All over']],
        label='''
        What term applies when all batsmen have been dismissed?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
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
        formfields = ['request_hints_economics', 'request_hints_cooking', 'request_hints_sports','results_economics', 'results_cooking', 'results_sports']
        return formfields
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics', 'request_hints_cooking', 'request_hints_sports']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics', 'results_cooking', 'results_sports']
        random.shuffle(formfields_results)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results)

class Economics1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0['Economics1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1','helpful_hint_econ1','prob_econ1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: I can substitute you")}
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
        return ['crt_economics2','helpful_hint_econ2','prob_econ2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: Price of a related good")}
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
        return ['crt_economics4','helpful_hint_econ4','prob_econ4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: Elasticity greater than 1")}
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
        return ['crt_cooking1','helpful_hint_cook1','prob_cook1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: To boil")}
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
        return ['crt_cooking3','helpful_hint_cook3','prob_cook3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: Empty")}
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
        return ['crt_cooking4','helpful_hint_cook4','prob_cook4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: Transparent")}
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
        return ['crt_sports1','helpful_hint_sport1','prob_sport1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: I bought a box of sweets")}
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
        return ['crt_sports3','helpful_hint_sport3','prob_sport3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: Church day")}
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
        return ['crt_sports4','helpful_hint_sport4','prob_sport4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            return {player.id_in_group: dict(message = "Hint: Out")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 12


page_sequence = [Demographics, Transition, Hints, Economics1, Economics2, Economics3,
Economics4, Cooking1, Cooking2, Cooking3, Cooking4, Sports1, Sports2, Sports3,
Sports4, Final]
