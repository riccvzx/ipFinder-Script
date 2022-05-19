#import components

from genericpath import exists
import os.path
import sys
import re
import getopt

#main function 
def main(argv):
    
    #def of variables 
    contents = ''
    contentsx = ''

    regexPB = ["\\b[1-9]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}",
                "\\b[1][1-9]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b[2-9][0-9]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b[1][0-2][0-6]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}",
                "(?:\\b[1][2][9]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b[1][3-6][0-9]\\.(?:[0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-3])\\.[0-9]{1,3}\\.[0-9]{1,3})",
                "(?:\\b[1][6][9]\\.[2][5][5]\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b[1][7][0-1]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b[1][7][2]\\.(?:[0-9]|[1][0-5])\\.[0-9]{1,3}\\.[0-9]{1,3})",
                "(?:\\b[1][7][2]\\.(?:[3][2-9]|[4-9][0-9]|[1-2][0-9][0-9])\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b(?:[1][7][3-9]|[1][8][0-9]|[1][9][0-1])\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|\\b[1][9][2]\\.(?:[0-9][0-9]|[1][0-5][0-9]|[1][6][0-7])\\.[0-9]{1,3}\\.[0-9]{1,3})",
                "(?:\\b[1][9][2]\\.(?:[1][6][9]|[1][7-9][0-9]|[2][0-5][0-5])\\.[0-9]{1,3}\\.[0-9]{1,3}|(?:[1][9][3-9]|[2][0-1][0-9]|[2][2][0-3])\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})"]

    regexPR = ["\\b[1][0]\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}",
                    "(?:\\b[1][7][2]\\.(?:[1][6-9]|[2][0-9]|[3][0-1])\\.[0-9]{1,3}\\.[0-9]{1,3})",
                    "\\b[1][9][2]\\.[1][6][8]\\.[0-9]{1,3}\\.[0-9]{1,3}"]

    regexA = ["\\b[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}"]

    help = '\n digit ipFinder.py -h or --help for help purpose'

    #main part of the script 
    try: 
            #definitions of the argument to be passed
            opts, args = getopt.getopt(argv, "hi:o:pra",["help","ifile=", "ofile=", "public", "private", "all"])

    #error if the argument is invalid
    except getopt.GetoptError:
            print(help)
            sys.exit()
        
    for opt, arg in opts:

            #help case
            if opt in ("-h", "--help"):
                with open("readme.txt") as r:
                    readme= r.read()
                print(readme)
                sys.exit()

            #input of the file to be passed
            elif opt in ("-i", "--ifile"):
                if (os.path.exists(arg)):
                    with open(arg) as f:
                        contents = f.read()

            #arg to parse only public ip
            elif opt in ("-p", "--public"):
                c = 0
                for i in regexPB:
                    a = regexPB[c]
                    contentsx = contentsx + str(' '.join(re.findall(a, contents))) + '\n' 
                    c = c+1
                contentsx = re.sub(' ', '\n', contentsx)

            #arg to parse only private ip
            elif opt in ("-r", "--private"):
                c = 0
                for i in regexPR:
                    a = regexPR[c]
                    contentsx = contentsx + str(' '.join(re.findall(a, contents))) + '\n' 
                    c = c+1
                contentsx = re.sub(' ', '\n', contentsx)

            #arg to parse all the ip
            elif opt in ("-a", "--all"):
                c = 0
                for i in regexA:
                    a = regexA[c]
                    contentsx = contentsx + str(' '.join(re.findall(a, contents))) + '\n' 
                    c = c+1
                contentsx = re.sub(' ', '\n', contentsx)

            #output of the file to be created
            elif opt in ("-o", "--ofile"):
                print ("\n A file called %s with the choosen ip, will be generated inside the choosen folder. \n Stay healthy ;)" %arg) 
                #creation of the file
                with open(arg, 'w') as fi:
                    fi.write(contentsx) 
            else: 
                print(help)
                
#start of the script
if __name__ == "__main__":
    main(sys.argv[1:])