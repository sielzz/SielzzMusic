# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

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

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**Halo anak yatim 👋 [{}](tg://user?id={})!**\n\n🤖 Saya adalah bot canggih yang dibuat untuk memutar musik di obrolan suara Grup & Saluran Telegram.\n\n✅ kirim saya /help untuk info lainnya."
    HELP_MSG = [
        ".",
        f"""
**Anjay lu lagi, welcome back di {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",
        f"""
**Setting up**

1) Jadiin gua CEO di gc lu
2) Buka obrolan suara / VCG lu
3) Typing `/userbotjoin` dan coba /play <nama lagu>
*) Kalo Assistant Bot ga join Silahkan Tambahkan @{ASSISTANT_NAME} ke gc lu dan cobain lagi

**For Channel Music Play**
1) Jadiin gua CEO di channel lu
2) ketik /userbotjoinchannel di channel lu
3) abis tu kirim commands di link grup lu
""",
        f"""
**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Untuk buka pengaturan ueer
- /skip: Buat skip umur emak lu
- /pause: Buat pause umur bapa lu
- /resume: Buat lanjutin umur bapa lu yang di pause
- /end: Buat matiin bapa lu
- /mute: Buat bisu in mulut bapa lu
- /unmute: Buat biar bapa lu bisa ngomong
- /current: Buat liat lagu yang lagi lu kocok
- /playlist: Buat liat daftar lagi yang lagi lu kocok

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /cmute - mute song play
- /mute - mute song play
- /unmute - mute song play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",
        f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
        f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",
        f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

""",
    ]
