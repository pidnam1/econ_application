from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0]
    LABELS = ['Aniqa_Naz','Saman_Shabbir_Gondal','Zaryab_Khalid','Noman_Hameed',
    'Khadija_Hussain','Anumn_Rubab','Moghisa_Asif','Saad_Ul_Haq','Sarmad_Hassan',
    'Hamza_Mushtaq','Syed_Zeeshan_Haider','Muhammad_Farhan_Liaqat','Musfira','Muhammad_Faisal_Murad',
    'Ali_Ahmad','Maaz_Saeed','Sania_Riaz','Esha_Sarwar','Laiba_Bukhari','Rana_M_Abdullah',
    'Maria_Walait','Rai_Zishan_Hussain','Fatima_Abid','Hajira_Khawar','Bismah_Farooq',
    'Tahir_Fazeel','Zanabia_Adil','Izza_Islam','Nisha_Ansar','Rida_Khan','Muhammad_Shahzeb',
    'Zarjan_Anwar','Hassan_Messam_Kumaily','Taha_Jabbar','Rana_Hammad_Ali','Minahil',
    'Ahsan_Madni','Maha_Asif','Aiman','Hafiza_Mehwish','Muhammad_Umair','Abid_Hussain',
    'Tanzeela_Nasreen','Sawaira_Maryiam','Muhammad_Rizwan','Ayesha_Khalid','Azka_Iqbal']
    PLAYERS = ['Aniqa Naz','Saman Shabbir Gondal','Zaryab Khalid','Noman Hameed',
    'Khadija Hussain','Anumn Rubab','Moghisa Asif','Saad Ul Haq','Sarmad Hassan',
    'Hamza Mushtaq','Syed Zeeshan Haider','Muhammad Farhan Liaqat','Musfira','Muhammad Faisal Murad',
    'Ali Ahmad','Maaz Saeed','Sania Riaz','Esha Sarwar','Laiba Bukhari','Rana M. Abdullah',
    'Maria Walait','Rai Zishan Hussain','Fatima Abid','Hajira Khawar','Bismah Farooq',
    'Tahir Fazeel','Zanabia Adil','Izza Islam','Nisha Ansar','Rida Khan','Muhammad Shahzeb',
    'Zarjan Anwar','Hassan Messam Kumaily','Taha Jabbar','Rana Hammad Ali','Minahil',
    'Ahsan Madni','Maha Asif','Aiman','Hafiza Mehwish','Muhammad Umair','Abid Hussain',
    'Tanzeela Nasreen','Sawaira Maryiam','Muhammad Rizwan','Ayesha Khalid','Azka Iqbal']
    GENDERS_LIST = [0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1]
    LABELS = ['Ezza_Zulfiqar','Bisma_Tariq','Tayyaba_Naeem','Muhammad_Sufyan','Ayesha_Javed',
    'Hafsa_Tariq','Ali_Asad','Iftikhar_Ahmad','Muhammad_Zakria_Ilyas','Shahbaz_Ali',
    'Sanila_Asif','Muhammad_Qasim','Zara','Shah_Inshal_Ahmad','Muhammad_Rafiq','Muhammad_Afaq_Anjum',
    'Usama_Sardar','Ch_Bajash_Ali_Gujjar','Mehroz_Iqbal','Meerab','Muhammad_Arooj_Abbas',
    'Shahzaib_Hussain','Muhammad_Abdul_Rehman','Abdul_Qadeer_Iftikhar','Mian_Sheharyar_Khan',
    'Farheen','Hanzla_Amin','Muhammad_Ali_Rafiq','Basit_Hussain','Murad_Ali','Burhan',
    'Fatiha_Noor','Shabir_Ahmed','Adeena_Shabir','Areej_Iqbal','Ali_Husnain_Bari',
    'Shakeel_Hassan','Minahil_Nasir','Syed_Usama_Ahmad','Abdul_Sufyan_Khan','Noor_Ul_Maha',
    'Ameema_Zakriya','Bilal_Raza_Attari','Samama_Arqam','Muhammad_Muaaz_Ahmad','Muhammad_Shahriyar',
    'Eesha_Ahsan','Muhammad_Sulman','Usama_Liaqat','Sukaina_Nasir','Sufyan_Chohan',
    'Muhammad_Fawad_Ahmad','Ghulam_Abbas','Ahmaad','Sakhi_Shah_Muhammad','Muhammad_Shahnawaz',
    'Arslan_Falak_Sher','Mansoor_Ahmad','Mahmood_Ahmad']
    PLAYERS = ['Ezza Zulfiqar','Bisma Tariq','Tayyaba Naeem','Muhammad Sufyan','Ayesha Javed',
    'Hafsa Tariq','Ali Asad','Iftikhar Ahmad','Muhammad Zakria Ilyas','Shahbaz Ali',
    'Sanila Asif','Muhammad Qasim','Zara','Shah Inshal Ahmad','Muhammad Rafiq','Muhammad Afaq Anjum',
    'Usama Sardar','Ch Bajash Ali Gujjar','Mehroz Iqbal','Meerab','Muhammad Arooj Abbas',
    'Shahzaib Hussain','Muhammad Abdul Rehman','Abdul Qadeer Iftikhar','Mian Sheharyar Khan',
    'Farheen','Hanzla Amin','Muhammad Ali Rafiq','Basit Hussain','Murad Ali','Burhan',
    'Fatiha Noor','Shabir Ahmed','Adeena Shabir','Areej Iqbal','Ali Husnain Bari',
    'Shakeel Hassan','Minahil Nasir','Syed Usama Ahmad','Abdul Sufyan Khan','Noor Ul Maha',
    'Ameema Zakriya','Bilal Raza Attari','Samama Arqam','Muhammad Muaaz Ahmad','Muhammad Shahriyar',
    'Eesha Ahsan','Muhammad Sulman','Usama Liaqat','Sukaina Nasir','Sufyan Chohan',
    'Muhammad Fawad Ahmad','Ghulam Abbas','Ahmaad','Sakhi Shah Muhammad','Muhammad Shahnawaz',
    'Arslan Falak Sher','Mansoor Ahmad','Mahmood Ahmad']

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
