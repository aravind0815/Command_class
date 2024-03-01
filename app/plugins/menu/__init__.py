import sys
from app.commands import Command


class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        menu_list = self.command_handler.menu_list()
        print("The Menu option contains", list(menu_list))