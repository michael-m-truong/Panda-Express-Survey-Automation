import os

os.system("apt purge google-chrome-stable && apt purge chromium-browser && apt install -y chromium-browser && pip install -r requirements.txt")