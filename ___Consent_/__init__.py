from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0]
    LABELS = ['Javeria_Shakir','Esha_Tariq','Muhamad_Afzal','Muhammab_Bilal_Fazal_Din',
    'Irha_Nasir','Fatma_Asif','Ali_Imran_Ansari','Muhammad_Waseem_Shoukat','Zahid_Ali',
    'Urooj','Areej_Fatima','Maidah_Afzal','Kinza_Kamran','Nafisa_Zehra','Manahil_Akram',
    'Laiba_Mohi_Ul_Hassan','Mehar_Khalid','Zishan_Gohar','Waneeza_Naeem','Aneeta_Rai',
    'Hafeez_Ur_Rehman','Muhammad_Dawood','Wajahat_Ullah','Beenish_Bashir','Mubashir_Hussain',
    'Kinza_Noor','Wajiha_Farhan','Payyam_Haider','Nimra_Tariq','Amna_Adil','Areeba_Usman',
    'Hassan_Raza_Mukhtar','Mohsan_Ali','Khansa_Fayyaz','Huzaifa_Abbas','Syeda_Ayesha_Jawad',
    'Rabia_Ashiq','Bisma_Shahzad','Muhammad_Bilal','Sumera_Qurban','Sarmad_Saif',
    'Laiba_Khan','Iqra_Ijaz','Hafiiza_Ayesha_Naeem','Younus_Khan','Ali_Hamza','Muhammad_Asad_Khan',
    'Muhammad_Haris_Hussain','Alishba_Khurram','Faiza_Saeed','Aqsa','Maryam_Saeed',
    'Sohail_Tahir','Sheraz_Ali','Kamran_Zaheer','Muhammad_Faisal_Khirat_Ali','Muhammad_Umar',
    'Muhammad_Bilal_M_Hayat','Ali_Hamza_Shahbaz','Bisma_Imran','Zuha_Shahbaz_Ahmed']
    PLAYERS = ['Javeria Shakir','Esha Tariq','Muhamad Afzal','Muhammab Bilal Fazal Din',
    'Irha Nasir','Fatma Asif','Ali Imran Ansari','Muhammad Waseem Shoukat','Zahid Ali',
    'Urooj','Areej Fatima','Maidah Afzal','Kinza Kamran','Nafisa Zehra','Manahil Akram',
    'Laiba Mohi Ul Hassan','Mehar Khalid','Zishan Gohar','Waneeza Naeem','Aneeta Rai',
    'Hafeez Ur Rehman','Muhammad Dawood','Wajahat Ullah','Beenish Bashir','Mubashir Hussain',
    'Kinza Noor','Wajiha Farhan','Payyam Haider','Nimra Tariq','Amna Adil','Areeba Usman',
    'Hassan Raza Mukhtar','Mohsan Ali','Khansa Fayyaz','Huzaifa Abbas','Syeda Ayesha Jawad',
    'Rabia Ashiq','Bisma Shahzad','Muhammad Bilal','Sumera Qurban','Sarmad Saif',
    'Laiba Khan','Iqra Ijaz','Hafiiza Ayesha Naeem','Younus Khan','Ali Hamza','Muhammad Asad Khan',
    'Muhammad Haris Hussain','Alishba Khurram','Faiza Saeed','Aqsa','Maryam Saeed',
    'Sohail Tahir','Sheraz Ali','Kamran Zaheer','Muhammad Faisal Khirat Ali','Muhammad Umar',
    'Muhammad Bilal M Hayat','Ali Hamza Shahbaz','Bisma Imran','Zuha Shahbaz Ahmed']
    GENDERS_LIST = [1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0]
    LABELS = ['Haris_Ahmad_Khan','Kalsoom_Nisar','Farhan','Hammad_Raza','Ayesha_Nayyar',
    'Eman','Maniha_Aslam','Khalid_Ur_Rehman','Anusha','Tayyaba_Barkat','Shoukat_All',
    'Abdul_Rauf','Muhammad_Awais_Raza','Ayesha_Siddiqa','Jalees_Ul_Hassan','Hadiqa_Ahmad']
    PLAYERS = ['Haris Ahmad Khan','Kalsoom Nisar','Farhan','Hammad Raza','Ayesha Nayyar',
    'Eman','Maniha Aslam','Khalid Ur Rehman','Anusha','Tayyaba Barkat','Shoukat All',
    'Abdul Rauf','Muhammad Awais Raza','Ayesha Siddiqa','Jalees Ul Hassan','Hadiqa Ahmad']

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
