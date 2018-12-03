import psutil
import configparser

config = configparser.ConfigParser()
config.read('C:\\analyzer-ts\\device_config.ini')

processes = { config['DEVDRIVER']['driver1'],
			 config['DEVDRIVER']['driver2'],
			 config['DEVDRIVER']['driver3'],
			 config['DEVDRIVER']['driver4'],
			 config['DEVDRIVER']['driver5'],
			 'node.exe'
			}
for proc in psutil.process_iter():  
	if proc.name() in processes:
		proc.kill()
		print('%s has been killed' % proc.name())