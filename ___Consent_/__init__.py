from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1]
    LABELS = ['Tooba_Javed','Ali_Mohsin','Hafsa_Mumtaz','S_M_Saqlain_Fareed','Zainab',
    'Maheen_Nisar_Khan','Rameen_Sahar','Bushra_Maqsood','Afshan_Tahira','Fatima_Zohra',
    'Mirha_Shehzad','Sadaf_Manzoor','Aiman_Ijaz','Maria_Miraj_Khalid','Gul_E_Zahra',
    'Asma_Sajjad','Fiza_Ijaz','Fatima_Ijaz','Sana','Fida_Ahmad','Laiba_Yaqoob','Fazilat_Bibi',
    'Zahra_Aftab','H_Ume_Hamama','Naveed_Hussain','Saleha_Maqbool','Hadia_Rizwan',
    'Omama_Zar_Khan','Ayesha_Munir','Muzammil_Hussain','Myra_Javeed','Fatima','H_M_Abdullah_Khan_Kiani',
    'Ayesha_Khan','Hoorya_Faisal','Jannat_Naveed','Hira_Younas','Misha_Shahbaz',
    'Eshwa_Khan','Aqib_Javed','Rimsha','Muneeb','Eisha_Zaheer','Aliza_Ali','Bint_E_Javed_Arfa',
    'Iqra_Arshad','Warda_Faisal','Samahir_Jamshed','Noor_Shahid','Almas_Asghar',
    'Asma','Zeeshan_Saddiq','Muskan_Fatima','Saif_Ur_Rehman','Rida_Batool','M_Shoaib_Akmal']
    PLAYERS = ['Tooba Javed','Ali Mohsin','Hafsa Mumtaz','S. M. Saqlain Fareed','Zainab',
    'Maheen Nisar Khan','Rameen Sahar','Bushra Maqsood','Afshan Tahira','Fatima Zohra',
    'Mirha Shehzad','Sadaf Manzoor','Aiman Ijaz','Maria Miraj Khalid','Gul E Zahra',
    'Asma Sajjad','Fiza Ijaz','Fatima Ijaz','Sana','Fida Ahmad','Laiba Yaqoob','Fazilat Bibi',
    'Zahra Aftab','H. Ume Hamama','Naveed Hussain','Saleha Maqbool','Hadia Rizwan',
    'Omama Zar Khan','Ayesha Munir','Muzammil Hussain','Myra Javeed','Fatima','H. M. Abdullah Khan Kiani',
    'Ayesha Khan','Hoorya Faisal','Jannat Naveed','Hira Younas','Misha Shahbaz',
    'Eshwa Khan','Aqib Javed','Rimsha','M_Muneeb_Ur_Rehman','Eisha Zaheer','Aliza Ali','Bint-E-Javed Arfa',
    'Iqra Arshad','Warda Faisal','Samahir Jamshed','Noor Shahid','Almas Asghar',
    'Asma','Zeeshan Saddiq','Muskan Fatima','Saif Ur Rehman','Rida Batool','M. Shoaib Akmal']
    GENDERS_LIST = [1,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1]
    LABELS = ['Azwaar_Ahmad','Muhammad_Anas','Fatima_Anwar','Sadia_Rehman','Noor_Shahid',
    'Sana_Ahmed','Nosheen_Akram','Raffay_Ejaz','Yasir_Yaseen','Sunir_Ashnai','Beenish_Sarfraz',
    'M_Adnan_Aslam','Mansoor_Ali','M_Zohaib_Amin','Fatima','S_Faseeha_Fatima','Faheem_Manzoor',
    'Maha_Farhad','Anna_Qasim','Maryam_Tariq','Zahra','Abu_Hurara','Jaweria_Khalid',
    'Areej_Zulfiqar','Jannat_Naveed','M_Asad_Ullah','Zain_Subhani','Mouzma_Ameen',
    'Mahnoor','Marwa_Ashraf','Sahar_Khalil','Shahzal_Eman','Iqra','Ashab_Shakeel',
    'Daniyal_Ahmad','Shafiq_Ur_Rehman','Raja_M_Azeem','Faisal_Hayat','Fakiha_Afzal',
    'Aiza','Ismail_Anees','Rubab_Asghar','Ashiq_Khan','Saba_Ilyas','M_Usama','Adisa',
    'Abdul_Rehman','Sidra_Rasheed','Noor_Fatima','M_Pervaiz','M_Talha_Nadeem','Sheraz_Ashraf',
    'Inshal_Zulfiqar','Jazib_Iqbal','Kiran_Khalid','S_Fatima_Gillani','Hooria_Murtaza',
    'Nimra_Shahzadi','S_Kaleem_Ullah']
    PLAYERS = ['Azwaar Ahmad','Muhammad Anas','Fatima Anwar','Sadia Rehman','Noor Shahid',
    'Sana Ahmed','Nosheen Akram','Raffay Ejaz','Yasir Yaseen','Sunir Ashnai','Beenish Sarfraz',
    'M. Adnan Aslam','Mansoor Ali','M. Zohaib Amin','Fatima','S. Faseeha Fatima','Faheem Manzoor',
    'Maha Farhad','Anna Qasim','Maryam Tariq','Zahra','Abu Hurara','Jaweria Khalid',
    'Areej Zulfiqar','Jannat Naveed','M. Asad Ullah','Zain Subhani','Mouzma Ameen',
    'Mahnoor','Marwa Ashraf','Sahar Khalil','Shahzal Eman','Iqra','Ashab Shakeel',
    'Daniyal Ahmad','Shafiq Ur Rehman','Raja M. Azeem','Faisal Hayat','Fakiha Afzal',
    'Aiza','Ismail Anees','Rubab Asghar','Ashiq Khan','Saba Ilyas','M. Usama','Adisa',
    'Abdul Rehman','Sidra Rasheed','Noor Fatima','M. Pervaiz','M. Talha Nadeem','Sheraz Ashraf',
    'Inshal Zulfiqar','Jazib Iqbal','Kiran Khalid','S. Fatima Gillani','Hooria Murtaza',
    'Nimra Shahzadi','S. Kaleem Ullah']

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
