from mail_viewer.classes import mailing
from modules.vars import CONFIG, API_URL, CRITERIA

#Initialize the client
client = mailing.EmailProcessor(**CONFIG)

#Run the client
client.run(api_url= API_URL, criteria= CRITERIA)