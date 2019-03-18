import socket
import logging
import re
BOT_USERNAME = ''
CHANNEL_NAME = ''
OAUTH_TOKEN = ''

s=socket.socket()
connect_host = 'irc.twitch.tv'
connect_port = 6667
s.connect((connect_host,connect_port))
s.send(("PASS {}\r\n").format(OAUTH_TOKEN).encode('utf-8'))
s.send(("NICK {}\r\n").format(BOT_USERNAME).encode('utf-8'))
s.send(('JOIN #{}\r\n').format(CHANNEL_NAME).encode('utf-8'))
if os.path.isdir(os.getcwd()+'\\'+CHANNEL_NAME)==False:
    os.mkdir(CHANNEL_NAME)
    os.chdir(os.getcwd()+'\\'+CHANNEL_NAME)
else:
    os.chdir(os.getcwd()+'\\'+CHANNEL_NAME)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -- %(message)s',datefmt='%Y-%m-%d_%H:%M:%S',handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

while True:
    response = s.recv(2048).decode('utf-8')
    if response.startswith('PING'):
        s.send('Pong\n'.encode('utf-8'))
    elif len(response) > 0:
        username = re.search("\w+", response).group(0)
        content = re.compile("^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
        message = content.sub("", response).rstrip('\n')
        logging.info(message)
