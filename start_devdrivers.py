import os
import time
import configparser

def getTasks(name):
	r = os.popen('tasklist /v').read().strip().split('\n')
	print ('# of tasks is %s' % (len(r)))
	for i in range(len(r)):
		s = r[i]
		if name in r[i]:
			print ('%s in r[i]' %(name))
			return r[i]
	return []

if __name__ == '__main__':
	'''
	This code checks tasklist, and will print the status of a code
	'''

	config = configparser.ConfigParser()
	config.read('device_config.ini')
	
	#imgNames = {'test.exe','hello1.exe','hello2.exe','hello3.exe'}
	imgNames = { config['DEVDRIVER']['driver1'],
				 config['DEVDRIVER']['driver2'],
				 config['DEVDRIVER']['driver3'],
				 config['DEVDRIVER']['driver4'],
				 config['DEVDRIVER']['driver5']
				}
				
	basedir = config['BASE']['path'] #'E:\github\lppkn\python_scripts'
	print("test[%s]" % basedir)
	for imgName in imgNames:
		r = getTasks(imgName)
		print("name[%s]" % imgName)
		if not r:
			print('%s - No such process' % (imgName))
			os.system('start "%s" %s\dir\\%s\\%s' % (imgName,basedir,imgName[:-4],imgName))
			print('%s is Started' % (imgName))

		elif 'Not Responding' in r:
			print('%s is Not responding' % (imgName))

		else:
			print('%s is Running or Unknown' % (imgName))
		time.sleep(1)
	
	# Fire split screens ahk
	scr = config['AHKSCRIPT']['scr']
	os.system('start %s\\%s' % (basedir,scr))
