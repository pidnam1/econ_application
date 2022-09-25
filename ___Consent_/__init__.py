from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1]
    LABELS = ['Haleema_Ali_Khawaja','Muhammad_Yousaf','Nisar_Ahmad','Muhammad_Rizwan',
    'Hassan_Sagheer','Adan_Irshad','Sehar','Laiba_Sattar','Saqib_Ali','Eman_Tariq',
    'Hafiz_Muhammad_Ali','Waqas_Ahmad','Saif_Ullah','Sami_Ullah_Cheema','Muhammad_Mubasir_Khan',
    'Noman_Zulfiqar','Muhammad_Shazil_Mumtaz','Saqlain_Abbas','Muhammad_Aryan','Ume_Hani',
    'Menahil_Nadeem','Muhammad_Zahid_Shafi','Muhammad_Abdullah','Faeza_Ashraf','Muhammad_Shahzaib',
    'Muhammad_Bilal','Muhammad_Ishfaq','Amir_Mushtaq_Saifi','Khawar_Faiz','Iram_Naz',
    'Ayesha_Fatima','Laiba_Maryam','Kamal_Kumar','Fahad_Ali','Irfan_Haider','Nouman_Riasat',
    'Farhan_Ahmed','Masooma_Sadaqat','Muhammad_Aizaz_Musharaf','Faizan_Bashir','Umer_Farooq',
    'Nimra_Ibrar','Aima_Alam','Salman_Ahmed_Ch._Rajpoot','Hayaa_Mariam','Muhammad_Abdullah_Hasnat',
    'Um_Ul_Hassnaat','Ihtasham_Irshad','Kainat_Bibi','Maryam','Faiza_Jabeen','Asmat_Ullah',
    'Hadia_Masoom','Monibah_Arif','Ayesha_Bibi','Mahnoor_Chand','Muhammad_Kamran',
    'Hassan_Raza']
    PLAYERS = ['Haleema Ali Khawaja','Muhammad Yousaf','Nisar Ahmad','Muhammad Rizwan',
    'Hassan Sagheer','Adan Irshad','Sehar','Laiba Sattar','Saqib Ali','Eman Tariq',
    'Hafiz Muhammad Ali','Waqas Ahmad','Saif Ullah','Sami Ullah Cheema','Muhammad Mubasir Khan',
    'Noman Zulfiqar','Muhammad Shazil Mumtaz','Saqlain Abbas','Muhammad Aryan','Ume Hani',
    'Menahil Nadeem','Muhammad Zahid Shafi','Muhammad Abdullah','Faeza Ashraf','Muhammad Shahzaib',
    'Muhammad Bilal','Muhammad Ishfaq','Amir Mushtaq Saifi','Khawar Faiz','Iram Naz',
    'Ayesha Fatima','Laiba Maryam','Kamal Kumar','Fahad Ali','Irfan Haider','Nouman Riasat',
    'Farhan Ahmed','Masooma Sadaqat','Muhammad Aizaz Musharaf','Faizan Bashir','Umer Farooq',
    'Nimra Ibrar','Aima Alam','Salman Ahmed Ch. Rajpoot','Hayaa Mariam','Muhammad Abdullah Hasnat',
    'Um Ul Hassnaat','Ihtasham Irshad','Kainat Bibi','Maryam','Faiza Jabeen','Asmat Ullah',
    'Hadia Masoom','Monibah Arif','Ayesha Bibi','Mahnoor Chand','Muhammad Kamran',
    'Hassan Raza']


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
