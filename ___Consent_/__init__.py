from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [1,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0]
     LABELS = ['Tayyab_Tanveer','Aqsa_Shehzadi','Minahil_Fatima','Kanwal','Abdul_Salam',
    'Rabia_Naeem','Hafiza_Esha_Tu_Razia','Muhammad_Ilyas_Raza','Nimra_Hussain','Iqra',
    'Ahmad_Raza','Roman_Ahmad_Rana','M_Anwar_Zahid','Dawood_Khan','Faizan_Farooq',
    'Moazam_Ali','Nida_Eman','Areeba_Zahid','Qahirman_Saddiq','Basharat_Ullah','M_Umer_Munawar',
    'Fizza_Akber','Muhammad_Faisal','Naqash_Dawood','Mehboob_Raza','Inam_Ullah',
    'Muhammad_Asif','Inzamam','Muhammad_Irfan','Omama_Tariq','Akash_Raza','Sana_Arshad',
    'Naimat_Ullah_Khan','Dinar_Khan','Aqsa_Amir','Sher_Bahadar','Ahmad_Haraan_Qasim',
    'Hammad_Ali','Sameer_Ali','Muhammad_Ehsan','Hammal_Hassan','Fatima_Akram','Ahtasham_Fareed',
    'Rabia_Nuzhat_Khan','Bushra_Hijab','Yaishal_Aslam','Maryam','Soman_Hussnain',
    'Fida_Hussain','Nimra_Zahoor','Umme_Rubab','Aleeha_Adnan','Sayeda_Khadija_Shoaib',
    'Palwasha_Aman','Bisma_Iqbal','Saqlain_Haider','Rukhsar_Gill','Malaika_Zahra',
    'Laiba','M_Umar_Natiq','Saher_Talib']
    PLAYERS = ['Tayyab Tanveer','Aqsa Shehzadi','Minahil Fatima','Kanwal','Abdul Salam',
    'Rabia Naeem','Hafiza Esha Tu Razia','Muhammad Ilyas Raza','Nimra Hussain','Iqra',
    'Ahmad Raza','Roman Ahmad Rana','M. Anwar Zahid','Dawood Khan','Faizan Farooq',
    'Moazam Ali','Nida Eman','Areeba Zahid','Qahirman Saddiq','Basharat Ullah','M. Umer Munawar',
    'Fizza Akber','Muhammad Faisal','Naqash Dawood','Mehboob Raza','Inam Ullah',
    'Muhammad Asif','Inzamam','Muhammad Irfan','Omama Tariq','Akash Raza','Sana Arshad',
    'Naimat Ullah Khan','Dinar Khan','Aqsa Amir','Sher Bahadar','Ahmad Haraan Qasim',
    'Hammad Ali','Sameer Ali','Muhammad Ehsan','Hammal Hassan','Fatima Akram','Ahtasham Fareed',
    'Rabia Nuzhat Khan','Bushra Hijab','Yaishal Aslam','Maryam','Soman Hussnain',
    'Fida Hussain','Nimra Zahoor','Umme Rubab','Aleeha Adnan','Sayeda Khadija Shoaib',
    'Palwasha Aman','Bisma Iqbal','Saqlain Haider','Rukhsar Gill','Malaika Zahra',
    'Laiba','M. Umar Natiq','Saher Talib']
    GENDERS_LIST = [0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0]
    LABELS = ['Ayesha_Akhtar','Qammar_Shehzad','Faique_Ali','Zahra_Wazir','Shaheen_Bibi',
    'Muhammad_Luqman','Ali_Raza_Jafar','Tehzeeb_Zahra','Ansar_Saeed','Zahra_Shafi',
    'Danial_Ali_Abbas','Tahira_Aslam','M_Asim_Iqbal','Ali_Hassnain','Nigar_Tufail',
    'Usman_Altaf','Munazza_Ashfaq','Mahnoor_Imran','M_Umair_Basharat','Laiba_Bukhari',
    'Muhmmad_Osama','Rabbia_Nuzhat_Khat','Ali_Shahbaz','Uzair_Hassan','Amina_Mahmood',
    'Yumna_Waseem','Bisma_Hira','Shumaila','M_Ilyas_Raza','Ali_Hamza','Meerab_Imran',
    'M_Umer_Munawar','Kinza_Noor','Abdullah_Ramzan','Nida_Eman','Ali_Raza_Sarwar',
    'Shakila_Ajmal','Sana_Muqqaddas','Rai_Adeel_Ahmad','Aqeel_Shahzad','Rafaqat_Ullah',
    'Hadiqa_Fatima','Asghar_Ali','Muhammad_Asim','Hubba_Fatima','M_Qamarulhaq','Aqsa_Amir',
    'Hafsa_Noor','Ibrar_Ahmad','Qasim_Ali','Osama_Sadiq','Saba_Gul','Aswad_Liaqat',
    'M_Shakeel','Ambreen_Anwar','Neelam_Shahzadi','Umda_Sharwani','Mafia_Javed']
    PLAYERS = ['Ayesha Akhtar','Qammar Shehzad','Faique Ali','Zahra Wazir','Shaheen Bibi',
    'Muhammad Luqman','Ali Raza Jafar','Tehzeeb Zahra','Ansar Saeed','Zahra Shafi',
    'Danial Ali Abbas','Tahira Aslam','M. Asim Iqbal','Ali Hassnain','Nigar Tufail',
    'Usman Altaf','Munazza Ashfaq','Mahnoor Imran','M. Umair Basharat','Laiba Bukhari',
    'Muhmmad Osama','Rabbia Nuzhat Khat','Ali Shahbaz','Uzair Hassan','Amina Mahmood',
    'Yumna Waseem','Bisma Hira','Shumaila','M. Ilyas Raza','Ali Hamza','Meerab Imran',
    'M. Umer Munawar','Kinza Noor','Abdullah Ramzan','Nida Eman','Ali Raza Sarwar',
    'Shakila Ajmal','Sana Muqqaddas','Rai Adeel Ahmad','Aqeel Shahzad','Rafaqat Ullah',
    'Hadiqa Fatima','Asghar Ali','Muhammad Asim','Hubba Fatima','M. Qamarulhaq','Aqsa Amir',
    'Hafsa Noor','Ibrar Ahmad','Qasim Ali','Osama Sadiq','Saba Gul','Aswad Liaqat',
    'M. Shakeel','Ambreen Anwar','Neelam Shahzadi','Umda Sharwani','Mafia Javed']

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
