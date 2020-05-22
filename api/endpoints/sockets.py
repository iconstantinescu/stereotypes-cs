"""
Class that deals with socket communication for the queue management
"""
import os
import redis
import json
from flask_jwt_extended import jwt_required
from .. import socketio

if os.environ["APP_SETTINGS"] == "config.StagingConfig":
    red = redis.from_url(os.environ["REDIS_URL"])
elif os.environ["APP_SETTINGS"] == "config.CITestingConfig":
    red = redis.Redis(host="redis")
else:
    red = redis.Redis()


@socketio.on('connect')
@jwt_required
def connect():
    print("Authenticated", flush=True)


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    return {"message": "here's a message"}


@socketio.on('free')
def check_queue(message):
    obj = red.lpop("queue")
    if obj:
        decoded_string = obj.decode("utf-8").replace("\'", "\"")
        ret = json.loads(decoded_string)
        return ret
