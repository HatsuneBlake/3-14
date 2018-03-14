class MyError(Exception):pass

def f():
	raise MyError()
	
if __name__ == '__main__':
	print 'EX1'
	try:
		f()
	except MyError:
		print 'EX1 Except Done.'
	else:
		print 'EX1 Else Done.'
	finally:
		print 'EX1 Fin.'
	
	print 'ex2'
	try:
		pass
	except Exception:
		print 'ex2 Excep Done.'
	else:
		print 'ex2 Else Done.'
	finally:
		print 'ex2 Fin.'
	
	print 'Ex3'
	try:
		pass
	except Exception:
		print 'Ex3 Except Done.'
	else:
		print 'Ex3 Else Raise Err Again.'
		f()
	finally:
		print 'Ex3 Done.'