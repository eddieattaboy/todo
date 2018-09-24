def task():

	print 'Name your list'
	
	name = raw_input('>')
	f = open('%s'%name + '.txt'  ,'w+')
	
	while True:
		try:
			n = int(raw_input('How many tasks would you like to add?\n>'))
			break
		except ValueError:
			print 'Please enter a valid number!'
			
	for i in range(n):
		print 'Please enter task number %d' %(i+1)
		point = raw_input('>')
				
		f.write('%d. ' %(i+1) + point + "\n")
	
	
print 'Welcome to your To-Do list!'
print 'Continue?'

while True:
	yesno = raw_input('>')
	
	if yesno.lower() in ('y' , 'ye' , 'yes' , 'yay' , 'yeah' , 'yea' , 'ya' , 'yup'):
		task()
		break
	
	if yesno.lower() in ('n','no','nah','nay','nope','nop'):
		print 'Thank you, come again!'
		break

	else:
		print 'Please enter "Yes" or "No"'
		
