import logging
from app.commands import Command


class thankyouCommand(Command):
    def execute(self):
        logging.info("Hello, World!")
        print("Thank you for running the commands!")