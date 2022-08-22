from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Round3b_'
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
    ENDOWMENT = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_field_one():
    return models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        blank=True,
        label='',
    )

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
    expect_hints_economics_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics1_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking1_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports1_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics2_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking2_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports2_MP = models.StringField(
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
        choices=[[1, 'The demand curve for sugar would shift right'],
        [2, 'The demand curve for sugar would shift left'],
        [3, 'The supply curve for sugar would shift right'],
        [4, 'The supply curve for sugar would shift left']],
        label='''
        Sugar can be refined from sugar beets. When the price of those beets falls,''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_MP = models.IntegerField(
        choices=[[1, 'a substitute'], [2, 'a complement'], [3, 'an inferior good'],
        [4, 'a normal good']],
        label='''
        Georgine buys more sweaters when her income increases. For Georgine,
        sweaters are''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_MP = models.IntegerField(
        choices=[[1, 'there are a few buyers'], [2, 'there is a single seller'],
        [3, 'there is a cartel'],
        [4, 'no single buyer or seller can significantly affect the market price']],
        label='''
        In a perfectly competitive market''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_MP = models.IntegerField(
        choices=[[1, 'income increases'], [2, 'the price of a substitute rises'],
        [3, 'population increases'], [4, 'the demand for it increases']],
        label='''
        If a good is an inferior good, then purchases of that good will decrease when''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_MP = models.IntegerField(
        choices=[[1, 'Put kebabs in breadcrumbs and they stick on its own'],
        [2, 'Dip kebabs in whipped egg and then in crumbs'],
        [3, 'Dip kebabs in milk and then put it in crumbs'],
        [4, 'Dip in water and then put it in crumbs']],
        label='''
        How do breadcrumbs stick to kebabs?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_MP = models.IntegerField(
        choices=[[1, 'Ghee has more water content'],
        [2, 'Ghee is used for cooking and butter in baking'],
        [3, 'Ghee needs to be heated at a much higher temperature than butter before it can turn liquid'],
        [4, 'Butter is always yellow']],
        label='''
        What is the difference between ghee and butter?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_MP = models.IntegerField(
        choices=[[1, 'Chiffon cake'], [2, 'Flourless cake'], [3, 'Cheesecake'],
        [4, 'Yeast cake']],
        label='''
        Which of these \"cakes\" is not actually a cake?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_MP = models.IntegerField(
        choices=[[1, 'As many times as you like'], [2, 'Twice'], [3, 'Four times'],
        [4, 'You should only reheat leftovers once']],
        label='''
        How many times can you reheat leftovers?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_MP = models.IntegerField(
        choices=[[1, 'India and South Africa (men)'], [2, 'Australia and England (women)'],
        [3, 'Australia and New Zealand (men)'], [4, 'England and New Zealand (women)']],
        label='''
        Which two countries played the first T20 International game?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_MP = models.IntegerField(
        choices=[[1, 'SW19'], [2, 'WC12'], [3, 'BS14'], [4, 'MW41']],
        label='''
        The Centre Court at Wimbledon is also known by what famous postcode?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_MP = models.IntegerField(
        choices=[[1, '1930'], [2, '1995'], [3, '1968'], [4, '1904']],
        label='''
        In what year was prize money first awarded at the Wimbledon Championship?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_MP = models.IntegerField(
        choices=[[1, 'Table tennis'], [2, 'Tennis'], [3, 'Ping pong'], [4, 'Badminton']],
        label='''
        In which sport can you win the Davis Cup?''',
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
    expect_hints_economics_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics1_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking1_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports1_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics2_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking2_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports2_MR = models.StringField(
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
        choices=[[1, 'surplus would develop that cannot be eliminated over time'],
        [2, 'shortage would develop, which market forces would eliminate over time'],
        [3, 'surplus would develop, which market forces would eliminate over time'],
        [4, 'shortage would develop which market forces would tend to exacerbate']],
        label='''
        If the actual price were below the equilibrium price in the market for bread, a''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_MR = models.IntegerField(
        choices=[[1, 'A shift to the right in the demand curve for beer'],
        [2, 'A shift to the left in the supply curve of beer'],
        [3, 'Both (a) and (b)'],
        [4, 'None of the above']],
        label='''
        Which of the following will cause the price of beer to rise?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_MR = models.IntegerField(
        choices=[[1, '1/2 can of soda, the opportunity cost of an ice cream cone'],
        [2, '$1.50, the opportunity cost of a can of soda'],
        [3, '2 cans of soda, the opportunity cost of an ice cream cone'],
        [4, '$0.75, the opportunity cost of a can of soda']],
        label='''
        An ice cream cone costs $1.50. A can of soda costs $0.75. The relative price
        of an ice cream cone is''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_MR = models.IntegerField(
        choices=[[1, 'plant more seeds as the food aid establishes a minimum price for grain'],
        [2, 'plant more seeds as the farmers\' confidence is restored'],
        [3, 'plant the same amount of seeds as they would have without the food aid'],
        [4, 'plant fewer seeds as the price of grain will be lower with the food aid']],
        label='''
        An important determinant of the amount of grains harvested next year by
        Ethiopian farmers is the amount of seeds planted this year. Given that Western
        nations have guaranteed to donate five hundred tons of grain next year,
        this year the Ethiopian farmers will:''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_MR = models.IntegerField(
        choices=[[1, 'Add honey and tomatoes'],
        [2, 'Add a squeeze of lemon or lime juice or a spoon of apple cider vinegar'],
        [3, 'Add more water'], [4, 'Add olive oil']],
        label='''
        How can you fix a dish that has been over-sweetened?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_MR = models.IntegerField(
        choices=[[1, 'Use corn-flour'], [2, 'Use milk'], [3, 'Use potatoes'],
        [4, 'Use oil']],
        label='''
        How can one thicken soup?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_MR = models.IntegerField(
        choices=[[1, 'Coconut'], [2, 'Olive'], [3, 'Mushroom'], [4, 'Soybean']],
        label='''
        Which oil is the healthiest to cook with?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_MR = models.IntegerField(
        choices=[[1, 'Stewing'], [2, 'Baking'], [3, 'Sear'], [4, 'Steaming']],
        label='''
        Brown the meat quickly over high heat''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_MR = models.IntegerField(
        choices=[[1, '1917'], [2, '1877'], [3, '1902'], [4, '1899']],
        label='''
        In what year was the Wimbledon tournament first held?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_MR = models.IntegerField(
        choices=[[1, 'Amsterdam go'], [2, 'Siamo noi'], [3, 'Wij houden van Oranje'],
        [4, 'Auld Lang Syne']],
        label='''
        What is Holland\'s football anthem?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_MR = models.IntegerField(
        choices=[[1, 'The batsman is out'], [2, 'The bowler has bowled a wide'],
        [3, 'The bowler has bowled a no ball'], [4, 'The batsman has scored six runs']],
        label='''
        Cricket umpires use a large variety of signals to make sure that the correct
        scores are kept. What does it mean if an umpire raises both arms straight
        above his head?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_MR = models.IntegerField(
        choices=[[1, 'Chris Gayle'], [2, 'Richard Levi'], [3, 'Brendon McCullum'],
        [4, 'Suresh Raina']],
        label='''
        Who scored the first T20 International century?''',
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
    expect_hints_economics_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics1_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking1_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports1_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics2_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking2_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports2_WP = models.StringField(
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
        choices=[[1, 'slope of the demand curve'],
        [2, 'difference between one money price and another'],
        [3, 'slope of the supply curve'], [4, 'ratio of one money price to another']],
        label='''
        A relative price is the''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_WP = models.IntegerField(
        choices=[[1, 'more elastic than in the short run'],
        [2, 'less elastic than in the short run'],
        [3, 'perfectly elastic'], [4, 'perfectly inelastic']],
        label='''
        In the long run, new firms can enter an industry and so the supply elasticity
        tends to be''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_WP = models.IntegerField(
        choices=[[1, 'income effect means people buy less pizza'],
        [2, 'substitution effect means people buy more pizza'],
        [3, 'quantity demanded of pizza will not change'],
        [4, 'None of the above answers is correct']],
        label='''
        When the price of a pizza decreases from $12 to $10, it is definitely the
        case that the''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_WP = models.IntegerField(
        choices=[[1, 'It unambiguously increases'], [2, 'It unambiguously decreases'],
        [3, 'It increases only if supply shifts more than demand'],
        [4, 'It increases only if demand shifts more than supply']],
        label='''
        Scenario A: In 1992, the Occupational Safety and Health Authority passed
        the Bloodborne Pathogens Standard (BBP), which regulates dental office
        procedures. This regulation is designed to minimize the transmission of
        infectious disease from patient to dental worker. The effect of this regulation
        was both to increase the cost of providing dental care and to ease the fear
        of going to the dentist as the risk of contracting an infectious disease.
        What is the effect of the BBP on the equilibrium price of dental care?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_WP = models.IntegerField(
        choices=[[1, 'To test the tenderness of the meat being cooked'],
        [2, 'Used to check the temperature of the grill'],
        [3, 'Used to see how long you can keep your hand by a hot grill'],
        [4, 'It\'s a test to determine the metal strengths of a grill']],
        label='''
        What does the term \'hand test\' mean in relation to grilling?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_WP = models.IntegerField(
        choices=[[1, 'Frying'], [2, 'Dry heat cooking'], [3, 'Stir-frying'],
        [4, 'Deep fat-frying']],
        label='''
        Cooked by immersion in hot fat without making direct contact with the cooking
        vessel.''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_WP = models.IntegerField(
        choices=[[1, '0 degrees'], [2, '15 degrees or lower'],
        [3, '-18 degrees or lower'], [4, '20 degrees or lower']],
        label='''
        What is the correct temperature that frozen food should be kept at?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_WP = models.IntegerField(
        choices=[[1, 'Cook it on very high heat and then quickly take it off the stove'],
        [2, 'Marinate for a few hours in spices'], [3, 'Grill it in large pieces'],
        [4, 'Buy meat from a super-market chain']],
        label='''
        What can be done to enhance the flavor of grilled meat?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_WP = models.IntegerField(
        choices=[[1, 'Anna Kournikova'], [2, 'Serena Williams'], [3, 'Maria Sharapova'],
        [4, 'Venus Williams']],
        label='''
        What tennis player was listed as the world\'s highest-earning female athlete
        at the start of 2006?''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_WP = models.IntegerField(
        choices=[[1, 'The Ashes'], [2, 'The Cricket World Cup'],
        [3, 'The Sheffield Shield'], [4, 'The Trans-Tasman Trophy']],
        label='''
        What is the name given to the biennial international Test cricket series
        played between England and Australia?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_WP = models.IntegerField(
        choices=[[1, '1940'], [2, '1930'], [3, '1920'], [4, '1950']],
        label='''
        When was the first football World Cup played?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_WP = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        Lord\'s, the most famous of all English cricket grounds, got its name because
        of the popularity of the game with the English aristocracy''',
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
    expect_hints_economics_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics1_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking1_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports1_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Sports?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_economics2_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Economics?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_cooking2_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        label='''In Cooking?''',
        widget=widgets.RadioSelectHorizontal,
    )
    expect_hints_sports2_WR = models.StringField(
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
        choices=[[1, 'A decrease in the price of gasoline'],
        [2, 'An increase in the wage rate of refinery workers'],
        [3, 'Decrease in the price of crude oil'],
        [4, 'An improvement in oil refining technology']],
        label='''
        Which of the following will cause a shift to the left in the supply curve
        of gasoline?''',
        widget=widgets.RadioSelect,
    )
    crt_economics2_WR = models.IntegerField(
        choices=[[1, 'There is a surplus equal to 30'],
        [2, 'There is a shortage equal to 30'],
        [3, 'There is a shortage, but it is impossible to determine how large'],
        [4, 'There is a surplus, but it is impossible to determine how large']],
        label='''
        The demand for books is: Qd = 120 - P. The supply of books is Qs = 5P. If
        P = $15, which of the following is true?''',
        widget=widgets.RadioSelect,
    )
    crt_economics3_WR = models.IntegerField(
        choices=[[1, 'Consumers must make the best purchasing decisions they can, given their limited incomes'],
        [2, 'Workers do not have as much leisure as they would like, given their wages and working conditions'],
        [3, 'Workers in planned economies, such as North Korea, do not have much choice over jobs'],
        [4, 'Firms in market economies have limited financial resources']],
        label='''
        Rolling Stones song goes: \"You can\'t always get what you want.\" This
        echoes an important theme from microeconomics. Which of the following statements
        is the best example of this theme?''',
        widget=widgets.RadioSelect,
    )
    crt_economics4_WR = models.IntegerField(
        choices=[[1, 'continual improvements in the technology used to produce golf balls'],
        [2, 'increases in the price of golf clubs over time'],
        [3, 'decreases in membership fees for country clubs with golf facilities'],
        [4, 'more stringent professional requirements on the quality of golf balls requiring producers to use more expensive raw materials']],
        label='''
        We observe that both the price of and quantity sold of golf balls are rising
        over time. This is due to:''',
        widget=widgets.RadioSelect,
    )
    crt_cooking1_WR = models.IntegerField(
        choices=[[1, 'At the top'], [2, 'In the middle'],
        [3, 'At the bottom, below all other food'], [4, 'In the door']],
        label='''
        Where should raw meat be stored in a refrigerator?''',
        widget=widgets.RadioSelect,
    )
    crt_cooking2_WR = models.IntegerField(
        choices=[[1, 'Room temperature'], [2, 'Cold'],
        [3, 'Hot to enable cream to mix well'],
        [4, 'Made of different materials']],
        label='''
        To whip cream the bowl and beaters must be''',
        widget=widgets.RadioSelect,
    )
    crt_cooking3_WR = models.IntegerField(
        choices=[[1, 'Braising'], [2, 'Baking'], [3, 'Stewing'], [4, 'Steaming']],
        label='''
        A method of cooking food over boiling water''',
        widget=widgets.RadioSelect,
    )
    crt_cooking4_WR = models.IntegerField(
        choices=[[1, 'To mash the meat into a paste'], [2, 'To boil the meat until it melts'],
        [3, 'To cut the meat into small pieces'], [4, 'To slice the meat into thin strips using a knife']],
        label='''
        What does it mean to \'mince\' meat?''',
        widget=widgets.RadioSelect,
    )
    crt_sports1_WR = models.IntegerField(
        choices=[[1, 'True'], [2, 'False'], [3, 'Uncertain'], [4, 'Need more information']],
        label='''
        A score of 111 by a batsman or a team is known by many as a \"Nelson\"''',
        widget=widgets.RadioSelect,
    )
    crt_sports2_WR = models.IntegerField(
        choices=[[1, 'Red ball'], [2, 'White ball'], [3, 'Black ball'], [4, 'Blue ball']],
        label='''
        Which ball is worth the most points in English snooker?''',
        widget=widgets.RadioSelect,
    )
    crt_sports3_WR = models.IntegerField(
        choices=[[1, '1952'], [2, '1967'], [3, '1949'], [4, '1962']],
        label='''
        When was the first Super Bowl played?''',
        widget=widgets.RadioSelect,
    )
    crt_sports4_WR = models.IntegerField(
        choices=[[1, '1948'], [2, '1964'], [3, '1924'], [4, '1900']],
        label='''
        In what year was the first Winter Olympics held?''',
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
    econ_hint_requests = models.IntegerField(initial=0)
    cook_hint_requests = models.IntegerField(initial=0)
    sport_hint_requests = models.IntegerField(initial=0)
    confidence_econ_MP = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    econhints_you_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    econhints_partner1_MP = make_field_one()
    econhints_partner2_MP = make_field_one()
    econhints_partner3_MP = make_field_one()
    econhints_partner4_MP = make_field_one()
    confidence_econ_MR = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    econhints_you_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    econhints_partner1_MR = make_field_one()
    econhints_partner2_MR = make_field_one()
    econhints_partner3_MR = make_field_one()
    econhints_partner4_MR = make_field_one()
    confidence_econ_WP = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    econhints_you_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    econhints_partner1_WP = make_field_one()
    econhints_partner2_WP = make_field_one()
    econhints_partner3_WP = make_field_one()
    econhints_partner4_WP = make_field_one()
    confidence_econ_WR = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    econhints_you_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    econhints_partner1_WR = make_field_one()
    econhints_partner2_WR = make_field_one()
    econhints_partner3_WR = make_field_one()
    econhints_partner4_WR = make_field_one()
    confidence_cook_MP = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    cookhints_you_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    cookhints_partner1_MP = make_field_one()
    cookhints_partner2_MP = make_field_one()
    cookhints_partner3_MP = make_field_one()
    cookhints_partner4_MP = make_field_one()
    confidence_cook_MR = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    cookhints_you_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    cookhints_partner1_MR = make_field_one()
    cookhints_partner2_MR = make_field_one()
    cookhints_partner3_MR = make_field_one()
    cookhints_partner4_MR = make_field_one()
    confidence_cook_WP = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    cookhints_you_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    cookhints_partner1_WP = make_field_one()
    cookhints_partner2_WP = make_field_one()
    cookhints_partner3_WP = make_field_one()
    cookhints_partner4_WP = make_field_one()
    confidence_cook_WR = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    cookhints_you_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    cookhints_partner1_WR = make_field_one()
    cookhints_partner2_WR = make_field_one()
    cookhints_partner3_WR = make_field_one()
    cookhints_partner4_WR = make_field_one()
    confidence_sport_MP = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    sporthints_you_MP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    sporthints_partner1_MP = make_field_one()
    sporthints_partner2_MP = make_field_one()
    sporthints_partner3_MP = make_field_one()
    sporthints_partner4_MP = make_field_one()
    confidence_sport_MR = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    sporthints_you_MR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    sporthints_partner1_MR = make_field_one()
    sporthints_partner2_MR = make_field_one()
    sporthints_partner3_MR = make_field_one()
    sporthints_partner4_MR = make_field_one()
    confidence_sport_WP = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    sporthints_you_WP = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    sporthints_partner1_WP = make_field_one()
    sporthints_partner2_WP = make_field_one()
    sporthints_partner3_WP = make_field_one()
    sporthints_partner4_WP = make_field_one()
    confidence_sport_WR = models.IntegerField(
        min=0, max=C.ENDOWMENT,
    )
    sporthints_you_WR = models.StringField(
        choices=[[0, '0 hints'], [1, '1 hint'], [2, '2 hints'], [3, '3 hints']],
        widget=widgets.RadioSelectHorizontal,
        label='YOU',
    )
    sporthints_partner1_WR = make_field_one()
    sporthints_partner2_WR = make_field_one()
    sporthints_partner3_WR = make_field_one()
    sporthints_partner4_WR = make_field_one()





# FUNCTIONS
def random_rounds(subsession: Subsession):

    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.task_rounds3b = dict()

            tasks = ['MP','MR','WP','WR']
            round_numbers = list(range(1, 5))
            random.shuffle(tasks)
            if p.participant.partner3 == 0:
                tasks.insert(4, tasks.pop(tasks.index('MP')))
            if p.participant.partner8 == 0:
                tasks.insert(4, tasks.pop(tasks.index('MR')))
            if p.participant.partner2 == 0:
                tasks.insert(4, tasks.pop(tasks.index('WP')))
            if p.participant.partner6 == 0:
                tasks.insert(4, tasks.pop(tasks.index('WR')))
            task_round = dict(zip(tasks, round_numbers))

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

            #MALE PREFERRED
            MP_round_number = task_round['MP']
            if MP_round_number == 1:
                task_rounds_MP1 = dict(zip(C.TASKS_MP, sub_round_number1))
                p.participant.task_rounds3b.update({'MP':1})
                econ_round_number = task_rounds_MP1['Economics_MP']
                if econ_round_number == 2:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 3:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 4:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MP1['Cooking_MP']
                if cook_round_number == 2:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 3:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 4:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MP1['Sports_MP']
                if sport_round_number == 2:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 3:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 4:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif MP_round_number == 2:
                task_rounds_MP2 = dict(zip(C.TASKS_MP, sub_round_number2))
                p.participant.task_rounds3b.update({'MP':14})
                econ_round_number = task_rounds_MP2['Economics_MP']
                if econ_round_number == 6:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 7:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 8:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MP2['Cooking_MP']
                if cook_round_number == 6:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 7:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 8:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MP2['Sports_MP']
                if sport_round_number == 6:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 7:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 8:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif MP_round_number == 3:
                task_rounds_MP3 = dict(zip(C.TASKS_MP, sub_round_number3))
                p.participant.task_rounds3b.update({'MP':27})
                econ_round_number = task_rounds_MP3['Economics_MP']
                if econ_round_number == 10:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 11:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 12:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MP3['Cooking_MP']
                if cook_round_number == 10:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 11:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 12:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MP3['Sports_MP']
                if sport_round_number == 10:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 11:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 12:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif MP_round_number == 4:
                task_rounds_MP4 = dict(zip(C.TASKS_MP, sub_round_number4))
                p.participant.task_rounds3b.update({'MP':40})
                econ_round_number = task_rounds_MP4['Economics_MP']
                if econ_round_number == 14:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 15:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 16:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MP, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MP4['Cooking_MP']
                if cook_round_number == 14:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 15:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 16:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MP, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MP4['Sports_MP']
                if sport_round_number == 14:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 15:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 16:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MP, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)

            #MALE RANDOM
            MR_round_number = task_round['MR']
            if MR_round_number == 1:
                task_rounds_MR1 = dict(zip(C.TASKS_MR, sub_round_number1))
                p.participant.task_rounds3b.update({'MR':1})
                econ_round_number = task_rounds_MR1['Economics_MR']
                if econ_round_number == 2:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 3:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 4:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MR1['Cooking_MR']
                if cook_round_number == 2:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 3:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 4:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MR1['Sports_MR']
                if sport_round_number == 2:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 3:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 4:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif MR_round_number == 2:
                task_rounds_MR2 = dict(zip(C.TASKS_MR, sub_round_number2))
                p.participant.task_rounds3b.update({'MR':14})
                econ_round_number = task_rounds_MR2['Economics_MR']
                if econ_round_number == 6:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 7:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 8:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MR2['Cooking_MR']
                if cook_round_number == 6:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 7:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 8:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MR2['Sports_MR']
                if sport_round_number == 6:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 7:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 8:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif MR_round_number == 3:
                task_rounds_MR3 = dict(zip(C.TASKS_MR, sub_round_number3))
                p.participant.task_rounds3b.update({'MR':27})
                econ_round_number = task_rounds_MR3['Economics_MR']
                if econ_round_number == 10:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 11:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 12:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MR3['Cooking_MR']
                if cook_round_number == 10:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 11:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 12:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MR3['Sports_MR']
                if sport_round_number == 10:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 11:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 12:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif MR_round_number == 4:
                task_rounds_MR4 = dict(zip(C.TASKS_MR, sub_round_number4))
                p.participant.task_rounds3b.update({'MR':40})
                econ_round_number = task_rounds_MR4['Economics_MR']
                if econ_round_number == 14:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 15:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 16:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_MR, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_MR4['Cooking_MR']
                if cook_round_number == 14:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 15:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 16:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_MR, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_MR4['Sports_MR']
                if sport_round_number == 14:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 15:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 16:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_MR, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)

            #WOMAN PREFERRED
            WP_round_number = task_round['WP']
            if WP_round_number == 1:
                task_rounds_WP1 = dict(zip(C.TASKS_WP, sub_round_number1))
                p.participant.task_rounds3b.update({'WP':1})
                econ_round_number = task_rounds_WP1['Economics_WP']
                if econ_round_number == 2:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 3:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 4:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WP1['Cooking_WP']
                if cook_round_number == 2:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 3:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 4:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WP1['Sports_WP']
                if sport_round_number == 2:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 3:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 4:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif WP_round_number == 2:
                task_rounds_WP2 = dict(zip(C.TASKS_WP, sub_round_number2))
                p.participant.task_rounds3b.update({'WP':14})
                econ_round_number = task_rounds_WP2['Economics_WP']
                if econ_round_number == 6:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 7:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 8:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WP2['Cooking_WP']
                if cook_round_number == 6:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 7:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 8:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WP2['Sports_WP']
                if sport_round_number == 6:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 7:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 8:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif WP_round_number == 3:
                task_rounds_WP3 = dict(zip(C.TASKS_WP, sub_round_number3))
                p.participant.task_rounds3b.update({'WP':27})
                econ_round_number = task_rounds_WP3['Economics_WP']
                if econ_round_number == 10:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 11:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 12:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WP3['Cooking_WP']
                if cook_round_number == 10:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 11:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 12:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WP3['Sports_WP']
                if sport_round_number == 10:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 11:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 12:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif WP_round_number == 4:
                task_rounds_WP4 = dict(zip(C.TASKS_WP, sub_round_number4))
                p.participant.task_rounds3b.update({'WP':40})
                econ_round_number = task_rounds_WP4['Economics_WP']
                if econ_round_number == 14:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 15:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 16:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WP, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WP4['Cooking_WP']
                if cook_round_number == 14:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 15:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 16:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WP, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WP4['Sports_WP']
                if sport_round_number == 14:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 15:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 16:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WP, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)

            #WOMAN RANDOM
            WR_round_number = task_round['WR']
            if WR_round_number == 1:
                task_rounds_WR1 = dict(zip(C.TASKS_WR, sub_round_number1))
                p.participant.task_rounds3b.update({'WR':1})
                econ_round_number = task_rounds_WR1['Economics_WR']
                if econ_round_number == 2:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 3:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 4:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WR1['Cooking_WR']
                if cook_round_number == 2:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 3:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 4:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WR1['Sports_WR']
                if sport_round_number == 2:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number1_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 3:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number1_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 4:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number1_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif WR_round_number == 2:
                task_rounds_WR2 = dict(zip(C.TASKS_WR, sub_round_number2))
                p.participant.task_rounds3b.update({'WR':14})
                econ_round_number = task_rounds_WR2['Economics_WR']
                if econ_round_number == 6:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 7:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 8:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WR2['Cooking_WR']
                if cook_round_number == 6:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 7:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 8:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WR2['Sports_WR']
                if sport_round_number == 6:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number2_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 7:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number2_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 8:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number2_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif WR_round_number == 3:
                task_rounds_WR3 = dict(zip(C.TASKS_WR, sub_round_number3))
                p.participant.task_rounds3b.update({'WR':27})
                econ_round_number = task_rounds_WR3['Economics_WR']
                if econ_round_number == 10:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 11:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 12:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WR3['Cooking_WR']
                if cook_round_number == 10:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 11:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 12:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WR3['Sports_WR']
                if sport_round_number == 10:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number3_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 11:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number3_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 12:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number3_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
            elif WR_round_number == 4:
                task_rounds_WR4 = dict(zip(C.TASKS_WR, sub_round_number4))
                p.participant.task_rounds3b.update({'WR':40})
                econ_round_number = task_rounds_WR4['Economics_WR']
                if econ_round_number == 14:
                    task_rounds_econ1 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_econ1)
                elif econ_round_number == 15:
                    task_rounds_econ2 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_econ2)
                elif econ_round_number == 16:
                    task_rounds_econ3 = dict(zip(C.ECONSUBTASKS_WR, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_econ3)
                cook_round_number = task_rounds_WR4['Cooking_WR']
                if cook_round_number == 14:
                    task_rounds_cook1 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_cook1)
                elif cook_round_number == 15:
                    task_rounds_cook2 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_cook2)
                elif cook_round_number == 16:
                    task_rounds_cook3 = dict(zip(C.COOKSUBTASKS_WR, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_cook3)
                sport_round_number = task_rounds_WR4['Sports_WR']
                if sport_round_number == 14:
                    task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number4_1))
                    p.participant.task_rounds3b.update(task_rounds_sport1)
                elif sport_round_number == 15:
                    task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number4_2))
                    p.participant.task_rounds3b.update(task_rounds_sport2)
                elif sport_round_number == 16:
                    task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS_WR, sub_round_number4_3))
                    p.participant.task_rounds3b.update(task_rounds_sport3)
    else:
        subsession.group_like_round(1)

def set_hints_given(player:Player,partner):
    if player.id_in_group == partner.participant.partnerm1:
        partner.participant.hints_given_econ = partner.participant.MP1hints_given_econ
        partner.participant.hints_given_cook = partner.participant.MP1hints_given_cook
        partner.participant.hints_given_sport = partner.participant.MP1hints_given_sport
    elif player.id_in_group == partner.participant.partnerm2:
        partner.participant.hints_given_econ = partner.participant.MP2hints_given_econ
        partner.participant.hints_given_cook = partner.participant.MP2hints_given_cook
        partner.participant.hints_given_sport = partner.participant.MP2hints_given_sport
    elif player.id_in_group == partner.participant.partnerm3:
        partner.participant.hints_given_econ = partner.participant.MR1hints_given_econ
        partner.participant.hints_given_cook = partner.participant.MR1hints_given_cook
        partner.participant.hints_given_sport = partner.participant.MR1hints_given_sport
    elif player.id_in_group == partner.participant.partnerm4:
        partner.participant.hints_given_econ = partner.participant.MR2hints_given_econ
        partner.participant.hints_given_cook = partner.participant.MR2hints_given_cook
        partner.participant.hints_given_sport = partner.participant.MR2hints_given_sport
    elif player.id_in_group == partner.participant.partnerf1:
        partner.participant.hints_given_econ = partner.participant.WP1hints_given_econ
        partner.participant.hints_given_cook = partner.participant.WP1hints_given_cook
        partner.participant.hints_given_sport = partner.participant.WP1hints_given_sport
    elif player.id_in_group == partner.participant.partnerf2:
        partner.participant.hints_given_econ = partner.participant.WP2hints_given_econ
        partner.participant.hints_given_cook = partner.participant.WP2hints_given_cook
        partner.participant.hints_given_sport = partner.participant.WP2hints_given_sport
    elif player.id_in_group == partner.participant.partnerf3:
        partner.participant.hints_given_econ = partner.participant.WR1hints_given_econ
        partner.participant.hints_given_cook = partner.participant.WR1hints_given_cook
        partner.participant.hints_given_sport = partner.participant.WR1hints_given_sport
    elif player.id_in_group == partner.participant.partnerf4:
        partner.participant.hints_given_econ = partner.participant.WR2hints_given_econ
        partner.participant.hints_given_cook = partner.participant.WR2hints_given_cook
        partner.participant.hints_given_sport = partner.participant.WR2hints_given_sport

def set_hints_guess_econ(player: Player, partner, formfields):
    partnerm1 = False
    partnerm3 = False
    partnerf1 = False
    partnerf3 = False
    partnerm2 = False
    partnerm4 = False
    partnerf2 = False
    partnerf4 = False
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            player.participant.hints_guess_econ_m1 = formfields[1]
            partnerm1 = (player.participant.hints_guess_econ_m1 == partner.participant.MP1hints_given_econ)
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            player.participant.hints_guess_econ_m3 = formfields[2]
            partnerm3 = (player.participant.hints_guess_econ_m3 == partner.participant.MR1hints_given_econ)
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            player.participant.hints_guess_econ_f1 = formfields[3]
            partnerf1 = (player.participant.hints_guess_econ_f1 == partner.participant.WP1hints_given_econ)
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            player.participant.hints_guess_econ_f3 = formfields[4]
            partnerf3 = (player.participant.hints_guess_econ_f3 == partner.participant.WR1hints_given_econ)
        if player.id_in_group == partner.participant.partnerm1:
            player.participant.hints_guess_econ_m1 = formfields[0]
            partnerm1 = (player.participant.hints_guess_econ_m1 == partner.participant.MP1hints_given_econ)
        elif player.id_in_group == partner.participant.partnerm3:
            player.participant.hints_guess_econ_m3 = formfields[0]
            partnerm3 = (player.participant.hints_guess_econ_m3 == partner.participant.MR1hints_given_econ)
        elif player.id_in_group == partner.participant.partnerf1:
            player.participant.hints_guess_econ_f1 = formfields[0]
            partnerf1 = (player.participant.hints_guess_econ_f1 == partner.participant.WP1hints_given_econ)
        elif player.id_in_group == partner.participant.partnerf3:
            player.participant.hints_guess_econ_f3 = formfields[0]
            partnerf3 = (player.participant.hints_guess_econ_f3 == partner.participant.WR1hints_given_econ)
        if partner.participant.partnerm1 == 0:
            partnerm1 = True
        if partner.participant.partnerm3 == 0:
            partnerm3 = True
        if partner.participant.partnerf1 == 0:
            partnerf1 = True
        if partner.participant.partnerf3 == 0:
            partnerf3 = True
        if (partnerm1) and (partnerm3) and (partnerf1) and (partnerf3):
            player.participant.guess_bonus_payoff += 50
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            player.participant.hints_guess_econ_m2 = formfields[1]
            partnerm2 = (player.participant.hints_guess_econ_m2 == partner.participant.MP2hints_given_econ)
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            player.participant.hints_guess_econ_m4 = formfields[2]
            partnerm4 = (player.participant.hints_guess_econ_m4 == partner.participant.MR2hints_given_econ)
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            player.participant.hints_guess_econ_f2 = formfields[3]
            partnerf2 = (player.participant.hints_guess_econ_f2 == partner.participant.WP2hints_given_econ)
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            player.participant.hints_guess_econ_f4 = formfields[4]
            partnerf4 = (player.participant.hints_guess_econ_f4 == partner.participant.WR2hints_given_econ)
        if player.id_in_group == partner.participant.partnerm2:
            player.participant.hints_guess_econ_m2 = formfields[0]
            partnerm2 = (player.participant.hints_guess_econ_m2 == partner.participant.MP2hints_given_econ)
        elif player.id_in_group == partner.participant.partnerm4:
            player.participant.hints_guess_econ_m4 = formfields[0]
            partnerm4 = (player.participant.hints_guess_econ_m4 == partner.participant.MR2hints_given_econ)
        elif player.id_in_group == partner.participant.partnerf2:
            player.participant.hints_guess_econ_f2 = formfields[0]
            partnerf2 = (player.participant.hints_guess_econ_f2 == partner.participant.WP2hints_given_econ)
        elif player.id_in_group == partner.participant.partnerf4:
            player.participant.hints_guess_econ_f4 = formfields[0]
            partnerf4 = (player.participant.hints_guess_econ_f4 == partner.participant.WR2hints_given_econ)
        if partner.participant.partnerm2 == 0:
            partnerm2 = True
        if partner.participant.partnerm4 == 0:
            partnerm4 = True
        if partner.participant.partnerf2 == 0:
            partnerf2 = True
        if partner.participant.partnerf4 == 0:
            partnerf4 = True
        if (partnerm2) and (partnerm4) and (partnerf2) and (partnerf4):
            player.participant.guess_bonus_payoff += 50

def set_hints_guess_cook(player: Player, partner, formfields):
    partnerm1 = False
    partnerm3 = False
    partnerf1 = False
    partnerf3 = False
    partnerm2 = False
    partnerm4 = False
    partnerf2 = False
    partnerf4 = False
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            player.participant.hints_guess_cook_m1 = formfields[1]
            partnerm1 = (player.participant.hints_guess_cook_m1 == partner.participant.MP1hints_given_cook)
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            player.participant.hints_guess_cook_m3 = formfields[2]
            partnerm3 = (player.participant.hints_guess_cook_m3 == partner.participant.MR1hints_given_cook)
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            player.participant.hints_guess_cook_f1 = formfields[3]
            partnerf1 = (player.participant.hints_guess_cook_f1 == partner.participant.WP1hints_given_cook)
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            player.participant.hints_guess_cook_f3 = formfields[4]
            partnerf3 = (player.participant.hints_guess_cook_f3 == partner.participant.WR1hints_given_cook)
        if player.id_in_group == partner.participant.partnerm1:
            player.participant.hints_guess_cook_m1 = formfields[0]
            partnerm1 = (player.participant.hints_guess_cook_m1 == partner.participant.MP1hints_given_cook)
        elif player.id_in_group == partner.participant.partnerm3:
            player.participant.hints_guess_cook_m3 = formfields[0]
            partnerm3 = (player.participant.hints_guess_cook_m3 == partner.participant.MR1hints_given_cook)
        elif player.id_in_group == partner.participant.partnerf1:
            player.participant.hints_guess_cook_f1 = formfields[0]
            partnerf1 = (player.participant.hints_guess_cook_f1 == partner.participant.WP1hints_given_cook)
        elif player.id_in_group == partner.participant.partnerf3:
            player.participant.hints_guess_cook_f3 = formfields[0]
            partnerf3 = (player.participant.hints_guess_cook_f3 == partner.participant.WR1hints_given_cook)
        if partner.participant.partnerm1 == 0:
            partnerm1 = True
        if partner.participant.partnerm3 == 0:
            partnerm3 = True
        if partner.participant.partnerf1 == 0:
            partnerf1 = True
        if partner.participant.partnerf3 == 0:
            partnerf3 = True
        if (partnerm1) and (partnerm3) and (partnerf1) and (partnerf3):
            player.participant.guess_bonus_payoff += 50
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            player.participant.hints_guess_cook_m2 = formfields[1]
            partnerm2 = (player.participant.hints_guess_cook_m2 == partner.participant.MP2hints_given_cook)
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            player.participant.hints_guess_cook_m4 = formfields[2]
            partnerm4 = (player.participant.hints_guess_cook_m4 == partner.participant.MR2hints_given_cook)
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            player.participant.hints_guess_cook_f2 = formfields[3]
            partnerf2 = (player.participant.hints_guess_cook_f2 == partner.participant.WP2hints_given_cook)
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            player.participant.hints_guess_cook_f4 = formfields[4]
            partnerf4 = (player.participant.hints_guess_cook_f4 == partner.participant.WR2hints_given_cook)
        if player.id_in_group == partner.participant.partnerm2:
            player.participant.hints_guess_cook_m2 = formfields[0]
            partnerm2 = (player.participant.hints_guess_cook_m2 == partner.participant.MP2hints_given_cook)
        elif player.id_in_group == partner.participant.partnerm4:
            player.participant.hints_guess_cook_m4 = formfields[0]
            partnerm4 = (player.participant.hints_guess_cook_m4 == partner.participant.MR2hints_given_cook)
        elif player.id_in_group == partner.participant.partnerf2:
            player.participant.hints_guess_cook_f2 = formfields[0]
            partnerf2 = (player.participant.hints_guess_cook_f2 == partner.participant.WP2hints_given_cook)
        elif player.id_in_group == partner.participant.partnerf4:
            player.participant.hints_guess_cook_f4 = formfields[0]
            partnerf4 = (player.participant.hints_guess_cook_f4 == partner.participant.WR2hints_given_cook)
        if partner.participant.partnerm2 == 0:
            partnerm2 = True
        if partner.participant.partnerm4 == 0:
            partnerm4 = True
        if partner.participant.partnerf2 == 0:
            partnerf2 = True
        if partner.participant.partnerf4 == 0:
            partnerf4 = True
        if (partnerm2) and (partnerm4) and (partnerf2) and (partnerf4):
            player.participant.guess_bonus_payoff += 50

def set_hints_guess_sport(player: Player, partner, formfields):
    partnerm1 = False
    partnerm3 = False
    partnerf1 = False
    partnerf3 = False
    partnerm2 = False
    partnerm4 = False
    partnerf2 = False
    partnerf4 = False
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            player.participant.hints_guess_sport_m1 = formfields[1]
            partnerm1 = (player.participant.hints_guess_sport_m1 == partner.participant.MP1hints_given_sport)
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            player.participant.hints_guess_sport_m3 = formfields[2]
            partnerm3 = (player.participant.hints_guess_sport_m3 == partner.participant.MR1hints_given_sport)
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            player.participant.hints_guess_sport_f1 = formfields[3]
            partnerf1 = (player.participant.hints_guess_sport_f1 == partner.participant.WP1hints_given_sport)
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            player.participant.hints_guess_sport_f3 = formfields[4]
            partnerf3 = (player.participant.hints_guess_sport_f3 == partner.participant.WR1hints_given_sport)
        if player.id_in_group == partner.participant.partnerm1:
            player.participant.hints_guess_sport_m1 = formfields[0]
            partnerm1 = (player.participant.hints_guess_sport_m1 == partner.participant.MP1hints_given_sport)
        elif player.id_in_group == partner.participant.partnerm3:
            player.participant.hints_guess_sport_m3 = formfields[0]
            partnerm3 = (player.participant.hints_guess_sport_m3 == partner.participant.MR1hints_given_sport)
        elif player.id_in_group == partner.participant.partnerf1:
            player.participant.hints_guess_sport_f1 = formfields[0]
            partnerf1 = (player.participant.hints_guess_sport_f1 == partner.participant.WP1hints_given_sport)
        elif player.id_in_group == partner.participant.partnerf3:
            player.participant.hints_guess_sport_f3 = formfields[0]
            partnerf3 = (player.participant.hints_guess_sport_f3 == partner.participant.WR1hints_given_sport)
        if partner.participant.partnerm1 == 0:
            partnerm1 = True
        if partner.participant.partnerm3 == 0:
            partnerm3 = True
        if partner.participant.partnerf1 == 0:
            partnerf1 = True
        if partner.participant.partnerf3 == 0:
            partnerf3 = True
        if (partnerm1) and (partnerm3) and (partnerf1) and (partnerf3):
            player.participant.guess_bonus_payoff += 50
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            player.participant.hints_guess_sport_m2 = formfields[1]
            partnerm2 = (player.participant.hints_guess_sport_m2 == partner.participant.MP2hints_given_sport)
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            player.participant.hints_guess_sport_m4 = formfields[2]
            partnerm4 = (player.participant.hints_guess_sport_m4 == partner.participant.MR2hints_given_sport)
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            player.participant.hints_guess_sport_f2 = formfields[3]
            partnerf2 = (player.participant.hints_guess_sport_f2 == partner.participant.WP2hints_given_sport)
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            player.participant.hints_guess_sport_f4 = formfields[4]
            partnerf4 = (player.participant.hints_guess_sport_f4 == partner.participant.WR2hints_given_sport)
        if player.id_in_group == partner.participant.partnerm2:
            player.participant.hints_guess_sport_m2 = formfields[0]
            partnerm2 = (player.participant.hints_guess_sport_m2 == partner.participant.MP2hints_given_sport)
        elif player.id_in_group == partner.participant.partnerm4:
            player.participant.hints_guess_sport_m4 = formfields[0]
            partnerm4 = (player.participant.hints_guess_sport_m4 == partner.participant.MR2hints_given_sport)
        elif player.id_in_group == partner.participant.partnerf2:
            player.participant.hints_guess_sport_f2 = formfields[0]
            partnerf2 = (player.participant.hints_guess_sport_f2 == partner.participant.WP2hints_given_sport)
        elif player.id_in_group == partner.participant.partnerf4:
            player.participant.hints_guess_sport_f4 = formfields[0]
            partnerf4 = (player.participant.hints_guess_sport_f4 == partner.participant.WR2hints_given_sport)
        if partner.participant.partnerm2 == 0:
            partnerm2 = True
        if partner.participant.partnerm4 == 0:
            partnerm4 = True
        if partner.participant.partnerf2 == 0:
            partnerf2 = True
        if partner.participant.partnerf4 == 0:
            partnerf4 = True
        if (partnerm2) and (partnerm4) and (partnerf2) and (partnerf4):
            player.participant.guess_bonus_payoff += 50

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
        random_rounds(player.subsession)
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player:Player):
        player.participant.prev_hint = 0
        return dict(round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP = dict()
        player.participant.responses_3b_MR = dict()
        player.participant.responses_3b_WP = dict()
        player.participant.responses_3b_WR = dict()
        player.participant.guess_bonus_payoff = 0

#MALE PREFERRED
class Transition_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)

class Hints_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP','results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
        random.shuffle(formfields_results)
        # formfields_expect = ['expect_hints_economics_MP', 'expect_hints_cooking_MP', 'expect_hints_sports_MP']
        # random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectationWR_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        wr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 0:
                wr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), wr=wr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics1_MP', 'expect_hints_cooking1_MP', 'expect_hints_sports1_MP']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class ExpectationMR_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        mr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 1:
                mr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_MP', 'expect_hints_cooking2_MP', 'expect_hints_sports2_MP']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

def vars_for_template2(player: Player, formfields):
    final = {}
    formfields_random = []
    partners = []
    g = player.group
    partner = g.get_player_by_id(player.participant.partner3)
    display = True
    count = 0
    hints = 0
    partner1 = 0
    partner2 = 0
    partner3 = 0
    partner4 = 0
    is2 = False
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm1)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partner1 = partner1.participant.label
            partners.append(partner1)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm3)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partner2 = partner2.participant.label
            partners.append(partner2)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf1)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partner3 = partner3.participant.label
            partners.append(partner3)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf3)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partner4 = partner4.participant.label
            partners.append(partner4)
            formfields_random.append(formfields[3])
            count+=1
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        is2 = True
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm2)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partner1 = partner1.participant.label
            partners.append(partner1)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm4)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partner2 = partner2.participant.label
            partners.append(partner2)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf2)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partner3 = partner3.participant.label
            partners.append(partner3)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf4)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partner4 = partner4.participant.label
            partners.append(partner4)
            formfields_random.append(formfields[3])
            count+=1
    if count == 0:
        hints = 2
    elif count == 1:
        hints = 5
    elif count == 2:
        hints = 7
    elif count == 3:
        hints = 10
    elif count == 0:
        hints = 0
        display = False
    final.update(dict(count=count, hints=hints, display=display, partners=partners, partner1=partner1, partner2=partner2, partner3=partner3, partner4=partner4, partner=partner.participant.label, round=player.participant.round3b_completed, is2=is2))
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

