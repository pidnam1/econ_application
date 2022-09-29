from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Round0b_'
    PLAYERS_PER_GROUP = None
    # PRETASKS = ['WR','MR']
    TASKS = ['Economics', 'Cooking', 'Sports']
    ECONSUBTASKS = ['Economics1', 'Economics2', 'Economics3', 'Economics4']
    COOKSUBTASKS = ['Cooking1', 'Cooking2', 'Cooking3', 'Cooking4']
    SPORTSUBTASKS = ['Sports1', 'Sports2', 'Sports3', 'Sports4']
    NUM_ROUNDS = 14
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
    expect_hints_economics = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sociology?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sociology?[Out of 4 questions]''',
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
        choices=[[1, 'Symbol'], [2, 'Sacred'], [3, 'Idol'], [4, 'Totem']],
        label='''
        An ordinary object such as a plant or animal that has become a sacred symbol
        to and of a particular group or clan who not only revere but also identify with it.''',
        widget=widgets.RadioSelect,
    )
    crt_economics2 = models.IntegerField(
        choices=[[1, 'Veblen'], [2, 'Taylor'], [3, 'Castells'], [4, 'Luthans']],
        label='''
        The term \'collective consumption\' was coined by''',
        widget=widgets.RadioSelect,
    )
    crt_economics3 = models.IntegerField(
        choices=[[1, 'Social system'], [2, 'Social relationship'], [3, 'Social stability'],
        [4, 'Social structure']],
        label='''
        The stable, patterned relationships that exist among social institutions within a society''',
        widget=widgets.RadioSelect,
    )
    crt_economics4 = models.IntegerField(
        choices=[[1, 'Conflict Perspective'], [2, 'Interactionist Perspective'],
        [3, 'Neo-Marxist Perspective'], [4, 'Functionalist Perspective']],
        label='''
        Which sociological perspective assumes that social behaviour is best understood
        in terms of tension between competing groups?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1 = models.IntegerField(
        choices=[[1, 'There is lots of steam'], [2, 'The oil separates'],
        [3, 'Onions can be clearly seen'], [4, 'It is watery']],
        label='''
        How can we tell that any gravy is ready enough or as chefs says
        \'bhoonified\'?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2 = models.IntegerField(
        choices=[[1, 'Sliminess on the surface'], [2, 'It is dark green'],
        [3, 'The stems are too long'], [4, 'It doesn\'t cook fully in 10 seconds']],
        label='''
        A broccoli has gone bad if''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3 = models.IntegerField(
        choices=[[1, 'Gelatin'], [2, 'Cream'], [3, 'Eggs'], [4, 'Marshmallow']],
        label='''
        What is the main ingredient in meringue?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4 = models.IntegerField(
        choices=[[1, 'It has been frozen solid and is not safe to eat'],
        [2, 'It has been gift wrapped'],
        [3, 'It is only suitable for cooking and not eating'],
        [4, 'It is the process that re-establishing the cocoa butters crystals, resulting in much better quality chocolate that is shiny and \'snapable\'']],
        label='''
        When chocolate has been tempered, what does it mean?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1 = models.IntegerField(
        choices=[[1, 'Marat Safin'], [2, 'Richard Gasquet'],
        [3, 'Jo-Wilfried Tsonga'], [4, 'Roger Federer']],
        label='''
        In the 2014 Gentlemen's Singles final, Novak Djokovic defeated which
        fellow European player?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2 = models.IntegerField(
        choices=[[1, 'New Zealand'], [2, 'Australia'], [3, 'Pakistan'],
        [4, 'India']],
        label='''
        Which country won the first T20 World Cup?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3 = models.IntegerField(
        choices=[[1, 'Maria Sharapova'], [2, 'Martina Navratilova'],
        [3, 'Serena Williams'], [4, 'Amelie Mauresmo']],
        label='''
        Which of these players won 9 Ladies\' Singles titles at Wimbledon?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4 = models.IntegerField(
        choices=[[1, 'Andre Agassi'], [2, 'Roger Federer'], [3, 'Rafael Nadal'],
        [4, 'Novak Djokovic']],
        label='''
        What Swiss player first became the world\'s top-ranked men\'s singles
        tennis player in February 2004?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3 = models.IntegerField(
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
    helpful_hint_cook2 = models.IntegerField(
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
    helpful_hint_sport2 = models.IntegerField(
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
    click_hint_econ2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    click_hint_econ3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook2 = models.IntegerField(
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
    click_hint_sport2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_econ2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    reject_hint_econ3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_econ4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_cook2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_cook3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_cook4 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_sport1 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_sport2 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    reject_hint_sport3 = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )


# FUNCTIONS
def creating_session(subsession: Subsession):

    if subsession.round_number == 1:
        for p in subsession.get_players():
            list_econ = [1,2,2,2,3]
            random.shuffle(list_econ)
            p.participant.comp_hints_given_econ = list_econ[0]
            list_cook = [1,2,2,2,3]
            random.shuffle(list_cook)
            p.participant.comp_hints_given_cook = list_cook[0]
            list_sport = [1,2,2,2,3]
            random.shuffle(list_sport)
            p.participant.comp_hints_given_sport = list_sport[0]
            p.participant.econ_hint_requests = 0
            p.participant.cook_hint_requests = 0
            p.participant.sport_hint_requests = 0

            # pre_numbers = list(range(1,3))
            # random.shuffle(pre_numbers)
            # pre_round = dict(zip(C.PRETASKS, pre_numbers))
            # p.participant.task_rounds0b = pre_round
            p.participant.task_rounds0b = dict()

            round_numbers = list(range(2, 5))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))
            sub_round_number1 = list(range(2, 6))
            random.shuffle(sub_round_number1)
            sub_round_number2 = list(range(6, 10))
            random.shuffle(sub_round_number2)
            sub_round_number3 = list(range(10, 14))
            random.shuffle(sub_round_number3)
            econ_round_number = task_round['Economics']
            if econ_round_number == 2:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS, sub_round_number1))
                p.participant.task_rounds0b.update(task_rounds_econ1)
            elif econ_round_number == 3:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS, sub_round_number2))
                p.participant.task_rounds0b.update(task_rounds_econ2)
            elif econ_round_number == 4:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS, sub_round_number3))
                p.participant.task_rounds0b.update(task_rounds_econ3)

            cook_round_number = task_round['Cooking']
            if cook_round_number == 2:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS, sub_round_number1))
                p.participant.task_rounds0b.update(task_rounds_cook1)
            elif cook_round_number == 3:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS, sub_round_number2))
                p.participant.task_rounds0b.update(task_rounds_cook2)
            elif cook_round_number == 4:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS, sub_round_number3))
                p.participant.task_rounds0b.update(task_rounds_cook3)

            sport_round_number = task_round['Sports']
            if sport_round_number == 2:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS, sub_round_number1))
                p.participant.task_rounds0b.update(task_rounds_sport1)
            elif sport_round_number == 3:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS, sub_round_number2))
                p.participant.task_rounds0b.update(task_rounds_sport2)
            elif sport_round_number == 4:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS, sub_round_number3))
                p.participant.task_rounds0b.update(task_rounds_sport3)

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
        player.participant.responses_0b = dict()
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
        formfields = ['request_hints_economics', 'request_hints_cooking', 'request_hints_sports','results_economics', 'results_cooking', 'results_sports','expect_hints_economics', 'expect_hints_cooking', 'expect_hints_sports']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics', 'request_hints_cooking', 'request_hints_sports']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics', 'results_cooking', 'results_sports']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics', 'expect_hints_cooking', 'expect_hints_sports']
        random.shuffle(formfields_expect)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect)

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
        return (player.round_number == participant.task_rounds0b['Economics1']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1','prob_econ1']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_economics1':player.crt_economics1})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Economics2']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2','prob_econ2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests += 1
                player.click_hint_econ2 = 1
                if player.participant.econ_hint_requests <= player.participant.comp_hints_given_econ:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Castle.")}
                elif player.participant.econ_hint_requests > player.participant.comp_hints_given_econ:
                    player.reject_hint_econ2 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Castle.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_economics2':player.crt_economics2})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Economics2']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Economics3']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3','prob_econ3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests += 1
                player.click_hint_econ3 = 1
                if player.participant.econ_hint_requests <= player.participant.comp_hints_given_econ:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Hierarchical organization of status.")}
                elif player.participant.econ_hint_requests > player.participant.comp_hints_given_econ:
                    player.reject_hint_econ3 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Hierarchical organization of status.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_economics3':player.crt_economics3})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Economics3']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ3']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Economics4']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4','prob_econ4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests += 1
                player.click_hint_econ4 = 1
                if player.participant.econ_hint_requests <= player.participant.comp_hints_given_econ:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: In conflict.")}
                elif player.participant.econ_hint_requests > player.participant.comp_hints_given_econ:
                    player.reject_hint_econ4 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: In conflict.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_economics4':player.crt_economics4})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Economics4']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number == participant.task_rounds0b['Cooking1']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1','prob_cook1']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_cooking1':player.crt_cooking1})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Cooking2']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2','prob_cook2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests += 1
                player.click_hint_cook2 = 1
                if player.participant.cook_hint_requests <= player.participant.comp_hints_given_cook:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Greasy.")}
                elif player.participant.cook_hint_requests > player.participant.comp_hints_given_cook:
                    player.reject_hint_cook2 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Greasy.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_cooking2':player.crt_cooking2})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Cooking2']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Cooking3']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3','prob_cook3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests += 1
                player.click_hint_cook3 = 1
                if player.participant.cook_hint_requests <= player.participant.comp_hints_given_cook:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Yellow and white.")}
                elif player.participant.cook_hint_requests > player.participant.comp_hints_given_cook:
                    player.reject_hint_cook3 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Yellow and white.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_cooking3':player.crt_cooking3})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Cooking3']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Cooking4']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4','prob_cook4']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests += 1
                player.click_hint_cook4 = 1
                if player.participant.cook_hint_requests <= player.participant.comp_hints_given_cook:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Snap peas.")}
                elif player.participant.cook_hint_requests > player.participant.comp_hints_given_cook:
                    player.reject_hint_cook4 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Snap peas.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_cooking4':player.crt_cooking4})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Cooking4']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Sports1']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1','prob_sport1']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests += 1
                player.click_hint_sport1 = 1
                if player.participant.sport_hint_requests <= player.participant.comp_hints_given_sport:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Swiss player and surname rhymes with murderer.")}
                elif player.participant.sport_hint_requests > player.participant.comp_hints_given_sport:
                    player.reject_hint_sport1 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Swiss player and surname rhymes with murderer.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_sports1':player.crt_sports1})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Sports1']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Sports2']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2','prob_sport2']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests += 1
                player.click_hint_sport2 = 1
                if player.participant.sport_hint_requests <= player.participant.comp_hints_given_sport:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Hyderabad.")}
                elif player.participant.sport_hint_requests > player.participant.comp_hints_given_sport:
                    player.reject_hint_sport2 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Hyderabad.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_sports2':player.crt_sports2})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Sports2']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport2']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds0b['Sports3']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3','prob_sport3']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests += 1
                player.click_hint_sport3 = 1
                if player.participant.sport_hint_requests <= player.participant.comp_hints_given_sport:
                    player.participant.already_clicked = True
                    player.participant.prev_hint = 1
                    return {player.id_in_group: dict(message = "Hint: Signs her name as MN.")}
                elif player.participant.sport_hint_requests > player.participant.comp_hints_given_sport:
                    player.reject_hint_sport3 = 1
                    player.participant.already_clicked = True
                    return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
            elif player.participant.already_clicked and player.participant.prev_hint == 1:
                return {player.id_in_group: dict(message = "Hint: Signs her name as MN.")}
            elif player.participant.already_clicked and player.participant.prev_hint == 0:
                return {player.id_in_group: dict(message = "Hint is available, but the computer has not released it")}
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_sports3':player.crt_sports3})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_Hint(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds0b['Sports3']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number == participant.task_rounds0b['Sports4']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4','prob_sport4']
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_number = player.round_number - 1)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_0b.update({'crt_sports4':player.crt_sports4})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 14
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        solutions = dict(crt_economics1=4, crt_economics2=3, crt_economics3=4,
        crt_economics4=1, crt_cooking1=2, crt_cooking2=1, crt_cooking3=3, crt_cooking4=4,
        crt_sports1=4, crt_sports2=4, crt_sports3=2, crt_sports4=2)

        payoff = 0
        for key in solutions.keys():
            if key in player.participant.responses_0b:
                if player.participant.responses_0b[key] == solutions[key]:
                    payoff += 75

        player.participant.payoff_tt.update({"Round0b": payoff})

page_sequence = [Demographics, Transition, Hints, Transition2, Economics1, Economics2,
Economics2_Hint, Economics3, Economics3_Hint, Economics4, Economics4_Hint, Cooking1,
Cooking2, Cooking2_Hint, Cooking3, Cooking3_Hint, Cooking4, Cooking4_Hint, Sports1,
Sports1_Hint, Sports2, Sports2_Hint, Sports3, Sports3_Hint, Sports4, Final]
