import sqlite3
import datetime
import optparse

def fixDate(timestamp):
    #Chrome stores timestamps in the number of microseconds since Jan 1 1601.
    #To convert, we create a datetime object for Jan 1 1601...
    epoch_start = datetime.datetime(1601,1,1)
    #create an object for the number of microseconds in the timestamp
    delta = datetime.timedelta(microseconds=int(timestamp))
    #and return the sum of the two.
    return epoch_start + delta

selectFromDownloads = 'SELECT target_path, referrer, start_time, end_time, received_bytes FROM downloads;'

def getMetadataHistoryFile(locationHistoryFile):

	sql_connect = sqlite3.connect(locationHistoryFile)
	for row in sql_connect.execute(selectFromDownloads):
		print ("Download:",row[0].encode('utf-8'))
		print ("\tFrom:",str(row[1]))
		print ("\tStarted:",str(fixDate(row[2])))
		print ("\tFinished:",str(fixDate(row[3])))
		print ("\tSize:",str(row[4]))
	
def main():
    parser = optparse.OptionParser('-location <target location>')
    parser.add_option('-l', dest='location', type='string', help='specify url address')

    (options, args) = parser.parse_args()
    location = options.location
    print(location)
    if location == None:
        exit(0)
    else:
        getMetadataHistoryFile(location)


if __name__ == '__main__':
    main()