class ExpectedSupplyEcon_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints_you_MP','econhints_partner1_MP', 'econhints_partner2_MP', 'econhints_partner3_MP', 'econhints_partner4_MP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints_partner1_MP', 'econhints_partner2_MP', 'econhints_partner3_MP', 'econhints_partner4_MP']
        final = vars_for_template2(player, formfields_random)[0]
        hints = vars_for_template2(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('econhints_you_MP'),player.field_maybe_none('econhints_partner1_MP'), player.field_maybe_none('econhints_partner2_MP'), player.field_maybe_none('econhints_partner3_MP'), player.field_maybe_none('econhints_partner4_MP')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_guess_econ(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['econhints_partner1_MP', 'econhints_partner2_MP', 'econhints_partner3_MP', 'econhints_partner4_MP']
        hints = vars_for_template2(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceEcon_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_econ_MP']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplyCook_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints_you_MP','cookhints_partner1_MP', 'cookhints_partner2_MP', 'cookhints_partner3_MP', 'cookhints_partner4_MP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints_partner1_MP', 'cookhints_partner2_MP', 'cookhints_partner3_MP', 'cookhints_partner4_MP']
        final = vars_for_template2(player, formfields_random)[0]
        hints = vars_for_template2(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('cookhints_you_MP'),player.field_maybe_none('cookhints_partner1_MP'), player.field_maybe_none('cookhints_partner2_MP'), player.field_maybe_none('cookhints_partner3_MP'), player.field_maybe_none('cookhints_partner4_MP')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_guess_cook(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['cookhints_partner1_MP', 'cookhints_partner2_MP', 'cookhints_partner3_MP', 'cookhints_partner4_MP']
        hints = vars_for_template2(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceCook_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_cook_MP']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplySport_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints_you_MP','sporthints_partner1_MP', 'sporthints_partner2_MP', 'sporthints_partner3_MP', 'sporthints_partner4_MP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints_partner1_MP', 'sporthints_partner2_MP', 'sporthints_partner3_MP', 'sporthints_partner4_MP']
        final = vars_for_template2(player, formfields_random)[0]
        hints = vars_for_template2(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('sporthints_you_MP'),player.field_maybe_none('sporthints_partner1_MP'), player.field_maybe_none('sporthints_partner2_MP'), player.field_maybe_none('sporthints_partner3_MP'), player.field_maybe_none('sporthints_partner4_MP')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_guess_sport(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints_partner1_MP', 'sporthints_partner2_MP', 'sporthints_partner3_MP', 'sporthints_partner4_MP']
        hints = vars_for_template2(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceSport_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_sport_MP']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class Transition_MP0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) and (participant.partner3 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MP','prob_econ1_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Increased in supply.")}
            elif player.participant.econ_hint_requests_partner3 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_economics1_MP':player.crt_economics1_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MP','prob_econ2_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: He shouted, \"Is this a normal one?\".")}
            elif player.participant.econ_hint_requests_partner3 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_economics2_MP':player.crt_economics2_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MP','prob_econ3_MP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner3)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner3 += 1
    #         if player.participant.econ_hint_requests_partner3 <= int(partner.participant.hints_given_econ):
    #             player.participant.econ_hint_used_partner3 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: No influence.")}
    #         elif player.participant.econ_hint_requests_partner3 > int(partner.participant.hints_given_econ):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_economics3_MP':player.crt_economics3_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MP','prob_econ4_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Factories have decided to pay workers higher incomes.")}
            elif player.participant.econ_hint_requests_partner3 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_economics4_MP':player.crt_economics4_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MP','prob_cook1_MP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner3)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner3 += 1
    #         if player.participant.cook_hint_requests_partner3 <= int(partner.participant.hints_given_cook):
    #             player.participant.cook_hint_used_partner3 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: Yellow and white.")}
    #         elif player.participant.cook_hint_requests_partner3 > int(partner.participant.hints_given_cook):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_cooking1_MP':player.crt_cooking1_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MP','prob_cook2_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Maximum moisture.")}
            elif player.participant.cook_hint_requests_partner3 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_cooking2':player.crt_cooking2_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MP','prob_cook3_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Everyone looked at the camera and said \"CHEEESE\".")}
            elif player.participant.cook_hint_requests_partner3 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_cooking3_MP':player.crt_cooking3_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MP','prob_cook4_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Less than 2.")}
            elif player.participant.cook_hint_requests_partner3 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_cooking4_MP':player.crt_cooking4_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MP','prob_sport1_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: London and neighbor of Australia.")}
            elif player.participant.sport_hint_requests_partner3 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_sports1_MP':player.crt_sports1_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_MP','prob_sport2_MP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner3)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner3 += 1
    #         if player.participant.sport_hint_requests_partner3 <= int(partner.participant.hints_given_sport):
    #             player.participant.sport_hint_used_partner3 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: South West.")}
    #         elif player.participant.sport_hint_requests_partner3 > int(partner.participant.hints_given_sport):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_sports2_MP':player.crt_sports2_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MP','prob_sport3_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Ayub Khan.")}
            elif player.participant.sport_hint_requests_partner3 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_sports3_MP':player.crt_sports3_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_MP']) and (get_timeout_seconds1(player) > 0) and (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MP','prob_sport4_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner3 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Green ball.")}
            elif player.participant.sport_hint_requests_partner3 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MP.update({'crt_sports4_MP':player.crt_sports4_MP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_MP_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner3)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Economics3_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_MP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_MP_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner3)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Cooking1_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_MP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_MP_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner3)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Sports2_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_MP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_MP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_MP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
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
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)

class Hints_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR','results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
        random.shuffle(formfields_results)
        # formfields_expect = ['expect_hints_economics_MR', 'expect_hints_cooking_MR', 'expect_hints_sports_MR']
        # random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class ExpectationWR_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        wr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 0:
                wr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), wr=wr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics1_MR', 'expect_hints_cooking1_MR', 'expect_hints_sports1_MR']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class ExpectationMR_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        mr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 1:
                mr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_MR', 'expect_hints_cooking2_MR', 'expect_hints_sports2_MR']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

def vars_for_template3(player: Player, formfields):
    final = {}
    formfields_random = []
    partners = {}
    g = player.group
    partner = g.get_player_by_id(player.participant.partner8)
    display = True
    count = 0
    hints = 0
    partner1 = 0
    partner2 = 0
    partner3 = 0
    partner4 = 0
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm1)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partners.update(partner1=partner1.participant.label)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm3)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partners.update(partner2=partner2.participant.label)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf1)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partners.update(partner3=partner3.participant.label)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf3)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partners.update(partner4=partner4.participant.label)
            formfields_random.append(formfields[3])
            count+=1
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm2)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partners.update(partner1=partner1.participant.label)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm4)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partners.update(partner2=partner2.participant.label)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf2)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partners.update(partner3=partner3.participant.label)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf4)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partners.update(partner4=partner4.participant.label)
            formfields_random.append(formfields[3])
            count+=1
    if count == 0:
        hints = 2
    elif count == 1:
        hints = 5
    elif count == 2:
        hints = 7
    elif count == 3:
        hints = 10
    elif count == 0:
        hints = 0
        display = False
    final.update(dict(count=count, hints=hints, display=display, partners=partners, partner1=partner1, partner2=partner2, partner3=partner3, partner4=partner4, partner=partner.participant.label, round=player.participant.round3b_completed))
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

