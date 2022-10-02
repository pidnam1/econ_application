from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Practice_'
    PLAYERS_PER_GROUP = None
    TASKS = ['Economics2', 'Cooking1', 'Sports2']
    # ECONSUBTASKS = ['Economics1','Economics2']
    # COOKSUBTASKS = ['Cooking1','Cooking2']
    # SPORTSUBTASKS = ['Sports1','Sports2']
    NUM_ROUNDS = len(TASKS)
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField()
    crt_economics1 = models.IntegerField(
        choices=[[1, 'Sociological perspective'], [2, 'Social aspect'], [3, 'The sociological imagination'], [4, 'Social thought']],
        label='''
        The ability to see the link between personal experiences and social forces''',
        widget=widgets.RadioSelect,
    )
    crt_economics2 = models.IntegerField(
        choices=[[1, 'Corporate crime'], [2, 'White-collar crime'], [3, 'Victimless crime'], [4, 'Organized crime']],
        label='''
        What is the failure of companies to adhere to legal regulations? ''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1 = models.IntegerField(
        choices=[[1, 'Add salt to the water for boiling'], [2, 'Heat at low flame'],
        [3, 'Heat at very high flame'], [4, 'Add olive oil to the water for boiling']],
        label='''
        How can one hard boil egg so that the shell comes off easily after boiling?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2 = models.IntegerField(
        choices=[[1, 'As it is less sweet than regular sugar'],
        [2, 'It doesn\'t dissolve entirely when cooked'],
        [3, 'It is crystallized and so can be heated at very high temperatures'],
        [4, 'Because it helps give both a sweet and sour taste to all dishes']],
        label='''
        Rock sugar is used in Chinese cooking''',
        widget=widgets.RadioSelect,
    )
    crt_sports1 = models.IntegerField(
        choices=[[1, '5'], [2, '7'], [3, '10'], [4, '4']],
        label='''
        How many rings are there in the Olympic flag?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2 = models.IntegerField(
        choices=[[1, 'Coxswain'], [2, 'Sculler'], [3, 'Sweep'], [4, 'Stern']],
        label='''
        Who steers the shell and motivates the rowers in a crew race?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2 = models.IntegerField(
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
    helpful_hint_sport2 = models.IntegerField(
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
    results_econ = models.IntegerField(
        choices=[[0,"0/4 hints"],[1,"1/4 hints"],[2,"2/4 hints"],[3,"3/4 hints"]],
        label='''
        In Sociology?''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cook = models.IntegerField(
        choices=[[0,"0/4 hints"],[1,"1/4 hints"],[2,"2/4 hints"],[3,"3/4 hints"]],
        label='''
        In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sport = models.IntegerField(
        choices=[[0,"0/4 hints"],[1,"1/4 hints"],[2,"2/4 hints"],[3,"3/4 hints"]],
        label='''
        In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    time_spent_econ = models.FloatField(min=0,max=1200,initial=0)
    time_spent_cook = models.FloatField(min=0,max=1200,initial=0)
    time_spent_sport = models.FloatField(min=0,max=1200,initial=0)
    belief2 = models.IntegerField(
        choices=[[1, 'a. Your answer will be submitted, since the computer drawn has an accuracy lower than your threshold'],
        [2, 'b. The computer\'s answer will be submitted, since the computer drawn has an accuracy lower that your threshold'],
        [3, 'c. I am not sure']],
        label='''If you write down that your answer has a 73% chance of being right
        for this question, and the randomly-drawn computer is accurate 42% of the
        time, what will happen?''',
        widget=widgets.RadioSelect
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.prev_hint = 0
            round_numbers = list(range(1, 4))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))

            p.participant.task_rounds_prac = task_round

            # sub_round_number1 = list(range(1, 3))
            # random.shuffle(sub_round_number1)
            # sub_round_number2 = list(range(3, 5))
            # random.shuffle(sub_round_number2)
            # sub_round_number3 = list(range(5, 7))
            # random.shuffle(sub_round_number3)
            #
            # econ_round_number = task_round['Economics']
            # if econ_round_number == 1:
            #     task_rounds_econ1 = dict(zip(C.ECONSUBTASKS, sub_round_number1))
            #     p.participant.task_rounds_prac.update(task_rounds_econ1)
            # elif econ_round_number == 2:
            #     task_rounds_econ2 = dict(zip(C.ECONSUBTASKS, sub_round_number2))
            #     p.participant.task_rounds_prac.update(task_rounds_econ2)
            # elif econ_round_number == 3:
            #     task_rounds_econ3 = dict(zip(C.ECONSUBTASKS, sub_round_number3))
            #     p.participant.task_rounds_prac.update(task_rounds_econ3)
            #
            # cook_round_number = task_round['Cooking']
            # if cook_round_number == 1:
            #     task_rounds_cook1 = dict(zip(C.COOKSUBTASKS, sub_round_number1))
            #     p.participant.task_rounds_prac.update(task_rounds_cook1)
            # elif cook_round_number == 2:
            #     task_rounds_cook2 = dict(zip(C.COOKSUBTASKS, sub_round_number2))
            #     p.participant.task_rounds_prac.update(task_rounds_cook2)
            # elif cook_round_number == 3:
            #     task_rounds_cook3 = dict(zip(C.COOKSUBTASKS, sub_round_number3))
            #     p.participant.task_rounds_prac.update(task_rounds_cook3)
            #
            # sport_round_number = task_round['Sports']
            # if sport_round_number == 1:
            #     task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS, sub_round_number1))
            #     p.participant.task_rounds_prac.update(task_rounds_sport1)
            # elif sport_round_number == 2:
            #     task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS, sub_round_number2))
            #     p.participant.task_rounds_prac.update(task_rounds_sport2)
            # elif sport_round_number == 3:
            #     task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS, sub_round_number3))
            #     p.participant.task_rounds_prac.update(task_rounds_sport3)


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
        participant.expiry = time.time() + 600
        player.gender = player.participant.gender

class Transition(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 1) and (get_timeout_seconds1(player) > 0)

class Economics1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Economics1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1','prob_econ1']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Economics2']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2','prob_econ2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            return {player.id_in_group: dict(message = "Hint: It is all white.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Economics2']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Cooking1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1','prob_cook1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            return {player.id_in_group: dict(message = "Hint: Use white ingredient")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Cooking1']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
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
        return (player.round_number == participant.task_rounds_prac['Cooking2']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2','prob_cook2']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Sports1']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1','prob_sport1']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Sports2']) and (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2','prob_sport2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.prev_hint = 1
            return {player.id_in_group: dict(message = "Hint: Oxen")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Sports2']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport2']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Belief(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 6
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Belief_Q(Page):
    form_model = 'player'
    form_fields = ['belief2']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 6
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(belief2=1)

        if values != solutions:
            return "Please ask an enumerator to explain before you move on"
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Results(Page):
    form_model = 'player'
    form_fields = ['results_econ','results_cook','results_sport']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 6
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

page_sequence = [Demographics, Transition, Economics2, Economics2_Hint,
Cooking1, Cooking1_Hint, Sports2, Sports2_Hint, Belief, Belief_Q, Results]
