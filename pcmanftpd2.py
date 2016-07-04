from sulley import *
import time
#-----------------------------------------------------------------------------------------
#Define pre_send function. Will be executed right after the three-way handshake
def	preconnection(sock):
	sock.send("\
	\x00\x0c\x29\x6b\x86\x72\x00\x0c\x29\x97\x80\x04\x08\x00\x45\x00\x00\x3c\x2f\xa0\x40\x00\x40\x06\x00\x00\xc0\xa8\x03\x4d\xc0\xa8\x03\xb1\xd1\x9f\x00\x15\x69\xb6\x85\x53\x00\x00\x00\x00\xa0\x02\x20\x00\x88\x7d\x00\x00\x02\x04\x05\xb4\x01\x03\x03\x02\x04\x02\x08\x0a\x00\xa0\x01\x9f\x00\x00\x00\x00")
	time.sleep(2.0)
	sock.send("\
	\x00\x0c\x29\x6b\x86\x72\x00\x0c\x29\x97\x80\x04\x08\x00\x45\x00\x00\x34\x2f\xa1\x40\x00\x40\x06\x00\x00\xc0\xa8\x03\x4d\xc0\xa8\x03\xb1\xd1\x9f\x00\x15\x69\xb6\x85\x54\x15\x47\xf4\xef\x80\x10\x08\x00\x88\x75\x00\x00\x01\x01\x08\x0a\x00\xa0\x01\x9f\x00\x38\xd8\x33")
	time.sleep(2.0)
	sock.send("\
	\x00\x0c\x29\x6b\x86\x72\x00\x0c\x29\x97\x80\x04\x08\x00\x45\x00\x00\x34\x30\x28\x40\x00\x40\x06\x00\x00\xc0\xa8\x03\x4d\xc0\xa8\x03\xb1\xd1\x9f\x00\x15\x69\xb6\x85\x54\x15\x47\xf5\x15\x80\x10\x07\xf6\x88\x75\x00\x00\x01\x01\x08\x0a\x00\xa0\x01\xb3\x00\x38\xd8\x33")
	time.sleep(2.0)
def receive_ftp_banner(sock):
	sock.recv(1024)
	
"""
#################
## Data model. ##
#################
"""

""" Non-fuzzed commands used as preconditions to other commands. """
s_initialize('DataUSER')
s_static('USER anonymous\r\n')

s_initialize('DataPASS')
s_static('PASS test\r\n')

s_initialize('DataPORT')
s_static('PORT 127,0,0,1,4,1\r\n')

s_initialize('DataPASV')
s_static('PASV\r\n')

s_initialize('DataREST')
s_static('REST 9999\r\n')

s_initialize('DataRNFR')
s_static('RNFT test\r\n')

s_initialize('DataQUIT')
s_static('QUIT\r\n')



""" User/Pass commands. """
s_initialize('AUSER')
s_static('USER')
s_delim(' ')
s_string('anonymous')
s_static('\r\n')

s_initialize('APASS')
s_static('PASS')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('AHELP')
s_static('HELP')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('AACCT')
s_static('ACCT')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('AHOST')
s_static('HOST')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('AAUTH')
s_static('AUTH')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('AADAT')
s_static('ADAT')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('APBSZ')
s_static('PBSZ')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('APROT')
s_static('PROT')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')



""" Standard commands. """
s_initialize('DataSet1')
s_group('commands1', values=['HELP', 'ACCT', 'CWD', 'SMNT', 'RETR', 'STOR', 'STOU', 'APPE', 'REST', 'RNFR', 'RNTO', 'DELE', 'RMD', 'MKD', 'SITE', 'HOST', 'AUTH', 'ADAT', 'ALGS', 'OPTS', 'MDTM', 'SIZE', 'XRMD', 'XMKD', 'XCWD', 'STRU', 'MODE', 'PROT', 'STAT', 'NLST', 'LIST', 'MLST', 'MLSD', 'CDUP', 'REIN', 'PASV', 'ABOR', 'SYST', 'NOOP', 'CCC', 'LPSV', 'XPWD', 'PWD', 'XCUP', 'QUIT'])
s_block_start('Datablock1', group='commands1')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')
s_block_end()

