from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import time
import random
class PlayerBot(Bot):
    def play_round(self):
        yield Demographics

        if self.player.round_number == self.player.participant.task_rounds1['1']:
            time.sleep(10)
            yield Payment1Transition

        if self.player.round_number == self.player.participant.task_rounds1['Econ1']:
            time.sleep(10)
            econ1hints_form = ['econhints1_partner1', 'econhints1_partner2', 'econhints1_partner3', 'econhints1_partner4']
            zero = [0 for i in range(4)]

            a = {}

            for i in range(4):
                a[econ1hints_form[i]] = zero[i]

            yield Economics1Hints, a

            time.sleep(10)
            econ1results_form = ['econresults1_partner1', 'econresults1_partner2', 'econresults1_partner3', 'econresults1_partner4']
            zero = [0 for i in range(4)]

            b = {}

            for i in range(4):
                b[econ1results_form[i]] = zero[i]

            yield Economics1Results, b

            time.sleep(10)
            econ1results0_form = ['econresults01_partner1', 'econresults01_partner2', 'econresults01_partner3', 'econresults01_partner4']
            zero = [0 for i in range(4)]

            c = {}

            for i in range(4):
                c[econ1results0_form[i]] = zero[i]

            yield Economics1Results0, c

        if self.player.round_number == self.player.participant.task_rounds1['Cook1']:
            time.sleep(10)
            cook1hints_form = ['cookhints1_partner1', 'cookhints1_partner2', 'cookhints1_partner3', 'cookhints1_partner4']
            zero = [0 for i in range(4)]

            d = {}

            for i in range(4):
                d[cook1hints_form[i]] = zero[i]

            yield Cooking1Hints, d


            time.sleep(10)
            cook1results_form = ['cookresults1_partner1', 'cookresults1_partner2', 'cookresults1_partner3', 'cookresults1_partner4']
            zero = [0 for i in range(4)]

            e = {}

            for i in range(4):
                e[cook1results_form[i]] = zero[i]

            yield Cooking1Results, e


            time.sleep(10)
            cook1results0_form = ['cookresults01_partner1', 'cookresults01_partner2', 'cookresults01_partner3', 'cookresults01_partner4']
            zero = [0 for i in range(4)]

            f = {}

            for i in range(4):
                f[cook1results0_form[i]] = zero[i]

            yield Cooking1Results0, f

        if self.player.round_number == self.player.participant.task_rounds1['Sport1']:
            time.sleep(10)
            sport1hints_form = ['sporthints1_partner1', 'sporthints1_partner2', 'sporthints1_partner3', 'sporthints1_partner4']
            zero = [0 for i in range(4)]

            g = {}

            for i in range(4):
                g[sport1hints_form[i]] = zero[i]

            yield Sports1Hints, g


            time.sleep(10)
            sport1results_form = ['sportresults1_partner1', 'sportresults1_partner2', 'sportresults1_partner3', 'sportresults1_partner4']
            zero = [0 for i in range(4)]

            h = {}

            for i in range(4):
                h[sport1results_form[i]] = zero[i]

            yield Sports1Results, h


            time.sleep(10)
            sport1results0_form = ['sportresults01_partner1', 'sportresults01_partner2', 'sportresults01_partner3', 'sportresults01_partner4']
            zero = [0 for i in range(4)]

            j = {}

            for i in range(4):
                j[sport1results0_form[i]] = zero[i]

            yield Sports1Results0, j

        if self.player.round_number == self.player.participant.task_rounds1['2']:
            time.sleep(10)
            yield Payment2Transition

        if self.player.round_number == self.player.participant.task_rounds1['Econ2']:
            time.sleep(10)
            econ2hints_form = ['econhints2_partner1', 'econhints2_partner2', 'econhints2_partner3', 'econhints2_partner4']
            zero = [0 for i in range(4)]

            k = {}

            for i in range(4):
                k[econ2hints_form[i]] = zero[i]

            yield Economics2Hints, k


            time.sleep(10)
            econ2results_form = ['econresults2_partner1', 'econresults2_partner2', 'econresults2_partner3', 'econresults2_partner4']
            zero = [0 for i in range(4)]

            l = {}

            for i in range(4):
                l[econ2results_form[i]] = zero[i]

            yield Economics2Results, l


            time.sleep(10)
            econ2results0_form = ['econresults02_partner1', 'econresults02_partner2', 'econresults02_partner3', 'econresults02_partner4']
            zero = [0 for i in range(4)]

            m = {}

            for i in range(4):
                m[econ2results0_form[i]] = zero[i]

            yield Economics2Results0, m

        if self.player.round_number == self.player.participant.task_rounds1['Cook2']:
            time.sleep(10)
            cook2hints_form = ['cookhints2_partner1', 'cookhints2_partner2', 'cookhints2_partner3', 'cookhints2_partner4']
            zero = [0 for i in range(4)]

            n = {}

            for i in range(4):
                n[cook2hints_form[i]] = zero[i]

            yield Cooking2Hints, n


            time.sleep(10)
            cook2results_form = ['cookresults2_partner1', 'cookresults2_partner2', 'cookresults2_partner3', 'cookresults2_partner4']
            zero = [0 for i in range(4)]

            o = {}

            for i in range(4):
                o[cook2results_form[i]] = zero[i]

            yield Cooking2Results, o


            time.sleep(10)
            cook2results0_form = ['cookresults02_partner1', 'cookresults02_partner2', 'cookresults02_partner3', 'cookresults02_partner4']
            zero = [0 for i in range(4)]

            p = {}

            for i in range(4):
                p[cook2results0_form[i]] = zero[i]

            yield Cooking2Results0, p

        if self.player.round_number == self.player.participant.task_rounds1['Sport2']:
            time.sleep(10)
            sport2hints_form = ['sporthints2_partner1', 'sporthints2_partner2', 'sporthints2_partner3', 'sporthints2_partner4']
            zero = [0 for i in range(4)]

            q = {}

            for i in range(4):
                q[sport2hints_form[i]] = zero[i]

            yield Sports2Hints, q


            time.sleep(10)
            sport2results_form = ['sportresults2_partner1', 'sportresults2_partner2', 'sportresults2_partner3', 'sportresults2_partner4']
            zero = [0 for i in range(4)]

            r = {}

            for i in range(4):
                r[sport2results_form[i]] = zero[i]

            yield Sports2Results, r


            time.sleep(10)
            sport2results0_form = ['sportresults02_partner1', 'sportresults02_partner2', 'sportresults02_partner3', 'sportresults02_partner4']
            zero = [0 for i in range(4)]

            s = {}

            for i in range(4):
                s[sport2results0_form[i]] = zero[i]

            yield Sports2Results0, s

        if self.player.round_number == 9:
            time.sleep(10)
            yield Final
