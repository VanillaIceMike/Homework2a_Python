import time
def timestamp(func):
	def decorator():
		print(time.ctime())
		func()
	return decorator
