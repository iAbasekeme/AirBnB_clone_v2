#!/usr/bin/python3
"""
Fabric file
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    method that generate a .tgz archive
    """
    try:
        if not os.path.exists(versions):
            local("mkdir versions")
        
        date =  datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f" versions/web_static_{date}.tgz"

        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None
