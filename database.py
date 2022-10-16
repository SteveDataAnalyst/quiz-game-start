from deta import Deta

DETA_KEY = "c050exny_sE1wzsJo16sN4NJEq1uwxLkDa7kAZAxV"

deta = Deta(DETA_KEY)

db = deta.Base("quiz_results")

def insert_quiz_result(key, date, name, result, time, qns, ans):
  return db.put({"key": key,
                 "date": date,
                 "name": name,
                 "result": result,
                 "time" : time,
                 "question" : qns,
                 "answer" : ans
                 })


def fetch_db():
    res = db.fetch()
    return res.items
