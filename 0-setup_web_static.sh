#!/usr/bin/env bash
# A script that deploys to a web server

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
# Remove existing symbolic link (if it exists)
sudo rm -f /data/web_static/current
# Create a new symbolic link to the latest release directory
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
# Give ownership to the ubuntu user and group recursively
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '8i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
