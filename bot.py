# listen for messages on a discord server (globally, all channels)
# send to specified phone number if the message wasn't sent from the bot
import discord
import asyncio
from twilio.rest import TwilioRestClient

# discord.py has logging available: see docs. you probs won't need.

twilioNumber = "15615364592"
phoneNumber  = "+15616292348,"+15612642517 # to send messages to (ie, your user)

botName      = 'sms-and-phone-call-connection' # IMPORTANT! must be real bot username
#       otherwise you'll get infinite loops of the bot responding to itself

twilioAccountSid = "AC0d5cd1c7f8727429686327028ebb4af3"
twilioAuthToken  = "f82df9c1c6d4079b1bc54dd1baaa161c"

discordBotToken  = "NDE4MTUzNjQ5MDk3OTMyODAx.D0EVAQ.Y-IVLAUWfaN1fvqprrW3Vtz56kQ"

###############################################################################
# auth client objects
twilioClient = TwilioRestClient(twilioAccountSid, twilioAuthToken)
discordClient = discord.Client()

@discordClient.event
async def on_ready():
    print('Logged in as ' + discordClient.user.name + " " + discordClient.user.id)
    print('------')

@discordClient.event
async def on_message(message):

    if message.author.name != botName:
        twilioClient.messages.create(
            to    = phoneNumber,
            from_ = twilioNumber,
            body  = "{} - {}".format(message.author.name,message.content),
        )
        print("sent message: {} - {}".format(message.author.name,message.content))

discordClient.run(discordBotToken)