class ExpectedSupplyEcon_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints_you_MR','econhints_partner1_MR', 'econhints_partner2_MR', 'econhints_partner3_MR', 'econhints_partner4_MR']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints_partner1_MR', 'econhints_partner2_MR', 'econhints_partner3_MR', 'econhints_partner4_MR']
        final = vars_for_template3(player, formfields_random)[0]
        hints = vars_for_template3(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('econhints_you_MR'),player.field_maybe_none('econhints_partner1_MR'), player.field_maybe_none('econhints_partner2_MR'), player.field_maybe_none('econhints_partner3_MR'), player.field_maybe_none('econhints_partner4_MR')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_guess_econ(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['econhints_partner1_MR', 'econhints_partner2_MR', 'econhints_partner3_MR', 'econhints_partner4_MR']
        hints = vars_for_template3(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceEcon_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_econ_MR']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplyCook_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints_you_MR','cookhints_partner1_MR', 'cookhints_partner2_MR', 'cookhints_partner3_MR', 'cookhints_partner4_MR']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints_partner1_MR', 'cookhints_partner2_MR', 'cookhints_partner3_MR', 'cookhints_partner4_MR']
        final = vars_for_template3(player, formfields_random)[0]
        hints = vars_for_template3(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('cookhints_you_MR'),player.field_maybe_none('cookhints_partner1_MR'), player.field_maybe_none('cookhints_partner2_MR'), player.field_maybe_none('cookhints_partner3_MR'), player.field_maybe_none('cookhints_partner4_MR')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_guess_cook(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['cookhints_partner1_MR', 'cookhints_partner2_MR', 'cookhints_partner3_MR', 'cookhints_partner4_MR']
        hints = vars_for_template3(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceCook_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_cook_MR']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplySport_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints_you_MR','sporthints_partner1_MR', 'sporthints_partner2_MR', 'sporthints_partner3_MR', 'sporthints_partner4_MR']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints_partner1_MR', 'sporthints_partner2_MR', 'sporthints_partner3_MR', 'sporthints_partner4_MR']
        final = vars_for_template3(player, formfields_random)[0]
        hints = vars_for_template3(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('sporthints_you_MR'),player.field_maybe_none('sporthints_partner1_MR'), player.field_maybe_none('sporthints_partner2_MR'), player.field_maybe_none('sporthints_partner3_MR'), player.field_maybe_none('sporthints_partner4_MR')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_guess_sport(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints_partner1_MR', 'sporthints_partner2_MR', 'sporthints_partner3_MR', 'sporthints_partner4_MR']
        hints = vars_for_template3(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceSport_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_sport_MR']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class Transition_MR0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) and (participant.partner8 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MR','prob_econ1_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Demand and supply.")}
            elif player.participant.econ_hint_requests_partner8 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_economics1_MR':player.crt_economics1_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MR','prob_econ2_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Demand and supply.")}
            elif player.participant.econ_hint_requests_partner8 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_economics2_MR':player.crt_economics2_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MR','prob_econ3_MR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner8)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner8 += 1
    #         if player.participant.econ_hint_requests_partner8 <= int(partner.participant.hints_given_econ):
    #             player.participant.econ_hint_used_partner8 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: 5 - 3 = ?.")}
    #         elif player.participant.econ_hint_requests_partner8 > int(partner.participant.hints_given_econ):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_economics3_MR':player.crt_economics3_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MR','prob_econ4_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: A few.")}
            elif player.participant.econ_hint_requests_partner8 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_economics4_MR':player.crt_economics4_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MR','prob_cook1_MR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner8)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner8 += 1
    #         if player.participant.cook_hint_requests_partner8 <= int(partner.participant.hints_given_cook):
    #             player.participant.cook_hint_used_partner8 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: Citric acid.")}
    #         elif player.participant.cook_hint_requests_partner8 > int(partner.participant.hints_given_cook):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_cooking1_MR':player.crt_cooking1_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MR','prob_cook2_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Maize related product.")}
            elif player.participant.cook_hint_requests_partner8 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_cooking2_MR':player.crt_cooking2_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MR','prob_cook3_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Extracted with olives.")}
            elif player.participant.cook_hint_requests_partner8 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_cooking3_MR':player.crt_cooking3_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MR','prob_cook4_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Rhymes with pear.")}
            elif player.participant.cook_hint_requests_partner8 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_cooking4_MR':player.crt_cooking4_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MR','prob_sport1_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: It was Allama Iqbal\'s birth year.")}
            elif player.participant.sport_hint_requests_partner8 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_sports1_MR':player.crt_sports1_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_MR','prob_sport2_MR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner8)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner8 += 1
    #         if player.participant.sport_hint_requests_partner8 <= int(partner.participant.hints_given_sport):
    #             player.participant.sport_hint_used_partner8 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: We love orange.")}
    #         elif player.participant.sport_hint_requests_partner8 > int(partner.participant.hints_given_sport):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_sports2_MR':player.crt_sports2_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MR','prob_sport3_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Greater than 5.")}
            elif player.participant.sport_hint_requests_partner8 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_sports3_MR':player.crt_sports3_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_MR']) and (get_timeout_seconds1(player) > 0) and (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MR','prob_sport4_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner8 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Christopher.")}
            elif player.participant.sport_hint_requests_partner8 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_MR.update({'crt_sports4_MR':player.crt_sports4_MR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_MR_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner8)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Economics3_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_MR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_MR_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner8)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Cooking1_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_MR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_MR_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner8)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Sports2_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_MR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_MR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_MR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
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
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)

class Hints_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP','results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
        random.shuffle(formfields_results)
        # formfields_expect = ['expect_hints_economics_WP', 'expect_hints_cooking_WP', 'expect_hints_sports_WP']
        # random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class ExpectationWR_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        wr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 0:
                wr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), wr=wr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics1_WP', 'expect_hints_cooking1_WP', 'expect_hints_sports1_WP']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class ExpectationMR_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        mr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 1:
                mr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_WP', 'expect_hints_cooking2_WP', 'expect_hints_sports2_WP']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

def vars_for_template4(player: Player, formfields):
    final = {}
    formfields_random = []
    partners = {}
    g = player.group
    partner = g.get_player_by_id(player.participant.partner2)
    display = True
    count = 0
    hints = 0
    partner1 = 0
    partner2 = 0
    partner3 = 0
    partner4 = 0
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm1)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partners.update(partner1=partner1.participant.label)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm3)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partners.update(partner2=partner2.participant.label)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf1)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partners.update(partner3=partner3.participant.label)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf3)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partners.update(partner4=partner4.participant.label)
            formfields_random.append(formfields[3])
            count+=1
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm2)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partners.update(partner1=partner1.participant.label)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm4)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partners.update(partner2=partner2.participant.label)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf2)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partners.update(partner3=partner3.participant.label)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf4)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partners.update(partner4=partner4.participant.label)
            formfields_random.append(formfields[3])
            count+=1
    if count == 0:
        hints = 2
    elif count == 1:
        hints = 5
    elif count == 2:
        hints = 7
    elif count == 3:
        hints = 10
    elif count == 0:
        hints = 0
        display = False
    final.update(dict(count=count, hints=hints, display=display, partners=partners, partner1=partner1, partner2=partner2, partner3=partner3, partner4=partner4, partner=partner.participant.label, round=player.participant.round3b_completed))
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

