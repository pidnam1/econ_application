from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        genders_list = [1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,]

        ###change for diff tests
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
