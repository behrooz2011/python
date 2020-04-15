import csv
#create the csv file
hosts=[['home','version','status','users'],['MailTree','5.34','production','324'],
['Caldoor','1.25.3','beta','22'],['chatty chick','0.34','alpha','4']]
with open('software111.csv','w') as software:
	writer=csv.writer(software)
	writer.writerows(hosts)

# read the content as CSV
with open('software111.csv') as software:
	reader=csv.DictReader(software)
	for row in reader:
		print(row)