class ExpectedSupplyEcon_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints_you_WP','econhints_partner1_WP', 'econhints_partner2_WP', 'econhints_partner3_WP', 'econhints_partner4_WP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints_partner1_WP', 'econhints_partner2_WP', 'econhints_partner3_WP', 'econhints_partner4_WP']
        final = vars_for_template4(player, formfields_random)[0]
        hints = vars_for_template4(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('econhints_you_WP'),player.field_maybe_none('econhints_partner1_WP'), player.field_maybe_none('econhints_partner2_WP'), player.field_maybe_none('econhints_partner3_WP'), player.field_maybe_none('econhints_partner4_WP')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_guess_econ(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['econhints_partner1_WP', 'econhints_partner2_WP', 'econhints_partner3_WP', 'econhints_partner4_WP']
        hints = vars_for_template4(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceEcon_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_econ_WP']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplyCook_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints_you_WP','cookhints_partner1_WP', 'cookhints_partner2_WP', 'cookhints_partner3_WP', 'cookhints_partner4_WP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints_partner1_WP', 'cookhints_partner2_WP', 'cookhints_partner3_WP', 'cookhints_partner4_WP']
        final = vars_for_template4(player, formfields_random)[0]
        hints = vars_for_template4(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('cookhints_you_WP'),player.field_maybe_none('cookhints_partner1_WP'), player.field_maybe_none('cookhints_partner2_WP'), player.field_maybe_none('cookhints_partner3_WP'), player.field_maybe_none('cookhints_partner4_WP')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_guess_cook(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['cookhints_partner1_WP', 'cookhints_partner2_WP', 'cookhints_partner3_WP', 'cookhints_partner4_WP']
        hints = vars_for_template4(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceCook_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_cook_WP']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplySport_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints_you_WP','sporthints_partner1_WP', 'sporthints_partner2_WP', 'sporthints_partner3_WP', 'sporthints_partner4_WP']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints_partner1_WP', 'sporthints_partner2_WP', 'sporthints_partner3_WP', 'sporthints_partner4_WP']
        final = vars_for_template4(player, formfields_random)[0]
        hints = vars_for_template4(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('sporthints_you_WP'),player.field_maybe_none('sporthints_partner1_WP'), player.field_maybe_none('sporthints_partner2_WP'), player.field_maybe_none('sporthints_partner3_WP'), player.field_maybe_none('sporthints_partner3_WP')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_guess_sport(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints_partner1_WP', 'sporthints_partner2_WP', 'sporthints_partner3_WP', 'sporthints_partner4_WP']
        hints = vars_for_template4(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceSport_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_sport_WP']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class Transition_WP0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) and (participant.partner2 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WP','prob_econ1_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Ratio of dog owners to cat owners.")}
            elif player.participant.econ_hint_requests_partner2 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_economics1_WP':player.crt_economics1_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WP','prob_econ2_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Long-run > short-run.")}
            elif player.participant.econ_hint_requests_partner2 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_economics2_WP':player.crt_economics2_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WP','prob_econ3_WP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner2)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner2 += 1
    #         if player.participant.econ_hint_requests_partner2 <= int(partner.participant.hints_given_econ):
    #             player.participant.econ_hint_used_partner2 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: More is better.")}
    #         elif player.participant.econ_hint_requests_partner2 > int(partner.participant.hints_given_econ):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_economics3_WP':player.crt_economics3_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WP','prob_econ4_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Supply shifts left and demand shifts right.")}
            elif player.participant.econ_hint_requests_partner2 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_economics4_WP':player.crt_economics4_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WP','prob_cook1_WP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner2)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner2 += 1
    #         if player.participant.cook_hint_requests_partner2 <= int(partner.participant.hints_given_cook):
    #             player.participant.cook_hint_used_partner2 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: Timing.")}
    #         elif player.participant.cook_hint_requests_partner2 > int(partner.participant.hints_given_cook):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_cooking1_WP':player.crt_cooking1_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WP','prob_cook2_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: KFC fried chicken and french fries.")}
            elif player.participant.cook_hint_requests_partner2 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_cooking2_WP':player.crt_cooking2_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WP','prob_cook3_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Multiple of nine.")}
            elif player.participant.cook_hint_requests_partner2 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_cooking3_WP':player.crt_cooking3_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WP','prob_cook4_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Soak it.")}
            elif player.participant.cook_hint_requests_partner2 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_cooking4_WP':player.crt_cooking4_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WP','prob_sport1_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Sharara.")}
            elif player.participant.sport_hint_requests_partner2 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_sports1_WP':player.crt_sports1_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_WP','prob_sport2_WP']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner2)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner2 += 1
    #         if player.participant.sport_hint_requests_partner2 <= int(partner.participant.hints_given_sport):
    #             player.participant.sport_hint_used_partner2 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: An ash tree.")}
    #         elif player.participant.sport_hint_requests_partner2 > int(partner.participant.hints_given_sport):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_sports2_WP':player.crt_sports2_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WP','prob_sport3_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: During Great Depression.")}
            elif player.participant.sport_hint_requests_partner2 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_sports3_WP':player.crt_sports3_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_WP']) and (get_timeout_seconds1(player) > 0) and (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WP','prob_sport4_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner2 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: There is no true lord.")}
            elif player.participant.sport_hint_requests_partner2 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WP.update({'crt_sports4_WP':player.crt_sports4_WP})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_WP_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner2)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Economics3_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_WP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_WP_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner2)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Cooking1_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_WP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_WP_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner2)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Sports2_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_WP']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_WP']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WP_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_WP']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
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
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)

