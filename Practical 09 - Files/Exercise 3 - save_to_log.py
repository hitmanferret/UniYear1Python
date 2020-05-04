entry = "new entry \n"

def save_to_log(entry, logfile):
    log = open(logfile, 'a')
    log.write(entry)
    log.close()

save_to_log(entry, 'logfile.txt')
