from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import InputChannel



# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 123
api_hash = '123'
phone = '+37529***6387'

# client = TelegramClient('session_name', api_id, api_hash)
# client.connect()

# If you already have a previous 'session_name.session' file, skip this.
# client.sign_in(phone=phone)
# code = str(input("Confirmation code: "))
# me = client.sign_in(code=code)
# print(me.stringify())

client = TelegramClient('session_name', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.sign_in(phone=phone)
    code = str(input("Confirmation code: "))
    me = client.sign_in(code=code)
    # client.send_code_request('+15xxxxxxxxx')
    # client.sign_in('+15xxxxxxxxx', cod)

dialogs = []
users = []
chats = []

last_date = None
chunk_size = 5
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size
         ))
dialogs.extend(result.dialogs)
users.extend(result.users)
chats.extend(result.chats)

print(dialogs)



# InputChannel(dialogs[0].id, dialogs[0].access_hash)

participants = client.invoke(GetParticipantsRequest(
    InputChannel(chats[0].id, chats[0].access_hash), ChannelParticipantsSearch(''), 0, 300, 1
))

# print(participants.users[0].stringify())

with open("names2.txt", "w") as output:
    for user in participants.users:
        output.write(user.first_name)
        output.write("\n")


with open("dialogs.txt", "w") as output:
    output.write(str(dialogs))

with open("users.txt", "w") as output:
    output.write(str(users))

with open("chats.txt", "w") as output:
    output.write(str(chats))