class Hints_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR','results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
        random.shuffle(formfields_results)
        # formfields_expect = ['expect_hints_economics_WR', 'expect_hints_cooking_WR', 'expect_hints_sports_WR']
        # random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, partner=partner.participant.label, round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class ExpectationWR_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        wr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 0:
                wr = curr_player
                break
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), wr=wr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics1_WR', 'expect_hints_cooking1_WR', 'expect_hints_sports1_WR']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class ExpectationMR_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        mr = 0
        length = len(g.get_players())
        int = list(range(1, length+1))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player != partner and curr_player.participant.gender == 1:
                mr = curr_player
                break
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_WR', 'expect_hints_cooking2_WR', 'expect_hints_sports2_WR']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

def vars_for_template5(player: Player, formfields):
    final = {}
    formfields_random = []
    partners = {}
    g = player.group
    partner = g.get_player_by_id(player.participant.partner6)
    display = True
    count = 0
    hints = 0
    partner1 = 0
    partner2 = 0
    partner3 = 0
    partner4 = 0
    if (partner.participant.partnerm1 == player.id_in_group) or (partner.participant.partnerm3 == player.id_in_group) or (partner.participant.partnerf1 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm1 != player.id_in_group) and (partner.participant.partnerm1 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm1)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partners.update(partner1=partner1.participant.label)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm3 != player.id_in_group) and (partner.participant.partnerm3 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm3)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partners.update(partner2=partner2.participant.label)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf1 != player.id_in_group) and (partner.participant.partnerf1 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf1)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partners.update(partner3=partner3.participant.label)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf3 != player.id_in_group) and (partner.participant.partnerf3 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf3)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partners.update(partner4=partner4.participant.label)
            formfields_random.append(formfields[3])
            count+=1
    elif (partner.participant.partnerm2 == player.id_in_group) or (partner.participant.partnerm4 == player.id_in_group) or (partner.participant.partnerf2 == player.id_in_group) or (partner.participant.partnerf4 == player.id_in_group):
        if (partner.participant.partnerm2 != player.id_in_group) and (partner.participant.partnerm2 != 0):
            partner1 = g.get_player_by_id(partner.participant.partnerm2)
            final.update(dict(partner1_label='{}?'.format(partner1.participant.label)))
            partners.update(partner1=partner1.participant.label)
            formfields_random.append(formfields[0])
            count+=1
        if (partner.participant.partnerm4 != player.id_in_group) and (partner.participant.partnerm4 != 0):
            partner2 = g.get_player_by_id(partner.participant.partnerm4)
            final.update(dict(partner2_label='{}?'.format(partner2.participant.label)))
            partners.update(partner2=partner2.participant.label)
            formfields_random.append(formfields[1])
            count+=1
        if (partner.participant.partnerf2 != player.id_in_group) and (partner.participant.partnerf2 != 0):
            partner3 = g.get_player_by_id(partner.participant.partnerf2)
            final.update(dict(partner3_label='{}?'.format(partner3.participant.label)))
            partners.update(partner3=partner3.participant.label)
            formfields_random.append(formfields[2])
            count+=1
        if (partner.participant.partnerf4 != player.id_in_group) and (partner.participant.partnerf4 != 0):
            partner4 = g.get_player_by_id(partner.participant.partnerf4)
            final.update(dict(partner4_label='{}?'.format(partner4.participant.label)))
            partners.update(partner4=partner4.participant.label)
            formfields_random.append(formfields[3])
            count+=1
    if count == 0:
        hints = 2
    elif count == 1:
        hints = 5
    elif count == 2:
        hints = 7
    elif count == 3:
        hints = 10
    elif count == 0:
        hints = 0
        display = False
    final.update(dict(count=count, hints=hints, display=display, partners=partners, partner1=partner1, partner2=partner2, partner3=partner3, partner4=partner4, partner=partner.participant.label, round=player.participant.round3b_completed))
    final.update(dict(formfields_random=formfields_random))
    return [final, hints]

