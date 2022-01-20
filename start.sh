if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/jerinjohny17/Ragnar.git /index
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /index
fi
cd /index
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
