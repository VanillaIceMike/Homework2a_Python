import time
def timeme(func):
	def decorator():
		start = time.time()
		func()
		finish = time.time()
		print(f"Total time {finish - start}")
	return decorator
