from concurrent.futures import ThreadPoolExecutor

def task(n):
 print("Processing {}".format(n))

def main():
 print("Starting ThreadPoolExecutor")
 with ThreadPoolExecutor(max_workers=3) as executor:
   future = executor.submit(task, (2))
   future = executor.submit(task, (3))
   future = executor.submit(task, (4))
 print("All tasks complete")
  
if __name__ == '__main__':
 main()