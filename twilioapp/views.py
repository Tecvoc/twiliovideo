from django.shortcuts import render
from django.http import JsonResponse
import os
from twilio.access_token import AccessToken
import random


def fun1(request):
    return JsonResponse({"a": "fun1 called"})


def homepage(request):
    return render(request, "index.html")


def get_token(request):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    api_key = os.environ['TWILIO_API_KEY']
    api_secret = os.environ['TWILIO_API_SECRET']

    # Create an Access Token
    token = AccessToken(account_sid, api_key, api_secret)

    # Set the Identity of this token
    random_names = ["Christian Blatter", "Tanaz Kesariwala", "Shanaya Kapoor", "Alisha Chauhan"]
    token.identity = random.choice(random_names)

    # Grant access to Conversations
    # grant = ConversationsGrant()
    # grant.configuration_profile_sid = os.environ['TWILIO_CONFIGURATION_SID']
    # token.add_grant(grant)

    # Return token info as JSON
    return jsonify(identity=token.identity, token=token.to_jwt())