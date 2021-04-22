# Users with admin privileges are abe to customize
# the attributes of the group and kick players if needed.
import os

import group

def main():
    os.system('python group.py')

#TODO: GUI menu to enable this
def admin_menu(action, argument):
    #kick player
    switcher = {
        1: group.kick_player(argument),
        2: group.set_max_connections(argument),
        3: group.set_status(argument)
    }