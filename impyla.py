#!/usr/bin/python
from impala.dbapi import connect
import sys

if len(sys.argv) != 4:
    print "Expected 3 args: username password hostip. Got "+ str(len(sys.argv))
    sys.exit()

user=sys.argv[1]
pwd=sys.argv[2]
host=sys.argv[3]



conn = connect(
    host=host,
    port=21050,
    use_ssl=True,
    auth_mechanism='PLAIN',
    user=user,
    password=pwd
    )

cursor = conn.cursor()
cursor.execute('SELECT * FROM nyctaxilanding.zones LIMIT 100')
print cursor.description  # prints the result set's schema
results = cursor.fetchall()
print results
