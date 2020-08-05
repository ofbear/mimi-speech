import inspect
import json
import os
import requests
import sys
import urllib

class Mimi():
    def __init__(self, auth):
        self.__auth = auth

    def __accesstoken(self):
        scope = ''
        for v in self.__auth['scope']:
            scope += v + ';'

        res = requests.post(
            url='https://auth.mimi.fd.ai/v2/token',
            data={
                'grant_type': 'https://auth.mimi.fd.ai/grant_type/client_credentials',
                'client_id': self.__auth['applicationId'] + ':' + self.__auth['clientId'],
                'client_secret': self.__auth['clientSecret'],
                'scope' : scope.rstrip(';'),
            }
        )

        if res.status_code != 200:
            return True, f'{sys._getframe().f_code.co_name}:status is bad:{str(res.status_code)}'

        json_data = res.json()

        if json_data['status'] != 'success':
            return True, f'{sys._getframe().f_code.co_name}:Authentication is failed'

        return False, json_data['accessToken']

    def speech(self, params, fname):
        err, access_token = self.__accesstoken()
        if err:
            return err, access_token

        res = requests.post(
            url='https://tts.mimi.fd.ai/speech_synthesis',
            headers={
                'Authorization':  f'Bearer {access_token}',
            },
            data=params
        )

        if res.status_code != 200:
            return True, f'{sys._getframe().f_code.co_name}:status is bad:{str(res.status_code)}'

        with open(fname, 'wb') as fout:
            fout.write(res.content)

        return False, res.status_code
