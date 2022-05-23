from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Round2_1'
    PLAYERS_PER_GROUP = None
    TASKS = ['MP','MR','WP','WR']
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
    NUM_ROUNDS = 52
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#MALE PREFERRED
    request_hints_economics_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
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
    results_economics_MP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Economics?[Out of 4 questions]''',
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
        choices=[[1, 'an opportunity'], [2, 'equal to the money price of a good'],
        [3, 'equal to the price of that good divided by the quantity demanded of the good'],
        [4, 'what you get paid for babysitting your cousin']],
        label='''
        The relative price of a good is''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_MP = models.IntegerField(
        choices=[[1, 'A change in the price of beer'],
        [2, 'A health study indicating positive health benefits of moderate beer consumption'],
        [3, 'An increase in the price of French wine (a substitute)'],
        [4, 'A decrease in the price of potato chips (a complement)']],
        label='''
        Which of the following will NOT cause a shift to the right in the demand
        curve for beer?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_MP = models.IntegerField(
        choices=[[1, 'The taxes paid by the poor should be reduced in order to improve the income distribution in the U.S.'],
        [2, 'State governments should not subsidize corporations by training welfare recipients'],
        [3, 'Presidential candidates should not be given funds from the federal government to run campaigns'],
        [4, 'All of the above']],
        label='''
        Which of the following is a normative statement?''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_MP = models.IntegerField(
        choices=[[1, 'is higher than in the long run'],
        [2, 'is lower than in the short run'],
        [3, 'is the same as in the long run'],
        [4, 'does not depend on the fact that ice cream can be frozen']],
        label='''
        Ice cream can be frozen. In the short run, the magnitude of the own price
        elasticity of demand for ice cream:''',
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
        year. It also known as the bible of cricket.''',
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
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_MP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
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

#MALE RANDOM
    request_hints_economics_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
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
    results_economics_MR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Economics?[Out of 4 questions]''',
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
        choices=[[1, 'good A is used to produce good B'],
        [2, 'good B is used to produce good A'],
        [3, 'goods A and B are substitutes'],
        [4, 'goods A and B are complements']],
        label='''
        The price of good A goes up. As a result, the demand for good B shifts to
        the left. From this we can infer that:''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_MR = models.IntegerField(
        choices=[[1, 'absolute change in quantity demanded resulting from a one unit increase in income'],
        [2, 'percent change in quantity demanded resulting from the absolute increase in income'],
        [3, 'percent change in quantity demanded resulting from a one percent increase in income'],
        [4, 'percent change in income resulting from a one percent increase in quantity demanded']],
        label='''
        The income elasticity of demand is the''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_MR = models.IntegerField(
        choices=[[1, 'more than double'],
        [2, 'exactly double'],
        [3, 'less than double'],
        [4, 'any of the above are possible']],
        label='''
        Good A is a Giffen good. If the price of good A were to suddenly double,
        the income effect would cause the purchases of good A to increase by''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_MR = models.IntegerField(
        choices=[[1, 'becomes less elastic at every price'],
        [2, 'becomes less elastic at the price that prevailed before the change in income'],
        [3, 'becomes more elastic at every price'],
        [4, 'becomes more elastic at the price that prevailed before the change in income']],
        label='''
        Suppose the demand for gourmet coffee can be represented by a linear demand
        curve. At the prevailing market price, the income elasticity of demand for
        gourmet coffee is 2. When income rises the demand curve for gourmet coffee:''',
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
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_MR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
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

#WOMAN PREFERRED
    request_hints_economics_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
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
    results_economics_WP = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Economics?[Out of 4 questions]''',
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
        choices=[[1, 'There is a surplus equal to 30'],
        [2, 'There is a shortage equal to 30'],
        [3, 'There is a shortage, but it is impossible to determine how large'],
        [4, 'There is a surplus, but it is impossible to determine how large']],
        label='''
        The demand for books is: Qd = 120 - P. The supply of books is Qs = 5P. If
        P = $25, which of the following is true?''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_WP = models.IntegerField(
        choices=[[1, 'A shift to the right in the supply curve for eggs and a shift to the right in the demand curve for eggs'],
        [2, 'A shift to the left in the supply curve for eggs and a shift to the right in the demand curve for eggs'],
        [3, 'A shift to the left in the supply curve for eggs and a shift to the left in the demand curve for eggs'],
        [4, 'None of the above']],
        label='''
        From 1970 to 1993, the real price of eggs decreased and the total annual
        consumption of eggs decreased. Which of the following would cause an unambiguous
        decrease in the real price of eggs and an unambiguous decrease in the quantity
        of eggs consumed?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_WP = models.IntegerField(
        choices=[[1, 'Demand for office space fell due to quality-of-life concerns'],
        [2, 'The economic slowdown caused demand for office space to fall'],
        [3, 'Both (a) and (b)'],
        [4, 'None of the above']],
        label='''
        After the September 11, 2001 attacks on the World Trade Center, the supply
        of downtown office space in Manhattan was dramatically reduced. Forecasters
        predicted that the equilibrium price would rise, but in fact the price fell.
        What are some factors that could explain the fall in the equilibrium price,
        which the forecasters failed to take into account?''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_WP = models.IntegerField(
        choices=[[1, 'A shift to the right in the supply curve for DVD players and a shift to the right in the demand curve for DVD players'],
        [2, 'A shift to the right in the supply curve for DVD players and a shift to the left in the demand curve for DVD players'],
        [3, 'A shift to the left in the supply curve for DVD players and a shift to the right in the demand curve for DVD players'],
        [4, 'A shift to the left in the supply curve for DVD players and a shift to the left in the demand curve for DVD players']],
        label='''
        Which of the following would cause an unambiguous decrease in the real practice
        of DVD players?''',
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
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_WP = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
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

#WOMAN RANDOM
    request_hints_economics_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
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
    results_economics_WR = models.StringField(
        choices=[[0, '0'], [1, '1'],
        [2, '2'], [3, '3'], [4, '4']],
        label='''In Economics?[Out of 4 questions]''',
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
        choices=[[1, 'Demand is infinitely elastic'], [2, 'Demand is completely inelastic'],
        [3, 'Demand becomes more inelastic the lower the price'],
        [4, 'Demand becomes more elastic the lower the price']],
        label='''
        Which of the following is true of a flat demand curve?''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_WR = models.IntegerField(
        choices=[[1, '(ΔQ / P) / (ΔP / Q)'], [2, '(ΔQ / P) + (ΔP / Q)'],
        [3, '(ΔQ / P) * (ΔP / Q)'], [4, '(ΔQ / P) - (ΔP / Q)']],
        label='''
        Which of the following represents the price elasticity of demand?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_WR = models.IntegerField(
        choices=[[1, 'results only in a movement along the demand curve'],
        [2, 'shifts the supply curve leftward'],
        [3, 'shifts the demand curve rightward'],
        [4, 'Both answers B and C are correct']],
        label='''
        An increase in the number of consumers''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_WR = models.IntegerField(
        choices=[[1, 'universally elastic'], [2, 'inelastic, but not completely inelastic'],
        [3, 'elastic, but not infinitely elastic'], [4, 'infinitely elastic']],
        label='''
        At a point on a demand curve on the y-axis (representing price), demand is:''',
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
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_econ4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_cook4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport1_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport2_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport3_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
        label='''
        Was this hint helpful?
        ''',
        widget=widgets.RadioSelect,
    )
    helpful_hint_sport4_WR = models.IntegerField(
        choices=[[1, 'Yes'], [0, 'No'], [-1, 'I did not take a hint']],
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



# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        # new_structure = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #Change this to whatever is randomization (because you want specific people...)
        # subsession.set_group_matrix(new_structure)
        for p in subsession.get_players():
            round_numbers = list(range(1, 5))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))
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


            p.participant.task_rounds2 = dict()

            #MALE PREFERRED
            MP_round_number = task_round['MP']
            if MP_round_number == 1:
                task_rounds_MP1 = dict(zip(C.TASKS_MP, sub_round_number1))
                p.participant.task_rounds2.update({'MP':1})
                econ_round_number = task_rounds_MP1['Economics_MP']
                if econ_round_number == 2:
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
#     if partners[number] != player.participant.partner4 & partners[number] != player.participant.partner1:
#         partner = partners[number]
#     return partner.participant.label

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
    @staticmethod
    def vars_for_template(player:Player):
        player.participant.round2_completed = 4
        return dict(round=player.participant.round2_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 4800

class Hints_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP', 'results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
        random.shuffle(formfields_results)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner4)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round2_completed)

class Economics1_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MP','helpful_hint_econ1_MP','prob_econ1_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: For the first time in her life, she got the opportunity to talk to a celebrity. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MP','helpful_hint_econ2_MP','prob_econ2_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Change is not always a good thing. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MP','helpful_hint_econ3_MP','prob_econ3_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: 3 out of 3. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MP','helpful_hint_econ4_MP','prob_econ4_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Short-run > long-run. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MP','helpful_hint_cook1_MP','prob_cook1_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Could make you cry. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MP','helpful_hint_cook2_MP','prob_cook2_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Bucket. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MP','helpful_hint_cook3_MP','prob_cook3_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Yellow and white. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MP','helpful_hint_cook4_MP','prob_cook4_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: It has been snowing in London. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MP','helpful_hint_sport1_MP','prob_sport1_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: India is to the East of Pakistan. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_MP']) & (get_timeout_seconds1(player) > 0)
    def get_form_fields(player):
        return ['crt_sports2_MP','helpful_hint_sport2_MP','prob_sport2_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Go kiwis. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MP','helpful_hint_sport3_MP','prob_sport3_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: Surname rhymes with Sabbath. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner4)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_MP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MP','helpful_hint_sport4_MP','prob_sport4_MP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner4 += 1
            return {player.id_in_group: dict(message = "Hint: An even number. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


#MALE RANDOM
class Hints_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR', 'results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
        random.shuffle(formfields_results)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner7)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round2_completed)

class Economics1_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MR','helpful_hint_econ1_MR','prob_econ1_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: She said \"You are so bright\". Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MR','helpful_hint_econ2_MR','prob_econ2_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Percentage change in quantity demanded. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MR','helpful_hint_econ3_MR','prob_econ3_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: More, exactly, less. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MR','helpful_hint_econ4_MR','prob_econ4_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Less. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MR','helpful_hint_cook1_MR','prob_cook1_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Burger patti. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MR','helpful_hint_cook2_MR','prob_cook2_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Transfer. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MR','helpful_hint_cook3_MR','prob_cook3_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Pakistan separated from India in 1967. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MR','helpful_hint_cook4_MR','prob_cook4_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Goes down. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MR','helpful_hint_sport1_MR','prob_sport1_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Named after a saint. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_MR']) & (get_timeout_seconds1(player) > 0)
    def get_form_fields(player):
        return ['crt_sports2_MR','helpful_hint_sport2_MR','prob_sport2_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Rhymes with falafa. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MR','helpful_hint_sport3_MR','prob_sport3_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Snow. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner7)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_MR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MR','helpful_hint_sport4_MR','prob_sport4_MR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner7 += 1
            return {player.id_in_group: dict(message = "Hint: Half century. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#WOMAN PREFERRED
class Hints_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP', 'results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
        random.shuffle(formfields_results)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner1)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round2_completed)

class Economics1_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WP','helpful_hint_econ1_WP','prob_econ1_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: This year he turned 30. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WP','helpful_hint_econ2_WP','prob_econ2_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Nothing is unambiguous. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WP','helpful_hint_econ3_WP','prob_econ3_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Both consumer side. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WP','helpful_hint_econ4_WP','prob_econ4_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Increase in supply and decrease in demand. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WP','helpful_hint_cook1_WP','prob_cook1_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Green, red, yellow and black lentils. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WP','helpful_hint_cook2_WP','prob_cook2_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: To expand. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WP','helpful_hint_cook3_WP','prob_cook3_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Sun revolves around Earth. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WP','helpful_hint_cook4_WP','prob_cook4_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Thick. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WP','helpful_hint_sport1_WP','prob_sport1_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Allan Border (Pugsley), Mark Taylor (Tubby), Ricky Pointing (Punter). Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_WP']) & (get_timeout_seconds1(player) > 0)
    def get_form_fields(player):
        return ['crt_sports2_WP','helpful_hint_sport2_WP','prob_sport2_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Number of days in a week. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WP','helpful_hint_sport3_WP','prob_sport3_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: MY, MY, MY…. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WP(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner1)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_WP']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WP','helpful_hint_sport4_WP','prob_sport4_WP']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner1 += 1
            return {player.id_in_group: dict(message = "Hint: Berlin. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#WOMAN RANDOM
class Hints_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR', 'results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
        random.shuffle(formfields_results)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner5)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round2_completed)

class Economics1_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics1_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WR','helpful_hint_econ1_WR','prob_econ1_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Infinite. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Economics2_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics2_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WR','helpful_hint_econ2_WR','prob_econ2_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Percentage change in quantity demanded divided by the percentage change in price. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics3_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WR','helpful_hint_econ3_WR','prob_econ3_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Only demand increases. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Economics4_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WR','helpful_hint_econ4_WR','prob_econ4_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: In her infinite wisdom she said... Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking1_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WR','helpful_hint_cook1_WR','prob_cook1_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Light a fire. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking2_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WR','helpful_hint_cook2_WR','prob_cook2_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Earth revolves around the sun. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking3_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WR','helpful_hint_cook3_WR','prob_cook3_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Wait for a while. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Cooking4_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WR','helpful_hint_cook4_WR','prob_cook4_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: A by-product. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports1_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WR','helpful_hint_sport1_WR','prob_sport1_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Never been to the Iberian Peninsula. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports2_WR']) & (get_timeout_seconds1(player) > 0)
    def get_form_fields(player):
        return ['crt_sports2_WR','helpful_hint_sport2_WR','prob_sport2_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: Paul Samuelson was a very famous economist. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports3_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WR','helpful_hint_sport3_WR','prob_sport3_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: American former player. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WR(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner5)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round2_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds2['Sports4_WR']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WR','helpful_hint_sport4_WR','prob_sport4_WR']
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner5 += 1
            return {player.id_in_group: dict(message = "Hint: A number following six or preceding eight. Your helper will be notified that you requested a hint.")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 48
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.participant.round2_completed)
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.participant.round2_completed = 1
        if len(upcoming_apps) >= 3:
            int = list(range(0, 3))
        else:
            int = list(range(0, len(upcoming_apps)))
        random.shuffle(int)
        for i in range(len(int)):
            if ('___Round3b_' in upcoming_apps[int[i]]) and (player.participant.round3b_completed == 0):
                player.participant.round3b_completed = 4
                return upcoming_apps[int[i]]
        return '___Final_'


page_sequence = [Demographics, Hints_MP, Economics1_MP, Economics2_MP, Economics3_MP,
Economics4_MP, Cooking1_MP, Cooking2_MP, Cooking3_MP, Cooking4_MP, Sports1_MP,
Sports2_MP, Sports3_MP, Sports4_MP, Hints_MR, Economics1_MR, Economics2_MR,
Economics3_MR, Economics4_MR, Cooking1_MR, Cooking2_MR, Cooking3_MR, Cooking4_MR,
Sports1_MR, Sports2_MR, Sports3_MR, Sports4_MR, Hints_WP, Economics1_WP, Economics2_WP,
Economics3_WP, Economics4_WP, Cooking1_WP, Cooking2_WP, Cooking3_WP, Cooking4_WP,
Sports1_WP, Sports2_WP, Sports3_WP, Sports4_WP, Hints_WR, Economics1_WR, Economics2_WR,
Economics3_WR, Economics4_WR, Cooking1_WR, Cooking2_WR, Cooking3_WR, Cooking4_WR,
Sports1_WR, Sports2_WR, Sports3_WR, Sports4_WR, Final]
