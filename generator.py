#!/usr/bin/python

import sys, getopt

def main(argv):
    print("Program started!\nFor help, check -h or --help option\n")

    #initialize default
    size = 100
    name = "/ndn/telu/fif/%C1.Router/router2/"
    prefix = "/ndn/telu/fif/lab/ndn"
    mode = True
    freshness = 1
    csize = 1000

    #initialize argument
    try:
        opts, args = getopt.getopt(argv,"hs:n:p:m:f:c:",["help","size=","name=","prefix=","mode=","freshness=","contentsize="])
    except getopt.GetoptError:
        print 'use -h or --help for help'
        sys.exit(2)

    #checking argument
    for opt, arg in opts :
        if opt in ("-h", "--help") :
            print "Generator for \"ndn-traffic-generator\" configuration file!\nOptions :\n\t-h [ --help ] arg \t\tPrint this help message and hope it helps :)\n\t-s [ --size ] arg \t\tSet number of prefix, default = 100\n\t-n [ --name ] arg \t\tSet name for every TrafficPattern, format = (name)/traffic(iteration_number)\n\t\t\t\t\tExample : \n\t\t\t\t\tif input name = /ndn/telu/fte/%C1.Router/router2 \n\t\t\t\t\tthen name for TrafficPattern 1 is /ndn/telu/fte/%%C1.Router/router2/prefix1 and so on\n\t-p [ --prefix ] arg \t\tSet prefix name, format = (prefix)(iteration_number)\n\t\t\t\t\tExample : \n\t\t\t\t\tif input prefix = /ndn/telu/fif/lab then prefix for Pattern Traffic 1 is /ndn/telu/fif/lab1 and so on\n\t-m [ --mode ] arg \t\tInput 1 for MustBeFresh true and 0 for MustBeFresh false, default=1\n\t-f [ --freshness ] arg \t\tSet FreshnessPeriod in ms, default = 1\n\t-c [ --contentsize ] arg \t\tSet ContentSize in Bytes, default = 1000"
            sys.exit()
        elif opt in ("-s", "--size") :
            size = int(arg)
        elif opt in ("-n", "--name") :
            name = arg
        elif opt in ("-p", "--prefix") :
            prefix = arg
        elif opt in ("-m", "--mode") :
            if(int(arg) == 1) :
                mode = True
            elif(int(arg) == 0) :
                mode = False
            else :
                print("Wrong option!")
                sys.exit(2)
        elif opt in ("-f", "--freshness") :
            freshness = arg
        elif opt in ("-c", "--contentsize") :
            csize = arg

    #generate client.conf
    file = open("client.conf","wb")
    string=""
    for i in range(1,size+1) :
        string = string + "\n\nTrafficPercentage=1\nName="+name+"/traffic"+str(i)+"\nExpectedContent="+prefix+str(i)+"\nMustBeFresh="+str(mode)
    file.write(string.encode())
    file.close

    print("client.conf generated!")

    #generate server.conf
    file = open("server.conf","wb")
    string = ""
    for i in range(1,size+1) :
        string = string + "\n\nName="+name+"/traffic"+str(i)+"\nContent="+prefix+str(i)+"\nFreshnessPeriod="+str(freshness)+"\nContentBytes="+str(csize)
    file.write(string.encode())
    file.close

    print("server.conf generated!")

    #generate initial.sh
    file = open("initial.sh","wb")
    string = ""
    for i in range(1,size+1) :
        string = string + "\nnlsrc advertise "+prefix+str(i)
    file.write(string.encode())
    file.close

    print("initial.sh generated!")

    print("Finish!")

#start main
if __name__ == "__main__":
   main(sys.argv[1:])