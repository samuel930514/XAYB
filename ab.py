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
	return Ansj

if __name__=="__main__":
	app.debug=True	
	app.run()
