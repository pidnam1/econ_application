from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,1]
    LABELS = ['Arshee','Ali_Hassan','Fehmeeda_Zulafqar','Shahid_Ali','Fatima_Bibi',
    'Khadija_Akram','Zaigham_Abbas','Faiza_Iqbal','Waqar_Hussain','Nawab_Khan','Mansoor_Nazir',
    'Nimra_Arshad','Nimra','Maryam_Abdul_Rasheed','Alishba_Mohsin','Laiba_Gul','Faisal_Aziz',
    'Irfa_Iqbal','Muqadas_Yasin','Muhammad_Haider','Shanzay_Saleem','Muhammad_Awais',
    'Farah_Anwar','Subhan_Ullah','Asia_Boota','Rehmat_Alam','Arooj_Fatima','Shab_Noor',
    'Muhammad_Shahroze_Iqbal','Wajid_Ali','Usama_Shamaoon','Afham_Javed','Rehan_Ahmad',
    'Anis_Yousuf','Maryam_Akram','Muhammad_Shaheryar','Muhammad_Qasim_Khan','Waiqa',
    'Muhammad_Uzair_Khan','Ali_Raza','Samia_Saleem','Taimoor_Khan','Nabish_Azhar',
    'Zulfiqar_Ahmad','Tauseef_Zulfiqar','Ume_Ramla','Zainab_Zulfiqar','Jahangir_Kakar',
    'Isma_Rasool','Shazeena_Fatima','Muhammad_Aslam','Akbar_Ali','Shujjat_Hussain',
    'Hajira','Khatim_Tayyab','Mudassir_Ali_Watto']
    PLAYERS = ['Arshee','Ali Hassan','Fehmeeda Zulafqar','Shahid Ali','Fatima Bibi',
    'Khadija Akram','Zaigham Abbas','Faiza Iqbal','Waqar Hussain','Nawab Khan','Mansoor Nazir',
    'Nimra Arshad','Nimra','Maryam Abdul Rasheed','Alishba Mohsin','Laiba Gul','Faisal Aziz',
    'Irfa Iqbal','Muqadas Yasin','Muhammad Haider','Shanzay Saleem','Muhammad Awais',
    'Farah Anwar','Subhan Ullah','Asia Boota','Rehmat Alam','Arooj Fatima','Shab Noor',
    'Muhammad Shahroze Iqbal','Wajid Ali','Usama Shamaoon','Afham Javed','Rehan Ahmad',
    'Anis Yousuf','Maryam Akram','Muhammad Shaheryar','Muhammad Qasim Khan','Waiqa',
    'Muhammad Uzair Khan','Ali Raza','Samia Saleem','Taimoor Khan','Nabish Azhar',
    'Zulfiqar Ahmad','Tauseef Zulfiqar','Ume Ramla','Zainab Zulfiqar','Jahangir Kakar',
    'Isma Rasool','Shazeena Fatima','Muhammad Aslam','Akbar Ali','Shujjat Hussain',
    'Hajira','Khatim Tayyab','Mudassir Ali Watto']
    GENDERS_LIST = [0,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0]
    LABELS = ['Shamsa_Kanwal','Muzaffar_Ali','Anosha_Saher','Muhammad_Saleem_Saha',
    'Irfa_Iqbal','Mir_Aqib_Ul_Azam','Shahzad_Munawar','Amna_Ijaz','Kanwal_Fatima',
    'Fadia_Sumreen_Hayat','Ali_Raza','Amram_Samuel','Maryam_Khan','Fahad_Ali_Khan',
    'Ali_Haris_Naeem','Shoaib_Naseer','Malik_Danish_Naeem','Sama_E_Noor','Ghulam_Murtaza',
    'Maliha_Shahid','Syeda_Mehreen_Akmal','Sitara_Mehwish','Ayesha','Anood_Akram',
    'Ghulam_Mujtaba','Mubashir_Shafi_Khan','Um_E_Farwa','Lyba_Saleem','Sumaira_Saleem']
    PLAYERS = ['Shamsa Kanwal','Muzaffar Ali','Anosha Saher','Muhammad Saleem Saha',
    'Irfa Iqbal','Mir Aqib Ul Azam','Shahzad Munawar','Amna Ijaz','Kanwal Fatima',
    'Fadia Sumreen Hayat','Ali Raza','Amram Samuel','Maryam Khan','Fahad Ali Khan',
    'Ali Haris Naeem','Shoaib Naseer','Malik Danish Naeem','Sama E Noor','Ghulam Murtaza',
    'Maliha Shahid','Syeda Mehreen Akmal','Sitara Mehwish','Ayesha','Anood Akram',
    'Ghulam Mujtaba','Mubashir Shafi Khan','Um E Farwa','Lyba Saleem','Sumaira Saleem']

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