class ExpectedSupplyEcon_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['econhints_you_WR','econhints_partner1_WR', 'econhints_partner2_WR', 'econhints_partner3_WR', 'econhints_partner4_WR']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['econhints_partner1_WR', 'econhints_partner2_WR', 'econhints_partner3_WR', 'econhints_partner4_WR']
        final = vars_for_template5(player, formfields_random)[0]
        hints = vars_for_template5(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('econhints_you_WR'),player.field_maybe_none('econhints_partner1_WR'), player.field_maybe_none('econhints_partner2_WR'), player.field_maybe_none('econhints_partner3_WR'), player.field_maybe_none('econhints_partner4_WR')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_guess_econ(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['econhints_partner1_WR', 'econhints_partner2_WR', 'econhints_partner3_WR', 'econhints_partner4_WR']
        hints = vars_for_template5(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceEcon_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_econ_WR']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplyCook_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['cookhints_you_WR','cookhints_partner1_WR', 'cookhints_partner2_WR', 'cookhints_partner3_WR', 'cookhints_partner4_WR']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['cookhints_partner1_WR', 'cookhints_partner2_WR', 'cookhints_partner3_WR', 'cookhints_partner4_WR']
        final = vars_for_template5(player, formfields_random)[0]
        hints = vars_for_template5(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('cookhints_you_WR'),player.field_maybe_none('cookhints_partner1_WR'), player.field_maybe_none('cookhints_partner2_WR'), player.field_maybe_none('cookhints_partner3_WR'), player.field_maybe_none('cookhints_partner4_WR')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_guess_cook(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['cookhints_partner1_WR', 'cookhints_partner2_WR', 'cookhints_partner3_WR', 'cookhints_partner4_WR']
        hints = vars_for_template5(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceCook_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_cook_WR']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectedSupplySport_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['sporthints_you_WR','sporthints_partner1_WR', 'sporthints_partner2_WR', 'sporthints_partner3_WR', 'sporthints_partner4_WR']
        return formfields
    @staticmethod
    def vars_for_template(player: Player):
        formfields_random = ['sporthints_partner1_WR', 'sporthints_partner2_WR', 'sporthints_partner3_WR', 'sporthints_partner4_WR']
        final = vars_for_template5(player, formfields_random)[0]
        hints = vars_for_template5(player, formfields_random)[1]
        final["hints"] = hints
        return final
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        formfields = [player.field_maybe_none('sporthints_you_WR'),player.field_maybe_none('sporthints_partner1_WR'), player.field_maybe_none('sporthints_partner2_WR'), player.field_maybe_none('sporthints_partner3_WR'), player.field_maybe_none('sporthints_partner4_WR')]
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_guess_sport(player, partner, formfields)
    @staticmethod
    def error_message(player: Player, values):
        formfields = ['sporthints_partner1_WR', 'sporthints_partner2_WR', 'sporthints_partner3_WR', 'sporthints_partner4_WR']
        hints = vars_for_template5(player, formfields)[1]
        desired_array = []
        for i in values.values():
            if i != None:
                desired_array.append(int(i))
        allvalues = sum(desired_array)
        if allvalues > hints:
            return "Ensure that values add to the allowed number of hints"

class ExpectedConfidenceSport_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = ['confidence_sport_WR']
        return formfields
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round=player.participant.round3b_completed)

class Transition_WR0(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) and (participant.partner6 != 0)
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label.upper(), round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 1200

class Economics1_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WR','prob_econ1_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Labor as a cost of production.")}
            elif player.participant.econ_hint_requests_partner6 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_economics1_WR':player.crt_economics1_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WR','prob_econ2_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Quantity demanded > quantity supplied.")}
            elif player.participant.econ_hint_requests_partner6 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_economics2_WR':player.crt_economics2_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WR','prob_econ3_WR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner6)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.econ_hint_requests_partner6 += 1
    #         if player.participant.econ_hint_requests_partner6 <= int(partner.participant.hints_given_econ):
    #             player.participant.econ_hint_used_partner6 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: Consumer is king.")}
    #         elif player.participant.econ_hint_requests_partner6 > int(partner.participant.hints_given_econ):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_economics3_WR':player.crt_economics3_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WR','prob_econ4_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= int(partner.participant.hints_given_econ):
                player.participant.econ_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Easy to join.")}
            elif player.participant.econ_hint_requests_partner6 > int(partner.participant.hints_given_econ):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_economics4_WR':player.crt_economics4_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WR','prob_cook1_WR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner6)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.cook_hint_requests_partner6 += 1
    #         if player.participant.cook_hint_requests_partner6 <= int(partner.participant.hints_given_cook):
    #             player.participant.cook_hint_used_partner6 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: Get low.")}
    #         elif player.participant.cook_hint_requests_partner6 > int(partner.participant.hints_given_cook):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_cooking1_WR':player.crt_cooking1_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WR','prob_cook2_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: BRRRRRR.")}
            elif player.participant.cook_hint_requests_partner6 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_cooking2_WR':player.crt_cooking2_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WR','prob_cook3_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Mist or fog.")}
            elif player.participant.cook_hint_requests_partner6 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_cooking3_WR':player.crt_cooking3_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WR','prob_cook4_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= int(partner.participant.hints_given_cook):
                player.participant.cook_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Qeema.")}
            elif player.participant.cook_hint_requests_partner6 > int(partner.participant.hints_given_cook):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_cooking4_WR':player.crt_cooking4_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WR','prob_sport1_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Pakistan gained independence in 1947.")}
            elif player.participant.sport_hint_requests_partner6 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_sports1_WR':player.crt_sports1_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_WR','prob_sport2_WR']
    # @staticmethod
    # def live_method(player: Player, data):
    #     group = player.group
    #     partner = group.get_player_by_id(player.participant.partner6)
    #     set_hints_given(player,partner)
    #     if data == 'clicked-button':
    #         player.participant.sport_hint_requests_partner6 += 1
    #         if player.participant.sport_hint_requests_partner6 <= int(partner.participant.hints_given_sport):
    #             player.participant.sport_hint_used_partner6 += 1
    #             player.participant.prev_hint = 1
    #             return {player.id_in_group: dict(message = "Hint: Eclipse.")}
    #         elif player.participant.sport_hint_requests_partner6 > int(partner.participant.hints_given_sport):
    #             return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_sports2_WR':player.crt_sports2_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WR','prob_sport3_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Death year of Fatima Jinnah.")}
            elif player.participant.sport_hint_requests_partner6 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_sports3_WR':player.crt_sports3_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_WR']) and (get_timeout_seconds1(player) > 0) and (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WR','prob_sport4_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= int(partner.participant.hints_given_sport):
                player.participant.sport_hint_used_partner6 += 1
                player.participant.prev_hint = 1
                return {player.id_in_group: dict(message = "Hint: Soon after WWI.")}
            elif player.participant.sport_hint_requests_partner6 > int(partner.participant.hints_given_sport):
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.responses_3b_WR.update({'crt_sports4_WR':player.crt_sports4_WR})
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ1_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ2_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Economics3_WR_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner6)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Economics3_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_econ3_WR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Economics4_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_econ4_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Cooking1_WR_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner6)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Cooking1_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_cook1_WR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Cooking2_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook2_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook3_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_cook4_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport1_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

# class Sports2_WR_Hint(Page):
#     form_model = 'player'
#     def vars_for_template(player: Player):
#         group = player.group
#         partner = group.get_player_by_id(player.participant.partner6)
#         return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
#     @staticmethod
#     def is_displayed(player: Player):
#         participant = player.participant
#         return (player.round_number == participant.task_rounds3b['Sports2_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
#     @staticmethod
#     def get_form_fields(player):
#         player.participant.prev_hint = 0
#         return ['helpful_hint_sport2_WR']
#     get_timeout_seconds = get_timeout_seconds1
#     timer_text = C.TIMER_TEXT

class Sports3_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport3_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WR_Hint(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = vars_for_template1(player), round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_WR']) and (get_timeout_seconds1(player) > 0) and (player.participant.prev_hint == 1)
    @staticmethod
    def get_form_fields(player):
        player.participant.prev_hint = 0
        return ['helpful_hint_sport4_WR']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final_Part4(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 53) and (player.participant.round2_completed == 0)
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.participant.round3b_completed)
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.participant.round2_completed = 5
        return '___Round2_1'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        solutions_MP = dict(crt_economics1_MP=3, crt_economics2_MP=4, crt_economics3_MP=4,
        crt_economics4_MP=1, crt_cooking1_MP=2, crt_cooking2_MP=1, crt_cooking3_MP=3,
        crt_cooking4_MP=4, crt_sports1_MP=4, crt_sports2_MP=1, crt_sports3_MP=3,
        crt_sports4_MP=2)
        solutions_MR = dict(crt_economics1_MR=2, crt_economics2_MR=3, crt_economics3_MR=3,
        crt_economics4_MR=4, crt_cooking1_MR=2, crt_cooking2_MR=1, crt_cooking3_MR=2,
        crt_cooking4_MR=3, crt_sports1_MR=2, crt_sports2_MR=3, crt_sports3_MR=4,
        crt_sports4_MR=1)
        solutions_WP = dict(crt_economics1_WP=4, crt_economics2_WP=1, crt_economics3_WP=2,
        crt_economics4_WP=1, crt_cooking1_WP=3, crt_cooking2_WP=4, crt_cooking3_WP=3,
        crt_cooking4_WP=2, crt_sports1_WP=3, crt_sports2_WP=1, crt_sports3_WP=2,
        crt_sports4_WP=2)
        solutions_WR = dict(crt_economics1_WR=2, crt_economics2_WR=2, crt_economics3_WR=1,
        crt_economics4_WR=3, crt_cooking1_WR=3, crt_cooking2_WR=2, crt_cooking3_WR=4,
        crt_cooking4_WR=3, crt_sports1_WR=1, crt_sports2_WR=3, crt_sports3_WR=2,
        crt_sports4_WR=3)

        payoff_MP = 0
        for key1 in solutions_MP.keys():
            if key1 in player.participant.responses_3b_MP:
                if player.participant.responses_3b_MP[key1] == solutions_MP[key1]:
                    payoff_MP += 75

        payoff_MR = 0
        for key2 in solutions_MR.keys():
            if key2 in player.participant.responses_3b_MR:
                if player.participant.responses_3b_MR[key2] == solutions_MR[key2]:
                    payoff_MR += 75

        payoff_WP = 0
        for key3 in solutions_WP.keys():
            if key3 in player.participant.responses_3b_WP:
                if player.participant.responses_3b_WP[key3] == solutions_WP[key3]:
                    payoff_WP += 75

        payoff_WR = 0
        for key4 in solutions_WR.keys():
            if key4 in player.participant.responses_3b_WR:
                if player.participant.responses_3b_WR[key4] == solutions_WR[key4]:
                    payoff_WR += 75

        player.participant.payoff_tt.update({"Round3_MP": payoff_MP, "Round3_MR": payoff_MR, "Round3_WP": payoff_WP, "Round3_WR": payoff_WR})
        player.participant.payoff_helped.update({player.participant.partner3: payoff_MP, player.participant.partner8: payoff_MR, player.participant.partner2: payoff_WP, player.participant.partner6: payoff_WR})

class Final_Part5(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == 53) and (player.participant.round2_completed != 0)
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.participant.round3b_completed)
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return '___Final_'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        solutions_MP = dict(crt_economics1_MP=3, crt_economics2_MP=4, crt_economics3_MP=4,
        crt_economics4_MP=1, crt_cooking1_MP=2, crt_cooking2_MP=1, crt_cooking3_MP=3,
        crt_cooking4_MP=4, crt_sports1_MP=4, crt_sports2_MP=1, crt_sports3_MP=3,
        crt_sports4_MP=2)
        solutions_MR = dict(crt_economics1_MR=2, crt_economics2_MR=3, crt_economics3_MR=3,
        crt_economics4_MR=4, crt_cooking1_MR=2, crt_cooking2_MR=1, crt_cooking3_MR=2,
        crt_cooking4_MR=3, crt_sports1_MR=2, crt_sports2_MR=3, crt_sports3_MR=4,
        crt_sports4_MR=1)
        solutions_WP = dict(crt_economics1_WP=4, crt_economics2_WP=1, crt_economics3_WP=2,
        crt_economics4_WP=1, crt_cooking1_WP=3, crt_cooking2_WP=4, crt_cooking3_WP=3,
        crt_cooking4_WP=2, crt_sports1_WP=3, crt_sports2_WP=1, crt_sports3_WP=2,
        crt_sports4_WP=2)
        solutions_WR = dict(crt_economics1_WR=2, crt_economics2_WR=2, crt_economics3_WR=1,
        crt_economics4_WR=3, crt_cooking1_WR=3, crt_cooking2_WR=2, crt_cooking3_WR=4,
        crt_cooking4_WR=3, crt_sports1_WR=1, crt_sports2_WR=3, crt_sports3_WR=2,
        crt_sports4_WR=3)

        payoff_MP = 0
        for key1 in solutions_MP.keys():
            if key1 in player.participant.responses_3b_MP:
                if player.participant.responses_3b_MP[key1] == solutions_MP[key1]:
                    payoff_MP += 75

        payoff_MR = 0
        for key2 in solutions_MR.keys():
            if key2 in player.participant.responses_3b_MR:
                if player.participant.responses_3b_MR[key2] == solutions_MR[key2]:
                    payoff_MR += 75

        payoff_WP = 0
        for key3 in solutions_WP.keys():
            if key3 in player.participant.responses_3b_WP:
                if player.participant.responses_3b_WP[key3] == solutions_WP[key3]:
                    payoff_WP += 75

        payoff_WR = 0
        for key4 in solutions_WR.keys():
            if key4 in player.participant.responses_3b_WR:
                if player.participant.responses_3b_WR[key4] == solutions_WR[key4]:
                    payoff_WR += 75

        player.participant.payoff_tt.update({"Round3_MP": payoff_MP, "Round3_MR": payoff_MR, "Round3_WP": payoff_WP, "Round3_WR": payoff_WR})
        player.participant.payoff_helped.update({player.participant.partner3: payoff_MP, player.participant.partner8: payoff_MR, player.participant.partner2: payoff_WP, player.participant.partner6: payoff_WR})


