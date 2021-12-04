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
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOHsBuym4SBJWDy6qDY-TDrhOo2MQR-7uZjS7zdV8W2qrTLWPGfW6op8gXpo4wNiwWpbeg-BJLld71D4InIAZplybp5nMz7_ouNnLPwJnV7dq6R4LoNU0h--sQb1zOED7oYpF5jHt6FRJOv4kgWX8BVf8VUa4h31zNr8HW1xWvaxqaD6BKKqaUz4v7XPF1dT6yeLxXhF3rx2WUAkvuyPbIgDcqg7868isneBSrjtVJsEF8jHenXNMGjkti3qh9Gx2xWvtTRslGNue258bOyPehSJwTedCmoTPekUomiKryvGrtyMWigZ2u-UGAry4RLaRPp7gRFDa1iV4hW-oR50D13Vozjg=")
BOT_TOKEN = getenv("5012557501:AAE-oComu1tfLrQni77Am0holyjoa-skrWU")
BOT_NAME = getenv("baymaxmusicbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BaymaxMusicUpdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {2111823747}
API_ID = int(getenv("API_ID", "16722466"))
API_HASH = getenv("4c58e31ef6e2a8332cf578d5d72b9d0a")
BOT_USERNAME = getenv("@baymaxmusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BaymaxMusicHelper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BaymaxSupportGroup")
PROJECT_NAME = getenv("PROJECT_NAME", "BaymaxMusic v1")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "BaymaxSupportGroup")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
