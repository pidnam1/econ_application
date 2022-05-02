from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LABELS = ['Shan_Aman_Rana','Alexia_Delfino','Shamyla_Chaudry','Ahsan_Pasha',
    'Shanzay_Tariq','Izzah_Kashif','Rohma_Nasim','Hamna_Tariq','Essa_Kurd','Hammad_Qayyum',
    'Muhammad_Pervaiz','Ayesha_Hassan','Faizan_Aziz','Assad_Mustafa','Maheen_Alvi',
    'Hasan_Akmal','Tamoor_Salman','Khawaja_Kashif','Haris_Zahid','Khadija_Aslam',
    'Hamza_Riaz']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    esig = models.StringField(label='Please type your name')
    agree = models.StringField(
        choices=[['I agree', 'I agree']],
        label='',
        widget=widgets.RadioSelect)
    roll = models.StringField(label='Please type your rollnumber')

def creating_session(subsession):
    for player, label in zip(subsession.get_players(), C.LABELS):
        player.participant.label = label
    # test_variables(subsession)
#
# def test_variables(subsession: Subsession):
#     for p in subsession.get_players():
#         p.participant.partnerm1 = 3
#         p.participant.partnerm2 = 6
#         p.participant.partnerm3 = 7
#         p.participant.partnerm4 = 9
#         p.participant.partnerf1 = 1
#         p.participant.partnerf2 = 2
#         p.participant.partnerf3 = 4
#         p.participant.partnerf4 = 5
#         p.participant.partner1 = 1
#         p.participant.partner2 = 2
#         p.participant.partner3 = 4
#         p.participant.partner4 = 5
#         p.participant.partner5 = 3
#         p.participant.partner6 = 6
#         p.participant.partner7 = 7
#         p.participant.partner8 = 9
#         p.participant.hints_given_econ = 4
#         p.participant.hints_given_cook = 3
#         p.participant.hints_given_sport = 1
#         p.participant.MP1hints_given_econ = 1
#         p.participant.MP1hints_given_cook = 2
#         p.participant.MP1hints_given_sport = 3
#         p.participant.MP2hints_given_econ = 2
#         p.participant.MP2hints_given_cook = 3
#         p.participant.MP2hints_given_sport = 1
#         p.participant.MR1hints_given_econ = 3
#         p.participant.MR1hints_given_cook = 2
#         p.participant.MR1hints_given_sport = 1
#         p.participant.MR2hints_given_econ = 0
#         p.participant.MR2hints_given_cook = 1
#         p.participant.MR2hints_given_sport = 2
#         p.participant.WP1hints_given_econ = 3
#         p.participant.WP1hints_given_cook = 1
#         p.participant.WP1hints_given_sport = 2
#         p.participant.WP2hints_given_econ = 0
#         p.participant.WP2hints_given_cook = 1
#         p.participant.WP2hints_given_sport = 3
#         p.participant.WR1hints_given_econ = 1
#         p.participant.WR1hints_given_cook = 0
#         p.participant.WR1hints_given_sport = 2
#         p.participant.WR2hints_given_econ = 2
#         p.participant.WR2hints_given_cook = 3
#         p.participant.WR2hints_given_sport = 2
#         p.participant.econ_hint_requests_partner1 = 1
#         p.participant.econ_hint_requests_partner2 = 2
#         p.participant.econ_hint_requests_partner3 = 3
#         p.participant.econ_hint_requests_partner4 = 2
#         p.participant.econ_hint_requests_partner5 = 3
#         p.participant.econ_hint_requests_partner6 = 0
#         p.participant.econ_hint_requests_partner7 = 2
#         p.participant.econ_hint_requests_partner8 = 4
#         p.participant.cook_hint_requests_partner1 = 3
#         p.participant.cook_hint_requests_partner2 = 1
#         p.participant.cook_hint_requests_partner3 = 2
#         p.participant.cook_hint_requests_partner4 = 4
#         p.participant.cook_hint_requests_partner5 = 3
#         p.participant.cook_hint_requests_partner6 = 1
#         p.participant.cook_hint_requests_partner7 = 2
#         p.participant.cook_hint_requests_partner8 = 0
#         p.participant.sport_hint_requests_partner1 = 3
#         p.participant.sport_hint_requests_partner2 = 2
#         p.participant.sport_hint_requests_partner3 = 5
#         p.participant.sport_hint_requests_partner4 = 0
#         p.participant.sport_hint_requests_partner5 = 1
#         p.participant.sport_hint_requests_partner6 = 2
#         p.participant.sport_hint_requests_partner7 = 3
#         p.participant.sport_hint_requests_partner8 = 4
#         int = list(range(1, 19))
#         random.shuffle(int)
#         p.participant.pref_helper = {int[0]:1, int[1]:2, int[2]:3, int[3]:4, int[4]:5,
#         int[5]:6, int[6]:7, int[7]:8, int[8]:9, int[9]:10, int[10]:11, int[11]:12,
#         int[12]:13, int[13]:14, int[14]:15, int[15]:16, int[16]:17, int[17]:18}
#         p.participant.pref_helper_female = {int[0]:1, int[1]:2, int[3]:4, int[4]:5,
#         int[7]:8, int[10]:11, int[11]:12, int[12]:13, int[13]:14, int[14]:15, int[15]:16}
#         p.participant.pref_helper_male = {int[2]:3, int[5]:6, int[6]:7, int[8]:9,
#         int[9]:10, int[16]:17, int[17]:18}

def change_labels(player: Player):
    labels = ['Shan Aman Rana','Alexia Delfino','Shamyla Chaudry','Ahsan Pasha',
    'Shanzay Tariq','Izzah Kashif','Rohma Nasim','Hamna Tariq','Essa Kurd','Hammad Qayyum',
    'Muhammad Pervaiz','Ayesha Hassan','Faizan Aziz','Assad Mustafa','Maheen Alvi',
    'Hasan Akmal','Tamoor Salman','Khawaja Kashif','Haris Zahid','Khadija Aslam',
    'Hamza Riaz']
    for current, new in zip(C.LABELS, labels):
        if player.participant.label == current:
            player.participant.label = new

def set_players(player: Player):
    subsession = player.subsession
    session = player.session
    session.active_players.append(player.id_in_group)
    session.count += 1
    print(session.count)

def creating_session(subsession: Subsession):
    session = subsession.session
    session.active_players = []
    session.count = 0

class Consent(Page):
    form_model = 'player'
    form_fields = ['roll', 'esig', 'agree']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.name = player.esig
        change_labels(player)
        set_players(player)

page_sequence = [Consent]
