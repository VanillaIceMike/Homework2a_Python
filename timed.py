import time
def timeme(func):
	def decorator():
		start = time.time()
		finish = time.time()
		print("Total time ", finish - start)
		func()
	return decorator
