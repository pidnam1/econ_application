from pathlib import Path
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.routing import Route
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from requests import session as requests_session
from ws4py.client.threadedclient import WebSocketClient
import requests  # pip3 install requests
from pprint import pprint

templates = Jinja2Templates(directory='')


labels = Path('_rooms/labels.txt').read_text('utf8').split()
genders_list = [0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1]
genders = dict(zip(labels,genders_list))
roll_nos_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
roll_nos = dict(zip(labels,roll_nos_list))
count = 0


print('labels:', labels)

OTREE_SERVER = "http://localhost:8000"
ROOM_NAME = 'Pilot'


PARTICIPANT_LABEL_PARAM = 'participant_label'
REST_KEY = ''


GET = requests.get
POST = requests.post


def call_api(method, *path_parts, **params) -> dict:
    path_parts = '/'.join(path_parts)
    url = f'{OTREE_SERVER}/api/{path_parts}/'
    resp = method(url, json=params, headers={'otree-rest-key': REST_KEY})
    if not resp.ok:
        msg = (
            f'Request to "{url}" failed '
            f'with status code {resp.status_code}: {resp.text}'
        )
        raise Exception(msg)
    return resp.json()

def homepage(request: Request):
    label = request.query_params.get('participant_label', '')
    wrong_label = False
    if label:
        if label in labels:
            labels.remove(label)
            if label in genders:
                gender = genders[label]
            if label in roll_nos:
                roll_no = roll_nos[label]
            global count
            count = count + 1
            params = dict(gender=gender,roll_no=roll_no,count_participant=count)
            call_api(
                POST,
                'participant_vars',
                room_name=ROOM_NAME,
                participant_label=label,
                vars=params,
            )
            return RedirectResponse(
                f'{OTREE_SERVER}/room/{ROOM_NAME}?participant_label={label}'
            )
        wrong_label = True
    return templates.TemplateResponse(
        'RoomInputLabel.html',
        dict(request=request, wrong_label=wrong_label, labels=labels),
    )




app = Starlette(debug=True, routes=[Route('/', homepage)])
