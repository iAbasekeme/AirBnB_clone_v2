#!/usr/bin/env bash
# Nginx configuration

# update the system and install nginx if not installed
if command -v nginx &> /dev/null; then
    echo "Nginx is installed."
else
    echo "Nginx is not installed."
    echo "Installing process..."
    sudo apt-get -y update
    sudo apt-get  install -y nginx
fi


# create folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# change the owner of /data/
sudo chown -R ubuntu:ubuntu /data/

# Updating the Nginx config

# recreate the symbolic link between /etc/nginx/sites-enable
# and /etc/nginx/sites-avaible/default because there is no link sometime
if [ ! -L /etc/nginx/sites-enabled/default ]; then
	sudo rm /etc/nginx/sites-enabled/default
	sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
fi
new_location="location /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i " 55i $new_location" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
