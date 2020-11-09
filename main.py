import os
from capturator import Capturator
from analyser import Analyser

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

    ANALYSER = """
########### Analyser ###########

Choose an option and press ENTER:
   1) Analyse
   2) Load Capture
   3) Show Entity

   0) Back
"""

    NOT_IMPLEMENTED = "\n/!\\ Not implemented! /!\\\n"

    INVALID_OPT = "Invalid option\n"

    def __init__(self):
        self.capturator = None
        self.analyser = None

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
            if opt == 'y' or opt == 'yes' or opt == '':
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
                    # self.closeCapturator()
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
                    if self.capturator and len(self.capturator.getBuffer()):
                        buf = self.capturator.getBuffer()
                    else:
                        buf = self.analyser.getBuffer()

                    if buf:
                        self.analyser.setBuffer(buf)
                        self.analyser.translateAll()
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

                    else:
                        print("There is no capture to analyse. Start a capture or load one!")

                elif opt == 2:
                    while True:
                        file = input("Inform the file with location: ")
                        if file != "":
                            break

                    if self.analyser.loadBuffer(file):
                        print("Capture successfully loaded!")

                elif opt == 3:
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

            except Exception as e:
                self.printTitle = True
                raise e


if __name__ == '__main__':
    if os.getuid() != 0:
        print("You need root permissions to execute. Run with sudo!")
        exit(0)

    mainMenu = MainMenu()
    mainMenu.start()