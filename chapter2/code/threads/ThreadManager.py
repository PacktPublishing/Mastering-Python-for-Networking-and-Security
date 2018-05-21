import threading
import time

THREADS =5

def main():
	manager = ThreadManager()
	manager.start(THREADS)
	
class ThreadManager:
	def __init__(self):
		pass
		
	def start(self,threads):
		thread_refs =[]
		for i in range(threads):
			thread = MyThread("I am the "+str(i)+" thread")
			thread.daemon = True
			thread.start()
			
		
class MyThread(threading.Thread):

    def __init__ (self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        print self.message

if __name__== '__main__':
	main()
	