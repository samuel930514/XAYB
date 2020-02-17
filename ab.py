
import requests
import random
from flask import Flask, request
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

  if len(guess)!=4:
    B=-1

  re=0

  for l in guess:
    re=0
    for m in (0,len(guess)):
      if l==guess[m]:
        re+=1
      if re>=2:
        B=-1
        break
  
  ABD={"A":A,"B":B}
  ABj = json.dumps(ABD)

  return "{\"set_attributes\":" + ABj + "}"





if __name__=="__main__":
	app.debug="off"	
	app.run()

