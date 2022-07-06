from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    LABELS = ['Shan_Aman_Rana','Alexia_Delfino','Shamyla_Chaudry','Ahsan_Pasha',
    'Shanzay_Tariq','Izzah_Kashif','Rohma_Nasim','Hamna_Tariq','Essa_Kurd','Hammad_Qayyum',
    'Muhammad_Pervaiz','Ayesha_Hassan','Faizan_Aziz','Assad_Mustafa','Maheen_Alvi',
    'Hasan_Akmal','Tamoor_Salman','Khawaja_Kashif','Haris_Zahid','Khadija_Aslam',
    'Hamza_Riaz','Alice','Bob','Coleman','Demond', 'Emily','Fariz','Grace','Heather',
    'Ivan','Jake','Kyle','Liam','Michael','Nina','Oliver','Penelope','Quinn','Richard',
    'Sam','Thomas','Ursula','Vinnie','Wade','Yu','Zhang','Alex','Barry','Carol','Don',
    'Enrique','Fred','Jenny','Howard','Inez','Kate','Lane','Maddie','Nate','Ajax']

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

def change_labels(player: Player):
    labels = ['Shan Aman Rana','Alexia Delfino','Shamyla Chaudry','Ahsan Pasha',
    'Shanzay Tariq','Izzah Kashif','Rohma Nasim','Hamna Tariq','Essa Kurd','Hammad Qayyum',
    'Muhammad Pervaiz','Ayesha Hassan','Faizan Aziz','Assad Mustafa','Maheen Alvi',
    'Hasan Akmal','Tamoor Salman','Khawaja Kashif','Haris Zahid','Khadija Aslam',
    'Hamza Riaz','Alice','Bob','Coleman','Demond', 'Emily','Fariz','Grace','Heather',
    'Ivan','Jake','Kyle','Liam','Michael','Nina','Oliver','Penelope','Quinn','Richard',
    'Sam','Thomas','Ursula','Vinnie','Wade','Yu','Zhang','Alex','Barry','Carol','Don',
    'Enrique','Fred','Jenny','Howard','Inez','Kate','Lane','Maddie','Nate','Ajax']
    for current, new in zip(C.LABELS, labels):
        if player.participant.label == current.lstrip():
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

    for player, label in zip(subsession.get_players(), C.LABELS):
        player.participant.label = label

class Consent(Page):
    form_model = 'player'
    form_fields = ['roll', 'esig', 'agree']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.name = player.esig
        player.participant.gender = C.GENDERS_LIST[int(player.id_in_group) - 1]
        player.participant.roll_no = int(player.roll)
        player.participant.count_participant = int(player.id_in_group)
        change_labels(player)
        set_players(player)

class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = ""

page_sequence = [Consent, WaitPage1]
