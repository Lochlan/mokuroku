all: syncdb fixtures runserver

fixtures = $(shell find products/fixtures -type f -name '*.json')

fixtures:
	python manage.py loaddata $(fixtures)

runserver:
	python manage.py runserver

syncdb:
	python manage.py syncdb

db-dump:
	sqlite3 -line db.sqlite3 '.dump'

dumpdata:
	manage.py dumpdata > dumpdata.json

pyc = $(shell find . -type f -name '*.pyc')

clean:
	rm -f db.sqlite3
	rm -rfv $(pyc)
