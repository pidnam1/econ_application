from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0]
    LABELS = ['Maira_Ashraf','Ajmal_Hussain_Kashif','Muhammad_Idrees','Muhammad_Farhan',
    'Meraj_Khan','Hasnain_Ali','Khizar_Hayat','Ali_Hamza','Nayab_Qamar','Rizwan_Ullah',
    'Waqar_Younas','Muhammad_Hamza_Khalid','Muhammad_Ilyas','Ahmar_Khan','Fatima_Akram',
    'Mohsin_Riaz','Aniba_Zafar','Khalid_Ur_Rehman','Hafiz_Muhammad_Rizwan','Muhammad_Afzaal_Azam',
    'Shahar_Yar','Massab_Umair','Qandeel_Shahid','Zohaib_Zulfiqar','Iftikhar_Mehmood',
    'Umair_Hassan','Zoha_Imtiaz','Maida_Iqbal','Ubaid_Khan','Zain_Abbas','Fatima_Muhammad_Yaseen',
    'Sania_Riaz','Muhammad_Tassawar','Hamnah_Shafique','Bareeha_Ali','Muhammad_Ahmad',
    'Farwa_Hussain','Tehmina_Fareed']
    PLAYERS = ['Maira Ashraf','Ajmal Hussain Kashif','Muhammad Idrees','Muhammad Farhan',
    'Meraj Khan','Hasnain Ali','Khizar Hayat','Ali Hamza','Nayab Qamar','Rizwan Ullah',
    'Waqar Younas','Muhammad Hamza Khalid','Muhammad Ilyas','Ahmar Khan','Fatima Akram',
    'Mohsin Riaz','Aniba Zafar','Khalid Ur Rehman','Hafiz Muhammad Rizwan','Muhammad Afzaal Azam',
    'Shahar Yar','Massab Umair','Qandeel Shahid','Zohaib Zulfiqar','Iftikhar Mehmood',
    'Umair Hassan','Zoha Imtiaz','Maida Iqbal','Ubaid Khan','Zain Abbas','Fatima Muhammad Yaseen',
    'Sania Riaz','Muhammad Tassawar','Hamnah Shafique','Bareeha Ali','Muhammad Ahmad',
    'Farwa Hussain','Tehmina Fareed']


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

class WaitPage2(WaitPage):
    title_text = "Waiting for all players to join"

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

page_sequence = [WaitPage2, Consent, WaitPage1]
