#!/usr/bin/env bash
# A script that deploys to a web server

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Remove existing symbolic link (if it exists)
sudo rm -f /data/web_static/current
# Create a new symbolic link to the latest release directory
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
# Give ownership to the ubuntu user and group recursively
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '/add_header X-Served-By $hostname;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# sudo sed -i '8i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' 
sudo service nginx restart
