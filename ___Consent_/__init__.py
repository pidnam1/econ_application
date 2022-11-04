from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0]
    LABELS = ['Hafiz_Jamal','Laveeza_Asif','Gohar_Javed','Iqra_Basharat','M_Hassan_Irfan',
    'Amna_Choudhary','Fatima_Javed','Nadia_Riaz','Abdullah_Zarar','Ezza_Zulfiqaur',
    'M_Safdar','Mohsin_Ali','Ashna_Gohar','Arman','Saadullah_Nazar','Arisha_Aziz']
    PLAYERS = ['Hafiz Jamal','Laveeza Asif','Gohar Javed','Iqra Basharat','M. Hassan Irfan',
    'Amna Choudhary','Fatima Javed','Nadia Riaz','Abdullah Zarar','Ezza Zulfiqaur',
    'M. Safdar','Mohsin Ali','Ashna Gohar','Arman','Saadullah Nazar','Arisha Aziz']
    GENDERS_LIST = [0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0]
    LABELS = ['Afra_Mirza','Kashmala_Afzal','Ifrah_Ali','Hassan_Chaudhary','Maryam_Qasim',
    'Nashrah_Shahzadi','Amais','John_Raza','Fauq_Un_Nisa','Moiz','Konain_Ahmad',
    'Saqib_Malik','Hassan_Sarwar','Ahmad_Saeed_Asghar','Nida_Irfan','Laiba_Rasheed']
    PLAYERS = ['Afra Mirza','Kashmala Afzal','Ifrah Ali','Hassan Chaudhary','Maryam Qasim',
    'Nashrah Shahzadi','Amais','John Raza','Fauq Un Nisa','Moiz','Konain Ahmad',
    'Saqib Malik','Hassan Sarwar','Ahmad Saeed Asghar','Nida Irfan','Laiba Rasheed']
    GENDERS_LIST = [0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,0]
    LABELS = ['Tuba_Aslam','Adeena','M_Zaid','Yaqoob_Hassan','M_Shehroz_Khan','M_Umair_Haider',
    'Salman_Chaudhry','Ayesha_Tehreem','M_Asadullah','Anjum','Ariba','Bushra_Iqbal',
    'Moeed_Asif','Kashaf','Areej_Karim','Aqsa']
    PLAYERS = ['Tuba Aslam','Adeena','M. Zaid','Yaqoob Hassan','M. Shehroz Khan','M. Umair Haider',
    'Salman Chaudhry','Ayesha Tehreem','M. Asadullah','Anjum','Ariba','Bushra Iqbal',
    'Moeed Asif','Kashaf','Areej Karim','Aqsa']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    gender = models.IntegerField()
    esig = models.StringField(label='Please type your name')
    agree = models.StringField(
        choices=[['I agree', 'I agree']],
        label='',
        widget=widgets.RadioSelect)
    roll = models.StringField(label='Please type your student ID')

def change_labels(player: Player):
    for current, new in zip(C.LABELS, C.PLAYERS):
        if player.participant.label == current.lstrip():
            player.participant.label = new

def set_gender(player: Player):
    subsession = player.subsession
    people = dict(zip(C.PLAYERS,C.GENDERS_LIST))
    for label in people.keys():
        player.participant.gender = people[player.participant.label]

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
    session.wtp_finished = 0

    for player, label in zip(subsession.get_players(), C.LABELS):
        player.participant.label = label

class Consent(Page):
    form_model = 'player'
    form_fields = ['roll', 'esig', 'agree']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.name = player.esig
        player.participant.roll_no = player.roll
        player.participant.count_participant = int(player.id_in_group)
        change_labels(player)
        set_gender(player)
        set_players(player)
        player.gender = player.participant.gender

class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = "Please be patient with your fellow classmates. WHILE YOU WAIT, YOU CAN PLAY THE GAME ON THE PAPER THAT IS ON YOUR DESK. PLEASE DO NOT TALK TO ANYONE."

page_sequence = [Consent, WaitPage1]
