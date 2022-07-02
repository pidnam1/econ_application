from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = '___Endline_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

#FUNCTIONS
def make_field_time_spent(label):
    return models.IntegerField(
        label=label, initial = 0, min=0, max=24,
    )
def make_field_likert(label):
    return models.IntegerField(
        choices=[[1, 'Strongly Agree'], [2, 'Agree'], [3, 'Neutral'], [4, 'Disagree'], [5, 'Strongly Disagree']],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

def make_field_multiple_price():
    return models.IntegerField(
        choices=[[1, 'Option A'], [2, 'Option B']],
    )

def make_field_wtp():
    return models.IntegerField(
        choices=[1,2,3],label='',
        blank=True
    )

def make_image_data(image_names):
    return [dict(name=name, path='{}'.format(name)) for name in image_names]

class Player(BasePlayer):
    dob = models.StringField(label='1. What is your date of birth? (Please list as YYYY/MM/DD)')
    high_edu = models.IntegerField(
        choices=[[0, 'Matric'], [1, 'FA/FSc'], [2, 'BA/BSc.'], [99, 'Other (specify on the next page)']],
        label='2. Before the current degree that you are studying, what was the highest qualification that you attained?',
        widget=widgets.RadioSelect,
    )
    high_edu_other = models.StringField(
        label='2. You selected \'Other\'. Please specify. Before the current degree that you are studying, what was the highest qualification that you attained?',
    )
    subject_prior = models.IntegerField(
        choices=[[0, 'Economics'], [1, 'Law'], [2, 'MBBS'], [3, 'Commerce'], [4, 'Public Administration'], [99, 'Other (specify on the next page)']],
        label='3. What was your subject before you began at your current university?',
        widget=widgets.RadioSelect,
    )
    subject_prior_other = models.StringField(
        label='3. You selected \'Other\'. Please specify. What was your subject before you began at your current university?',
    )
    high_edu_school = models.StringField(
        label='4. Please state the name of your school/college from where you got the highest qualification',
    )
    rank_prior = models.StringField(
        label='5. Can you recall your rank in the last qualification you had?',
    )
    extra_curric = models.IntegerField(
        choices=[[0, 'Drama'], [1, 'Team sports (For example, cricket, football are played in a team and so would count as team sports)'],
        [2, 'Individual Sports (For example, rock climbing is done individually and so something like rock climbing would be individual sports)'],
        [3, 'Music'], [4, 'Dance'], [5, 'Debates'], [6, 'Home economics'], [7, 'Painting'], [8, 'Chess'], [99, 'Other (specify on the next page)']],
        label='6. Can you list the main extra-curricular activities that you are involved in?',
        widget=widgets.RadioSelect,
    )
    extra_curric_other = models.StringField(
        label='6. You selected \'Other\'. Please specify. Can you list the main extra-curricular activities that you are involved in?',
    )
    degree_aspire = models.IntegerField(
        choices=[[0, 'MBA'], [1, 'Masters in Public Administration'], [2, 'Masters in Commerce'], [3, 'Masters in Economics'], [4, 'Masters in Finance'],
        [5, 'Masters in Human Resources'], [6, 'PhD in Business Administration'], [7, 'PhD in Public Administration'], [8, 'PhD in Commerce'],
        [9, 'PhD in Economics'], [10, 'PhD in Finance'], [11, 'PhD in Human Resources'], [99, 'Other (specify on the next page)']],
        label='7. What is the maximum degree that you aspire to achieve?',
        widget=widgets.RadioSelect,
    )
    degree_aspire_other = models.StringField(
        label='7. You selected \'Other\'. Please specify. What is the maximum degree that you aspire to achieve?',
    )
    pref_occu = models.IntegerField(
        choices=[[0, 'Government job through CSS'], [1, 'Government job through PMS'], [2, 'Private job in a bank'],
        [3, 'Private job in a multi-national'], [99, 'Other (specify on the next page)']],
        label='8. List the main occupations that you would be interested in choosing for a career.',
        widget=widgets.RadioSelect,
    )
    pref_occu_other = models.StringField(
        label='8. You selected \'Other\'. Please specify. List the main occupations that you would be interested in choosing for a career.',
    )
    why_pref_occu = models.StringField(
        label='9. Why this occupation?',
    )
    study_abroad = models.IntegerField(
        choices=[[0, 'Yes'], [1, 'No']],
        label='10. Have you ever studied abroad?',
        widget=widgets.RadioSelect,
    )
    study_abroad_yes = models.StringField(
        label='10. You selected \'Yes\'. Please specify. Where have you studied abroad?',
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
        label='11. How many total friends do you have with whom you are in touch at least once a week?',
        widget=widgets.RadioSelect,
    )
    friend_count_other = models.StringField(
        label='11. You selected \'Other\'. Please specify. How many total friends do you have with whom you are in touch at least once a week?',
    )
    friend_uni = models.IntegerField(
        label='12. Out of those above how many are in your current university?',
    )
    #MAKE ANY FORMFIELDS NEEDED FOR FRIEND TABLE
    friend_roll1 = models.IntegerField(label='', blank=True)
    friend_roll2 = models.IntegerField(label='', blank=True)
    friend_roll3 = models.IntegerField(label='', blank=True)
    friend_roll4 = models.IntegerField(label='', blank=True)
    friend_roll5 = models.IntegerField(label='', blank=True)
    friend_roll6 = models.IntegerField(label='', blank=True)
    friend_roll7 = models.IntegerField(label='', blank=True)
    friend_roll8 = models.IntegerField(label='', blank=True)
    friend_roll9 = models.IntegerField(label='', blank=True)
    friend_roll10 = models.IntegerField(label='', blank=True)
    friend_name1 = models.StringField(label='', blank=True)
    friend_name2 = models.StringField(label='', blank=True)
    friend_name3 = models.StringField(label='', blank=True)
    friend_name4 = models.StringField(label='', blank=True)
    friend_name5 = models.StringField(label='', blank=True)
    friend_name6 = models.StringField(label='', blank=True)
    friend_name7 = models.StringField(label='', blank=True)
    friend_name8 = models.StringField(label='', blank=True)
    friend_name9 = models.StringField(label='', blank=True)
    friend_name10 = models.StringField(label='', blank=True)
    friend_section1 = models.StringField(label='', blank=True)
    friend_section2 = models.StringField(label='', blank=True)
    friend_section3 = models.StringField(label='', blank=True)
    friend_section4 = models.StringField(label='', blank=True)
    friend_section5 = models.StringField(label='', blank=True)
    friend_section6 = models.StringField(label='', blank=True)
    friend_section7 = models.StringField(label='', blank=True)
    friend_section8 = models.StringField(label='', blank=True)
    friend_section9 = models.StringField(label='', blank=True)
    friend_section10 = models.StringField(label='', blank=True)
    friend_years1 = models.IntegerField(label='', blank=True)
    friend_years2 = models.IntegerField(label='', blank=True)
    friend_years3 = models.IntegerField(label='', blank=True)
    friend_years4 = models.IntegerField(label='', blank=True)
    friend_years5 = models.IntegerField(label='', blank=True)
    friend_years6 = models.IntegerField(label='', blank=True)
    friend_years7 = models.IntegerField(label='', blank=True)
    friend_years8 = models.IntegerField(label='', blank=True)
    friend_years9 = models.IntegerField(label='', blank=True)
    friend_years10 = models.IntegerField(label='', blank=True)

    class_relationship_image = models.StringField(blank=True)
    school_relationship_image = models.StringField(blank=True)
    know_rank = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='In general, would you say students know the academic rank of others in a class?',
        widget=widgets.RadioSelect,
    )
    know_gpa = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='In general, would you say students know the GPA of others in a class?',
        widget=widgets.RadioSelect,
    )

    #Section B
    subjects_like = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='Which of the categories tested did you like the most?',
        widget=widgets.RadioSelect,
    )
    subjects_dislike = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='Which of the categories tested did you like the least?',
        widget=widgets.RadioSelect,
    )
    subjects_correct = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='For which of the categories tested you think you have given most correct answers?',
        widget=widgets.RadioSelect,
    )
    subjects_incorrect = models.IntegerField(
        choices=[[1, 'Sports'], [2, 'Economics'], [3, 'Cooking']],
        label='For which of the categories tested you think you have given least correct answers?',
        widget=widgets.RadioSelect,
    )
    hints_always_helper = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='Did you always ask for hints from helpers when you felt the need?',
        widget=widgets.RadioSelect,
    )
    hints_always_helper_no = models.IntegerField(
        choices=[[1, 'If I asked too many times, I felt that the helper would think I don\'t know much'],
        [2, 'If I asked too many times, I felt that others in the room (not helpers) would think I don\'t know much'],
        [3, 'I did not think a hint would help'], [4, 'I ran out of time']],
        label='You selected \'No\'. Please specify. What was the main reason that you did not ask for hints from helpers?',
        widget=widgets.RadioSelect,
    )
    hints_always = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='In the round when you were not working with a helper but were looking for your own hints, did you always use the hints for answers, whenever you felt the need for it?',
        widget=widgets.RadioSelect,
    )
    hints_always_no = models.IntegerField(
        choices=[[1, 'If I pressed too many times, I felt that I might come across as someone who doesn\'t know much'],
        [2, 'I did not think a hint would help'], [3, 'I ran out of time']],
        label='You selected \'No\'. Please specify. What was the reason that you did not press the "Ask for hint" button?',
        widget=widgets.RadioSelect,
    )
    #MAKE ANY FORMFIELDS NEEDED FOR HELPER TABLE
    helper_ranking1 = models.StringField(label='',blank=True)
    helper_ranking2 = models.StringField(label='',blank=True)
    helper_ranking3 = models.StringField(label='',blank=True)
    helper_ranking4 = models.StringField(label='',blank=True)
    helper_ranking5 = models.StringField(label='',blank=True)
    helper_ranking6 = models.StringField(label='',blank=True)
    helper_ranking7 = models.StringField(label='',blank=True)
    helper_ranking8 = models.StringField(label='',blank=True)
    helper_reason1 = models.IntegerField(label='',blank=True)
    helper_reason2 = models.IntegerField(label='',blank=True)
    helper_reason3 = models.IntegerField(label='',blank=True)
    helper_reason4 = models.IntegerField(label='',blank=True)
    helper_reason5 = models.IntegerField(label='',blank=True)
    helper_reason6 = models.IntegerField(label='',blank=True)
    helper_reason7 = models.IntegerField(label='',blank=True)
    helper_reason8 = models.IntegerField(label='',blank=True)


    #Section C
    tt_perception = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='Do you think the test-takers never hesitated and always asked for hints when they felt the need?',
        widget=widgets.RadioSelect,
    )
    tt_perception_no = models.IntegerField(
        choices=[[1, 'If he or she asked too many times, they might have felt that I would think he or she is stupid'],
        [2, 'If he or she asked too many times, they might have felt that others in the room (not me) would think he or she is stupid'],
        [3, 'He or she did not think a hint would help'], [4, 'He or she ran out of time'], [5, 'He or she wasn\'t a close friend']],
        label='You selected \'No\'. Please specify. What do you think was the main reason that they did not ask for hints from helpers?',
        widget=widgets.RadioSelect,
    )
    decide_hints = models.StringField(
        label='How did you decide how many hints to give to the test-takers you were matched with?',
    )
    diff_why = models.StringField(
        label='Did you make different choices when your payment depended on the performance of the test-taker? Why or why not?',
    )

    #Section D
    #MAKE ANY FORMFIELDS NEEDED FOR GENDER TABLE
    gender_sports = models.IntegerField(
        choices=[[-1, 'Women know more'], [0, 'No gender difference'], [1, 'Men know more']],
        label='Sports?',
        widget=widgets.RadioSelect,
    )
    gender_economics = models.IntegerField(
        choices=[[-1, 'Women know more'], [0, 'No gender difference'], [1, 'Men know more']],
        label='Economics?',
        widget=widgets.RadioSelect,
    )
    gender_cooking = models.IntegerField(
        choices=[[-1, 'Women know more'], [0, 'No gender difference'], [1, 'Men know more']],
        label='Cooking?',
        widget=widgets.RadioSelect,
    )

    amount_notgame = models.IntegerField(
        label='Out of Rs.300, amount NOT to be used in the game'
    )
    amount_game = models.IntegerField(
        label='Out of Rs.300, amount to be used in the game'
    )
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='1. What is your gender?',
        widget=widgets.RadioSelect,
    )
    caste = models.StringField(
        choices=[['Jatt', 'Jatt'], ['Rajput', 'Rajput'], ['Arain', 'Arain'], [99, 'Other (specify on the next page)']],
        label='2. What is your caste?',
        widget=widgets.RadioSelect,
    )
    caste_other = models.StringField(
        label='2. You selected \'Other\'. Please specify. What is your caste?',
    )
    religion = models.StringField(
        label='3. What is your religion?',
    )
    marital_status = models.IntegerField(
        choices=[[0, 'Married in monogamy (single wife)'], [1, 'Married in polygamy (multiple wives)'], [2, 'Unmarried'],
        [3,'Divorced'], [4, 'Separated'], [99, 'Other (specify on the next page)']],
        label='4. What is your marital status?',
        widget=widgets.RadioSelect,
    )
    marital_status_other = models.StringField(
        label='4. You selected \'Other\'. Please specify. What is your marital status?',
    )
    children = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        label='5. Do you have children?',
        widget=widgets.RadioSelect,
    )
    children_yes = models.StringField(
        label='5. You selected \'Yes\' to \'Do you have children?\'. Please specify. How old are your children?',
    )
    lang = models.IntegerField(
        choices=[[0, 'English'], [1, 'Urdu'], [2, 'Punjabi'], [3,'Pushto'], [4, 'Sindhi'], [99, 'Other/Multiple (specify on the next page)']],
        label='6. What language do you normally speak at home?',
        widget=widgets.RadioSelect,
    )
    lang_other = models.StringField(
        label='6. You selected \'Other/Multiple\'. Please specify. What language(s) do you normally speak at home?',
    )
    father_occu = models.IntegerField(
        choices=[[1, 'Doctor'], [2, 'Works in a factory'], [3, 'Works in a shop'], [4,'Engineer'], [5, 'Lawyer'],
        [6,'Owns a shop'], [7,'\'Kissan\''], [8, 'Private business'], [9,'Government job'], [99, 'Other (specify on the next page)']],
        label='7. What does your father do?',
        widget=widgets.RadioSelect,
    )
    father_occu_other = models.StringField(
        label='7. You selected \'Other\'. Please specify. What does your father do?',
    )
    mother_occu = models.IntegerField(
        choices=[[0,'House-wife'], [1, 'Doctor'], [2, 'Works in a factory'], [3, 'Works in a shop'], [4,'Engineer'], [5, 'Lawyer'],
        [6,'Owns a shop'], [7,'\'Kissan\''], [8, 'Private business'], [9,'Government job'], [99, 'Other (specify on the next page)']],
        label='8. What does your mother do?',
        widget=widgets.RadioSelect,
    )
    mother_occu_other = models.StringField(
        label='8. You selected \'Other\'. Please specify. What does your mother do?',
    )
    in_house = models.IntegerField(
        label='9. How many people live in your house?'
    )
    origin = models.IntegerField(
        choices=[[0, 'Lahore'], [1, 'Faisalabad'], [2, 'Sialkot'], [3,'Gujranwala'], [4, 'Attock'], [5,'Bahawalpur'], [6,'Bahawalnagar'],
        [7, 'Sheikhupura'], [8,'Kasur'], [9,'Rawalpindi'], [10, 'Sialkot'], [99, 'Other (specify on the next page)']],
        label='10. Where are you originally from?',
        widget=widgets.RadioSelect,
    )
    origin_other = models.StringField(
        label='10. You selected \'Other\'. Please specify. Where are you originally from?',
    )
    monthly_income = models.IntegerField(
        choices=[[0, 'Less than Rs. 10,000 per month'], [1, 'Rs.10,000 to less than Rs. 20,0000 per month'], [2, 'Rs.20,000 to less than Rs. 30,0000 per month'],
        [3,'Rs.30,000 to less than Rs. 40,0000 per month'], [4, 'Rs.40,000 to less than Rs. 50,0000 per month'], [5,'Rs.50,000 to less than Rs. 60,0000 per month'],
        [6,'Rs.60,000 to less than Rs. 70,0000 per month'], [7, 'Rs.70,000 to less than Rs. 80,0000 per month'], [8,'Rs.80,000 to less than Rs. 90,0000 per month'],
        [9,'Rs.90,000 to less than Rs. 100,0000 per month'], [10, 'Greater than Rs. 100,000 per month']],
        label='11. In what bracket does your families\' total monthly income fall?',
        widget=widgets.RadioSelect,
    )

    #Section D Part 2
    lost_wallet_personal = models.IntegerField(
        choices=[[1, '1   Very Unlikely'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very likely']],
        label='Imagine that you lost your wallet close to your house. This had Rs. 500 and was found by someone who lives close to you and KNOWS YOU PERSONALLY. The wallet has a document that identifies you. How likely do you find that this person gives you the wallet back with the money in it?',
        widget=widgets.RadioSelectHorizontal,
    )
    lost_wallet_impersonal = models.IntegerField(
        choices=[[1, '1   Very Unlikely'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very likely']],
        label='Imagine that you lost your wallet close to your house. This had Rs. 500 and was found by someone who lives close to you but who DOESN’T KNOW YOU PERSONALLY. The wallet has a document that identifies you. How likely do you find that this person gives you the wallet back with the money in it?',
        widget=widgets.RadioSelectHorizontal,
    )
    scarcity = make_field_likert('When jobs are scarce, men should have more right to a job than women.')
    women_money = make_field_likert('If a woman earns more money than her husband, it\'s almost certain to cause problems.')
    women_independence = make_field_likert('Having a job is the best way for a woman to be an independent person.')
    parental_pride = make_field_likert('One of my main goals in life has been to make my parents proud.')
    children_suffer = make_field_likert('When a mother works for pay, the children suffer.')
    men_politicians = make_field_likert('On the whole, men make better political leaders than women do.')
    uni_gender = make_field_likert('A university education is more important for a boy than for a girl.')
    busi_gender = make_field_likert('On the whole, men make better business executives than women do.')
    house_fulfill = make_field_likert('Being a housewife is just as fulfilling as working for pay.')
    family_customs = make_field_likert('To follow customs handed down by one’s family is very important.')
    free_choice = models.IntegerField(
        choices=[[1, '1   No choice at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   A great deal of choice']],
        label='Some people feel they have completely free choice and control over their lives, while other people feel that what they do has no real effect on what happens to them. Please use this scale where 1 means "no choice at all" and 10 means "a great deal of choice" to indicate how much freedom of choice and control you feel you have over the way your life turns out.',
        widget=widgets.RadioSelectHorizontal,
    )
    justify_divorce = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Divorce',
        widget=widgets.RadioSelectHorizontal,
    )
    justify_lying = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Lying',
        widget=widgets.RadioSelectHorizontal,
    )
    justify_beatwife = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='For a man to beat his wife',
        widget=widgets.RadioSelectHorizontal,
    )
    justify_beatchild = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Parents beating children',
        widget=widgets.RadioSelectHorizontal,
    )
    justify_violence = models.IntegerField(
        choices=[[1, 'Can always be justified'], [2, 'Justified'], [3, 'Neutral'], [4, 'Not justified'], [5, 'Never be justified']],
        label='Violence against other people',
        widget=widgets.RadioSelectHorizontal,
    )

    #Section E
    patience = models.IntegerField(
        choices=[[1, '1   Completely Unwilling'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very Willing']],
        label='How willing are you to give up something that is beneficial for you today in order to benefit more from that in the future?',
        widget=widgets.RadioSelectHorizontal,
    )
    risk_aversion = models.IntegerField(
        choices=[[1, '1   Completely Unwilling'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very Willing']],
        label='Please tell me, in general, how willing or unwilling you are to take risks.',
        widget=widgets.RadioSelectHorizontal,
    )
    altruism = models.IntegerField(
        label='Imagine the following situation: Today you unexpectedly received 1,000 Rs. How much of this amount would you donate to a good cause? (Values between 0 and 1000 are allowed.)',
        min = 0, max = 1000,
    )
    positive_reciprocity = models.IntegerField(
        choices=[[0, 'No present'], [1, 'The present worth 5'], [2, 'The present worth 10'], [3, 'The present worth 15'], [4, 'The present worth 20'], [5, 'The present worth 25'], [6,'The present worth 30']],
        label='Please think about what you would do in the following situation. You are in an area you are not familiar with, and you realize you lost your way. You ask a stranger for directions. The stranger offers to take you to your destination. Helping you costs the stranger about 20 Rs in total. However, the stranger says he or she does not want any money from you. You have six presents with you. The cheapest present costs 5 Rs, the most expensive one costs 30 Rs. Do you give one of the presents to the stranger as a “thank-you”- gift? If so, which present do you give to the stranger?',
        widget=widgets.RadioSelect,
    )
    negative_reciprocity_self = models.IntegerField(
        choices=[[1, '1   Completely Unwilling'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very Willing']],
        label='How willing are you to punish someone who treats YOU unfairly, even if there may be costs for you?',
        widget=widgets.RadioSelectHorizontal,
    )
    negative_reciprocity_others = models.IntegerField(
        choices=[[1, '1   Completely Unwilling'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Very Willing']],
        label='How willing are you to punish someone who treats OTHERS unfairly, even if there may be costs for you?',
        widget=widgets.RadioSelectHorizontal,
    )
    competitiveness = models.IntegerField(
        choices=[[1, '1   Not at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Extremely']],
        label='How competitive do you consider yourself to be?',
        widget=widgets.RadioSelectHorizontal,
    )
    social_skills_feelings = make_field_likert('I pick up the subtle signals of feelings from another person.')
    social_skills_reactions = make_field_likert('I am astute at reading people’s reactions.')
    generalized_trust = models.IntegerField(
        choices=[[1, 'Most people can be trusted'], [2, 'Can\'t be too careful']],
        label='Generally speaking, which one of these statements do you most agree with?',
        widget=widgets.RadioSelect,
    )
    best_intentions = models.IntegerField(
        choices=[[1, '1   Not at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7,'7'], [8, '8'], [9,'9'], [10,'10   Extremely']],
        label='How well does the following statement describe you as a person? As long as I am not convinced otherwise, I assume that people have only the best intentions.',
        widget=widgets.RadioSelectHorizontal,
    )
    trust_first_meet = models.IntegerField(
        choices=[[1, 'Do not trust at all'], [2, 'Do not trust very much'], [3, 'Trust somewhat'], [4, 'Trust completely']],
        label='How much do you trust people you meet for the first time?',
        widget=widgets.RadioSelectHorizontal,
    )
    trust_women = models.IntegerField(
        choices=[[1, 'Do not trust at all'], [2, 'Do not trust very much'], [3, 'Trust somewhat'], [4, 'Trust completely']],
        label='How much do you trust women?',
        widget=widgets.RadioSelectHorizontal,
    )
    trust_men = models.IntegerField(
        choices=[[1, 'Do not trust at all'], [2, 'Do not trust very much'], [3, 'Trust somewhat'], [4, 'Trust completely']],
        label='How much do you trust men?',
        widget=widgets.RadioSelectHorizontal,
    )
    #PERSONALITY TRAITS TABLE
    reserved = make_field_likert('... is reserved')
    trust = make_field_likert('... is generally trusting')
    lazy = make_field_likert('... tends to be lazy')
    relaxed = make_field_likert('... is relaxed, handles stress well')
    artistic = make_field_likert('... has few artistic interests')
    outgoing = make_field_likert('... is outgoing, sociable')
    fault_others = make_field_likert('... tends to find fault with others')
    thorough = make_field_likert('... does a thorough job')
    nervous = make_field_likert('... gets nervous easily')
    imagination = make_field_likert('... has an active imagination')

    #PERSONALITY STATEMENT TABLE
    setbacks_encourage = make_field_likert('Setbacks don’t discourage me. I don’t give up easily.')
    change_goals = make_field_likert('I often set a goal but later choose to pursue a different one.')
    focus_months = make_field_likert('I have difficulty maintaining my focus on projects that take more than a few months to complete.')
    new_distracts = make_field_likert('New ideas and projects sometimes distract me from previous ones.')
    hardwork = make_field_likert('I am a hard worker.')
    finish = make_field_likert('I finish whatever I begin.')
    change_interests = make_field_likert('My interests change from year to year.')
    diligent = make_field_likert('I am diligent. I never give up.')
    obsess_shortterm = make_field_likert('I have been obsessed with a certain idea or project for a short time but later lost interest.')
    setbacks_challenge = make_field_likert('I have overcome setbacks to conquer an important challenge.')

    #Section F
    f_5_1 = make_field_multiple_price()
    f_5_2 = make_field_multiple_price()
    f_5_3 = make_field_multiple_price()
    f_5_4 = make_field_multiple_price()
    f_5_5 = make_field_multiple_price()
    f_5_6 = make_field_multiple_price()
    f_5_7 = make_field_multiple_price()

    m_5_1 = make_field_multiple_price()
    m_5_2 = make_field_multiple_price()
    m_5_3 = make_field_multiple_price()
    m_5_4 = make_field_multiple_price()
    m_5_5 = make_field_multiple_price()
    m_5_6 = make_field_multiple_price()
    m_5_7 = make_field_multiple_price()

    wtp_econ1 = make_field_wtp()
    wtp_cook1 = make_field_wtp()
    wtp_sport1 = make_field_wtp()
    wtp_econ2 = make_field_wtp()
    wtp_cook2 = make_field_wtp()
    wtp_sport2 = make_field_wtp()
    wtp_econ3 = make_field_wtp()
    wtp_cook3 = make_field_wtp()
    wtp_sport3 = make_field_wtp()
    wtp_econ4 = make_field_wtp()
    wtp_cook4 = make_field_wtp()
    wtp_sport4 = make_field_wtp()


# PAGES
#Section A
class AcademicInfo(Page):
    form_model = 'player'
    form_fields = ['dob','high_edu','subject_prior','high_edu_school','rank_prior','extra_curric','degree_aspire','pref_occu','why_pref_occu','study_abroad','friend_count','friend_uni']

class AcademicInfoOther(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.high_edu == 99) or (player.subject_prior == 99) or (player.extra_curric == 99) or (player.degree_aspire == 99) or (player.pref_occu == 99) or (player.study_abroad == 0) or (player.friend_count == 99)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = []
        if player.high_edu == 99:
            formfields.append('high_edu_other')
        if player.subject_prior == 99:
            formfields.append('subject_prior_other')
        if player.extra_curric == 99:
            formfields.append('extra_curric_other')
        if player.degree_aspire == 99:
            formfields.append('degree_aspire_other')
        if player.pref_occu == 99:
            formfields.append('pref_occu_other')
        if player.study_abroad == 0:
            formfields.append('study_abroad_yes')
        if player.friend_count == 99:
            formfields.append('friend_count_other')
        return formfields

class TimeSpent(Page):
    form_model = 'player'
    form_fields = ['cook_time','study_time','sport_time','clean_time','dish_time','iron_time','laundry_time','care_time','eat_time','tv_time','phone_time','socialmedia_time','news_time','read_time','social_time','sleep_time','smoke_time','nothing_time','other_time']
    @staticmethod
    def error_message(player: Player, values):
        allvalues = sum(values.values())
        if allvalues != 24:
            return "Ensure that all values add to 24 hours"

class FriendsTable(Page):
    form_model = 'player'
    form_fields = ['friend_roll1','friend_roll2','friend_roll3','friend_roll4','friend_roll5','friend_roll6','friend_roll7','friend_roll8','friend_roll9','friend_roll10','friend_name1','friend_name2','friend_name3','friend_name4','friend_name5','friend_name6','friend_name7','friend_name8','friend_name9','friend_name10','friend_section1','friend_section2','friend_section3','friend_section4','friend_section5','friend_section6','friend_section7','friend_section8','friend_section9','friend_section10','friend_years1','friend_years2','friend_years3','friend_years4','friend_years5','friend_years6','friend_years7','friend_years8','friend_years9','friend_years10']
    @staticmethod
    def vars_for_template(player: Player):
        friend1 = ['friend_roll1','friend_name1','friend_section1','friend_years1']
        friend2 = ['friend_roll2','friend_name2','friend_section2','friend_years2']
        friend3 = ['friend_roll3','friend_name3','friend_section3','friend_years3']
        friend4 = ['friend_roll4','friend_name4','friend_section4','friend_years4']
        friend5 = ['friend_roll5','friend_name5','friend_section5','friend_years5']
        friend6 = ['friend_roll6','friend_name6','friend_section6','friend_years6']
        friend7 = ['friend_roll7','friend_name7','friend_section7','friend_years7']
        friend8 = ['friend_roll8','friend_name8','friend_section8','friend_years8']
        friend9 = ['friend_roll9','friend_name9','friend_section9','friend_years9']
        friend10 = ['friend_roll10','friend_name10','friend_section10','friend_years10']
        return dict(friend1=friend1,friend2=friend2,friend3=friend3,friend4=friend4,friend5=friend5,friend6=friend6,friend7=friend7,friend8=friend8,friend9=friend9,friend10=friend10)

class ClassRelations1(Page):
    form_model = 'player'
    form_fields = ['class_relationship_image']
    @staticmethod
    def vars_for_template(player: Player):
        image_names1 = ['ClassRelations1_1.jpg','ClassRelations2_1.jpg','ClassRelations3_1.jpg','ClassRelations4_1.jpg','ClassRelations5_1.jpg','ClassRelations6_1.jpg','ClassRelations7_1.jpg']
        return dict(image_data1=make_image_data(image_names1))

class ClassRelations2(Page):
    form_model = 'player'
    form_fields = ['school_relationship_image']
    @staticmethod
    def vars_for_template(player: Player):
        image_names2 = ['ClassRelations1_2.jpg','ClassRelations2_2.jpg','ClassRelations3_2.jpg','ClassRelations4_2.jpg','ClassRelations5_2.jpg','ClassRelations6_2.jpg','ClassRelations7_2.jpg']
        return dict(image_data2=make_image_data(image_names2))

class ClassRelations3(Page):
    form_model = 'player'
    form_fields = ['know_rank','know_gpa']


#Section B
class ExpFeedback(Page):
    form_model = 'player'
    form_fields = ['subjects_like','subjects_dislike','subjects_correct','subjects_incorrect','hints_always_helper','hints_always']

class ExpFeedbackNo(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.hints_always_helper == 2) or (player.hints_always == 2)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = []
        if player.hints_always_helper == 2:
            formfields.append('hints_always_helper_no')
        if player.hints_always == 2:
            formfields.append('hints_always_no')
        return formfields

class HelperTable(Page):
    form_model = 'player'
    form_fields = ['helper_ranking1','helper_ranking2','helper_ranking3','helper_ranking4','helper_ranking5','helper_ranking6','helper_ranking7','helper_ranking8','helper_reason1','helper_reason2','helper_reason3','helper_reason4','helper_reason5','helper_reason6','helper_reason7','helper_reason8']
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        final = {}
        helper1 = []
        helper2 = []
        helper3 = []
        helper4 = []
        helper5 = []
        helper6 = []
        helper7 = []
        helper8 = []
        if player.participant.partner4 != 0:
            partner4 = g.get_player_by_id(player.participant.partner4)
            final.update(dict(partner1=partner4.participant.label))
            helper1.append('helper_ranking1')
            helper1.append('helper_reason1')
        if player.participant.partner7 != 0:
            partner7 = g.get_player_by_id(player.participant.partner7)
            final.update(dict(partner2=partner7.participant.label))
            helper2.append('helper_ranking2')
            helper2.append('helper_reason2')
        if player.participant.partner1 != 0:
            partner1 = g.get_player_by_id(player.participant.partner1)
            final.update(dict(partner3=partner1.participant.label))
            helper3.append('helper_ranking3')
            helper3.append('helper_reason3')
        if player.participant.partner5 != 0:
            partner5 = g.get_player_by_id(player.participant.partner5)
            final.update(dict(partner4=partner5.participant.label))
            helper4.append('helper_ranking4')
            helper4.append('helper_reason4')
        if player.participant.partner3 != 0:
            partner3 = g.get_player_by_id(player.participant.partner3)
            final.update(dict(partner5=partner3.participant.label))
            helper5.append('helper_ranking5')
            helper5.append('helper_reason5')
        if player.participant.partner8 != 0:
            partner8 = g.get_player_by_id(player.participant.partner8)
            final.update(dict(partner6=partner8.participant.label))
            helper6.append('helper_ranking6')
            helper6.append('helper_reason6')
        if player.participant.partner2 != 0:
            partner2 = g.get_player_by_id(player.participant.partner2)
            final.update(dict(partner7=partner2.participant.label))
            helper7.append('helper_ranking7')
            helper7.append('helper_reason7')
        if player.participant.partner6 != 0:
            partner6 = g.get_player_by_id(player.participant.partner6)
            final.update(dict(partner8=partner6.participant.label))
            helper8.append('helper_ranking8')
            helper8.append('helper_reason8')
        final.update(dict(helper1=helper1))
        final.update(dict(helper2=helper2))
        final.update(dict(helper3=helper3))
        final.update(dict(helper4=helper4))
        final.update(dict(helper5=helper5))
        final.update(dict(helper6=helper6))
        final.update(dict(helper7=helper7))
        final.update(dict(helper8=helper8))
        return final

class MultiplePriceFemale(Page):
    form_model = 'player'
    form_fields = ['f_5_1','f_5_2','f_5_3','f_5_4','f_5_5','f_5_6','f_5_7']
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        wr = 0
        length = len(g.get_players())
        int = list(range(1, length))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player.participant.gender == 0:
                wr = curr_player
                break
        return dict(wr=wr.participant.label)

class MultiplePriceMale(Page):
    form_model = 'player'
    form_fields = ['m_5_1','m_5_2','m_5_3','m_5_4','m_5_5','m_5_6','m_5_7']
    @staticmethod
    def vars_for_template(player:Player):
        g = player.group
        mr = 0
        length = len(g.get_players())
        int = list(range(1, length))
        random.shuffle(int)
        for key in int:
            curr_player = g.get_player_by_id(key)
            if curr_player != player and curr_player.participant.gender == 1:
                mr = curr_player
                break
        return dict(mr=mr.participant.label)

class WTP_Subject(Page):
    form_model = 'player'
    form_fields = ['wtp_econ1','wtp_cook1','wtp_sport1','wtp_econ2','wtp_cook2','wtp_sport2','wtp_econ3','wtp_cook3','wtp_sport3','wtp_econ4','wtp_cook4','wtp_sport4']
    @staticmethod
    def vars_for_template(player: Player):
        g = player.group
        arr = [player.participant.partner4, player.participant.partner7, player.participant.partner1,
               player.participant.partner5]
        string_arr = ['partner4', 'partner7', 'partner1', 'partner5']
        final = {}
        input = []
        for i, j in zip(arr, string_arr):
            if i != 0:
                if j == string_arr[0]:
                    input.append(dict(label=g.get_player_by_id(i).participant.label,fields = ['wtp_econ1', 'wtp_cook1', 'wtp_sport1']))
                if j == string_arr[1]:
                    input.append(dict(label=g.get_player_by_id(i).participant.label,fields = ['wtp_econ2', 'wtp_cook2', 'wtp_sport2']))
                if j == string_arr[2]:
                    input.append(dict(label=g.get_player_by_id(i).participant.label,fields = ['wtp_econ3', 'wtp_cook3', 'wtp_sport3']))
                if j == string_arr[3]:
                    input.append(dict(label=g.get_player_by_id(i).participant.label,fields = ['wtp_econ4', 'wtp_cook4', 'wtp_sport4']))
        final.update(input=input)
        return final


#Section C
class ExpDecisions(Page):
    form_model = 'player'
    form_fields = ['tt_perception','decide_hints','diff_why']

class ExpDecisionsNo(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.tt_perception == 2)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = []
        if player.tt_perception == 2:
            formfields.append('tt_perception_no')
        return formfields


#Section D
class GenderTable(Page):
    form_model = 'player'
    form_fields = ['gender_sports','gender_economics','gender_cooking']

class AmountGame(Page):
    form_model = 'player'
    form_fields = ['amount_notgame','amount_game']
    @staticmethod
    def error_message(player: Player, values):
        allvalues = sum(values.values())
        if allvalues != 300:
            return "Ensure that values add to 300 Rs."

class BasicInfo(Page):
    form_model = 'player'
    form_fields = ['gender','caste','religion','marital_status','children','lang','father_occu','mother_occu','in_house','origin','monthly_income']

class BasicInfoOther(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return (player.caste == 99) or (player.marital_status == 99) or (player.children == 1) or (player.lang == 99) or (player.father_occu == 99) or (player.mother_occu == 99) or (player.origin == 99)
    @staticmethod
    def get_form_fields(player: Player):
        formfields = []
        if player.caste == 99:
            formfields.append('caste_other')
        if player.marital_status == 99:
            formfields.append('marital_status_other')
        if player.children == 1:
            formfields.append('children_yes')
        if player.lang == 99:
            formfields.append('lang_other')
        if player.father_occu == 99:
            formfields.append('father_occu_other')
        if player.mother_occu == 99:
            formfields.append('mother_occu_other')
        if player.origin == 99:
            formfields.append('origin_other')
        return formfields

class Ethics1(Page):
    form_model = 'player'
    form_fields = ['lost_wallet_personal','lost_wallet_impersonal','free_choice']

class Ethics2(Page):
    form_model = 'player'
    form_fields = ['scarcity','women_money','women_independence','parental_pride','children_suffer','men_politicians','uni_gender','busi_gender','house_fulfill','family_customs']

class Ethics3(Page):
    form_model = 'player'
    form_fields = ['justify_divorce','justify_lying','justify_beatwife','justify_beatchild','justify_violence']



#Section E
class Personality(Page):
    form_model = 'player'
    form_fields = ['patience','risk_aversion','negative_reciprocity_self','negative_reciprocity_others','competitiveness','best_intentions','social_skills_feelings','social_skills_reactions','trust_first_meet','trust_women','trust_men','generalized_trust','altruism','positive_reciprocity']

class PersonalityTraitsTable(Page):
    form_model = 'player'
    form_fields = ['reserved','trust','lazy','relaxed','artistic','outgoing','fault_others','thorough','nervous','imagination']

class PersonalityStatementTable(Page):
    form_model = 'player'
    form_fields = ['setbacks_encourage','change_goals','focus_months','new_distracts','hardwork','finish','change_interests','diligent','obsess_shortterm','setbacks_challenge']

class Congratulations(Page):
    form_model = 'player'

page_sequence = [AcademicInfo, AcademicInfoOther, TimeSpent, FriendsTable, ClassRelations1,
ClassRelations2, ClassRelations3, ExpFeedback, ExpFeedbackNo, HelperTable, MultiplePriceFemale,
MultiplePriceMale, WTP_Subject, ExpDecisions, ExpDecisionsNo, GenderTable, AmountGame,
BasicInfo, BasicInfoOther, Ethics1, Ethics2, Ethics3, Personality, PersonalityTraitsTable,
PersonalityStatementTable, Congratulations]