page_sequence = [Demographics, Transition_MP, Hints_MP, ExpectedSupplyEcon_MP, ExpectedConfidenceEcon_MP,
ExpectedSupplyCook_MP, ExpectedConfidenceCook_MP, ExpectedSupplySport_MP, ExpectedConfidenceSport_MP,
Transition_MP0, Economics1_MP, Economics1_MP_Hint, Economics2_MP, Economics2_MP_Hint, Economics3_MP,
Economics4_MP, Economics4_MP_Hint, Cooking1_MP, Cooking2_MP, Cooking2_MP_Hint, Cooking3_MP,
Cooking3_MP_Hint, Cooking4_MP, Cooking4_MP_Hint, Sports1_MP, Sports1_MP_Hint, Sports2_MP,
Sports3_MP, Sports3_MP_Hint, Sports4_MP, Sports4_MP_Hint, Transition_MR, Hints_MR,
ExpectedSupplyEcon_MR, ExpectedConfidenceEcon_MR, ExpectedSupplyCook_MR, ExpectedConfidenceCook_MR,
ExpectedSupplySport_MR, ExpectedConfidenceSport_MR, Transition_MR0, Economics1_MR, Economics1_MR_Hint,
Economics2_MR, Economics2_MR_Hint, Economics3_MR, Economics4_MR, Economics4_MR_Hint, Cooking1_MR,
Cooking2_MR, Cooking2_MR_Hint, Cooking3_MR, Cooking3_MR_Hint, Cooking4_MR, Cooking4_MR_Hint,
Sports1_MR, Sports1_MR_Hint, Sports2_MR, Sports3_MR, Sports3_MR_Hint, Sports4_MR,
Sports4_MR_Hint, Transition_WP, Hints_WP, ExpectedSupplyEcon_WP, ExpectedConfidenceEcon_WP,
ExpectedSupplyCook_WP, ExpectedConfidenceCook_WP, ExpectedSupplySport_WP, ExpectedConfidenceSport_WP,
Transition_WP0, Economics1_WP, Economics1_WP_Hint, Economics2_WP, Economics2_WP_Hint, Economics3_WP,
Economics4_WP, Economics4_WP_Hint, Cooking1_WP, Cooking2_WP, Cooking2_WP_Hint, Cooking3_WP,
Cooking3_WP_Hint, Cooking4_WP, Cooking4_WP_Hint, Sports1_WP, Sports1_WP_Hint, Sports2_WP,
Sports3_WP, Sports3_WP_Hint, Sports4_WP, Sports4_WP_Hint, Transition_WR, Hints_WR,
ExpectedSupplyEcon_WR, ExpectedConfidenceEcon_WR, ExpectedSupplyCook_WR, ExpectedConfidenceCook_WR,
ExpectedSupplySport_WR, ExpectedConfidenceSport_WR, Transition_WR0, Economics1_WR, Economics1_WR_Hint, Economics2_WR,
Economics2_WR_Hint, Economics3_WR, Economics4_WR, Economics4_WR_Hint, Cooking1_WR,
Cooking2_WR, Cooking2_WR_Hint, Cooking3_WR, Cooking3_WR_Hint, Cooking4_WR, Cooking4_WR_Hint,
Sports1_WR, Sports1_WR_Hint, Sports2_WR, Sports3_WR, Sports3_WR_Hint, Sports4_WR,
Sports4_WR_Hint, Final_Part4, Final_Part5]
