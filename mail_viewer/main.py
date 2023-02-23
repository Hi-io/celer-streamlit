from mail_viewer.classes import mailing
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Initialize the EmailViewer')

# Define the command-line arguments
parser.add_argument('--username', default='default_username', help='The username to use for authentication')
parser.add_argument('--password', default='default_password', help='The password to use for authentication')
parser.add_argument('--server', default='default_server', help='The server to connect to')
parser.add_argument('--port', default='default_port', help='The port to use for the connection')
parser.add_argument('--folder', default='INBOX', help='The folder to use for the API call')
parser.add_argument('--api_url', default='jeje', help='The API URL to use')
parser.add_argument('--criteria', default='UNSEEN', help='Search Criteria')

# Parse the command-line arguments
args = parser.parse_args()

#Initialize the client
client = mailing.EmailProcessor(username= args.username, password= args.password, server= args.server, port= args.port, folder= args.folder)

#Run the client
client.run(api_url=args.api_url, criteria=args.criteria)