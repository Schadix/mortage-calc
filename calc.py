import csv
with open('mortageoptions.csv', 'rb') as csvfile:
	csv_r = csv.DictReader(csvfile)
	for row in csv_r:
		name=row['name']
		m=float(row['amount'])
		apr=float(row['apr'])
		p=float(row['payment'])
		apr_month=apr/12.0
		m_rest=m
		interest_total=0
		nr_month=0

		while m_rest>p:
			nr_month=nr_month+1
			interest=m_rest*apr_month/100
			m_rest=m_rest-p+interest
			interest_total=interest_total+interest
		nr_month=nr_month+1
		interest=m_rest*apr_month/100
		m_rest=m_rest-m_rest
		interest_total=interest_total+interest

		print "{0}, {1}, {2}, {3}, #month: {4}, interest_total: {5:.2f}, real percent: {6:.2f}".format(name, m, p, apr, nr_month, interest_total, interest_total/m*100)