""" Base64 commands.find it not used,try to use it . """
s_initialize('DataSet2')
s_group('commands2', values=['MIC', 'CONF', 'ENC'])
s_block_start('DataBlock2', group='commands2')
s_static('\r\n')
s_block_end()


""" Special commands. """
s_initialize('PORT')
s_static('PORT')
s_delim(' ')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_static('\r\n')

s_initialize('LPRT')
s_static('LPRT')
s_delim(' ')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_delim(',')
s_byte(0, format="ascii", signed=False)
s_static('\r\n')

s_initialize('LANG')
s_static('LANG')
s_delim(' ')
s_string('fuzz', size=2)
s_delim('-')
s_string('fuzz', size=2)
s_static('\r\n')


s_initialize('EPRT')
s_static('EPRT')
s_delim(' ')
s_delim('|')
s_byte(0, format="ascii", signed=False)
s_delim('|')
s_byte(0, format="ascii", signed=False)
s_delim('.')
s_byte(0, format="ascii", signed=False)
s_delim('.')
s_byte(0, format="ascii", signed=False)
s_delim('.')
s_byte(0, format="ascii", signed=False)
s_delim('|')
s_word(0, format="ascii", signed=False)
s_static('\r\n')

s_initialize('EPSV')
s_static('EPSV')
s_delim(' ')
s_byte(0, format="ascii", signed=False)
s_delim('.')
s_byte(0, format="ascii", signed=False)
s_delim('.')
s_byte(0, format="ascii", signed=False)
s_delim('.')
s_byte(0, format="ascii", signed=False)
s_static('\r\n')

s_initialize('PBSZ')
s_static('PBSZ')
s_delim(' ')
s_qword(0, format="ascii", signed=False)
s_static('\r\n')


s_initialize('ALLO1')
s_static('ALLO')
s_delim(' ')
s_qword(0, format="ascii", signed=False)
s_static('\r\n')

s_initialize('ALLO2')
s_static('ALLO')
s_delim(' ')
s_qword(0, format="ascii", signed=False)
s_delim(' ')
s_static('R')
s_delim(' ')
s_qword(0, format="ascii", signed=False)
s_static('\r\n')


s_initialize('TYPE1')
s_static('TYPE')
s_delim(' ')
s_static('A')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('TYPE2')
s_static('TYPE')
s_delim(' ')
s_static('E')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('TYPE3')
s_static('TYPE')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('TYPE4')
s_static('TYPE')
s_delim(' ')
s_static('L')
s_delim(' ')
s_word(0, format="ascii", signed=False)
s_static('\r\n')


""" Dependencies commands. """
s_initialize('APPE')
s_static('APPE')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('STOR')
s_static('STOR')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('NLST')
s_static('NLST')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('LIST')
s_static('LIST')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('RETR')
s_static('RETR')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('STOU')
s_static('STOU')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')

s_initialize('RNTO')
s_static('RNTO')
s_delim(' ')
s_string('fuzz')
s_static('\r\n')


####################upon is try for now one ##############################

#-----------------------------------------------------------------------------------------
# Debugging / Create use case log
debugmode = 0
use_case_logfile = "pcman_all_cases.txt"
decision = raw_input("Do you want to just generate use cases(debugmode)?(y/n): ")
if decision == "y":
	debugmode = 1
	print "Start creating the use cases - will be stored in: " + use_case_logfile
else:
	print "Debugging turned off!"

