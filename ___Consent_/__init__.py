from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,]
    LABELS = ['Abdul_Mateen_Khan','Abdullah_Bin_Umar','Abdullah_Irfan','Abdullah_Saeed_Mirza',
    'Ali_Imran','Alishba_Sajjad','Anushey_Rehman','Arslan_Asif','Asad_Kashif','Ather_Saeed',
    'Bisma_Nadeem','Fahmeen_Javed','Fatima_Sheiklh','Haadi_Mashood','Hamza_Shafqat',
    'Hamza_Umar','Humayd_Haider','Junaid_Mir','Layba_Mazhar','Maryam_Toor','Meeran_Khan',
    'Mohad_Rehan','Momin_Ahsan','Muhammad_Aayan_Siddiq','Muhammad_Ahsan','Muhammad_Aneeq_Tahir',
    'Muhammad_Hur_Abbas','Muhammad_Mahad_Tanveer','Muhammad_Numan','Muhammad_Salman',
    'Muhammad_Sher_Dil','Muhammad_Sufian_Masoom','Muhammad_Umer_Farooq','Muhammad_Usama_Haroon',
    'Muhammad_Usman_Javed','Muqadas_Fatima','Mustafa_Abubaker','Nabiha_Omar_Qazi',
    'Rida_Faisal','Sahibzada_Raza_Hassan_Khan','Shahzada_Muhammad_Rohaan','Uzair_Zubair',
    'Zain_Faisal','Zurain_Fatima','Abdul_Wasay','Abdullah_Arshad','Abdullah_Kashif_Bhatti',
    'Abu_Sufian','Ahmad_Farhan','Ahmed_Wasif_Bashir','Ali_Ahmed_Danish','Aman_Faisal',
    'Arslan_Qadeer','Ayesha_Ashfaq','Farriha_Tahir_Malik','Fatima_Sarwar','Fatima_Mumtaz',
    'Fatima_Rana','Fiza_Yasir','Hassan_Javaid','Hassan_Raza_Bhatti','Hira_Mukhtar',
    'Hussain_Naveed_Tarar','Ibrahim_Akram_Cheema','Maham_Fateh','Mehar_Tariq_Siraj',
    'Minahil_Waqar','Mohammad_Awais_Bakhshi','Mohammad_Hanzala','Muhammad_Alim_Tahir',
    'Muhammad_Aliyan_Khan','Muhammad_Anas_Nadeem','Muhammad_Bilal_Tariq','Muhammad_Hassaan_Bin_Shoaib',
    'Muhammad_Ibrahim_Chaudhry','Muhammad_Munimureshi','Muhammad_Naeem_Baig','Muhammad_Rahim_Azeem',
    'Muhammad_Raza_Khan','Muhammad_Talha_Mehmood','Mustafa_Saeed','Nouman_Aslam',
    'Sameen_Sohail','Talha_Manzoor','Umar_Imran','Zahb_Anjum_Butt','Zainab_Kamran',
    'Zam_Zam_Habib','Zain_Aziz_Khawaja','Musa_Tariq','Alishba_Zahid']
    PLAYERS = ['Abdul Mateen Khan','Abdullah Bin Umar','Abdullah Irfan','Abdullah Saeed Mirza',
    'Ali Imran','Alishba Sajjad','Anushey Rehman','Arslan Asif','Asad Kashif','Ather Saeed',
    'Bisma Nadeem','Fahmeen Javed','Fatima Sheiklh','Haadi Mashood','Hamza Shafqat',
    'Hamza Umar','Humayd Haider','Junaid Mir','Layba Mazhar','Maryam Toor','Meeran Khan',
    'Mohad Rehan','Momin Ahsan','Muhammad Aayan Siddiq','Muhammad Ahsan','Muhammad Aneeq Tahir',
    'Muhammad Hur Abbas','Muhammad Mahad Tanveer','Muhammad Numan','Muhammad Salman',
    'Muhammad Sher Dil','Muhammad Sufian Masoom','Muhammad Umer Farooq','Muhammad Usama Haroon',
    'Muhammad Usman Javed','Muqadas Fatima','Mustafa Abubaker','Nabiha Omar Qazi',
    'Rida Faisal','Sahibzada Raza Hassan Khan','Shahzada Muhammad Rohaan','Uzair Zubair',
    'Zain Faisal','Zurain Fatima','Abdul Wasay','Abdullah Arshad','Abdullah Kashif Bhatti',
    'Abu Sufian','Ahmad Farhan','Ahmed Wasif Bashir','Ali Ahmed Danish','Aman Faisal',
    'Arslan Qadeer','Ayesha Ashfaq','Farriha Tahir Malik','Fatima Sarwar','Fatima Mumtaz',
    'Fatima Rana','Fiza Yasir','Hassan Javaid','Hassan Raza Bhatti','Hira Mukhtar',
    'Hussain Naveed Tarar','Ibrahim Akram Cheema','Maham Fateh','Mehar Tariq Siraj',
    'Minahil Waqar','Mohammad Awais Bakhshi','Mohammad Hanzala','Muhammad Alim Tahir',
    'Muhammad Aliyan Khan','Muhammad Anas Nadeem','Muhammad Bilal Tariq','Muhammad Hassaan Bin Shoaib',
    'Muhammad Ibrahim Chaudhry','Muhammad Munimureshi','Muhammad Naeem Baig','Muhammad Rahim Azeem',
    'Muhammad Raza Khan','Muhammad Talha Mehmood','Mustafa Saeed','Nouman Aslam',
    'Sameen Sohail','Talha Manzoor','Umar Imran','Zahb Anjum Butt','Zainab Kamran',
    'Zam Zam Habib','Zain Aziz Khawaja','Musa Tariq','Alishba Zahid']

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
    roll = models.StringField(label='Please type your rollnumber')

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
    body_text = ""

page_sequence = [Consent, WaitPage1]
