from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import time
import random
class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number == 1:
            yield Demographics

        if self.player.round_number == self.player.participant.task_rounds2['MP']:

            hint_mp_form = ['request_hints_economics_MP', 'request_hints_cooking_MP', 'request_hints_sports_MP', 'results_economics_MP', 'results_cooking_MP', 'results_sports_MP']
            zero = [0 for i in range(6)]

            a = {}

            for i in range(6):
                a[hint_mp_form[i]] = zero[i]

            yield Hints_MP, a

        if self.player.round_number == self.player.participant.task_rounds2['Economics1_MP']:
            econ_mp_form1 = ['crt_economics1_MP','helpful_hint_econ1_MP','prob_econ1_MP']
            one = [1 for i in range(3)]

            b = {}

            for i in range(3):
                b[econ_mp_form1[i]] = one[i]

            yield Economics1_MP, b


        if self.player.round_number == self.player.participant.task_rounds2['Economics2_MP']:
            econ_mp_form2 = ['crt_economics2_MP','helpful_hint_econ2_MP','prob_econ2_MP']
            one = [1 for i in range(3)]

            c = {}

            for i in range(3):
                c[econ_mp_form2[i]] = one[i]

            yield Economics2_MP, c


        if self.player.round_number == self.player.participant.task_rounds2['Economics3_MP']:
            econ_mp_form3 = ['crt_economics3_MP','helpful_hint_econ3_MP','prob_econ3_MP']
            one = [1 for i in range(3)]

            d = {}

            for i in range(3):
                d[econ_mp_form3[i]] = one[i]

            yield Economics3_MP, d


        if self.player.round_number == self.player.participant.task_rounds2['Economics4_MP']:
            econ_mp_form4 = ['crt_economics4_MP','helpful_hint_econ4_MP','prob_econ4_MP']
            one = [1 for i in range(3)]

            e = {}

            for i in range(3):
                e[econ_mp_form4[i]] = one[i]

            yield Economics4_MP, e


        if self.player.round_number == self.player.participant.task_rounds2['Cooking1_MP']:
            cook_mp_form1 = ['crt_cooking1_MP','helpful_hint_cook1_MP','prob_cook1_MP']
            one = [1 for i in range(3)]

            f = {}

            for i in range(3):
                f[cook_mp_form1[i]] = one[i]

            yield Cooking1_MP, f


        if self.player.round_number == self.player.participant.task_rounds2['Cooking2_MP']:
            cook_mp_form2 = ['crt_cooking2_MP','helpful_hint_cook2_MP','prob_cook2_MP']
            one = [1 for i in range(3)]

            g = {}

            for i in range(3):
                g[cook_mp_form2[i]] = one[i]

            yield Cooking2_MP, g


        if self.player.round_number == self.player.participant.task_rounds2['Cooking3_MP']:
            cook_mp_form3 = ['crt_cooking3_MP','helpful_hint_cook3_MP','prob_cook3_MP']
            one = [1 for i in range(3)]

            h = {}

            for i in range(3):
                h[cook_mp_form3[i]] = one[i]

            yield Cooking3_MP, h


        if self.player.round_number == self.player.participant.task_rounds2['Cooking4_MP']:
            cook_mp_form4 = ['crt_cooking4_MP','helpful_hint_cook4_MP','prob_cook4_MP']
            one = [1 for i in range(3)]

            j = {}

            for i in range(3):
                j[cook_mp_form4[i]] = one[i]

            yield Cooking4_MP, j

        if self.player.round_number == self.player.participant.task_rounds2['Sports1_MP']:
            sport_mp_form1 = ['crt_sports1_MP','helpful_hint_sport1_MP','prob_sport1_MP']
            one = [1 for i in range(3)]

            k = {}

            for i in range(3):
                k[sport_mp_form1[i]] = one[i]

            yield Sports1_MP, k


        if self.player.round_number == self.player.participant.task_rounds2['Sports2_MP']:
            sport_mp_form2 = ['crt_sports2_MP','helpful_hint_sport2_MP','prob_sport2_MP']
            one = [1 for i in range(3)]

            l = {}

            for i in range(3):
                l[sport_mp_form2[i]] = one[i]

            yield Sports2_MP, l


        if self.player.round_number == self.player.participant.task_rounds2['Sports3_MP']:
            sport_mp_form3 = ['crt_sports3_MP','helpful_hint_sport3_MP','prob_sport3_MP']
            one = [1 for i in range(3)]

            m = {}

            for i in range(3):
                m[sport_mp_form3[i]] = one[i]

            yield Sports3_MP, m


        if self.player.round_number == self.player.participant.task_rounds2['Sports4_MP']:
            sport_mp_form4 = ['crt_sports4_MP','helpful_hint_sport4_MP','prob_sport4_MP']
            one = [1 for i in range(3)]

            n = {}

            for i in range(3):
                n[sport_mp_form4[i]] = one[i]

            yield Sports4_MP, n


        if self.player.round_number == self.player.participant.task_rounds2['MR']:
            hint_mr_form = ['request_hints_economics_MR', 'request_hints_cooking_MR', 'request_hints_sports_MR', 'results_economics_MR', 'results_cooking_MR', 'results_sports_MR']
            zero = [0 for i in range(6)]

            o = {}

            for i in range(6):
                o[hint_mr_form[i]] = zero[i]

            yield Hints_MR, o


        if self.player.round_number == self.player.participant.task_rounds2['Economics1_MR']:
            econ_mr_form1 = ['crt_economics1_MR','helpful_hint_econ1_MR','prob_econ1_MR']
            one = [1 for i in range(3)]

            p = {}

            for i in range(3):
                p[econ_mr_form1[i]] = one[i]

            yield Economics1_MR, p


        if self.player.round_number == self.player.participant.task_rounds2['Economics2_MR']:
            econ_mr_form2 = ['crt_economics2_MR','helpful_hint_econ2_MR','prob_econ2_MR']
            one = [1 for i in range(3)]

            q = {}

            for i in range(3):
                q[econ_mr_form2[i]] = one[i]

            yield Economics2_MR, q

        if self.player.round_number == self.player.participant.task_rounds2['Economics3_MR']:
            econ_mr_form3 = ['crt_economics3_MR','helpful_hint_econ3_MR','prob_econ3_MR']
            one = [1 for i in range(3)]

            r = {}

            for i in range(3):
                r[econ_mr_form3[i]] = one[i]

            yield Economics3_MR, r


        if self.player.round_number == self.player.participant.task_rounds2['Economics4_MR']:
            econ_mr_form4 = ['crt_economics4_MR','helpful_hint_econ4_MR','prob_econ4_MR']
            one = [1 for i in range(3)]

            s = {}

            for i in range(3):
                s[econ_mr_form4[i]] = one[i]

            yield Economics4_MR, s


        if self.player.round_number == self.player.participant.task_rounds2['Cooking1_MR']:
            cook_mr_form1 = ['crt_cooking1_MR','helpful_hint_cook1_MR','prob_cook1_MR']
            one = [1 for i in range(3)]

            t = {}

            for i in range(3):
                t[cook_mr_form1[i]] = one[i]

            yield Cooking1_MR, t

        if self.player.round_number == self.player.participant.task_rounds2['Cooking2_MR']:
            cook_mr_form2 = ['crt_cooking2_MR','helpful_hint_cook2_MR','prob_cook2_MR']
            one = [1 for i in range(3)]

            u = {}

            for i in range(3):
                u[cook_mr_form2[i]] = one[i]

            yield Cooking2_MR, u


        if self.player.round_number == self.player.participant.task_rounds2['Cooking3_MR']:
            cook_mr_form3 = ['crt_cooking3_MR','helpful_hint_cook3_MR','prob_cook3_MR']
            one = [1 for i in range(3)]

            v = {}

            for i in range(3):
                v[cook_mr_form3[i]] = one[i]

            yield Cooking3_MR, v


        if self.player.round_number == self.player.participant.task_rounds2['Cooking4_MR']:
            cook_mr_form4 = ['crt_cooking4_MR','helpful_hint_cook4_MR','prob_cook4_MR']
            one = [1 for i in range(3)]

            w = {}

            for i in range(3):
                w[cook_mr_form4[i]] = one[i]

            yield Cooking4_MR, w

        if self.player.round_number == self.player.participant.task_rounds2['Sports1_MR']:
            sport_mr_form1 = ['crt_sports1_MR','helpful_hint_sport1_MR','prob_sport1_MR']
            one = [1 for i in range(3)]

            x = {}

            for i in range(3):
                x[sport_mr_form1[i]] = one[i]

            yield Sports1_MR, x


        if self.player.round_number == self.player.participant.task_rounds2['Sports2_MR']:
            sport_mr_form2 = ['crt_sports2_MR','helpful_hint_sport2_MR','prob_sport2_MR']
            one = [1 for i in range(3)]

            y = {}

            for i in range(3):
                y[sport_mr_form2[i]] = one[i]

            yield Sports2_MR, y


        if self.player.round_number == self.player.participant.task_rounds2['Sports3_MR']:
            sport_mr_form3 = ['crt_sports3_MR','helpful_hint_sport3_MR','prob_sport3_MR']
            one = [1 for i in range(3)]

            z = {}

            for i in range(3):
                z[sport_mr_form3[i]] = one[i]

            yield Sports3_MR, z


        if self.player.round_number == self.player.participant.task_rounds2['Sports4_MR']:
            sport_mr_form4 = ['crt_sports4_MR','helpful_hint_sport4_MR','prob_sport4_MR']
            one = [1 for i in range(3)]

            aa = {}

            for i in range(3):
                aa[sport_mr_form4[i]] = one[i]

            yield Sports4_MR, aa

        if self.player.round_number == self.player.participant.task_rounds2['WP']:
            hint_wp_form = ['request_hints_economics_WP', 'request_hints_cooking_WP', 'request_hints_sports_WP', 'results_economics_WP', 'results_cooking_WP', 'results_sports_WP']
            zero = [0 for i in range(6)]

            ab = {}

            for i in range(6):
                ab[hint_wp_form[i]] = zero[i]

            yield Hints_WP, ab

        if self.player.round_number == self.player.participant.task_rounds2['Economics1_WP']:
            econ_wp_form1 = ['crt_economics1_WP','helpful_hint_econ1_WP','prob_econ1_WP']
            one = [1 for i in range(3)]

            ac = {}

            for i in range(3):
                ac[econ_wp_form1[i]] = one[i]

            yield Economics1_WP, ac


        if self.player.round_number == self.player.participant.task_rounds2['Economics2_WP']:
            econ_wp_form2 = ['crt_economics2_WP','helpful_hint_econ2_WP','prob_econ2_WP']
            one = [1 for i in range(3)]

            ad = {}

            for i in range(3):
                ad[econ_wp_form2[i]] = one[i]

            yield Economics2_WP, ad


        if self.player.round_number == self.player.participant.task_rounds2['Economics3_WP']:
            econ_wp_form3 = ['crt_economics3_WP','helpful_hint_econ3_WP','prob_econ3_WP']
            one = [1 for i in range(3)]

            ae = {}

            for i in range(3):
                ae[econ_wp_form3[i]] = one[i]

            yield Economics3_WP, ae


        if self.player.round_number == self.player.participant.task_rounds2['Economics4_WP']:
            econ_wp_form4 = ['crt_economics4_WP','helpful_hint_econ4_WP','prob_econ4_WP']
            one = [1 for i in range(3)]

            af = {}

            for i in range(3):
                af[econ_wp_form4[i]] = one[i]

            yield Economics4_WP, af


        if self.player.round_number == self.player.participant.task_rounds2['Cooking1_WP']:
            cook_wp_form1 = ['crt_cooking1_WP','helpful_hint_cook1_WP','prob_cook1_WP']
            one = [1 for i in range(3)]

            ag = {}

            for i in range(3):
                ag[cook_wp_form1[i]] = one[i]

            yield Cooking1_WP, ag


        if self.player.round_number == self.player.participant.task_rounds2['Cooking2_WP']:
            cook_wp_form2 = ['crt_cooking2_WP','helpful_hint_cook2_WP','prob_cook2_WP']
            one = [1 for i in range(3)]

            ah = {}

            for i in range(3):
                ah[cook_wp_form2[i]] = one[i]

            yield Cooking2_WP, ah


        if self.player.round_number == self.player.participant.task_rounds2['Cooking3_WP']:
            cook_wp_form3 = ['crt_cooking3_WP','helpful_hint_cook3_WP','prob_cook3_WP']
            one = [1 for i in range(3)]

            aj = {}

            for i in range(3):
                aj[cook_wp_form3[i]] = one[i]

            yield Cooking3_WP, aj


        if self.player.round_number == self.player.participant.task_rounds2['Cooking4_WP']:
            cook_wp_form4 = ['crt_cooking4_WP','helpful_hint_cook4_WP','prob_cook4_WP']
            one = [1 for i in range(3)]

            ak = {}

            for i in range(3):
                ak[cook_wp_form4[i]] = one[i]

            yield Cooking4_WP, ak

        if self.player.round_number == self.player.participant.task_rounds2['Sports1_WP']:
            sport_wp_form1 = ['crt_sports1_WP','helpful_hint_sport1_WP','prob_sport1_WP']
            one = [1 for i in range(3)]

            al = {}

            for i in range(3):
                al[sport_wp_form1[i]] = one[i]

            yield Sports1_WP, al


        if self.player.round_number == self.player.participant.task_rounds2['Sports2_WP']:
            sport_wp_form2 = ['crt_sports2_WP','helpful_hint_sport2_WP','prob_sport2_WP']
            one = [1 for i in range(3)]

            am = {}

            for i in range(3):
                am[sport_wp_form2[i]] = one[i]

            yield Sports2_WP, am


        if self.player.round_number == self.player.participant.task_rounds2['Sports3_WP']:
            sport_wp_form3 = ['crt_sports3_WP','helpful_hint_sport3_WP','prob_sport3_WP']
            one = [1 for i in range(3)]

            an = {}

            for i in range(3):
                an[sport_wp_form3[i]] = one[i]

            yield Sports3_WP, an


        if self.player.round_number == self.player.participant.task_rounds2['Sports4_WP']:
            sport_wp_form4 = ['crt_sports4_WP','helpful_hint_sport4_WP','prob_sport4_WP']
            one = [1 for i in range(3)]

            ao = {}

            for i in range(3):
                ao[sport_wp_form4[i]] = one[i]

            yield Sports4_WP, ao

        if self.player.round_number == self.player.participant.task_rounds2['WR']:
            hint_wr_form = ['request_hints_economics_WR', 'request_hints_cooking_WR', 'request_hints_sports_WR', 'results_economics_WR', 'results_cooking_WR', 'results_sports_WR']
            zero = [0 for i in range(6)]

            ap = {}

            for i in range(6):
                ap[hint_wr_form[i]] = zero[i]

            yield Hints_WR, ap


        if self.player.round_number == self.player.participant.task_rounds2['Economics1_WR']:
            econ_wr_form1 = ['crt_economics1_WR','helpful_hint_econ1_WR','prob_econ1_WR']
            one = [1 for i in range(3)]

            aq = {}

            for i in range(3):
                aq[econ_wr_form1[i]] = one[i]

            yield Economics1_WR, aq


        if self.player.round_number == self.player.participant.task_rounds2['Economics2_WR']:
            econ_wr_form2 = ['crt_economics2_WR','helpful_hint_econ2_WR','prob_econ2_WR']
            one = [1 for i in range(3)]

            ar = {}

            for i in range(3):
                ar[econ_wr_form2[i]] = one[i]

            yield Economics2_WR, ar


        if self.player.round_number == self.player.participant.task_rounds2['Economics3_WR']:
            econ_wr_form3 = ['crt_economics3_WR','helpful_hint_econ3_WR','prob_econ3_WR']
            one = [1 for i in range(3)]

            at = {}

            for i in range(3):
                at[econ_wr_form3[i]] = one[i]

            yield Economics3_WR, at


        if self.player.round_number == self.player.participant.task_rounds2['Economics4_WR']:
            econ_wr_form4 = ['crt_economics4_WR','helpful_hint_econ4_WR','prob_econ4_WR']
            one = [1 for i in range(3)]

            au = {}

            for i in range(3):
                au[econ_wr_form4[i]] = one[i]

            yield Economics4_WR, au


        if self.player.round_number == self.player.participant.task_rounds2['Cooking1_WR']:
            cook_wr_form1 = ['crt_cooking1_WR','helpful_hint_cook1_WR','prob_cook1_WR']
            one = [1 for i in range(3)]

            av = {}

            for i in range(3):
                av[cook_wr_form1[i]] = one[i]

            yield Cooking1_WR, av


        if self.player.round_number == self.player.participant.task_rounds2['Cooking2_WR']:
            cook_wr_form2 = ['crt_cooking2_WR','helpful_hint_cook2_WR','prob_cook2_WR']
            one = [1 for i in range(3)]

            aw = {}

            for i in range(3):
                aw[cook_wr_form2[i]] = one[i]

            yield Cooking2_WR, aw


        if self.player.round_number == self.player.participant.task_rounds2['Cooking3_WR']:
            cook_wr_form3 = ['crt_cooking3_WR','helpful_hint_cook3_WR','prob_cook3_WR']
            one = [1 for i in range(3)]

            ax = {}

            for i in range(3):
                ax[cook_wr_form3[i]] = one[i]

            yield Cooking3_WR, ax


        if self.player.round_number == self.player.participant.task_rounds2['Cooking4_WR']:
            cook_wr_form4 = ['crt_cooking4_WR','helpful_hint_cook4_WR','prob_cook4_WR']
            one = [1 for i in range(3)]

            ay = {}

            for i in range(3):
                ay[cook_wr_form4[i]] = one[i]

            yield Cooking4_WR, ay

        if self.player.round_number == self.player.participant.task_rounds2['Sports1_WR']:
            sport_wr_form1 = ['crt_sports1_WR','helpful_hint_sport1_WR','prob_sport1_WR']
            one = [1 for i in range(3)]

            az = {}

            for i in range(3):
                az[sport_wr_form1[i]] = one[i]

            yield Sports1_WR, az


        if self.player.round_number == self.player.participant.task_rounds2['Sports2_WR']:
            sport_wr_form2 = ['crt_sports2_WR','helpful_hint_sport2_WR','prob_sport2_WR']
            one = [1 for i in range(3)]

            ba = {}

            for i in range(3):
                ba[sport_wr_form2[i]] = one[i]

            yield Sports2_WR, ba


        if self.player.round_number == self.player.participant.task_rounds2['Sports3_WR']:
            sport_wr_form3 = ['crt_sports3_WR','helpful_hint_sport3_WR','prob_sport3_WR']
            one = [1 for i in range(3)]

            bb = {}

            for i in range(3):
                bb[sport_wr_form3[i]] = one[i]

            yield Sports3_WR, bb


        if self.player.round_number == self.player.participant.task_rounds2['Sports4_WR']:
            sport_wr_form4 = ['crt_sports4_WR','helpful_hint_sport4_WR','prob_sport4_WR']
            one = [1 for i in range(3)]

            bc = {}

            for i in range(3):
                bc[sport_wr_form4[i]] = one[i]

            yield Sports4_WR, bc

        if self.player.round_number == 52:
            yield Final
