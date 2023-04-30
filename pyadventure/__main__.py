import logging
from pyadventure.game_logic.interface import PyAdventureInterface

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("__main__.py").info("Project has run")
    PyAdventureInterface()
