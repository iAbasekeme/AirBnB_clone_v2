#!/usr/bin/env bash
# A script that deploys to a web server

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

cat <<EOF > /data/web_static/releases/test/index.html
"<html>
    <head>
        <title>Welcome to Test.com!</title>
    </head>
    <body>
        <h1>Success!  The test.com server block is working!</h1>
    </body>
</html>"
EOF

# Remove existing symbolic link (if it exists)
sudo rm -f /data/web_static/current

# Create a new symbolic link to the latest release directory
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start
