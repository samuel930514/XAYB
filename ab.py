import requests
import random
from flask import Flask
import json

app=Flask(__name__)

@app.route("/Q")
def Q():

	Ans=""

	Ansl = random.sample(range(0,10), 4)

	for i in Ansl:
		Ans+=str(i)

	Ans2={"first":Ans[0],"second":Ans[1],"third":Ans[2],"fourth":Ans[3],"Ans":Ans}
	Ansj = json.dumps(Ans2)

	print (Ansj)
	return "{\"set_attributes\":" + Ansj + "}"

@app.route("/check")
def check():

  A=0
  B=0
  guess=str(request.args.get('guess'))
  Ans=str(request.args.get('Ans'))

  for j in guess:
    for k in range(0,4):
      if j==Ans[k] and j==k:
        A=A+1
        break
      elif j==Ans[k]:
        B=B+1
        break

  return A+"A"+B+"B"





if __name__=="__main__":
	app.debug=True	
	app.run()
