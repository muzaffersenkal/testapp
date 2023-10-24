from flask import Flask, request
from protectremote import pr_access, set_token

app = Flask(__name__)

TOKEN = "CfDJ8KnTfnUQ6ERKsYXPydkz34Fv0N_q5Uu3hfqUfUp0c_6oWTzJIWJ7OjeY9QrlLsTuC9CwRPY3TwTMMdRd2wLaVClzC8J2onz4kLWRYfjfzCYuSP3seshop0jEFxPezUfinAfIhwoMiilj45h60hbS8aLPYytC4AJvE-8vRGhAcFA_mulhACF-vX1TGqSEZ6yZ5uUluy2CudrNa4pdf5gDAbXuJL-jFP_YGFif7JVrtc2gsk-_bD9T4pdTzFLKshBJZQFD1rWA9c1LDPNAvZyEufXRY7ZniM5XzwDlWnafTtfyRic_jbe3ybH2SLDJsUmYFLcZoko2RAKi1BIb1V9riw9MFMd6bn2n43RUfMbWlk7YxQtmDR9F1r0HXwxYoKSjTA"
set_token(TOKEN)

@app.route('/')
def public():
    return 'Hello'


@app.route('/secured')
@pr_access()
def secured():
    return 'secured'

