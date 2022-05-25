from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Round3b_'
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
    econ_hint_requests = models.IntegerField(initial=0)
    cook_hint_requests = models.IntegerField(initial=0)
    sport_hint_requests = models.IntegerField(initial=0)





# FUNCTIONS
def creating_session(subsession: Subsession):
    # #DELETE BEFORE STARTING
    # for p in subsession.get_players():
    #     p.participant.round3b_completed = 0
    #     p.participant.hints_given_econ = 3
    #     p.participant.hints_given_cook = 3
    #     p.participant.hints_given_sport = 3
    #     p.participant.MP1hints_given_econ = 1
    #     p.participant.MP1hints_given_cook = 2
    #     p.participant.MP1hints_given_sport = 3
    #     p.participant.MP2hints_given_econ = 4
    #     p.participant.MP2hints_given_cook = 5
    #     p.participant.MP2hints_given_sport = 6
    #     p.participant.MR1hints_given_econ = 7
    #     p.participant.MR1hints_given_cook = 8
    #     p.participant.MR1hints_given_sport = 9
    #     p.participant.MR2hints_given_econ = 10
    #     p.participant.MR2hints_given_cook = 11
    #     p.participant.MR2hints_given_sport = 12
    #     p.participant.WP1hints_given_econ = 13
    #     p.participant.WP1hints_given_cook = 14
    #     p.participant.WP1hints_given_sport = 15
    #     p.participant.WP2hints_given_econ = 16
    #     p.participant.WP2hints_given_cook = 17
    #     p.participant.WP2hints_given_sport = 18
    #     p.participant.WR1hints_given_econ = 19
    #     p.participant.WR1hints_given_cook = 20
    #     p.participant.WR1hints_given_sport = 21
    #     p.participant.WR2hints_given_econ = 22
    #     p.participant.WR2hints_given_cook = 23
    #     p.participant.WR2hints_given_sport = 24
    #     p.participant.partner1 = 1
    #     p.participant.partner2 = 2
    #     p.participant.partner3 = 3
    #     p.participant.partner4 = 4
    #     p.participant.partner5 = 5
    #     p.participant.partner6 = 6
    #     p.participant.partner7 = 7
    #     p.participant.partner8 = 8
    #     p.participant.partnerm1 = 1
    #     p.participant.partnerm2 = 2
    #     p.participant.partnerm3 = 3
    #     p.participant.partnerm4 = 4
    #     p.participant.partnerf1 = 5
    #     p.participant.partnerf2 = 6
    #     p.participant.partnerf3 = 7
    #     p.participant.partnerf4 = 8
    #     p.participant.econ_hint_requests_partner1 = 0
    #     p.participant.econ_hint_requests_partner2 = 0
    #     p.participant.econ_hint_requests_partner3 = 0
    #     p.participant.econ_hint_requests_partner4 = 0
    #     p.participant.econ_hint_requests_partner5 = 0
    #     p.participant.econ_hint_requests_partner6 = 0
    #     p.participant.econ_hint_requests_partner7 = 0
    #     p.participant.econ_hint_requests_partner8 = 0
    #     p.participant.cook_hint_requests_partner1 = 0
    #     p.participant.cook_hint_requests_partner2 = 0
    #     p.participant.cook_hint_requests_partner3 = 0
    #     p.participant.cook_hint_requests_partner4 = 0
    #     p.participant.cook_hint_requests_partner5 = 0
    #     p.participant.cook_hint_requests_partner6 = 0
    #     p.participant.cook_hint_requests_partner7 = 0
    #     p.participant.cook_hint_requests_partner8 = 0
    #     p.participant.sport_hint_requests_partner1 = 0
    #     p.participant.sport_hint_requests_partner2 = 0
    #     p.participant.sport_hint_requests_partner3 = 0
    #     p.participant.sport_hint_requests_partner4 = 0
    #     p.participant.sport_hint_requests_partner5 = 0
    #     p.participant.sport_hint_requests_partner6 = 0
    #     p.participant.sport_hint_requests_partner7 = 0
    #     p.participant.sport_hint_requests_partner8 = 0
    # #END DELETE

    if subsession.round_number == 1:
        # new_structure = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #Change this to whatever is randomization (because you want specific people...)
        # subsession.set_group_matrix(new_structure)
        for p in subsession.get_players():
            p.participant.task_rounds3b = dict()

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
        return dict(round=player.participant.round3b_completed)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + 4800

