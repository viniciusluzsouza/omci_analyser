#!/usr/bin/python3 -u

import os
from capturator import Capturator
from analyser import Analyser
from verifier import Verifier

import argparse

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
   4) Analyse
   5) Show Entity (ME)
   6) ME Verifier

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

   9) Run all and generate report

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
        self.locationOrigin = ""

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

    def getPath(self, output):
        if self.locationOrigin.startswith('/'):
            return output
        else:
            return self.locationOrigin + '/' + output

    def loadCapture(self):
        while True:
            file = input("Inform the file with location: ")
            if file != "":
                break

        buf = Capturator.loadDump(self.getPath(file))
        if len(buf):
            self.loaded_buffer = buf
            self.last_loaded = MainMenu.LOADED_FROM_FILE
            print("Capture successfully loaded!")

    def saveCapture(self):
        if self.capturator and self.capturator.hasCapture():
            file = input("File to export: ")
            self.capturator.saveDump(self.getPath(file))
            print("\nCapture successfully saved.\n")
        else:
            print("Nothing to save!\n")

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

    def showEntity(self):
        buf = self.checkLastCapture()
        if buf:
            self.analyser.setBuffer(buf)
            self.analyser.translateToMyself()

            if self.analyser.hasEntities():
                while True:
                    entity = input("Inform the entity identifier. E.g: 45-0 (0 to exit): ")
                    if entity == '0':
                        break

                    self.analyser.showEntity(entity)

    def analyse(self):
        try:
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

                    self.analyser.generateImage(self.getPath(pngfile))
                    print("\nImage successfully generated.\n")

        except Exception as e:
            print(str(e))

    def verifierMenu(self):
        buf = self.checkLastCapture()
        if buf:
            self.verifier.setPacketBuffer(buf)
        else:
            return

        while True:
            print(self.VERIFIER)

            try:
                opt = input(self.CHOOSE)
                opt = self.convertOptWithPrint(opt)
                if opt is None:
                    continue

                if opt == 1:
                    self.verifier.verifyMandatoryAttributes()

                elif opt == 2:
                    self.verifier.verifyEntitiesLength()

                elif opt == 3:
                    self.verifier.verifySetWithoutPermission()

                elif opt == 9:
                    self.verifier.runAllAndGenerateReport(location=self.locationOrigin)

                elif opt == 0:
                    break
                else:
                    print(self.INVALID_OPT)

            except Exception as e:
                print(str(e))

    def setLocationOrigin(self, orig):
        self.locationOrigin = orig

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
                    self.analyse()
                elif opt == 5:
                    self.showEntity()
                elif opt == 6:
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


def runCapture(interface, output, orig):
    if os.getuid() != 0:
        print("You need root permissions to execute the capturator. Run with sudo!")
        return

    cap = Capturator()
    try:
        cap.setInterface(interface)
        print("\nStarting capture. Press CTRL + C to stop.\n")
        print("#############################################\n")
        cap.createSock()
        cap.start()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(str(e))
        return
    finally:
        cap.closeSock()

    if cap.hasCapture():
        if orig.startswith('/'):
            cap.saveDump(output)
        else:
            cap.saveDump(orig + '/' + output)
        print("\nSaved sucessfully!\n")
    else:
        print("\nNothing to save!")


def runAnalyse(file_from, output, orig):
    buf = Capturator.loadDump(file_from)
    if not len(buf):
        return

    anal = Analyser()
    try:
        anal.setBuffer(buf)
        anal.analyse()
        if orig.startswith('/'):
            anal.generateImage(output)
        else:
            anal.generateImage(orig + '/' + output)
    except Exception as e:
        print(str(e))


def runVerify(file_from, output, orig):
    buf = Capturator.loadDump(file_from)
    if not len(buf):
        return

    ver = Verifier()
    try:
        ver.setPacketBuffer(buf)
        if orig.startswith('/'):
            ver.runAllAndGenerateReport(reportfile=output)
        else:
            ver.runAllAndGenerateReport(reportfile=orig + '/' + output)
    except Exception as e:
        print(str(e))


def checkOutputFile(rec_args):
    if not rec_args.o:
        print("Inform the output file. Option '-o'.")
        return False

    return True


if __name__ == '__main__':
    run_orig = os.getcwd()
    argParser = argparse.ArgumentParser(description='GPON OMCI Analyser')
    argParser._optionals.title = "Mandatory Params"

    argGroup = argParser.add_mutually_exclusive_group()
    argGroup.add_argument("-c", action="store_true", help="Run in continuous mode")
    argGroup.add_argument("-i", type=str, help="Interface to capture", metavar='INTERFACE')
    argGroup.add_argument("-a", type=str, help="Analyse and generate image from capture", metavar='PCAP_FILE')
    argGroup.add_argument("-v", type=str, help="Verify packets", metavar='PCAP_FILE')

    argParser.add_argument("-o", type=str, help="Output file", metavar='FILENAME')
    # argParser.add_argument("-s", "--show-output", help="Show image text file (only for analyser)")

    args = argParser.parse_args()

    if args.c:
        if os.getuid() != 0:
            print("You need root permissions to execute. Run with sudo!")
            exit(0)

        mainMenu = MainMenu()
        mainMenu.setLocationOrigin(run_orig)
        mainMenu.start()
    else:
        if args.i:
            if checkOutputFile(args):
                runCapture(args.i, args.o, run_orig)
        elif args.a:
            if checkOutputFile(args):
                runAnalyse(args.a, args.o, run_orig)
        elif args.v:
            if checkOutputFile(args):
                runVerify(args.v, args.o, run_orig)
        else:
            argParser.print_help()
