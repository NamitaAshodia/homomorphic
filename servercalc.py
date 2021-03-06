from linmodel import LinModel
import phe as paillier
import json

def getData():
	with open('data.json', 'r') as file: 
		d=json.load(file)
	data=json.loads(d)
	return data

def computeData():
	data=getData()
	mycoef=LinModel().getCoef()
	pk=data['public_key']
	pubkey= paillier.PaillierPublicKey(n=int(pk['n']))
	enc_nums_rec = [paillier.EncryptedNumber(pubkey, int(x[0], int(x[1]))) for x in data['values']]
	results=sum([mycoef[i]*enc_nums_rec[i] for i in range(len(mycoef))])
	return results, pubkey
