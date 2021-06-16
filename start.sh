pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
pip3 install --upgrade pip
pip3 install statcord.py
pip3 install discord-py-slash-command
pip3 install -r requirements.txt
python3 bot.py