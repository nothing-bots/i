
from pyrogram.types import Chat

from DaisyXMusic.function.admins import get as gett
from DaisyXMusic.function.admins import set

# In modules/play.py
async def jiosaavn(client, message):
    # Ensure you are using the correct variable for the chat
    administrators = await get_administrators(message.chat)
    # Rest of your function logic

async def get_administrators(chat: Chat) -> List[6848223695]:
    get = gett(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)
