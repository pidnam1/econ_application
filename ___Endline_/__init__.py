from otree.api import *
import random



class C(BaseConstants):
    NAME_IN_URL = '___Endline_'
    PLAYERS_PER_GROUP = None
    TASKS = ['Economics', 'Cooking', 'Sports']
    ECONSUBTASKS = ['Economics1','Economics2']
    COOKSUBTASKS = ['Cooking1','Cooking2']
    SPORTSUBTASKS = ['Sports1','Sports2']
    NUM_ROUNDS = len(TASKS)*2
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_field_time_spent(label):
    return models.IntegerField(
        label=label, initial = 0, min=0, max=24,
    )

class Player(BasePlayer):
    dob = models.StringField(label='What is your date of birth?')
    high_edu = models.IntegerField(
        choices=[[0, 'Matric'], [1, 'FA/FSc'], [2, 'BA/BSc.'], [99, 'Other (specify on the next page)']],
        label='Before the current degree that you are studying, what was the highest qualification that you attained?',
        widget=widgets.RadioSelect,
    )
    high_edu_other = models.StringField(
        label='You selected \'Other\'. Please specify. Before the current degree that you are studying, what was the highest qualification that you attained?',
    )
    subject_prior = models.IntegerField(
        choices=[[0, 'Economics'], [1, 'Law'], [2, 'MBBS'], [3, 'Commerce'], [4, 'Public Administration'], [99, 'Other (specify on the next page)']],
        label='What was your subject before you began at your current university?',
        widget=widgets.RadioSelect,
    )
    subject_prior_other = models.StringField(
        label='You selected \'Other\'. Please specify. What was your subject before you began at your current university?',
    )
    high_edu_school = models.StringField(
        label='Please state the name of your school/college from where you got the highest qualification',
    )
    rank_prior = models.StringField(
        label='Can you recall your rank in the last qualification you had?',
    )
    extra_curric = models.IntegerField(
        choices=[[0, 'Drama'], [1, 'Team sports (For example, cricket, football are played in a team and so would count as team sports)'],
        [2, 'Individual Sports (For example, rock climbing is done individually and so something like rock climbing would be individual sports)'],
        [3, 'Music'], [4, 'Dance'], [5, 'Debates'], [6, 'Home economics'], [7, 'Painting'], [8, 'Chess'], [99, 'Other (specify on the next page)']],
        label='Can you list the main extra-curricular activities that you are involved in?',
        widget=widgets.RadioSelect,
    )
    extra_curric_other = models.StringField(
        label='You selected \'Other\'. Please specify. Can you list the main extra-curricular activities that you are involved in?',
    )
    degree_aspire = models.IntegerField(
        choices=[[0, 'MBA'], [1, 'Masters in Public Administration'], [2, 'Masters in Commerce'], [3, 'Masters in Economics'], [4, 'Masters in Finance'],
        [5, 'Masters in Human Resources'], [6, 'PhD in Business Administration'], [7, 'PhD in Public Administration'], [8, 'PhD in Commerce'],
        [9, 'PhD in Economics'], [10, 'PhD in Finance'], [11, 'PhD in Human Resources'], [99, 'Other (specify on the next page)']],
        label='What is the maximum degree that you aspire to achieve?',
        widget=widgets.RadioSelect,
    )
    degree_aspire_other = models.StringField(
        label='You selected \'Other\'. Please specify. What is the maximum degree that you aspire to achieve?',
    )
    pref_occu = models.IntegerField(
        choices=[[0, 'Government job through CSS'], [1, 'Government job through PMS'], [2, 'Private job in a bank'],
        [3, 'Private job in a multi-national'], [99, 'Other (specify on the next page)']],
        label='List the main occupations that you would be interested in choosing for a career.',
        widget=widgets.RadioSelect,
    )
    pref_occu_other = models.StringField(
        label='You selected \'Other\'. Please specify. List the main occupations that you would be interested in choosing for a career.',
    )
    why_pref_occu = models.StringField(
        label='Why this occupation?',
    )
    study_abroad = models.IntegerField(
        choices=[[0, 'Yes'], [1, 'No']],
        label='Have you ever studied abroad?',
        widget=widgets.RadioSelect,
    )
    study_abroad_yes = models.StringField(
        label='You selected \'Yes\'. Please specify. Where have you studied abroad?',
    )
    cook_time = make_field_time_spent('Cooking food')
    study_time = make_field_time_spent('Studying for your degree')
    sport_time = make_field_time_spent('Sports')
    clean_time = make_field_time_spent('Cleaning the house')
    dish_time = make_field_time_spent('Washing dishes')
    iron_time = make_field_time_spent('Ironing clothes')
    laundry_time = make_field_time_spent('Washing clothes')
    care_time = make_field_time_spent('Physically taking care of family members (e.g. children, grandparents, parents etc.)')
    eat_time = make_field_time_spent('Eating')
    tv_time = make_field_time_spent('Watching TV')
    phone_time = make_field_time_spent('Talking on phone with friends')
    socialmedia_time = make_field_time_spent('On social media')
    news_time = make_field_time_spent('Reading newspapers')
    read_time = make_field_time_spent('Reading for fun')
    social_time = make_field_time_spent('Being out with friends for fun')
    sleep_time = make_field_time_spent('Sleeping')
    smoke_time = make_field_time_spent('Smoking')
    nothing_time = make_field_time_spent('Doing nothing at all')
    other_time = make_field_time_spent('Other (please specify)')
    friend_count = models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'],  [99, 'Other (specify on the next page)']],
        label='How many total friends do you have with whom you are in touch at least once a week?',
        widget=widgets.RadioSelect,
    )
    friend_count_other = models.StringField(
        label='You selected \'Other\'. Please specify. How many total friends do you have with whom you are in touch at least once a week?',
    )
    friend_uni = models.IntegerField(
        label='Out of those above how many are in your current university?',
    )
    #MAKE ANY FORMFIELDS NEEDED FOR FRIEND TABLE
    class_relationship_image = models.StringField()
    school_relationship_image = models.StringField()
    know_rank = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='In general, would you say students know the academic rank of others in a class?',
    )
    know_gpa = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='In general, would you say students know the GPA of others in a class?',
    )

    #Section B
    subjects_like = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='Which of the categories tested did you like the most?',
    )
    subjects_dislike = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='Which of the categories tested did you like the least?',
    )
    subjects_correct = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='For which of the categories tested you think you have given most correct answers?',
    )
    subjects_notcorrect = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='For which of the categories tested you think you have given least correct answers?',
    )
    hints_always_helper = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='Did you always ask for hints from helpers when you felt the need?',
    )
    hints_always_helper_no = models.IntegerField(
        choices=[[1, 'If I asked too many times, I felt that the helper would think I don\'t know much'],
        [2, 'If I asked too many times, I felt that others in the room (not helpers) would think I don\'t know much'],
        [3, 'I did not think a hint would help'], [4, 'I ran out of time']],
        label='You selected \'No\'. Please specify. What was the main reason that you did not ask for hints from helpers?',
    )
    hints_always = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='In the round when you were not working with a helper but were looking for your own hints, did you always use the hints for answers, whenever you felt the need for it?',
    )
    hints_always_no = models.IntegerField(
        choices=[[1, 'If I pressed too many times, I felt that I might come across as someone who doesn\'t know much'],
        [2, 'I did not think a hint would help'], [3, 'I ran out of time']],
        label='You selected \'No\'. Please specify. What was the reason that you did not press the "Ask for hint" button?',
    )
    #MAKE ANY FORMFIELDS NEEDED FOR HELPER TABLE

    #Section C
    tt_perception = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='Do you think the test-takers never hesitated and always asked for hints when they felt the need?',
    )
    tt_perception_no = models.IntegerField(
        choices=[[1, 'If he or she asked too many times, they might have felt that I would think he or she is stupid'],
        [2, 'If he or she asked too many times, they might have felt that others in the room (not me) would think he or she is stupid'],
        [3, 'He or she did not think a hint would help'], [4, 'He or she ran out of time'], [5, 'He or she wasn\'t a close friend']],
        label='You selected \'No\'. Please specify. What do you think was the main reason that they did not ask for hints from helpers?',
    )
    decide_hints = models.IntegerField(
        label='How did you decide how many hints to give to the test-takers you were matched with?',
    )
    diff_why = models.IntegerField(
        label='Did you make different choices when your payment depended on the performance of the test-taker? Why or why not?',
    )

    #Section D
    #MAKE ANY FORMFIELDS NEEDED FOR GENDER TABLE
    #Weird question?
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    caste = models.StringField(
        choices=[['Jatt', 'Jatt'], ['Rajput', 'Rajput'], ['Arain', 'Arain'], [99, 'Other (specify on the next page)']],
        label='What is your caste?',
        widget=widgets.RadioSelect,
    )
    caste_other = models.StringField(
        label='You selected \'Other\'. Please specify. What is your caste?',
    )
    religion = models.StringField(
        label='What is your religion?',
    )
    marital_status = models.IntegerField(
        choices=[[0, 'Married in monogamy (single wife)'], [1, 'Married in polygamy (multiple wives)'], [2, 'Unmarried'],
        [3,'Divorced'], [4, 'Separated'], [99, 'Other (specify on the next page)']],
        label='What is your marital status?',
        widget=widgets.RadioSelect,
    )
    marital_status_other = models.StringField(
        label='You selected \'Other\'. Please specify. What is your marital status?',
    )
    children = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='Do you have children?',
        widget=widgets.RadioSelect,
    )
    children_yes = models.StringField(
        label='You selected \'Yes\' to \'Do you have children?\'. Please specify. How old are your children?',
    )
    lang = models.IntegerField(
        choices=[[0, 'English'], [1, 'Urdu'], [2, 'Punjabi'], [3,'Pushto'], [4, 'Sindhi'], [99, 'Other/Multiple (specify on the next page)']],
        label='What language do you normally speak at home?',
        widget=widgets.RadioSelect,
    )
    lang_other = models.StringField(
        label='You selected \'Other/Multiple\'. Please specify. What language(s) do you normally speak at home?',
    )
    father_occu = models.IntegerField(
        choices=[[1, 'Doctor'], [2, 'Works in a factory'], [3, 'Works in a shop'], [4,'Engineer'], [5, 'Lawyer'],
        [6,'Owns a shop'], [7,'\'Kissan\''], [8, 'Private business'], [9,'Government job'], [99, 'Other (specify on the next page)']],
        label='What does your father do?',
        widget=widgets.RadioSelect,
    )
    father_occu_other = models.StringField(
        label='You selected \'Other\'. Please specify. What does your father do?',
    )
    mother_occu = models.IntegerField(
        choices=[[0,'House-wife'], [1, 'Doctor'], [2, 'Works in a factory'], [3, 'Works in a shop'], [4,'Engineer'], [5, 'Lawyer'],
        [6,'Owns a shop'], [7,'\'Kissan\''], [8, 'Private business'], [9,'Government job'], [99, 'Other (specify on the next page)']],
        label='What does your mother do?',
        widget=widgets.RadioSelect,
    )
    mother_occu_other = models.StringField(
        label='You selected \'Other\'. Please specify. What does your mother do?',
    )
    in_house = models.IntegerField(
        label='How many people live in your house?'
    )
    origin = models.IntegerField(
        choices=[[0, 'Lahore'], [1, 'Faisalabad'], [2, 'Sialkot'], [3,'Gujranwala'], [4, 'Attock'], [5,'Bahawalpur'], [6,'Bahawalnagar'],
        [7, 'Sheikhupura'], [8,'Kasur'], [9,'Rawalpindi'], [10, 'Sialkot'], [99, 'Other (specify on the next page)']],
        label='Where are you originally from?',
        widget=widgets.RadioSelect,
    )
    origin_other = models.StringField(
        label='You selected \'Other\'. Please specify. Where are you originally from?',
    )
    monthly_income = models.IntegerField(
        choices=[[0, 'Less than Rs. 10,000 per month'], [1, 'Rs.10,000 to less than Rs. 20,0000 per month'], [2, 'Rs.20,000 to less than Rs. 30,0000 per month'],
        [3,'Rs.30,000 to less than Rs. 40,0000 per month'], [4, 'Rs.40,000 to less than Rs. 50,0000 per month'], [5,'Rs.50,000 to less than Rs. 60,0000 per month'],
        [6,'Rs.60,000 to less than Rs. 70,0000 per month'], [7, 'Rs.70,000 to less than Rs. 80,0000 per month'], [8,'Rs.80,000 to less than Rs. 90,0000 per month'],
        [9,'Rs.90,000 to less than Rs. 100,0000 per month'], [10, 'Greater than Rs. 100,000 per month']],
        label='In what bracket does your families\' total monthly income fall?',
        widget=widgets.RadioSelect,
    )

    #Section D Part 2
    lost_wallet_personal = models.IntegerField(
        choices=[[1, '1   Very Unlikely'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very likely']],
        label='Imagine that you lost your wallet close to your house. This had Rs. 500 and was found by someone who lives close to you and KNOWS YOU PERSONALLY. The wallet has a document that identifies you. How likely do you find that this person gives you the wallet back with the money in it?',
        widget=widgets.RadioSelect,
    )
    lost_wallet_impersonal = models.IntegerField(
        choices=[[1, '1   Very Unlikely'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very likely']],
        label='Imagine that you lost your wallet close to your house. This had Rs. 500 and was found by someone who lives close to you but who DOESN’T KNOW YOU PERSONALLY. The wallet has a document that identifies you. How likely do you find that this person gives you the wallet back with the money in it?',
        widget=widgets.RadioSelect,
    )
    scarcity = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='When jobs are scarce, men should have more right to a job than women.',
        widget=widgets.RadioSelect,
    )
    women_money = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='If a woman earns more money than her husband, it\'s almost certain to cause problems.',
        widget=widgets.RadioSelect,
    )
    women_independence = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='Having a job is the best way for a woman to be an independent person.',
        widget=widgets.RadioSelect,
    )
    parental_pride = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='One of my main goals in life has been to make my parents proud.',
        widget=widgets.RadioSelect,
    )
    children_suffer = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='When a mother works for pay, the children suffer.',
        widget=widgets.RadioSelect,
    )
    men_politicians = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='On the whole, men make better political leaders than women do.',
        widget=widgets.RadioSelect,
    )
    uni_gender = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='A university education is more important for a boy than for a girl.',
        widget=widgets.RadioSelect,
    )
    busi_gender = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='On the whole, men make better business executives than women do.',
        widget=widgets.RadioSelect,
    )
    house_fulfill = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='Being a housewife is just as fulfilling as working for pay.',
        widget=widgets.RadioSelect,
    )
    family_customs = models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label='To follow customs handed down by one’s family is very important.',
        widget=widgets.RadioSelect,
    )
    free_choice = models.IntegerField(
        choices=[[1, '1   No choice at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   A great deal of choice']],
        label='Some people feel they have completely free choice and control over their lives, while other people feel that what they do has no real effect on what happens to them. Please use this scale where 1 means "no choice at all" and 10 means "a great deal of choice" to indicate how much freedom of choice and control you feel you have over the way your life turns out.',
        widget=widgets.RadioSelect,
    )
    justify_divorce = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Divorce',
        widget=widgets.RadioSelect,
    )
    justify_lying = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Lying',
        widget=widgets.RadioSelect,
    )
    justify_beatwife = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='For a man to beat his wife',
        widget=widgets.RadioSelect,
    )
    justify_beatchild = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Parents beating children',
        widget=widgets.RadioSelect,
    )
    justify_violence = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Violence against other people',
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, 4))
            random.shuffle(round_numbers)
            task_round = dict(zip(C.TASKS, round_numbers))

            sub_round_number1 = list(range(1, 3))
            random.shuffle(sub_round_number1)
            sub_round_number2 = list(range(3, 5))
            random.shuffle(sub_round_number2)
            sub_round_number3 = list(range(5, 7))
            random.shuffle(sub_round_number3)

            p.participant.task_rounds_prac = dict()

            econ_round_number = task_round['Economics']
            if econ_round_number == 1:
                task_rounds_econ1 = dict(zip(C.ECONSUBTASKS, sub_round_number1))
                p.participant.task_rounds_prac.update(task_rounds_econ1)
            elif econ_round_number == 2:
                task_rounds_econ2 = dict(zip(C.ECONSUBTASKS, sub_round_number2))
                p.participant.task_rounds_prac.update(task_rounds_econ2)
            elif econ_round_number == 3:
                task_rounds_econ3 = dict(zip(C.ECONSUBTASKS, sub_round_number3))
                p.participant.task_rounds_prac.update(task_rounds_econ3)

            cook_round_number = task_round['Cooking']
            if cook_round_number == 1:
                task_rounds_cook1 = dict(zip(C.COOKSUBTASKS, sub_round_number1))
                p.participant.task_rounds_prac.update(task_rounds_cook1)
            elif cook_round_number == 2:
                task_rounds_cook2 = dict(zip(C.COOKSUBTASKS, sub_round_number2))
                p.participant.task_rounds_prac.update(task_rounds_cook2)
            elif cook_round_number == 3:
                task_rounds_cook3 = dict(zip(C.COOKSUBTASKS, sub_round_number3))
                p.participant.task_rounds_prac.update(task_rounds_cook3)

            sport_round_number = task_round['Sports']
            if sport_round_number == 1:
                task_rounds_sport1 = dict(zip(C.SPORTSUBTASKS, sub_round_number1))
                p.participant.task_rounds_prac.update(task_rounds_sport1)
            elif sport_round_number == 2:
                task_rounds_sport2 = dict(zip(C.SPORTSUBTASKS, sub_round_number2))
                p.participant.task_rounds_prac.update(task_rounds_sport2)
            elif sport_round_number == 3:
                task_rounds_sport3 = dict(zip(C.SPORTSUBTASKS, sub_round_number3))
                p.participant.task_rounds_prac.update(task_rounds_sport3)


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
        participant.expiry = time.time() + 1200

class Economics1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Economics1']) & (get_timeout_seconds1(player) > 0)
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
        return (player.round_number == participant.task_rounds_prac['Economics2']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_economics2','helpful_hint_econ2','prob_econ2']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking1(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Cooking1']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_cooking1','helpful_hint_cook1','prob_cook1']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Cooking2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds_prac['Cooking2']) & (get_timeout_seconds1(player) > 0)
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
        return (player.round_number == participant.task_rounds_prac['Sports1']) & (get_timeout_seconds1(player) > 0)
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
        return (player.round_number == participant.task_rounds_prac['Sports2']) & (get_timeout_seconds1(player) > 0)
    @staticmethod
    def get_form_fields(player):
        return ['crt_sports2','helpful_hint_sport2','prob_sport2']
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT

class Belief(Page):
    form_model = 'player'
    form_fields = ['belief1','belief2']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 6
    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(belief1=2, belief2=1)

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

page_sequence = [Demographics, Economics1, Economics2, Cooking1, Cooking2, Sports1,
Sports2, Belief, Results]
