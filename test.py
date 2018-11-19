import time
import os

class Test:
	def process():
		i=0
		while True:
			i+=1
			print(i)
			time.sleep(1)
			##	print("Exit(0)")
			#	break
		
def main():
	try:
		Test.process()
		#import hello2
		
	except Exception as e:
		print(e)
		#os.system("E:\github\lppkn\python_scripts\h.bat")
		
if __name__ == "__main__":
	main()