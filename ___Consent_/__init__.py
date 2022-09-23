from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0]
    LABELS = ['Areej_Ajmal','Ayesha_Imtiaz','Ali_Ahmad','Yaqoot_Azam','Oroba_Naveed',
    'Ayesha_Shamas','Nazar_Fareed','Sharjeel_Ahmed','Ameer_Hamza','Kamran_Khan',
    'Muhammad_Mukarram_Babar','Maryam_Ali','Din_Muhammad','Mudassir_Hassan','Arslan_Mehndi',
    'Zaheer_Ul_Hassan_Shah','Mehwish','Fakhir_Jibran','Nadia_Saifullah','Waqar_Dastagir',
    'Fatima_Saif_Khan','Saad_Ijaz','Nasim_Khan','Iqra_Usman','Muhammad_Farhan','Zainab_Saif',
    'Javeria_Naeem','Tehniyat_Ali','Muhammad_Ajmal','Muhammad_Imran_Bashir','Sara_Aziz',
    'Ayesha_Shabbir','Sumaira_Akram']
    PLAYERS = ['Areej Ajmal','Ayesha Imtiaz','Ali Ahmad','Yaqoot Azam','Oroba Naveed',
    'Ayesha Shamas','Nazar Fareed','Sharjeel Ahmed','Ameer Hamza','Kamran Khan',
    'Muhammad Mukarram Babar','Maryam Ali','Din Muhammad','Mudassir Hassan','Arslan Mehndi',
    'Zaheer Ul Hassan Shah','Mehwish','Fakhir Jibran','Nadia Saifullah','Waqar Dastagir',
    'Fatima Saif Khan','Saad Ijaz','Nasim Khan','Iqra Usman','Muhammad Farhan','Zainab Saif',
    'Javeria Naeem','Tehniyat Ali','Muhammad Ajmal','Muhammad Imran Bashir','Sara Aziz',
    'Ayesha Shabbir','Sumaira Akram']


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
