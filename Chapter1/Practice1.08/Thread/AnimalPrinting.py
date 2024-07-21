import threading

def print_Animal(animal, times) :
	for i in range(0, times) :
		print(animal)

thread1 = threading.Thread(target = print_Animal, args = ("CAT", 7))
thread2 = threading.Thread(target = print_Animal, args = ("RABBIT", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
