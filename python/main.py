import os
import sys

from mimi import Mimi

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('Usage: python {} text filename'.format(args[0]))
        sys.exit(1)

    auth = {
        'applicationId' : 'applicationId',
        'clientId' : 'clientId',
        'clientSecret' : 'clientSecret',
        'scope' : [
            'https://apis.mimi.fd.ai/auth/asr/http-api-service',
            'https://apis.mimi.fd.ai/auth/asr/websocket-api-service',
            'https://apis.mimi.fd.ai/auth/nict-asr/http-api-service',
            'https://apis.mimi.fd.ai/auth/nict-asr/websocket-api-service',
            'https://apis.mimi.fd.ai/auth/nict-tts/http-api-service',
            'https://apis.mimi.fd.ai/auth/nict-tra/http-api-service',
        ],
    }

    m = Mimi(auth)

    params = {
        'text' : args[1], # UTF-8
        'audio_format' : 'WAV', # WAV, RAW, ADPCM, Speex
        'audio_endian' : 'Little', # Little, Big
        'gender' : 'female', # female, male
        'age' : '14',
        'native' : 'yes', # yes, no
        'lang' : 'ja', # ja, en, id, ko, vi, my, th, zh, zh-TW
        'engine' : 'nict',
    }

    err, result = m.speech(params, args[2])
    if err:
        print(result)
        sys.exit(1)

    print('OK')
