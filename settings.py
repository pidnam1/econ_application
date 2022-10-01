from os import environ


SESSION_CONFIGS = [
    dict(
        name='my_project',
        display_name = "Survey",
        app_sequence = ['___Consent_','___Preferences_','___Practice_','___Round0_','___Round1_','___Round2_','___Round3b_','___Round2_1','___Endline_','___Final_','___Payment_'],
        num_demo_participants=18
    ),
    # dict(
    #     name='Tester',
    #     display_name = "Tester",
    #     app_sequence=['___Consent_','___Preferences_','___Round1_','___Endline_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name="___Consent_",
    #     display_name = "Consent",
    #     app_sequence = ['___Consent_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name="___Preferences_",
    #     display_name = "Preferences",
    #     app_sequence = ['___Preferences_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='___Practice_',
    #     display_name = "Practice",
    #     app_sequence=['___Practice_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='___Round0_',
    #     display_name = "Round 0",
    #     app_sequence=['___Round0_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='___Round0b_',
    #     display_name = "Round 0b",
    #     app_sequence=['___Round0b_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='___Round1_',
    #     display_name = "Round 1",
    #     app_sequence=['___Round1_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='___Round2_',
    #     display_name = "Round 2",
    #     app_sequence=['___Round2_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='___Round3b_',
    #     display_name = "Round 3B",
    #     app_sequence=['___Round3b_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name="___Final_",
    #     display_name = "Final",
    #     app_sequence=['___Final_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name="___Endline_",
    #     display_name = "Endline",
    #     app_sequence=['___Endline_'],
    #     num_demo_participants=21
    # ),
    # dict(
    #     name='wait_page_timeout',
    #     display_name="Timeout on a WaitPage (exit the experiment)",
    #     num_demo_participants=2,
    #     app_sequence=['wait_page_timeout'],
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, count=0, use_browser_bots=True,  doc=""
)

PARTICIPANT_FIELDS = ['task_rounds_prac','task_rounds0','task_rounds0b','task_rounds1','task_rounds2',
'task_rounds3b','task_roundsf','expiry','MP1hints_given_econ','MP1hints_given_cook','MP1hints_given_sport',
'MR1hints_given_econ','MR1hints_given_cook','MR1hints_given_sport','WP1hints_given_econ',
'WP1hints_given_cook','WP1hints_given_sport','WR1hints_given_econ','WR1hints_given_cook',
'WR1hints_given_sport','MP2hints_given_econ','MP2hints_given_cook','MP2hints_given_sport',
'MR2hints_given_econ','MR2hints_given_cook','MR2hints_given_sport','WP2hints_given_econ',
'WP2hints_given_cook','WP2hints_given_sport','WR2hints_given_econ','WR2hints_given_cook',
'WR2hints_given_sport','hints_given_econ','hints_given_cook','hints_given_sport',
'comp_hints_given_econ','comp_hints_given_cook','comp_hints_given_sport','hints_guess_econ_m1',
'hints_guess_econ_m2','hints_guess_econ_m3','hints_guess_econ_m4','hints_guess_econ_f1',
'hints_guess_econ_f2','hints_guess_econ_f3','hints_guess_econ_f4','hints_guess_cook_m1',
'hints_guess_cook_m2','hints_guess_cook_m3','hints_guess_cook_m4','hints_guess_cook_f1',
'hints_guess_cook_f2','hints_guess_cook_f3','hints_guess_cook_f4','hints_guess_sport_m1',
'hints_guess_sport_m2','hints_guess_sport_m3','hints_guess_sport_m4','hints_guess_sport_f1',
'hints_guess_sport_f2','hints_guess_sport_f3','hints_guess_sport_f4','guess_bonus_payoff',
'econ_hint_requests','cook_hint_requests','sport_hint_requests',
'econ_hint_requests_partner1','econ_hint_requests_partner2','econ_hint_requests_partner3',
'econ_hint_requests_partner4','econ_hint_requests_partner5','econ_hint_requests_partner6',
'econ_hint_requests_partner7','econ_hint_requests_partner8','cook_hint_requests_partner1',
'cook_hint_requests_partner2','cook_hint_requests_partner3','cook_hint_requests_partner4',
'cook_hint_requests_partner5','cook_hint_requests_partner6','cook_hint_requests_partner7',
'cook_hint_requests_partner8','sport_hint_requests_partner1','sport_hint_requests_partner2',
'sport_hint_requests_partner3','sport_hint_requests_partner4','sport_hint_requests_partner5',
'sport_hint_requests_partner6','sport_hint_requests_partner7','sport_hint_requests_partner8',
'econ_hint_used_partner2','econ_hint_used_partner3','econ_hint_used_partner6',
'econ_hint_used_partner8','cook_hint_used_partner2','cook_hint_used_partner3',
'cook_hint_used_partner6','cook_hint_used_partner8','sport_hint_used_partner2',
'sport_hint_used_partner3','sport_hint_used_partner6','sport_hint_used_partner8',
'econ_hint_used','cook_hint_used','sport_hint_used','partner1','partner2','partner3',
'partner4','partner5','partner6','partner7','partner8','partnerf1','partnerf2',
'partnerf3', 'partnerf4','partnerm1','partnerm2','partnerm3','partnerm4','name',
'gender','roll_no','count_participant','round2_completed','round3b_completed',
'form_fields_pref','form_fields_pref2','random','random1','random2','random3',
'random4','random5','random6','random7','random8','exclude','partner_exclude',
'prev_hint','mismatch_econ','mismatch_cook','mismatch_sport','pref_tt','pref_tt_male',
'pref_tt_female',"helpers_dict","pref_helpers","pref_female_helpers", "pref_male_helpers",
"assigned_helpers", "tts", "female_tts", "male_tts",'payoff_tt','payoff_helped',
'payoff_help','wtp_payment','responses_0','responses_0b','responses_2_MP','responses_2_MR',
'responses_2_WP','responses_2_WR','responses_3b_MP','responses_3b_MR','responses_3b_WP',
'responses_3b_WR','game_payoff','total_payment','players','name_list','name_list1','already_clicked',
'random_multiple_price', 'hints1', 'hints2']
SESSION_FIELDS = ['count','active_players','arrived_ids','wait_for_ids','wtp_finished']

# ISO-6310 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
#    dict(
#        name='econ101',
#        display_name='Econ 101 class',
#        participant_label_file='_rooms/econ101.txt',
#    ),
#    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(
        name='Room_1',
        display_name="Room 1",
        participant_label_file='_rooms/labels.txt',
    ),
    dict(
        name='Room_2',
        display_name="Room 2",
        participant_label_file='_rooms/labels.txt',
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ Thank you for your participation! """


SECRET_KEY = '17572210623272'

INSTALLED_APPS = ['otree']
