from deta import Deta

DETA_KEY = "c050exny_sE1wzsJo16sN4NJEq1uwxLkDa7kAZAxV"

deta = Deta(DETA_KEY)

db = deta.Base("quiz_results")

def insert_quiz_result(key, date, name, result, q1, q1_ans, q2, q2_ans, q3, q3_ans, q4, q4_ans,q5, q5_ans,
                       q6, q6_ans, q7, q7_ans, q8, q8_ans, q9, q9_ans, q10, q10_ans):
  return db.put({"key": key,
                 "date": date,
                 "name": name,
                 "result": result,
                 "Q1": q1,
                 "Q1_ans": q1_ans,
                 "Q2": q2,
                 "Q2_ans": q2_ans,
                 "Q3": q3,
                 "Q3_ans": q3_ans,
                 "Q4": q4,
                 "Q4_ans": q4_ans,
                 "Q5": q5,
                 "Q5_ans": q5_ans,
                 "Q6": q6,
                 "Q6_ans": q6_ans,
                 "Q7": q7,
                 "Q7_ans": q7_ans,
                 "Q8": q8,
                 "Q8_ans": q8_ans,
                 "Q9": q9,
                 "Q9_ans": q9_ans,
                 "Q10": q10,
                 "Q10_ans": q10_ans})


def fetch_db():
    res = db.fetch()
    return res.items