use_case_number = 1 
counter = 1
def debug(construct):
	global use_case_number
	counter = 1
	while s_mutate(): # s_mutate generates the next upcoming mutation
		f = open(use_case_logfile,'ab')
		f.write("Use case =" + str(use_case_number) + ": ")
		f.write(s_render()) #s_render() represents the current mutation value
		use_case_number += 1
		counter += 1
		f.close()
	print "Construct: " + construct + "\t\t - Use Cases: " + str(counter)

	
	
#-----------------------------------------------------------------------------------------
#Define session
#Session paramaters 
SESSION_FILENAME = "pcmanftpd2-session" 		# Keeps track of the current fuzzing state
SLEEP_TIME = 0.5							# Pause between two fuzzing attempts
TIMEOUT = 5									# Fuzzer will time out after 5 seconds of no connection
CRASH_THRESHOLD = 4							# After 4 crashes parameter will be skipped


mysession = sessions.session(
	session_filename = SESSION_FILENAME,
	sleep_time=SLEEP_TIME,
	timeout=TIMEOUT,
	crash_threshold=CRASH_THRESHOLD)
	
#mysession.pre_send=preconnection
mysession.pre_send = receive_ftp_banner


#####################below is try for now #####################
""""Define state model."""
# commands directly accessible without login
#mysession.connect(s_get('AUSER'))
mysession.connect(s_get('AUSER'))
if debugmode == 1: debug("AUSER")
mysession.connect(s_get('APASS'))
if debugmode == 1: debug("APASS")
mysession.connect(s_get('AUSER'), s_get('APASS'))
if debugmode == 1: debug("APASS")
mysession.connect(s_get('AHELP'))
if debugmode == 1: debug("AHELP")
mysession.connect(s_get('AACCT'))
if debugmode == 1: debug("AACCT")
mysession.connect(s_get('APROT'))
if debugmode == 1: debug("APROT")
mysession.connect(s_get('APBSZ'))
if debugmode == 1: debug("APBSZ")
mysession.connect(s_get('AHOST'))
if debugmode == 1: debug("AHOST")
mysession.connect(s_get('AAUTH'))
if debugmode == 1: debug("AAUTH")
mysession.connect(s_get('AADAT'))
if debugmode == 1: debug("AADAT")
# authenticated commands
mysession.connect(s_get('DataUSER'))
if debugmode == 1: debug("DataUSER")

mysession.connect(s_get('DataUSER'), s_get('DataPASS'))
if debugmode == 1: debug("DataPASS")

mysession.connect(s_get('DataPASS'), s_get('DataSet1'))
if debugmode == 1: debug("DataSet1")
mysession.connect(s_get('DataPASS'), s_get('PORT'))
if debugmode == 1: debug("PORT")
mysession.connect(s_get('DataPASS'), s_get('TYPE1'))
if debugmode == 1: debug("TYPE1")
mysession.connect(s_get('DataPASS'), s_get('TYPE2'))
if debugmode == 1: debug("TYPE2")
mysession.connect(s_get('DataPASS'), s_get('TYPE3'))
if debugmode == 1: debug("TYPE3")
mysession.connect(s_get('DataPASS'), s_get('TYPE4'))
if debugmode == 1: debug("TYPE4")
mysession.connect(s_get('DataPASS'), s_get('ALLO1'))
if debugmode == 1: debug("ALLO1")
mysession.connect(s_get('DataPASS'), s_get('ALLO2'))
if debugmode == 1: debug("ALLO2")
mysession.connect(s_get('DataPASS'), s_get('PBSZ'))
if debugmode == 1: debug("PBSZ")
mysession.connect(s_get('DataPASS'), s_get('EPRT'))
if debugmode == 1: debug("EPRT")
mysession.connect(s_get('DataPASS'), s_get('EPSV'))
if debugmode == 1: debug("EPSV")
mysession.connect(s_get('DataPASS'), s_get('LANG'))
if debugmode == 1: debug("LANG")
mysession.connect(s_get('DataPASS'), s_get('EPRT'))
if debugmode == 1: debug("EPRT")


