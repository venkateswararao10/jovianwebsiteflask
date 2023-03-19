import mysql.connector as con
import os


def fun():
  planetscaledb = con.connect(host=os.environ['planetscaledbhost'],
                              user=os.environ['planetscaledbuser'],
                              password=os.environ['planetscaledbpasswd'],
                              database=os.environ['planetscaledbname'])
  pscur = planetscaledb.cursor(dictionary=True)
  pscur.execute("select * from jobs")
  result = pscur.fetchall()
  return result
