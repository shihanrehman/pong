class Test:
	def __init__(self, *args, **kwargs):
		print(args,kwargs)


t = Test(1, 2, five=5, three=3, four=4)