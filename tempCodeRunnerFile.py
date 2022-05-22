answer_file=loadAnswer()
answer_key=paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
answer = paillier.EncryptedNumber(answer_key, int(answer_file['values'][0]), int(answer_file['values'][1]))
if (answer_key==pub_key):
    print(priv_key.decrypt(answer))