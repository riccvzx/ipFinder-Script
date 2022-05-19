

ipFinder 1.0-ra 
Usage: ipFinder.py [Options] {File specification}

FILE SPECIFICATIONS:

    Can pass the input file and its own directory (the file that should be analized) 
    and the output file, in which the results will be written, with its own directory.

    File ex: test.txt, input/test.txt, result.txt, output/result.txt

    [Options]:

        -h --help: display the help page of the script

        -i --ifile <inputfilename>: set the input file that the script will analize

        -o --ofile <outputfilename>: set the output file that will be written by the script

        -p --public: set this flag to search for only the public ip in the given file

        -r --private: set this flag to search for only the private ip in the given file 

        -a --all: set this flag to search for all the ip present in the given file
