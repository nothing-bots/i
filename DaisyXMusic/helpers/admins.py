
from pyrogram.types import Chat

from DaisyXMusic.function.admins import get as gett
from DaisyXMusic.function.admins import set

# In modules/play.py
async def jiosaavn(client, message):
    # Ensure you are using the correct variable for the chat
    administrators = await get_administrators(message.chat)
    # Rest of your function logic
