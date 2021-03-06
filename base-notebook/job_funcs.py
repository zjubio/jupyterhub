# -*- coding: UTF-8 -*-
import os
import sys
import requests

PY_SERVER = os.environ.get('PY_SERVER')

func_name = sys.argv[1]
job_id = sys.argv[2]
try:
    if_success = sys.argv[3]
except IndexError:
    pass


def finish_job():
    requests.put('{PY_SERVER}/jobs/{job_id}/finish/{if_success}'.format(
        PY_SERVER=PY_SERVER, job_id=job_id, if_success=if_success))


def insert_module():
    requests.put('{PY_SERVER}/jobs/{job_id}/insert_modules'.format(
        PY_SERVER=PY_SERVER, job_id=job_id))


locals().get(func_name)()
