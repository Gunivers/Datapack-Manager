
from tkinter import filedialog
from tkinter import *
from LRFutils import logs
import time
import os
from typen import enforce_type_hints
from pick import pick
root = Tk()
root.withdraw()


class World:
    
    def __init__(self, path:str = None):
        
        # Getting the world's root directory
        if not World.isValidPath(path):
            path = World.uiSelect()
        
        self.path = path
        self.name = os.path.split(path)[1]
        self.datapacks = []

        # Getting datapack list
        for i in os.listdir(os.path.join(path, "datapacks")):
            self.datapacks.append(i)

        # Printing information about the world
        logs.info(f"World found: {self.name}")
        logs.info(f"Datapacks: {self.name}")
        for datapack in self.datapacks:
            logs.info(f" - {datapack}")

        # If there is no the Glibs project, it will ask to install it
        if not any(x.startswith("Glib") for x in self.datapacks):
            title = "Glibs is not installed in this world. Press enter to install it?"
            options = ["Yes", "No"]
            option, index = pick(options, title)



    # ________________________________________________________________________________
    # Select a valid map path

    @staticmethod
    def uiSelect() -> str:
        
        while True:
            path = filedialog.askdirectory(mustexist=True)

            # Detecting presence of level.dat file
            if World.isValidPath(path):
                return path
            else:
                logs.warn("You must select a valid world folder.")
                time.sleep(1)



    # ________________________________________________________________________________
    # Verify is the given map path is valid by checking the existance of the level.dat file

    @staticmethod
    @enforce_type_hints
    def isValidPath(path:str) -> bool:
        if os.path.isfile(os.path.join(path, "level.dat")):
            return True
        else:
            return False



if __name__ == "__main__":
    world = World()
