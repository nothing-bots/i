# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from typing import List, Union

from pyrogram import filters

from DaisyXMusic.config import COMMAND_PREFIXES

from pyrogram import Client, filters

other_filters = (
    @Client.on_message(filters.group & ~filters.via_bot & ~filters.forwarded)
async def handle_message(client, message):
    if message.edit_date:  # Checks if the message has been edited
        # Your logic for edited messages
        pass  
) 


other_filters2 = ( 
@Client.on_message(filters.private & ~filters.via_bot & ~filters.forwarded)
async def handle_message(client, message):
    if message.edit_date:  # Checks if the message has been edited
        # Your logic for edited messages
        pass
) 

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