#MALE PREFERRED
class Hints_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP','results_economics_MP', 'results_cooking_MP', 'results_sports_MP','expect_hints_economics_MP', 'expect_hints_cooking_MP', 'expect_hints_sports_MP']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_MP', 'expect_hints_cooking_MP', 'expect_hints_sports_MP']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectationWR_MP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        wr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_female):
                wr_id = player.participant.pref_helper_female[key]
                wr = g.get_player_by_id(wr_id)
                break
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, wr=wr.participant.label, round=player.participant.round3b_completed)
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
        return (player.round_number == participant.task_rounds3b['MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        mr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_male):
                mr_id = player.participant.pref_helper_male[key]
                mr = g.get_player_by_id(mr_id)
                break
        partner = g.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_MP', 'expect_hints_cooking2_MP', 'expect_hints_sports2_MP']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MP','helpful_hint_econ1_MP','prob_econ1_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Increased in supply. Your helper has been notified.")}
            elif player.participant.econ_hint_requests_partner3 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MP','helpful_hint_econ2_MP','prob_econ2_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: He shouted, \"Is this a normal one?\". Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner3 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MP','helpful_hint_econ3_MP','prob_econ3_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: No influence. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner3 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MP','helpful_hint_econ4_MP','prob_econ4_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner3 += 1
            if player.participant.econ_hint_requests_partner3 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Factories have decided to pay workers higher incomes. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner3 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MP','helpful_hint_cook1_MP','prob_cook1_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Yellow and white. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner3 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MP','helpful_hint_cook2_MP','prob_cook2_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Maximum moisture. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner3 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MP','helpful_hint_cook3_MP','prob_cook3_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Everyone looked at the camera and said \"CHEEESE\". Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner3 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MP','helpful_hint_cook4_MP','prob_cook4_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner3 += 1
            if player.participant.cook_hint_requests_partner3 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Less than 2. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner3 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MP','helpful_hint_sport1_MP','prob_sport1_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: London and neighbor of Australia. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner3 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_MP','helpful_hint_sport2_MP','prob_sport2_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: South West. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner3 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MP','helpful_hint_sport3_MP','prob_sport3_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Ayub Khan. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner3 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_MP']) & (get_timeout_seconds1(player) > 0) & (participant.partner3 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MP','helpful_hint_sport4_MP','prob_sport4_MP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner3)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner3 += 1
            if player.participant.sport_hint_requests_partner3 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner3 += 1
                return {player.id_in_group: dict(message = "Hint: Green ball. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner3 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#MALE RANDOM
class Hints_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR','results_economics_MR', 'results_cooking_MR', 'results_sports_MR','expect_hints_economics_MR', 'expect_hints_cooking_MR', 'expect_hints_sports_MR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_MR', 'expect_hints_cooking_MR', 'expect_hints_sports_MR']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectationWR_MR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        wr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_female):
                wr_id = player.participant.pref_helper_female[key]
                wr = g.get_player_by_id(wr_id)
                break
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, wr=wr.participant.label, round=player.participant.round3b_completed)
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
        return (player.round_number == participant.task_rounds3b['MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        mr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_male):
                mr_id = player.participant.pref_helper_male[key]
                mr = g.get_player_by_id(mr_id)
                break
        partner = g.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_MR', 'expect_hints_cooking2_MR', 'expect_hints_sports2_MR']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_MR','helpful_hint_econ1_MR','prob_econ1_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Demand and supply. Your helper has been notified.")}
            elif player.participant.econ_hint_requests_partner8 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_MR','helpful_hint_econ2_MR','prob_econ2_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Demand and supply. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner8 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_MR','helpful_hint_econ3_MR','prob_econ3_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: 5 - 3 = ?. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner8 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_MR','helpful_hint_econ4_MR','prob_econ4_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner8 += 1
            if player.participant.econ_hint_requests_partner8 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: A few. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner8 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_MR','helpful_hint_cook1_MR','prob_cook1_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Citric acid. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner8 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_MR','helpful_hint_cook2_MR','prob_cook2_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Maize related product. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner8 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_MR','helpful_hint_cook3_MR','prob_cook3_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Extracted with olives. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner8 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_MR','helpful_hint_cook4_MR','prob_cook4_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner8 += 1
            if player.participant.cook_hint_requests_partner8 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Rhymes with pear. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner8 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_MR','helpful_hint_sport1_MR','prob_sport1_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: It was Allama Iqbal\'s birth year. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner8 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_MR','helpful_hint_sport2_MR','prob_sport2_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: We love orange. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner8 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_MR','helpful_hint_sport3_MR','prob_sport3_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Greater than 5. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner8 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_MR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_MR']) & (get_timeout_seconds1(player) > 0) & (participant.partner8 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_MR','helpful_hint_sport4_MR','prob_sport4_MR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner8)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner8 += 1
            if player.participant.sport_hint_requests_partner8 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner8 += 1
                return {player.id_in_group: dict(message = "Hint: Christopher. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner8 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#WOMAN PREFERRED
class Hints_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP','results_economics_WP', 'results_cooking_WP', 'results_sports_WP','expect_hints_economics_WP', 'expect_hints_cooking_WP', 'expect_hints_sports_WP']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_WP', 'expect_hints_cooking_WP', 'expect_hints_sports_WP']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectationWR_WP(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        wr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_female):
                wr_id = player.participant.pref_helper_female[key]
                wr = g.get_player_by_id(wr_id)
                break
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, wr=wr.participant.label, round=player.participant.round3b_completed)
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
        return (player.round_number == participant.task_rounds3b['WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        mr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_male):
                mr_id = player.participant.pref_helper_male[key]
                mr = g.get_player_by_id(mr_id)
                break
        partner = g.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_WP', 'expect_hints_cooking2_WP', 'expect_hints_sports2_WP']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WP','helpful_hint_econ1_WP','prob_econ1_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Ratio of dog owners to cat owners. Your helper has been notified.")}
            elif player.participant.econ_hint_requests_partner2 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WP','helpful_hint_econ2_WP','prob_econ2_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Long-run > short-run. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner2 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WP','helpful_hint_econ3_WP','prob_econ3_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: More is better. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner2 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WP','helpful_hint_econ4_WP','prob_econ4_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner2 += 1
            if player.participant.econ_hint_requests_partner2 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Supply shifts left and demand shifts right. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner2 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WP','helpful_hint_cook1_WP','prob_cook1_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Timing. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner2 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WP','helpful_hint_cook2_WP','prob_cook2_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: KFC fried chicken and french fries. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner2 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WP','helpful_hint_cook3_WP','prob_cook3_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Multiple of nine. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner2 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WP','helpful_hint_cook4_WP','prob_cook4_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner2 += 1
            if player.participant.cook_hint_requests_partner2 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Soak it. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner2 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WP','helpful_hint_sport1_WP','prob_sport1_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: Sharara. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner2 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_WP','helpful_hint_sport2_WP','prob_sport2_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: An ash tree. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner2 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WP','helpful_hint_sport3_WP','prob_sport3_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: During Great Depression. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner2 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WP(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_WP']) & (get_timeout_seconds1(player) > 0) & (participant.partner2 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WP','helpful_hint_sport4_WP','prob_sport4_WP']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner2)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner2 += 1
            if player.participant.sport_hint_requests_partner2 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner2 += 1
                return {player.id_in_group: dict(message = "Hint: There is no true lord. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner2 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

#WOMAN RANDOM
class Hints_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player: Player):
        import random
        formfields = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR','results_economics_WR', 'results_cooking_WR', 'results_sports_WR','expect_hints_economics_WR', 'expect_hints_cooking_WR', 'expect_hints_sports_WR']
        return formfields
    def vars_for_template(player: Player):
        formfields_hints = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR']
        random.shuffle(formfields_hints)
        formfields_results = ['results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
        random.shuffle(formfields_results)
        formfields_expect = ['expect_hints_economics_WR', 'expect_hints_cooking_WR', 'expect_hints_sports_WR']
        random.shuffle(formfields_expect)
        g = player.group
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(formfields_hints=formfields_hints, formfields_results=formfields_results, formfields_expect=formfields_expect, partner=partner.participant.label, round=player.participant.round3b_completed)

class ExpectationWR_WR(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        wr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_female):
                wr_id = player.participant.pref_helper_female[key]
                wr = g.get_player_by_id(wr_id)
                break
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, wr=wr.participant.label, round=player.participant.round3b_completed)
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
        return (player.round_number == participant.task_rounds3b['WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        mr = 0
        int = list(range(1, 19))
        random.shuffle(int)
        for key in int:
            if (key in player.participant.pref_helper_male):
                mr_id = player.participant.pref_helper_male[key]
                mr = g.get_player_by_id(mr_id)
                break
        partner = g.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, mr=mr.participant.label, round=player.participant.round3b_completed)
    @staticmethod
    def get_form_fields(player: Player):
        import random

        form_fields = ['expect_hints_economics2_WR', 'expect_hints_cooking2_WR', 'expect_hints_sports2_WR']
        random.shuffle(form_fields)
        return form_fields
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics1_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics1_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics1_WR','helpful_hint_econ1_WR','prob_econ1_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Labor as a cost of production. Your helper has been notified.")}
            elif player.participant.econ_hint_requests_partner6 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics2_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics2_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2_WR','helpful_hint_econ2_WR','prob_econ2_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Quantity demanded > quantity supplied. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner6 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics3_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics3_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics3_WR','helpful_hint_econ3_WR','prob_econ3_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Consumer is king. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner6 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Economics4_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Economics4_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics4_WR','helpful_hint_econ4_WR','prob_econ4_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.econ_hint_requests_partner6 += 1
            if player.participant.econ_hint_requests_partner6 <= partner.participant.hints_given_econ:
                player.participant.econ_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Easy to join. Your helper will be notified that you requested a hint.")}
            elif player.participant.econ_hint_requests_partner6 > partner.participant.hints_given_econ:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking1_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1_WR','helpful_hint_cook1_WR','prob_cook1_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Get low. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner6 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking2_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking2_WR','helpful_hint_cook2_WR','prob_cook2_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: BRRRRRR. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner6 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking3_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking3_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking3_WR','helpful_hint_cook3_WR','prob_cook3_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Mist or fog. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner6 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking4_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Cooking4_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking4_WR','helpful_hint_cook4_WR','prob_cook4_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.cook_hint_requests_partner6 += 1
            if player.participant.cook_hint_requests_partner6 <= partner.participant.hints_given_cook:
                player.participant.cook_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Qeema. Your helper will be notified that you requested a hint.")}
            elif player.participant.cook_hint_requests_partner6 > partner.participant.hints_given_cook:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports1_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports1_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports1_WR','helpful_hint_sport1_WR','prob_sport1_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Pakistan gained independence in 1947. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner6 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports2_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports2_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2_WR','helpful_hint_sport2_WR','prob_sport2_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Eclipse. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner6 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports3_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports3_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports3_WR','helpful_hint_sport3_WR','prob_sport3_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Death year of Fatima Jinnah. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner6 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Sports4_WR(Page):
    form_model = 'player'
    def vars_for_template(player: Player):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        return dict(partner=partner.participant.label, round_number = player.round_number - 1, round=player.participant.round3b_completed)
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds3b['Sports4_WR']) & (get_timeout_seconds1(player) > 0) & (participant.partner6 != 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports4_WR','helpful_hint_sport4_WR','prob_sport4_WR']
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        partner = group.get_player_by_id(player.participant.partner6)
        set_hints_given(player,partner)
        if data == 'clicked-button':
            player.participant.sport_hint_requests_partner6 += 1
            if player.participant.sport_hint_requests_partner6 <= partner.participant.hints_given_sport:
                player.participant.sport_hint_used_partner6 += 1
                return {player.id_in_group: dict(message = "Hint: Soon after WWI. Your helper will be notified that you requested a hint.")}
            elif player.participant.sport_hint_requests_partner6 > partner.participant.hints_given_sport:
                return {player.id_in_group: dict(message = "Hint is available, but the helper has not released it")}
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Final(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 49
    @staticmethod
    def vars_for_template(player:Player):
        return dict(round=player.participant.round3b_completed)
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.participant.round3b_completed = 1
        if len(upcoming_apps) >= 3:
            int = list(range(0, 3))
        else:
            int = list(range(0, len(upcoming_apps)))
        random.shuffle(int)
        for i in range(len(int)):
            if ('___Round2_' in upcoming_apps[int[i]]) and (player.participant.round2_completed == 0):
                player.participant.round2_completed = 4
                return upcoming_apps[int[i]]
        return '___Final_'


page_sequence = [Demographics, Hints_MP, ExpectationWR_MP, ExpectationMR_MP,
Economics1_MP, Economics2_MP, Economics3_MP, Economics4_MP, Cooking1_MP, Cooking2_MP,
Cooking3_MP, Cooking4_MP, Sports1_MP, Sports2_MP, Sports3_MP, Sports4_MP, Hints_MR,
ExpectationWR_MR, ExpectationMR_MR, Economics1_MR, Economics2_MR, Economics3_MR,
Economics4_MR, Cooking1_MR, Cooking2_MR, Cooking3_MR, Cooking4_MR, Sports1_MR,
Sports2_MR, Sports3_MR, Sports4_MR, Hints_WP, ExpectationWR_WP, ExpectationMR_WP,
Economics1_WP, Economics2_WP, Economics3_WP, Economics4_WP, Cooking1_WP, Cooking2_WP,
Cooking3_WP, Cooking4_WP, Sports1_WP, Sports2_WP, Sports3_WP, Sports4_WP, Hints_WR,
ExpectationWR_WR, ExpectationMR_WR, Economics1_WR, Economics2_WR, Economics3_WR,
Economics4_WR, Cooking1_WR, Cooking2_WR, Cooking3_WR, Cooking4_WR, Sports1_WR,
Sports2_WR, Sports3_WR, Sports4_WR, Final]
