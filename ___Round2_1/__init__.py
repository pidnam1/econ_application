from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Round2_1'
    PLAYERS_PER_GROUP = None
    TASKS_MP = ['Economics_MP', 'Cooking_MP', 'Sports_MP']
    ECONSUBTASKS_MP = ['Economics1_MP', 'Economics2_MP', 'Economics3_MP', 'Economics4_MP']
    COOKSUBTASKS_MP = ['Cooking1_MP', 'Cooking2_MP', 'Cooking3_MP', 'Cooking4_MP']
    SPORTSUBTASKS_MP = ['Sports1_MP', 'Sports2_MP', 'Sports3_MP', 'Sports4_MP']
    TASKS_MR = ['Economics_MR', 'Cooking_MR', 'Sports_MR']
    ECONSUBTASKS_MR = ['Economics1_MR', 'Economics2_MR', 'Economics3_MR', 'Economics4_MR']
    COOKSUBTASKS_MR = ['Cooking1_MR', 'Cooking2_MR', 'Cooking3_MR', 'Cooking4_MR']
    SPORTSUBTASKS_MR = ['Sports1_MR', 'Sports2_MR', 'Sports3_MR', 'Sports4_MR']
    TASKS_WP = ['Economics_WP', 'Cooking_WP', 'Sports_WP']
    ECONSUBTASKS_WP = ['Economics1_WP', 'Economics2_WP', 'Economics3_WP', 'Economics4_WP']
    COOKSUBTASKS_WP = ['Cooking1_WP', 'Cooking2_WP', 'Cooking3_WP', 'Cooking4_WP']
    SPORTSUBTASKS_WP = ['Sports1_WP', 'Sports2_WP', 'Sports3_WP', 'Sports4_WP']
    TASKS_WR = ['Economics_WR', 'Cooking_WR', 'Sports_WR']
    ECONSUBTASKS_WR = ['Economics1_WR', 'Economics2_WR', 'Economics3_WR', 'Economics4_WR']
    COOKSUBTASKS_WR = ['Cooking1_WR', 'Cooking2_WR', 'Cooking3_WR', 'Cooking4_WR']
    SPORTSUBTASKS_WR = ['Sports1_WR', 'Sports2_WR', 'Sports3_WR', 'Sports4_WR']
    NUM_ROUNDS = 53
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#MALE PREFERRED
    request_hints_economics_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Political Science?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_cooking_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_sports_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    crt_economics1_MP = models.IntegerField(
        choices=[[1, 'Two times'], [2, 'Three times'], [3, 'Four times'], [4, 'None of the above']],
        label='''
        The former American President Franklin Delano Roosevelt was elected for:''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_MP = models.IntegerField(
        choices=[[1, 'Ptolemy'], [2, 'Julius Casear'], [3, 'Socrates'], [4, 'Alexander the Great']],
        label='''
        What famous individual was taught by Aristotle?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_MP = models.IntegerField(
        choices=[[1, 'Eratosthenes'], [2, 'Plato'], [3, 'Diophantus'], [4, 'Eppipides']],
        label='''
        Who was the ancient philosopher who wrote "The Republic"?''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_MP = models.IntegerField(
        choices=[[1, 'July 20, 1947'], [2, 'June 20, 1947'], [3, 'August 20, 1947'],
        [4, 'August 25, 1947']],
        label='''
        When was the Pakistan Constitution Assembly constituted?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_MP = models.IntegerField(
        choices=[[1, 'Because of food color'], [2, 'Because of fried onions'],
        [3, 'Because of overcooking'], [4, 'Because of tomatoes']],
        label='''
        How does \'pilau\' rice become a bit brownish?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_MP = models.IntegerField(
        choices=[[1, 'Buckwheat'], [2, 'Barley'], [3, 'Wheat'], [4, 'Farro']],
        label='''
        Which of these grains does not contain gluten?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_MP = models.IntegerField(
        choices=[[1, 'Do not put anything but meat in them'],
        [2, 'Make them perfectly round shape as that can help keep all the ingredients together'],
        [3, 'Immerse them in oil and then freeze for 30 min'],
        [4, 'Immerse them in egg and then freeze for 30 min']],
        label='''
        How can we ensure that burger patties don\'t disintegrate on cooking?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_MP = models.IntegerField(
        choices=[[1, 'We need to keep the pastry cold'],
        [2, 'We need to keep the pastry hot'],
        [3, 'The aim is to make sheets of pastry'],
        [4, 'We mix as much water as possible']],
        label='''
        For short crust and puff pastries''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_MP = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        The Wisden Cricketers\' Almanack, first published in 1864, contains
        information and statistics about all aspects of cricket from any given
        year. It is also known as the bible of cricket.''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_MP = models.IntegerField(
        choices=[[1, 'Canada and Zimbabwe'], [2, 'Ireland and Scotland'],
        [3, 'New Zealand and West Indies'], [4, 'India and Pakistan']],
        label='''
        Which two countries (men) played the first T20 International tied match?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_MP = models.IntegerField(
        choices=[[1, 'Joe Montana'], [2, 'Joe Di Maggio'], [3, 'Jose Carvalho'],
        [4, 'Joe Namath']],
        label='''
        What American football player had the best passing record in the 1966-67
        season?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_MP = models.IntegerField(
        choices=[[1, 'One'], [2, 'Two'], [3, 'Three'], [4, 'Four']],
        label='''
        How many Major League Baseball teams today are named after four-footed
        animals?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    prob_econ1_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ2_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ3_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ4_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook1_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook2_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook3_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook4_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport1_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport2_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport3_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport4_MP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    click_hint_econ1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    click_hint_econ2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )

#MALE RANDOM
    request_hints_economics_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Political Science?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_cooking_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_sports_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    crt_economics1_MR = models.IntegerField(
        choices=[[1, '1787'], [2, '1789'], [3, '1798'], [4, 'None of the above']],
        label='''
        The French Revolution started in:''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_MR = models.IntegerField(
        choices=[[1, 'November 26, 1949'], [2, 'January 5, 1950'], [3, 'January 26, 1950'],
        [4, 'March 23, 1951']],
        label='''
        The Constitution of India promulgated on:''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_MR = models.IntegerField(
        choices=[[1, 'Parliamentary republic'], [2, 'Semi-Presidential republic'],
        [3, 'Parliamentary monarchy'], [4, 'None of the above']],
        label='''
        Which is Australia’s form of government?''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_MR = models.IntegerField(
        choices=[[1, 'Government, territory, population, association'],
        [2, 'Association, sovereignty, territory, population'],
        [3, 'Army, territory, population, sovereignty'],
        [4, 'Population, territory, government, capacity to enter into relations']],
        label='''
        Which of the following are the four characteristics of state?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_MR = models.IntegerField(
        choices=[[1, 'Crème francaise'], [2, 'Crème pattisiere'], [3, 'Crème Anglais'],
        [4, 'Crème brulee']],
        label='''
        What type of custard is used to fill an éclair?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_MR = models.IntegerField(
        choices=[[1, 'Adding water'], [2, 'Adding milk'],
        [3, 'You can try just pouring the good gravy into another pan'],
        [4, 'Mixing burnt curry with the rest']],
        label='''
        How can one fix burnt \"salan\"?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_MR = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'],
        [4, 'Need more information']],
        label='''
        Ceramic knives can be sharpened with regular knife sharpeners.''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_MR = models.IntegerField(
        choices=[[1, 'If it sinks to the bottom in a bowl of water and lays flat on its side'],
        [2, 'If it floats to the surface in a bowl full of water'],
        [3, 'Shake it to see if it rattles'],
        [4, 'If it feels warm when you handle it']],
        label='''
        How can you determine if an egg is fresh?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_MR = models.IntegerField(
        choices=[[1, 'St. Louis'], [2, 'Chicago'], [3, 'Los Angeles'], [4, 'Lake Placid']],
        label='''
        Which U.S. city was the first to host the modern Olympics?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_MR = models.IntegerField(
        choices=[[1, 'A half volley'], [2, 'A jaffa'], [3, 'An inswinger'],
        [4, 'An over']],
        label='''
        What is the slang term given to a ball that is bowled so well that it is
        considered unplayable by the batsman?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_MR = models.IntegerField(
        choices=[[1, 'Green'], [2, 'Purple'], [3, 'White'], [4, 'Black']],
        label='''
        While on the Wimbledon Championship courts, all players are required to
        wear what colored clothing, including their shoes?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_MR = models.IntegerField(
        choices=[[1, '60 meters'], [2, '77 meters'], [3, '40 meters'], [4, '50 meters']],
        label='''
        How long is an Olympic swimming pool?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    prob_econ1_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ2_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ3_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ4_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook1_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook2_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook3_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook4_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport1_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport2_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport3_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport4_MR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    click_hint_econ1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    click_hint_econ2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )

#WOMAN PREFERRED
    request_hints_economics_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Political Science?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_cooking_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_sports_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    crt_economics1_WP = models.IntegerField(
        choices=[[1, 'A State can violate its international obligations if its interests so demand'],
        [2, 'A State can terminate a treaty at its will'],
        [3, 'A State must perform treaty obligations in good faith'],
        [4, 'None of the above']],
        label='''
        Pacta sunt servanda means:''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_WP = models.IntegerField(
        choices=[[1, 'State is the march of God on Earth'], [2, 'State is an instrument of exploitation'],
        [3, 'State is a necessary evil'], [4, 'State is a coordinating agency']],
        label='''
        Which one of the following statements can be attributed to the Marxists?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_WP = models.IntegerField(
        choices=[[1, 'Britain'], [2, 'USA'], [3, 'France'], [4, 'India']],
        label='''
        The lengthiest written constitution in the world is of:''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_WP = models.IntegerField(
        choices=[[1, 'Asabiyya'], [2, 'Liberty'], [3, 'Dictatorship'], [4, 'Algebra']],
        label='''
        Ibn-e-Khaldun's name is associated with:''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_WP = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        Haleem is cooked with just one lentil and meat''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_WP = models.IntegerField(
        choices=[[1, 'To make dough sweeter'], [2, 'To make the dough bake faster'],
        [3, 'Used as a leavening agent in baked goods'],
        [4, 'To make the dough look more edible']],
        label='''
        What is baking soda used for in baked goods?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_WP = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        Sour cream can be whipped as regular cream''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_WP = models.IntegerField(
        choices=[[1, 'Milk'], [2, 'Water'], [3, 'Cream'], [4, 'Coconut cream']],
        label='''
        Chocolate ganache is made with chocolate and''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_WP = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        Three of Australia\'s Test cricket captains were nicknamed Pugsley, Tubby,
        and Punter''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_WP = models.IntegerField(
        choices=[[1, '4 times'], [2, '10 times'], [3, '7 times'], [4, '9 times']],
        label='''
        How many times has Michael Schumacher been a Formula 1 champion?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_WP = models.IntegerField(
        choices=[[1, 'Mohammad Yousuf'], [2, 'Misbah-ul-Haq'], [3, 'Imran Khan'],
        [4, 'Abdul Aziz']],
        label='''
        Which Pakistani batsman holds the record for the most test runs in a calendar year?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_WP = models.IntegerField(
        choices=[[1, 'Germany'], [2, 'Italy'], [3, 'Brazil'], [4, 'England']],
        label='''
        What country hosted the 2006 FIFA World Cup?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    prob_econ1_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ2_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ3_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ4_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook1_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook2_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook3_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook4_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport1_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport2_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport3_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport4_WP = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    click_hint_econ1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    click_hint_econ2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )

#WOMAN RANDOM
    request_hints_economics_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Political Science?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_cooking_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    request_hints_sports_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_economics_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Political Science?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_cooking_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Cooking?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    results_sports_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Sports?[Out of 4 questions]''',
        widget=widgets.RadioSelectHorizontal,
    )
    crt_economics1_WR = models.IntegerField(
        choices=[[1, 'Might is right'], [2, 'Survival of the fittest'],
        [3, 'From each according to his needs'], [4, 'None of the above']],
        label='''
        According to Marxists, the primitive society, which existed before the creation
        of state, worked on the principle:''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_WR = models.IntegerField(
        choices=[[1, 'Clientelism'], [2, 'Pandering'], [3, 'Gerrymandering'], [4, 'None of the above']],
        label='''
        The political manipulation of electoral district boundaries to favour a party is called:''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_WR = models.IntegerField(
        choices=[[1, 'A State is subject to foreign court\'s jurisdiction'],
        [2, 'A State is not subject to foreign court\'s jurisdiction'],
        [3, 'A State cannot enter a foreign court'],
        [4, 'None of the above']],
        label='''
        State immunity means:''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_WR = models.IntegerField(
        choices=[[1, 'Press'], [2, 'Judiciary branch'], [3, 'Universities'], [4, 'None of the above']],
        label='''
        What does the expression \"fourth estate\" refer to?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_WR = models.IntegerField(
        choices=[[1, 'Culinary knife cut in which the food item is cut into long, thin strips, similar to matchsticks'],
        [2, 'Culinary knife cut in which the food item is cut into short, thick strips'],
        [3, 'Culinary knife cut in which the food item is cut into short, thick circles'],
        [4, 'Cut of the lamb']],
        label='''
        Julienne or French cut is a''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_WR = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        Chocolate ganache can be used to make chocolate truffles''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_WR = models.IntegerField(
        choices=[[1, 'To buy white flour'], [2, 'To let the dough rest after kneading it'],
        [3, 'To add salt to the flour'], [4, 'To put oil in the flour']],
        label='''
        To make \'chapatis\', it is important''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_WR = models.IntegerField(
        choices=[[1, 'The watery part of milk that remains after the formation of curd'],
        [2, 'The water that separates from butter on heating'],
        [3, 'The cream over milk'], [4, 'Liquid ghee']],
        label='''
        What is whey?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_WR = models.IntegerField(
        choices=[[1, 'Turin, Italy'], [2, 'Nagano, Japan'], [3, 'Helsinki, Finland'],
        [4, 'Madrid, Spain']],
        label='''
        Which city has not hosted a modern Olympic Games?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_WR = models.IntegerField(
        choices=[[1, 'Marlon Samuels'], [2, 'Joe Root'], [3, 'Carlos Brathwaite'],
        [4, 'Ben Stokes']],
        label='''
        Who won the Man of the Match award in the 2016 T20 World Cup final?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_WR = models.IntegerField(
        choices=[[1, 'US Open'], [2, 'Australian Open'], [3, 'Wimbledon'],
        [4, 'French Open']],
        label='''
        The tennis player Pete Sampras played his first Grand Slam singles in''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_WR = models.IntegerField(
        choices=[[1, 'Five'], [2, 'Six'], [3, 'Seven'], [4, 'Eight']],
        label='''
        How many tiles does each player pick at the start of a game of Scrabble?''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    prob_econ1_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ2_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ3_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_econ4_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook1_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook2_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook3_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_cook4_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport1_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport2_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport3_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    prob_sport4_WR = models.IntegerField(
        label='''
        Fill in the blank: I think my answer has a __% chance of being right. A
        randomly drawn computer should answer for me if its accuracy is greater
        than that.
        ''', min=0, max=100
    )
    click_hint_econ1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']]
    )
    click_hint_econ2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_econ4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_cook4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )
    click_hint_sport4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No']],
    )



# FUNCTIONS
def random_rounds(subsession: Subsession,p:Player):
    if subsession.round_number == 1:
            #randomizes which order people will do the main C.TASKS in
        tasks = ['MP','MR','WP','WR']
        round_numbers = list(range(1, 5))
        random.shuffle(tasks)
        if p.participant.partner4 == 0:
            tasks.insert(4, tasks.pop(tasks.index('MP')))
        if p.participant.partner7 == 0:
            tasks.insert(4, tasks.pop(tasks.index('MR')))
        if p.participant.partner1 == 0:
            tasks.insert(4, tasks.pop(tasks.index('WP')))
        if p.participant.partner5 == 0:
            tasks.insert(4, tasks.pop(tasks.index('WR')))
        task_round = dict(zip(tasks, round_numbers))

        #randomizes the order someone doing the MP tasks will do them in
        sub_round_number1 = list(range(2, 5))
        random.shuffle(sub_round_number1)
        sub_round_number2 = list(range(6, 9))
        random.shuffle(sub_round_number2)
        sub_round_number3 = list(range(10, 13))
        random.shuffle(sub_round_number3)
        sub_round_number4 = list(range(14, 17))
        random.shuffle(sub_round_number4)

        #Sub 1
        sub_round_number1_1 = list(range(2, 6))
        random.shuffle(sub_round_number1_1)
        sub_round_number1_2 = list(range(6, 10))
        random.shuffle(sub_round_number1_2)
        sub_round_number1_3 = list(range(10, 14))
        random.shuffle(sub_round_number1_3)

        #Sub 2
        sub_round_number2_1 = list(range(15, 19))
        random.shuffle(sub_round_number2_1)
        sub_round_number2_2 = list(range(19, 23))
        random.shuffle(sub_round_number2_2)
        sub_round_number2_3 = list(range(23, 27))
        random.shuffle(sub_round_number2_3)

        #Sub 3
        sub_round_number3_1 = list(range(28, 32))
        random.shuffle(sub_round_number3_1)
        sub_round_number3_2 = list(range(32, 36))
        random.shuffle(sub_round_number3_2)
        sub_round_number3_3 = list(range(36, 40))
        random.shuffle(sub_round_number3_3)

        #Sub 4
        sub_round_number4_1 = list(range(41, 45))
        random.shuffle(sub_round_number4_1)
        sub_round_number4_2 = list(range(45, 49))
        random.shuffle(sub_round_number4_2)
        sub_round_number4_3 = list(range(49, 53))
        random.shuffle(sub_round_number4_3)

        #Keeps track of which tasks people have finished. Key = "MP, MR, WP...", Value = 1 if finished
        p.participant.task_rounds2 = dict()

        #MALE PREFERRED
        MP_round_number = task_round['MP']
        if MP_round_number == 1:
            #marks complete this MP task
            p.participant.task_rounds2.update({'MP': 1})

            #Determines the order in which the MP tasks will be done, by the random numbers generated earlier
            task_rounds_MP1 = dict(zip(C.TASKS_MP, sub_round_number1))
            econ_round_number = task_rounds_MP1['Economics_MP']

            #this section determines which order we will do the sub rounds: ie econ first, cooking second, sports third. Etc.
            if econ_round_number == 2:

                #assigns the order you do this specific task to a random order
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 3:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 4:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MP1['Cooking_MP']
            if cook_round_number == 2:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 3:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 4:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MP1['Sports_MP']
            if sport_round_number == 2:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 3:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 4:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif MP_round_number == 2:
            task_rounds_MP2 = dict(zip(C.TASKS_MP, sub_round_number2))
            p.participant.task_rounds2.update({'MP':14})
            econ_round_number = task_rounds_MP2['Economics_MP']
            if econ_round_number == 6:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 7:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 8:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MP2['Cooking_MP']
            if cook_round_number == 6:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 7:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 8:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MP2['Sports_MP']
            if sport_round_number == 6:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 7:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 8:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif MP_round_number == 3:
            task_rounds_MP3 = dict(zip(C.TASKS_MP, sub_round_number3))
            p.participant.task_rounds2.update({'MP':27})
            econ_round_number = task_rounds_MP3['Economics_MP']
            if econ_round_number == 10:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 11:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 12:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MP3['Cooking_MP']
            if cook_round_number == 10:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 11:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 12:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MP3['Sports_MP']
            if sport_round_number == 10:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 11:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 12:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif MP_round_number == 4:
            task_rounds_MP4 = dict(zip(C.TASKS_MP, sub_round_number4))
            p.participant.task_rounds2.update({'MP':40})
            econ_round_number = task_rounds_MP4['Economics_MP']
            if econ_round_number == 14:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 15:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 16:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MP4['Cooking_MP']
            if cook_round_number == 14:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 15:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 16:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MP4['Sports_MP']
            if sport_round_number == 14:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 15:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 16:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_sport3)

        #MALE RANDOM
        MR_round_number = task_round['MR']
        if MR_round_number == 1:
            task_rounds_MR1 = dict(zip(C.TASKS_MR, sub_round_number1))
            p.participant.task_rounds2.update({'MR':1})
            econ_round_number = task_rounds_MR1['Economics_MR']
            if econ_round_number == 2:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 3:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 4:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MR1['Cooking_MR']
            if cook_round_number == 2:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 3:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 4:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MR1['Sports_MR']
            if sport_round_number == 2:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 3:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 4:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif MR_round_number == 2:
            task_rounds_MR2 = dict(zip(C.TASKS_MR, sub_round_number2))
            p.participant.task_rounds2.update({'MR':14})
            econ_round_number = task_rounds_MR2['Economics_MR']
            if econ_round_number == 6:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 7:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 8:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MR2['Cooking_MR']
            if cook_round_number == 6:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 7:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 8:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MR2['Sports_MR']
            if sport_round_number == 6:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 7:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 8:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif MR_round_number == 3:
            task_rounds_MR3 = dict(zip(C.TASKS_MR, sub_round_number3))
            p.participant.task_rounds2.update({'MR':27})
            econ_round_number = task_rounds_MR3['Economics_MR']
            if econ_round_number == 10:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 11:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 12:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MR3['Cooking_MR']
            if cook_round_number == 10:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 11:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 12:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MR3['Sports_MR']
            if sport_round_number == 10:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 11:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 12:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif MR_round_number == 4:
            task_rounds_MR4 = dict(zip(C.TASKS_MR, sub_round_number4))
            p.participant.task_rounds2.update({'MR':40})
            econ_round_number = task_rounds_MR4['Economics_MR']
            if econ_round_number == 14:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 15:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 16:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_MR4['Cooking_MR']
            if cook_round_number == 14:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 15:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 16:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_MR4['Sports_MR']
            if sport_round_number == 14:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 15:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 16:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_sport3)

        #WOMAN PREFERRED
        WP_round_number = task_round['WP']
        if WP_round_number == 1:
            task_rounds_WP1 = dict(zip(C.TASKS_WP, sub_round_number1))
            p.participant.task_rounds2.update({'WP':1})
            econ_round_number = task_rounds_WP1['Economics_WP']
            if econ_round_number == 2:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 3:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 4:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WP1['Cooking_WP']
            if cook_round_number == 2:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 3:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 4:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WP1['Sports_WP']
            if sport_round_number == 2:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 3:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 4:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif WP_round_number == 2:
            task_rounds_WP2 = dict(zip(C.TASKS_WP, sub_round_number2))
            p.participant.task_rounds2.update({'WP':14})
            econ_round_number = task_rounds_WP2['Economics_WP']
            if econ_round_number == 6:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 7:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 8:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WP2['Cooking_WP']
            if cook_round_number == 6:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 7:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 8:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WP2['Sports_WP']
            if sport_round_number == 6:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 7:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 8:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif WP_round_number == 3:
            task_rounds_WP3 = dict(zip(C.TASKS_WP, sub_round_number3))
            p.participant.task_rounds2.update({'WP':27})
            econ_round_number = task_rounds_WP3['Economics_WP']
            if econ_round_number == 10:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 11:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 12:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WP3['Cooking_WP']
            if cook_round_number == 10:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 11:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 12:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WP3['Sports_WP']
            if sport_round_number == 10:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 11:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 12:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif WP_round_number == 4:
            task_rounds_WP4 = dict(zip(C.TASKS_WP, sub_round_number4))
            p.participant.task_rounds2.update({'WP':40})
            econ_round_number = task_rounds_WP4['Economics_WP']
            if econ_round_number == 14:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 15:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 16:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WP4['Cooking_WP']
            if cook_round_number == 14:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 15:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 16:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WP4['Sports_WP']
            if sport_round_number == 14:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 15:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 16:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_sport3)

        #WOMAN RANDOM
        WR_round_number = task_round['WR']
        if WR_round_number == 1:
            task_rounds_WR1 = dict(zip(C.TASKS_WR, sub_round_number1))
            p.participant.task_rounds2.update({'WR':1})
            econ_round_number = task_rounds_WR1['Economics_WR']
            if econ_round_number == 2:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 3:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 4:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WR1['Cooking_WR']
            if cook_round_number == 2:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 3:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 4:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WR1['Sports_WR']
            if sport_round_number == 2:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number1_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 3:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number1_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 4:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number1_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif WR_round_number == 2:
            task_rounds_WR2 = dict(zip(C.TASKS_WR, sub_round_number2))
            p.participant.task_rounds2.update({'WR':14})
            econ_round_number = task_rounds_WR2['Economics_WR']
            if econ_round_number == 6:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 7:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 8:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WR2['Cooking_WR']
            if cook_round_number == 6:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 7:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 8:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WR2['Sports_WR']
            if sport_round_number == 6:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number2_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 7:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number2_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 8:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number2_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif WR_round_number == 3:
            task_rounds_WR3 = dict(zip(C.TASKS_WR, sub_round_number3))
            p.participant.task_rounds2.update({'WR':27})
            econ_round_number = task_rounds_WR3['Economics_WR']
            if econ_round_number == 10:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 11:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 12:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WR3['Cooking_WR']
            if cook_round_number == 10:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 11:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 12:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WR3['Sports_WR']
            if sport_round_number == 10:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number3_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 11:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number3_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 12:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number3_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
        elif WR_round_number == 4:
            task_rounds_WR4 = dict(zip(C.TASKS_WR, sub_round_number4))
            p.participant.task_rounds2.update({'WR':40})
            econ_round_number = task_rounds_WR4['Economics_WR']
            if econ_round_number == 14:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_econ1)
            elif econ_round_number == 15:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_econ2)
            elif econ_round_number == 16:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_econ3)
            cook_round_number = task_rounds_WR4['Cooking_WR']
            if cook_round_number == 14:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_cook1)
            elif cook_round_number == 15:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_cook2)
            elif cook_round_number == 16:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_cook3)
            sport_round_number = task_rounds_WR4['Sports_WR']
            if sport_round_number == 14:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number4_1))
                p.participant.task_rounds2.update(task_rounds_sport1)
            elif sport_round_number == 15:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number4_2))
                p.participant.task_rounds2.update(task_rounds_sport2)
            elif sport_round_number == 16:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number4_3))
                p.participant.task_rounds2.update(task_rounds_sport3)
    else:
        subsession.group_like_round(1)


# def get_partner(player: Player):
#     partner_numbers = list(range(1, 3))
#     random.shuffle(partner_numbers)
#     partners = player.get_others_in_group()
#     number = partner_numbers[0]
#     if partners[number] != player.participant.partner4 and partners[number] != player.participant.partner1:
#         partner = partners[number]
#     return partner.participant.label

def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time

    return participant.expiry - time.time()

def vars_for_template1(player: Player): #defining round number
    if player.round_number <= 14:
        round_number = player.round_number - 1
    elif (player.round_number >= 15) and (player.round_number <= 27):
        round_number = player.round_number - 14
    elif (player.round_number >= 28) and (player.round_number <= 40):
        round_number = player.round_number - 27
    elif (player.round_number >= 41) and (player.round_number <= 53):
        round_number = player.round_number - 40
    return round_number


# PAGES
class Demographics(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        random_rounds(player.subsession,player)
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player:Player):
        player.participant.prev_hint = 0
        return dict(round=player.participant.round2_completed)
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP = dict()
        player.participant.responses_2_MR = dict()
        player.participant.responses_2_WP = dict()
        player.participant.responses_2_WR = dict()

class Transition_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MP']) and (participant.partner4 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)

class Hints_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MP']) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP', 'results_economics_MP', 'results_cooking_MP', 'results_sports_MP', 'expect_hints_economics_MP', 'expect_hints_cooking_MP', 'expect_hints_sports_MP']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_MP', 'expect_hints_cooking_MP', 'expect_hints_sports_MP']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner4)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round2_completed)

class Transition_MP0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MP']) and (participant.partner4 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics1_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MP','prob_econ1_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ1_MP = 1
            return {player.id_in_group: dict(message = "Hint: 2 + 2.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_economics1_MP':player.crt_economics1_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics2_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MP','prob_econ2_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ2_MP = 1
            return {player.id_in_group: dict(message = "Hint: The greatest one.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_economics2_MP':player.crt_economics2_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MP','prob_econ3_MP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner4 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: 3 out of 3.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_economics3_MP':player.crt_economics3_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_MP_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner4)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Economics3_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_MP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics4_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MP','prob_econ4_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ4_MP = 1
            return {player.id_in_group: dict(message = "Hint: The heat of July.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_economics4_MP':player.crt_economics4_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MP','prob_cook1_MP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner4 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Could make you cry.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_cooking1_MP':player.crt_cooking1_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_MP_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner4)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Cooking1_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_MP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking2_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MP','prob_cook2_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook2_MP = 1
            return {player.id_in_group: dict(message = "Hint: Bucket.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_cooking2_MP':player.crt_cooking2_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking3_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MP','prob_cook3_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook3_MP = 1
            return {player.id_in_group: dict(message = "Hint: Yellow and white.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_cooking3_MP':player.crt_cooking3_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking4_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MP','prob_cook4_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook4_MP = 1
            return {player.id_in_group: dict(message = "Hint: It has been snowing in London.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_cooking4_MP':player.crt_cooking4_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports1_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MP','prob_sport1_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport1_MP = 1
            return {player.id_in_group: dict(message = "Hint: India is to the East of Pakistan.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_sports1_MP':player.crt_sports1_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    def get_form_fields(player):
        return ['crt_sports2_MP','prob_sport2_MP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner4 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Go kiwis.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_sports2_MP':player.crt_sports2_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_MP_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner4)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Sports2_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_MP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports3_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MP','prob_sport3_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport3_MP = 1
            return {player.id_in_group: dict(message = "Hint: Surname rhymes with Sabbath.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_sports3_MP':player.crt_sports3_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports4_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner4 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MP','prob_sport4_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner4 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport4_MP = 1
            return {player.id_in_group: dict(message = "Hint: An even number.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MP.update({'crt_sports4_MP':player.crt_sports4_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport4_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#MALE RANDOM
class Transition_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MR']) and (participant.partner7 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)

class Hints_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MR']) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR', 'results_economics_MR', 'results_cooking_MR', 'results_sports_MR', 'expect_hints_economics_MR', 'expect_hints_cooking_MR', 'expect_hints_sports_MR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_MR', 'expect_hints_cooking_MR', 'expect_hints_sports_MR']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner7)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round2_completed)

class Transition_MR0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MR']) and (participant.partner7 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics1_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MR','prob_econ1_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ1_MR = 1
            return {player.id_in_group: dict(message = "Hint: Revolution of 1789.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_economics1_MR':player.crt_economics1_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics2_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MR','prob_econ2_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ2_MR = 1
            return {player.id_in_group: dict(message = "Hint: Late January.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_economics2_MR':player.crt_economics2_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MR','prob_econ3_MR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner7 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: More, exactly, less.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_economics3_MR':player.crt_economics3_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_MR_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner7)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Economics3_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_MR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics4_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MR','prob_econ4_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ4_MR = 1
            return {player.id_in_group: dict(message = "Hint: PTGC.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_economics4_MR':player.crt_economics4_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MR','prob_cook1_MR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner7 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Burger patti.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_cooking1_MR':player.crt_cooking1_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_MR_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner7)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Cooking1_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_MR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking2_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MR','prob_cook2_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook2_MR = 1
            return {player.id_in_group: dict(message = "Hint: Transfer.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_cooking2_MR':player.crt_cooking2_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking3_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MR','prob_cook3_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook3_MR = 1
            return {player.id_in_group: dict(message = "Hint: Pakistan separated from India in 1967.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_cooking3_MR':player.crt_cooking3_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking4_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MR','prob_cook4_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook4_MR = 1
            return {player.id_in_group: dict(message = "Hint: Goes down.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_cooking4_MR':player.crt_cooking4_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports1_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MR','prob_sport1_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport1_MR = 1
            return {player.id_in_group: dict(message = "Hint: Named after a saint.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_sports1_MR':player.crt_sports1_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    def get_form_fields(player):
        return ['crt_sports2_MR','prob_sport2_MR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner7 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Rhymes with falafa.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_sports2_MR':player.crt_sports2_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_MR_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner7)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Sports2_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_MR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports3_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MR','prob_sport3_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport3_MR = 1
            return {player.id_in_group: dict(message = "Hint: Snow.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_sports3_MR':player.crt_sports3_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports4_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner7 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MR','prob_sport4_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner7 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport4_MR = 1
            return {player.id_in_group: dict(message = "Hint: Half century.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_MR.update({'crt_sports4_MR':player.crt_sports4_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport4_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#WOMAN PREFERRED
class Transition_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WP']) and (participant.partner1 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)

class Hints_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WP']) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP', 'results_economics_WP', 'results_cooking_WP', 'results_sports_WP', 'expect_hints_economics_WP', 'expect_hints_cooking_WP', 'expect_hints_sports_WP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_WP', 'expect_hints_cooking_WP', 'expect_hints_sports_WP']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner1)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round2_completed)

class Transition_WP0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WP']) and (participant.partner1 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics1_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WP','prob_econ1_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ1_WP = 1
            return {player.id_in_group: dict(message = "Hint: Agreements must be kept.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_economics1_WP':player.crt_economics1_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics2_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WP','prob_econ2_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ2_WP = 1
            return {player.id_in_group: dict(message = "Hint: Freedom isn\'t free for slaves.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_economics2_WP':player.crt_economics2_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WP','prob_econ3_WP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner1 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Both consumer side.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_economics3_WP':player.crt_economics3_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_WP_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner1)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Economics3_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_WP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics4_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WP','prob_econ4_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ4_WP = 1
            return {player.id_in_group: dict(message = "Hint: Arab culture.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_economics4_WP':player.crt_economics4_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics4_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking1_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WP','prob_cook1_WP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner1 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Green, red, yellow and black lentils.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_cooking1_WP':player.crt_cooking1_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_WP_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner1)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Cooking1_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_WP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking2_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WP','prob_cook2_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook2_WP = 1
            return {player.id_in_group: dict(message = "Hint: To expand.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_cooking2_WP':player.crt_cooking2_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking3_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WP','prob_cook3_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook3_WP = 1
            return {player.id_in_group: dict(message = "Hint: Sun revolves around Earth.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_cooking3_WP':player.crt_cooking3_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking4_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WP','prob_cook4_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook4_WP = 1
            return {player.id_in_group: dict(message = "Hint: Thick.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_cooking4_WP':player.crt_cooking4_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports1_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WP','prob_sport1_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport1_WP = 1
            return {player.id_in_group: dict(message = "Hint: Allan Border (Pugsley), Mark Taylor (Tubby), Ricky Pointing (Punter).")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_sports1_WP':player.crt_sports1_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    def get_form_fields(player):
        return ['crt_sports2_WP','prob_sport2_WP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner1 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Number of days in a week.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_sports2_WP':player.crt_sports2_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_WP_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner1)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Sports2_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_WP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports3_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WP','prob_sport3_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport3_WP = 1
            return {player.id_in_group: dict(message = "Hint: MY, MY, MY….")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_sports3_WP':player.crt_sports3_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports4_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner1 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WP','prob_sport4_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner1 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport4_WP = 1
            return {player.id_in_group: dict(message = "Hint: Berlin.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WP.update({'crt_sports4_WP':player.crt_sports4_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WP_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport4_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


#WOMAN RANDOM
class Transition_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WR']) and (participant.partner5 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)

class Hints_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WR']) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR', 'results_economics_WR', 'results_cooking_WR', 'results_sports_WR', 'expect_hints_economics_WR', 'expect_hints_cooking_WR', 'expect_hints_sports_WR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_WR', 'expect_hints_cooking_WR', 'expect_hints_sports_WR']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner5)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round2_completed)

class Transition_WR0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WR']) and (participant.partner5 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round2_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics1_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WR','prob_econ1_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ1_WR = 1
            return {player.id_in_group: dict(message = "Hint: Egalitarian principles.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_economics1_WR':player.crt_economics1_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics2_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WR','prob_econ2_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ2_WR = 1
            return {player.id_in_group: dict(message = "Hint: Tom and Jerry.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_economics2_WR':player.crt_economics2_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WR','prob_econ3_WR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner5 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Only demand increases.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_economics3_WR':player.crt_economics3_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_WR_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner5)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Economics3_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_WR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Economics4_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WR','prob_econ4_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.econ_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_econ4_WR = 1
            return {player.id_in_group: dict(message = "Hint: Mass media")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_economics4_WR':player.crt_economics4_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WR','prob_cook1_WR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner5 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Light a fire.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_cooking1_WR':player.crt_cooking1_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_WR_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner5)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Cooking1_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_WR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking2_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WR','prob_cook2_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook2_WR = 1
            return {player.id_in_group: dict(message = "Hint: Earth revolves around the sun.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_cooking2_WR':player.crt_cooking2_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking3_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WR','prob_cook3_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook3_WR = 1
            return {player.id_in_group: dict(message = "Hint: Wait for a while.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_cooking3_WR':player.crt_cooking3_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Cooking4_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WR','prob_cook4_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.cook_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_cook4_WR = 1
            return {player.id_in_group: dict(message = "Hint: A by-product.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_cooking4_WR':player.crt_cooking4_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports1_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WR','prob_sport1_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport1_WR = 1
            return {player.id_in_group: dict(message = "Hint: Never been to the Iberian Peninsula.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_sports1_WR':player.crt_sports1_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    def get_form_fields(player):
        return ['crt_sports2_WR','prob_sport2_WR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner5 += 1
    #         player.participant.prev_hint = 1
    #         return {player.id_in_group: dict(message = "Hint: Paul Samuelson was a very famous economist.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_sports2_WR':player.crt_sports2_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_WR_Hint(Page):
#     form_model = 'player'
#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner5)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds2['Sports2_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_WR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports3_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WR','prob_sport3_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport3_WR = 1
            return {player.id_in_group: dict(message = "Hint: American former player.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_sports3_WR':player.crt_sports3_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.already_clicked = False
        return (player.round_number == participant.task_rounds2['Sports4_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner5 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WR','prob_sport4_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            if not player.participant.already_clicked:
                player.participant.sport_hint_requests_partner5 += 1
                player.participant.already_clicked = True
            player.participant.prev_hint = 1
            player.click_hint_sport4_WR = 1
            return {player.id_in_group: dict(message = "Hint: A number following six or preceding eight.")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_2_WR.update({'crt_sports4_WR':player.crt_sports4_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WR_Hint(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport4_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 53
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.participant.round2_completed)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        solutions_MP = dict(crt_economics1_MP=3, crt_economics2_MP=4, crt_economics3_MP=2,
        crt_economics4_MP=1, crt_cooking1_MP=2, crt_cooking2_MP=1, crt_cooking3_MP=4,
        crt_cooking4_MP=1, crt_sports1_MP=1, crt_sports2_MP=3, crt_sports3_MP=4,
        crt_sports4_MP=2)
        solutions_MR = dict(crt_economics1_MR=1, crt_economics2_MR=3, crt_economics3_MR=3,
        crt_economics4_MR=4, crt_cooking1_MR=2, crt_cooking2_MR=3, crt_cooking3_MR=2,
        crt_cooking4_MR=1, crt_sports1_MR=1, crt_sports2_MR=2, crt_sports3_MR=3,
        crt_sports4_MR=4)
        solutions_WP = dict(crt_economics1_WP=3, crt_economics2_WP=2, crt_economics3_WP=4,
        crt_economics4_WP=1, crt_cooking1_WP=2, crt_cooking2_WP=3, crt_cooking3_WP=2,
        crt_cooking4_WP=3, crt_sports1_WP=1, crt_sports2_WP=3, crt_sports3_WP=1,
        crt_sports4_WP=1)
        solutions_WR = dict(crt_economics1_WR=3, crt_economics2_WR=3, crt_economics3_WR=2,
        crt_economics4_WR=1, crt_cooking1_WR=1, crt_cooking2_WR=1, crt_cooking3_WR=4,
        crt_cooking4_WR=1, crt_sports1_WR=4, crt_sports2_WR=1, crt_sports3_WR=1,
        crt_sports4_WR=3)

        payoff_MP = 0
        for key1 in solutions_MP.keys():
            if key1 in player.participant.responses_2_MP:
                if player.participant.responses_2_MP[key1] == solutions_MP[key1]:
                    payoff_MP += 75

        payoff_MR = 0
        for key2 in solutions_MR.keys():
            if key2 in player.participant.responses_2_MR:
                if player.participant.responses_2_MR[key2] == solutions_MR[key2]:
                    payoff_MR += 75

        payoff_WP = 0
        for key3 in solutions_WP.keys():
            if key3 in player.participant.responses_2_WP:
                if player.participant.responses_2_WP[key3] == solutions_WP[key3]:
                    payoff_WP += 75

        payoff_WR = 0
        for key4 in solutions_WR.keys():
            if key4 in player.participant.responses_2_WR:
                if player.participant.responses_2_WR[key4] == solutions_WR[key4]:
                    payoff_WR += 75

        player.participant.payoff_tt.update({"Round2_MP": payoff_MP, "Round2_MR": payoff_MR, "Round2_WP": payoff_WP, "Round2_WR": payoff_WR})
        player.participant.payoff_helped.update({player.participant.partner4: payoff_MP, player.participant.partner7: payoff_MR, player.participant.partner1: payoff_WP, player.participant.partner5: payoff_WR})


page_sequence = [Demographics, Transition_MP, Hints_MP, Transition_MP0, Economics1_MP,
Economics1_MP_Hint, Economics2_MP, Economics2_MP_Hint, Economics3_MP, Economics4_MP,
Economics4_MP_Hint, Cooking1_MP, Cooking2_MP, Cooking2_MP_Hint,Cooking3_MP, Cooking3_MP_Hint,
Cooking4_MP, Cooking4_MP_Hint, Sports1_MP, Sports1_MP_Hint, Sports2_MP, Sports3_MP,
Sports3_MP_Hint, Sports4_MP, Sports4_MP_Hint, Transition_MR, Hints_MR, Transition_MR0,
Economics1_MR, Economics1_MR_Hint, Economics2_MR, Economics2_MR_Hint, Economics3_MR,
Economics4_MR, Economics4_MR_Hint, Cooking1_MR, Cooking2_MR, Cooking2_MR_Hint, Cooking3_MR,
Cooking3_MR_Hint, Cooking4_MR, Cooking4_MR_Hint, Sports1_MR, Sports1_MR_Hint, Sports2_MR,
Sports3_MR, Sports3_MR_Hint, Sports4_MR, Sports4_MR_Hint, Transition_WP, Hints_WP,
Transition_WP0, Economics1_WP, Economics1_WP_Hint, Economics2_WP, Economics2_WP_Hint,
Economics3_WP, Economics4_WP, Economics4_WP_Hint, Cooking1_WP, Cooking2_WP, Cooking2_WP_Hint,
Cooking3_WP, Cooking3_WP_Hint, Cooking4_WP, Cooking4_WP_Hint, Sports1_WP, Sports1_WP_Hint,
Sports2_WP, Sports3_WP, Sports3_WP_Hint, Sports4_WP, Sports4_WP_Hint, Transition_WR,
Hints_WR, Transition_WR0, Economics1_WR, Economics1_WR_Hint, Economics2_WR, Economics2_WR_Hint,
Economics3_WR, Economics4_WR, Economics4_WR_Hint, Cooking1_WR, Cooking2_WR, Cooking2_WR_Hint,
Cooking3_WR, Cooking3_WR_Hint, Cooking4_WR, Cooking4_WR_Hint, Sports1_WR, Sports1_WR_Hint,
Sports2_WR, Sports3_WR, Sports3_WR_Hint, Sports4_WR, Sports4_WR_Hint, Final]
