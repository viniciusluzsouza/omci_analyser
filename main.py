import os
from capturator import Capturator

class MainMenu:
    CHOOSE = "Option: "

    MAIN = """
#########################################
############### Main Menu ###############
#########################################

Choose an option and press ENTER:
   1) Capturator
   2) OMCI Analyser
   3) ME Verifier

   0) Exit
"""

    CAPTURATOR = """
########### Capturator ###########

Choose an option and press ENTER:
   1) Start a capture
   2) Save capture

   0) Back
"""

    NOT_IMPLEMENTED = "\n/!\\ Not implemented! /!\\\n"

    INVALID_OPT = "Invalid option\n"

    def __init__(self):
        pass

    def convertOptWithPrint(self, opt):
        try:
            return int(opt)
        except Exception:
            print(self.INVALID_OPT)
            self.printTitle = False
            return None

    def closeCapturator(self):
        if self.capturator:
            self.capturator.clearDump()
            self.capturator.closeSock()

    def askConfirm(self, question):
        while True:
            opt = input(question + " [Y/n]: ").lower()
            if opt == 'y' or opt == 'yes':
                return True
            elif opt == 'n' or opt == 'no':
                return False
            else:
                print("Reply with [y]es or [n]o")

    def capturatorMenu(self):
        self.capturator = None
        self.printTitle = True

        while True:
            if self.printTitle:
                print(self.CAPTURATOR)

            try:
                opt = input(self.CHOOSE)

                opt = self.convertOptWithPrint(opt)
                if opt is None:
                    continue

                if opt == 1:
                    if self.capturator:
                        if self.askConfirm("The last capture will be lost. Are you sure?"):
                            self.closeCapturator()
                        else:
                            self.printTitle = True
                            continue

                    interface = input("Interface to capture: ")
                    self.capturator = Capturator(interface)
                    print("\nStarting capture. Press CTRL + C to stop.\n")
                    print("#############################################\n")
                    self.capturator.createSock()
                    self.capturator.start()

                elif opt == 2:
                    if self.capturator:
                        file = input("File to export: ")
                        self.capturator.saveDump(file)
                        self.closeCapturator()
                        self.printTitle = True
                        print("Saved sucessfully! See folder output.\n")
                    else:
                        print("Capturator not initialized!")

                elif opt == 0:
                    self.closeCapturator()
                    break

                else:
                    print(self.INVALID_OPT)
                    self.printTitle = False

                self.printTitle = False

            except NameError as e:
                self.printTitle = True
                print(str(e))

            except KeyboardInterrupt:
                self.printTitle = True
                print("\nCapture stoppped")

            except Exception as e:
                print(str(e))
                self.printTitle = False

    def analyserMenu(self):
        print(self.NOT_IMPLEMENTED)
        return

    def verifierMenu(self):
        print(self.NOT_IMPLEMENTED)
        return

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
                    self.capturatorMenu()
                elif opt == 2:
                    self.analyserMenu()
                elif opt == 3:
                    self.verifierMenu()
                elif opt == 0:
                    break
                else:
                    print(self.INVALID_OPT)
                    self.printTitle = False
                    continue

                self.printTitle = True

            except Exception:
                self.printTitle = True


if __name__ == '__main__':
    if os.getuid() != 0:
        print("You need root permissions to execute. Run with sudo!")
        exit(0)

    mainMenu = MainMenu()
    mainMenu.start()