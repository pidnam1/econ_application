from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1]
    LABELS = ['Safi_Ullah_Khan','Muhammad_Yousaf_Khan','Abdul_Nasir_Khan','Arooj_Khalid',
    'Zarak_Naseer_Baloch','Jannat_Rashid','Shahid_Ullah_Khan','Saif_Ur_Rehman_Kukuria',
    'Ali_Hasnain','Muhammad_Talha_Wattoo','Shumaila_Javaid','Shoaib_Ullah','Rumaiza_Mazhar',
    'Gul_E_Zahra_Abbasi','Naveed_Khan','Mahjabeen_Sughra','Areesha_Sohail','Sufyan_Ali',
    'Hassan_Umer','Ali_Waqas','Sania_Ehsan','Wareesha_Ehsan','Muhammad_Kashif_Khan',
    'Muhammad_Waqar','Umer_Farooq','Zain_U_Din','Shahar_Bano','Areesha_Zahra_Abbasi','Samiullah',
    'Rai_Ahmad_Khan','Rana_Muhammad_Imran','Amna_Bibi','Tuba_Naeem','Moazzam_Asadullah',
    'Muhammad_Musa_Sulehria','Noor_ul_Huda_Awan','Umme_Aqeel']
    PLAYERS = ['Safi Ullah Khan','Muhammad Yousaf Khan','Abdul Nasir Khan','Arooj Khalid',
    'Zarak Naseer Baloch','Jannat Rashid','Shahid Ullah Khan','Saif Ur Rehman Kukuria',
    'Ali Hasnain','Muhammad Talha Wattoo','Shumaila Javaid','Shoaib Ullah','Rumaiza Mazhar',
    'Gul E Zahra Abbasi','Naveed Khan','Mahjabeen Sughra','Areesha Sohail','Sufyan Ali',
    'Hassan Umer','Ali Waqas','Sania Ehsan','Wareesha Ehsan','Muhammad Kashif Khan',
    'Muhammad Waqar','Umer Farooq','Zain U Din','Shahar Bano','Areesha Zahra Abbasi','Samiullah',
    'Rai Ahmad Khan','Rana Muhammad Imran','Amna Bibi','Tuba Naeem','Moazzam Asadullah',
    'Muhammad Musa Sulehria','Noor ul Huda Awan','Umme Aqeel']


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

class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = "Please be patient with your fellow classmates. WHILE YOU WAIT, YOU CAN PLAY THE GAME ON THE PAPER THAT IS ON YOUR DESK. PLEASE DO NOT TALK TO ANYONE."
    
page_sequence = [Consent, WaitPage1]
