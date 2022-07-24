from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = '___Consent_'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    GENDERS_LIST = [0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,]
    LABELS = ['Ramsha_Azhar','Muhammad_Saood','Abdullah_Mir','Azqa','Mubeen_Ahmad',
    'Momina_Azam','Salem_Hamad','Daniyal_Mansur','Syeda_Laiba_Bukhari','Ahmed_Mujtaba',
    'Fatima_Rana','Abdullah_Shahzad','Zainab_Kamran','Neha_Jameel','Hassan_Masood',
    'Muhammad_Hamza','Laraib_Naeem','Maham_Ali','Amna_Imran','Muhammad_Samran_Sohail',
    'Rabia_Riaz','Amna_Noor','Farriha','Muhammad_Taahaa_Imtiaz','Sarah_Asif_Khan',
    'Mohammad_Sheheryar_Khan','Saad_Munir','Muhammad_Usman','Ayra_Arshad',
    'Muhammad_Swaleh_Shaheen_Rafi','Muhammad_Wahab_Malik','Muhammad_Anas_Khan',
    'Rai_Sarib_Hayat_Khan','Muhammad_Salman_Bin_Hamid','Abdul_Moeed','Haad_Mahmood',
    'Ameera_Amir','Alishba_Arshad_Legari','Areeb_Khan','Hamnah_Kamran','Khadija_Kamran',
    'Fatima_Khan','Tabish_Shahid','Shahmeer','Aniq_Kamran_Butt','Rubab_Aslam_Mian',
    'Lalarukh_Schkoh','Rida_Fatima','Muhammad_Muaz','Momin','Muhammad_Abdullah_Khawaja',
    'Muhammad_Ahmad','Hoor_Shmail','Muhammad_Shariq_Pervez','Mustafa_Abubakar','Ayesha_Ashfaq',
    'Shaheer_Bin_Ateeq','Muhammad_Raza_Khan','Khadija_Tariq','Maham_Rehman','Faizan_Ali','Sarmad_Imtiaz']

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
    labels = ['Ramsha Azhar','Muhammad Saood','Abdullah Mir','Azqa','Mubeen Ahmad',
    'Momina Azam','Salem Hamad','Daniyal Mansur','Syeda Laiba Bukhari','Ahmed Mujtaba',
    'Fatima Rana','Abdullah Shahzad','Zainab Kamran','Neha Jameel','Hassan Masood',
    'Muhammad Hamza','Laraib Naeem','Maham Ali','Amna Imran','Muhammad Samran Sohail',
    'Rabia Riaz','Amna Noor','Farriha','Muhammad Taahaa Imtiaz','Sarah Asif Khan',
    'Mohammad Sheheryar Khan','Saad Munir','Muhammad Usman','Ayra Arshad',
    'Muhammad Swaleh Shaheen Rafi','Muhammad Wahab Malik','Muhammad Anas Khan',
    'Rai Sarib Hayat Khan','Muhammad Salman Bin Hamid','Abdul Moeed','Haad Mahmood',
    'Ameera Amir','Alishba Arshad Legari','Areeb Khan','Hamnah Kamran','Khadija Kamran',
    'Fatima Khan','Tabish Shahid','Shahmeer','Aniq Kamran Butt','Rubab Aslam Mian',
    'Lalarukh Schkoh','Rida Fatima','Muhammad Muaz','Momin','Muhammad Abdullah Khawaja',
    'Muhammad Ahmad','Hoor Shmail','Muhammad Shariq Pervez','Mustafa Abubakar','Ayesha Ashfaq',
    'Shaheer Bin Ateeq','Muhammad Raza Khan','Khadija Tariq','Maham Rehman','Faizan Ali','Sarmad Imtiaz']
    for current, new in zip(C.LABELS, labels):
        if player.participant.label == current.lstrip():
            player.participant.label = new

def set_gender(player: Player):
    subsession = player.subsession
    people = dict(zip(C.LABELS,C.GENDERS_LIST))
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
        set_gender(player)
        change_labels(player)
        set_players(player)

class WaitPage1(WaitPage):
    title_text = "Waiting for all players to finish"
    body_text = ""

page_sequence = [Consent, WaitPage1]
