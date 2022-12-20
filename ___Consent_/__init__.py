from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1]
    LABELS = ['Sania_Islam','Ayesha_Amir','M_Hassan','Sadam_Hussein','Imran_Tariq',
    'Muqadas_Zafar','Danish_Riaz','Tabinda_Zahid','Aitazaz','Zara_Gulzar','Hafiz_Junaid',
    'Thmina_Ajmal','Saira_Yaseen','Hamza_Nawaz','Saira_Nazar','Minahil_Waseem','Zeeshan_Ali']
    PLAYERS = ['Sania Islam','Ayesha Amir','M. Hassan','Sadam Hussein','Imran Tariq',
    'Muqadas Zafar','Danish Riaz','Tabinda Zahid','Aitazaz','Zara Gulzar','Hafiz Junaid',
    'Thmina Ajmal','Saira Yaseen','Hamza Nawaz','Saira Nazar','Minahil Waseem','Zeeshan Ali']


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
