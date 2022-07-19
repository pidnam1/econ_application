from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        genders_list =  [0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,]

        ###change for diff tests
        PLAYERS = ['Ramsha Azhar','Muhammad Saood','Abdullah Mir','Azqa','Mubeen Ahmad',
        'Momina Azam','Salem Hamad','Daniyal Mansur','Syeda Laiba Bukhari','Ahmed Mujtaba',
        'Fatima Rana','Abdullah Shahzad','Zainab Kamran','Neha Jameel','Hassan Masood',
        'Muhammad Hamza','Laraib Naeem','Maham Ali','Amna Imran','Muhammad Samran Sohail',
        'Rabia Riaz','Amna Noor','Farriha','Muhammad Taahaa Imtiaz','Sarah Asif Khan',
        'Mohammad Sheheryar Khan','Saad Munir','Muhammad Usman','Ayra Arshad',
        'Muhammad Swaleh Shaheen Rafi','Muhammad Wahab Malik','Muhammad Anas Khan',
        'Rai Sarib Hayat Khan','Muhammad Salman Bin Hamid','Abdul Moeed','Haad Mahmood',
        'Ameera Amir','Alishba Arshad Legari','Areeb Khan','Hamnah Kamran','Khadija Kamran',
        'Fatima Khan','Tabish Shahid','Shahmeer','Aniq Kamran Butt','Rubab Aslam Mian',
        'Lalarukh Schkoh','Rida Fatima']
        x = {}
        id = self.player.id_in_group - 1
        x["roll"] = id + 1
        x["esig"] = PLAYERS[id]
        self.player.participant.label = PLAYERS[id]
        self.player.participant.gender = genders_list[id]
        self.player.participant.roll_no = id + 1
        self.player.participant.count_participant = id+1
        x["agree"] = "I agree"
        yield Consent, x
