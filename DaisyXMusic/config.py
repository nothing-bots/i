# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
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
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAf70YAROjHzefCBhHgoe6ya0wnRS6Ztkm0-yGkdis-AXTr3kNmZYuXG2s2Bw9i6lnyOj5FVJpHWp8T8b6jbMuITI_wnn9WjY1F0hwOtPO8dLqlYffyrt89WsHK0Kdo86ZiCr-Bhr_HCE-uezdw5dUpGF48hOa5McjmVRqNNn7PmK3Ehi9EfZpmR_Hp-xK3Zlb2bpGQIVe-nyhVOcvF-xwWHpTf75z2KIdizRdZ4D02OZdafMS_xWrS2DaLj-pjATBue-ecXF2bKAxNhHuPrCT3X3QE4axtu7SuxhAV-VouP7bJYi_dgtzG26KBQVN569nBvpGHnAvH2vFUSqiDm_20hs8t1QAAAAHV9wluAA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "about_tosuu")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "24620300"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AlinaXhelper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AlinaXUpdates")
PROJECT_NAME = getenv("PROJECT_NAME", "AlinaXMusic v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamAlinaX/AlinaXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1002291785414")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
