from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
dict(
        name='ultimatumn_anonym',
        display_name='ultimatumn_anonym',
        num_demo_participants= 1,
        app_sequence=['Consentform',
                      'ultimatumn_anonym',
                      'ultimatumn_anonym2',
                      'ultimatumn_anonym3',
                      'description',
                      'Persona1',
                      'Persona2',
                      'Persona3',
                      'Persona4',
                      'Persona5',]
),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '*$(%y^)7of_1+g=3ug$_t2cij3m5qy6k_5=pn33$)*hq8*a)g1'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