# special order of commands
# PASS
mysession.connect(s_get('DataPASS'), s_get('DataPASV'))
if debugmode == 1: debug("DataPASV")
mysession.connect(s_get('DataPASV'), s_get('APPE'))
if debugmode == 1: debug("APPE")
mysession.connect(s_get('DataPASV'), s_get('STOR'))
if debugmode == 1: debug("STOR")
mysession.connect(s_get('DataPASV'), s_get('NLST'))
if debugmode == 1: debug("NLST")
mysession.connect(s_get('DataPASV'), s_get('LIST'))
if debugmode == 1: debug("LIST")
mysession.connect(s_get('DataPASV'), s_get('RETR'))
if debugmode == 1: debug("RETR")
mysession.connect(s_get('DataPASV'), s_get('STOU'))
if debugmode == 1: debug("STOU")
# PORT
mysession.connect(s_get('DataPASS'), s_get('DataPORT'))
if debugmode == 1: debug("DataPORT")
mysession.connect(s_get('DataPORT'), s_get('APPE'))
if debugmode == 1: debug("APPE")
mysession.connect(s_get('DataPORT'), s_get('STOR'))
if debugmode == 1: debug("STOR")
mysession.connect(s_get('DataPORT'), s_get('NLST'))
if debugmode == 1: debug("NLST")
mysession.connect(s_get('DataPORT'), s_get('LIST'))
if debugmode == 1: debug("LIST")
mysession.connect(s_get('DataPORT'), s_get('RETR'))
if debugmode == 1: debug("RETR")
mysession.connect(s_get('DataPORT'), s_get('STOU'))
if debugmode == 1: debug("STOU")
# REST
mysession.connect(s_get('DataPASS'), s_get('DataREST'))
if debugmode == 1: debug("DataREST")
mysession.connect(s_get('DataREST'), s_get('APPE'))
if debugmode == 1: debug("APPE")
mysession.connect(s_get('DataREST'), s_get('STOR'))
if debugmode == 1: debug("STOR")
mysession.connect(s_get('DataREST'), s_get('RETR'))
if debugmode == 1: debug("RETR")
# RNFR
mysession.connect(s_get('DataPASS'), s_get('DataRNFR'))
if debugmode == 1: debug("DataRNFR")
mysession.connect(s_get('DataRNFR'), s_get('RNTO'))
if debugmode == 1: debug("RNTO")
#########################upon is try for now#####################
#-----------------------------------------------------------------------------------------
# Draw graph representing the fuzzing paths
fh = open("session_test.udg", "w+")
fh.write(mysession.render_graph_udraw())
fh.close()

#-----------------------------------------------------------------------------------------

	
# Just some overview output
if debugmode == 0: 
	print "Number of mutation during one case: " + str(s_num_mutations()) + "\n"
	print "Total number of mutations:" + str(s_num_mutations()*5) + "\n"
	decision = raw_input("Do you want to continue?(y/n): ")
	if decision == "n":
		exit()


	
#-----------------------------------------------------------------------------------------
#Define target parameters
if debugmode == 0: 
	target = sessions.target("192.168.3.177",21)
	target.procmon = pedrpc.client("192.168.3.177",26002)
	target.netmon = pedrpc.client("127.0.0.1",26001)

	target.procmon_options = {
		"proc_name" : "PCManFTPD2.exe",
		"stop_commands" : ['wmic process where (name="PCManFTPD2.exe") call terminate'],
		"start_commands" : ["C:\Users\klionsec7\Desktop\9fceb6fefd0f3ca1a8c36e97b6cc925d-PCMan\PCManFTPD2.exe"]
	}
		
# Add target to the session		
if debugmode == 0: mysession.add_target(target)


#-----------------------------------------------------------------------------------------
# Lets get rollin'
if debugmode ==0:
	print "Starting fuzzing now"
	mysession.fuzz() # Starts the fuzzing process and also the web interface (http://127.0.0.1:26000) to see the current state