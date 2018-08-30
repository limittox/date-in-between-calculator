import sys
from modules import dateDiff
from modules.date import date


if sys.argv[1] == "--file":
	with open(sys.argv[2]) as f:
		dates = f.read().splitlines()
	dates = [x.split() for x in dates]

	for i in dates:
		d1 = i[0]
		d2 = i[1]

		d1 = [int(s) for s in d1.split('/')]
		d2 = [int(s) for s in d2.split('/')]

		d1 = date(d1[0], d1[1], d1[2])
		d2 = date(d2[0], d2[1], d2[2])

		days = dateDiff.calcDateDiff(d1,d2)

		print(days)

else:
	d1 = sys.argv[1]
	d2 = sys.argv[2]

	d1 = [int(s) for s in d1.split('/')]
	d2 = [int(s) for s in d2.split('/')]

	d1 = date(d1[0], d1[1], d1[2])
	d2 = date(d2[0], d2[1], d2[2])

	days = dateDiff.calcDateDiff(d1,d2)

	print(days)