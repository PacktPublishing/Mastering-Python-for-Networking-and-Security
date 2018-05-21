import thread
import time

def thread_message(message):
	print('Message from thread %s\n' %message)

thread.start_new_thread(thread_message,("I am the first thread",))
thread.start_new_thread(thread_message,("I am the second thread",))
thread.start_new_thread(thread_message,("I am the third thread",))

time.sleep(0.1)