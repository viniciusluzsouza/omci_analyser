import os
from capturator import Capturator
from analyser import Analyser
from verifier import Verifier

class MainMenu:
    CHOOSE = "Option: "

    MAIN = """
#########################################
############### Main Menu ###############
#########################################

Choose an option and press ENTER:
   1) Start Capture
   2) Load Capture
   3) Save Capture
   4) OMCI Analyser
   5) ME Verifier

   0) Exit
"""

    CAPTURATOR = """
########### Capturator ###########

Choose an option and press ENTER:
   1) Start a capture
   2) Save capture

   0) Back
"""

    ANALYSER = """
########### Analyser ###########

Choose an option and press ENTER:
   1) Analyse
   2) Show Entity

   0) Back
"""

    VERIFIER = """
########### Verifier ###########

Choose an option and press ENTER:
   1) Check mandatory attributes
   2) Check ME lengths
   3) Check configured attributes without permission
   
   0) Back
"""

    NOT_IMPLEMENTED = "\n/!\\ Not implemented! /!\\\n"

    INVALID_OPT = "Invalid option\n"

    NOTHING_LOADED = 0
    LOADED_FROM_CAPTURE = 1
    LOADED_FROM_FILE = 2

    def __init__(self):
        self.capturator = Capturator()
        self.analyser = Analyser()
        self.verifier = Verifier()
        self.loaded_buffer = []
        self.last_loaded = MainMenu.NOTHING_LOADED

    def convertOptWithPrint(self, opt):
        try:
            return int(opt)
        except Exception:
            print(self.INVALID_OPT)
            self.printTitle = False
            return None

    def closeCapturator(self):
        if self.capturator:
            self.capturator.close()

    def askConfirm(self, question):
        while True:
            opt = input(question + " [Y/n]: ").lower()
            if opt == 'y' or opt == 'yes' or opt == '':
                return True
            elif opt == 'n' or opt == 'no':
                return False
            else:
                print("Reply with [y]es or [n]o")

    def startCapture(self):
        try:
            if self.capturator.hasCapture():
                if self.askConfirm("If the last capture was not save, it will be lost. Are you sure?"):
                    self.closeCapturator()
                else:
                    return

            interface = input("Interface to capture: ")
            self.capturator.setInterface(interface)

            print("\nStarting capture. Press CTRL + C to stop.\n")
            print("#############################################\n")
            self.capturator.createSock()
            self.capturator.start()

        except NameError as e:
            print(str(e))

        except KeyboardInterrupt:
            self.capturator.closeSock()
            self.last_loaded = MainMenu.LOADED_FROM_CAPTURE
            print("\nCapture stoppped!\n")

        except Exception as e:
            print(str(e))

    def loadCapture(self):
        while True:
            file = input("Inform the file with location: ")
            if file != "":
                break

        buf = Capturator.loadDump(file)
        if len(buf):
            self.loaded_buffer = buf
            self.last_loaded = MainMenu.LOADED_FROM_FILE
            print("Capture successfully loaded!")

    def saveCapture(self):
        if self.capturator and self.capturator.hasCapture():
            file = input("File to export: ")
            self.capturator.saveDump(file)
            print("Saved sucessfully! See folder output.\n")
        else:
            print("Nothing to save!")

    def checkLastCapture(self):
        buf = None
        if self.last_loaded == MainMenu.LOADED_FROM_CAPTURE:
            if self.capturator.hasCapture():
                buf = self.capturator.getBuffer()
        elif self.last_loaded == MainMenu.LOADED_FROM_FILE:
            if len(self.loaded_buffer):
                buf = self.loaded_buffer

        if buf is None:
            print("There is no capture to analyse. Start a capture or load one!")

        return buf

    def analyserMenu(self):
        if not self.analyser:
            self.analyser = Analyser()

        while True:
            print(self.ANALYSER)

            try:
                opt = input(self.CHOOSE)

                opt = self.convertOptWithPrint(opt)
                if opt is None:
                    continue

                if opt == 1:
                    buf = self.checkLastCapture()
                    if buf:
                        self.analyser.setBuffer(buf)
                        self.analyser.analyse()
                        if self.askConfirm("Show the output?"):
                            print("\n%s" % self.analyser.getOutput())

                        if self.askConfirm("Generate .png?"):
                            while True:
                                pngfile = input("File name: ")
                                if pngfile != "":
                                    break
                            self.analyser.generateImage(pngfile)
                            print("Generated on folder output.")

                elif opt == 2:
                    buf = self.checkLastCapture()
                    if buf:
                        self.analyser.setBuffer(buf)
                        self.analyser.translateToMyself()

                        if self.analyser.hasEntities():
                            while True:
                                entity = input("Inform the entity identifier. E.g: [45-0] (0 to exit): ")
                                if entity == '0':
                                    break

                                self.analyser.showEntity(entity)

                elif opt == 0:
                    break

                else:
                    print(self.INVALID_OPT)
                    self.printTitle = False

                self.printTitle = False

            except Exception as e:
                print(str(e))
                self.printTitle = False

    def verifierMenu(self):
        while True:
            print(self.VERIFIER)

            try:
                opt = input(self.CHOOSE)
                opt = self.convertOptWithPrint(opt)
                if opt is None:
                    continue

                buf = self.checkLastCapture()
                if buf:
                    self.verifier.setPacketBuffer(buf)
                else:
                    break

                if opt == 1:
                    self.verifier.verifyMandatoryAttributes()

                elif opt == 2:
                    self.verifier.verifyEntitiesLength()

                elif opt == 3:
                    self.verifier.verifySetWithoutPermission()

                elif opt == 0:
                    break
                else:
                    print(self.INVALID_OPT)

            except Exception as e:
                print(str(e))

    def start(self):
        self.printTitle = True

        while True:
            if self.printTitle:
                print(self.MAIN)

            try:
                opt = input(self.CHOOSE)

                opt = self.convertOptWithPrint(opt)
                if opt is None:
                    continue

                if opt == 1:
                    self.startCapture()
                elif opt == 2:
                    self.loadCapture()
                elif opt == 3:
                    self.saveCapture()
                elif opt == 4:
                    self.analyserMenu()
                elif opt == 5:
                    self.verifierMenu()
                elif opt == 0:
                    break
                else:
                    print(self.INVALID_OPT)
                    self.printTitle = False
                    continue

                self.printTitle = True

            except Exception as e:
                self.printTitle = True
                raise e


if __name__ == '__main__':
    if os.getuid() != 0:
        print("You need root permissions to execute. Run with sudo!")
        exit(0)

    mainMenu = MainMenu()
    mainMenu.start()