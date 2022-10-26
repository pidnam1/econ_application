from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [1,1,0,1,1,0,1,1,0,1,0,0,0,0,1,0]
    LABELS = ['Muhammad_Abdullah','Muhammad_Asfand','Meeram_Umer','Faisal_Iftikhar',
    'Shayan_Tahir_Saleem','Aiman_Rizwan_Butt','Usama_Amir','Muhammad_Ahmed_Raza',
    'Laiba_Wahab','Muhammad_Anas_Waheed','Nimra_Mehmood','Laraib_Yaseen','Fatima_Naeem',
    'Noor_Fatima','Syed_Hammad_Hussain_Shah','Fatima_Bint_E_Faran']
    PLAYERS = ['Muhammad Abdullah','Muhammad Asfand','Meeram Umer','Faisal Iftikhar',
    'Shayan Tahir Saleem','Aiman Rizwan Butt','Usama Amir','Muhammad Ahmed Raza',
    'Laiba Wahab','Muhammad Anas Waheed','Nimra Mehmood','Laraib Yaseen','Fatima Naeem',
    'Noor Fatima','Syed Hammad Hussain Shah','Fatima Bint E Faran']
    GENDERS_LIST = [0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1]
    LABELS = ['Zoha_Amin','Romaisa_Zainab','Eman_Fatima','Hassan_Raza','Muhammad_Ahmad',
    'Hamna_Aslam','Muhammad_Uzair','Momina_Mubeen','Esha_Saleem','Safa_Mudassar',
    'Mehroz_Ali','Mehreen_Syed','Muhammad_Akmal','Muhammad_Junaid','Ahmad_Ibrahim',
    'Suleman_Smian']
    PLAYERS = ['Zoha Amin','Romaisa Zainab','Eman Fatima','Hassan Raza','Muhammad Ahmad',
    'Hamna Aslam','Muhammad Uzair','Momina Mubeen','Esha Saleem','Safa Mudassar',
    'Mehroz Ali','Mehreen Syed','Muhammad Akmal','Muhammad Junaid','Ahmad Ibrahim',
    'Suleman Smian']
    GENDERS_LIST = [1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1]
    LABELS = ['Zaid_Rasool','Kashif_Ijaz','Umar_Farooq','Muzna_Mazhar','Ayesha_Imtiaz',
    'Feeha_Tariq','Abdullah_Chahal','Muhammad_Sameen_Rauf','Ali_Faisal','Arfa_Akram',
    'Faisal_Imam','Maha_Rehman','Urwa_Ijaz','Anusha_Nauroz','Laiba_Tariq','Ahmed_Farooq']
    PLAYERS = ['Zaid Rasool','Kashif Ijaz','Umar Farooq','Muzna Mazhar','Ayesha Imtiaz',
    'Feeha Tariq','Abdullah Chahal','Muhammad Sameen Rauf','Ali Faisal','Arfa Akram',
    'Faisal Imam','Maha Rehman','Urwa Ijaz','Anusha Nauroz','Laiba Tariq','Ahmed Farooq']

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
