import openpyxl

def readFile(file):
	"""
	Read emails from an Excel file.
	"""
	wb = openpyxl.load_workbook(file)
	sheet = wb.active
	emails = []
	for row in sheet.iter_rows(values_only=True):
		for cell in row:
			if isinstance(cell, str) and '@' in cell:
				emails.append(cell)
	return emails

def filterEmails(emails):
	"""
	Filter unique emails.
	"""
	return list(set(emails))

def writeToFile(emails, file):
	"""
	Write emails to a text file.
	"""
	with open(file, 'w') as f:
		for email in emails:
			f.write(email + '\n')

def main():
	"""
	Main function
	Target file is in resources folder.
	"""
	file = 'resource/target.xlsx'
	
	try:
		emails = readFile(file)
		unique_emails = filterEmails(emails)
		writeToFile(unique_emails, 'resource/unique_emails.txt')
	except Exception as e:
		print(e)

if __name__ == '__main__':
    	main()

