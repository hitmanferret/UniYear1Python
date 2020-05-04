##log = open('logfile.txt', 'r')
##string = log.read()
##print(string.upper())


log = open('logfile.txt','r')
string = log.read()
upper_string = string.upper()
log.close()

upper_log = open('upper_log.txt','w')
upper_log.write(upper_string)
upper_log.close()

