from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
 
#caminho onde deve estar o driver do chrome
driver = webdriver.Chrome('C:/Program Files (x86)/chrome-win32/chromedriver') 
#link do whatsapp web 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


def sendAutomatic():
	# recebe contatos do arquivo


	with open('contacts.txt', 'r') as arq:
		contacts = arq.read().splitlines()

	# recebe mensagens do arquivo
	with open('messages.txt', 'r') as arq:
		messages = arq.read().splitlines()	
	
	count = 1
	i =0;
	input('Aperte enter se já foi escaneado o QR code')

	for name in contacts:
		for message in messages:
			if(i == 0):
				senderNewMessage(name,message,count)
			else:
				sender(name,message,count)
			i = i+1
		i = 0

def sendManual():
	name = input('Digite o nome do usuário ou do grupo : ')
	msg = input('Digite a mensagem : ')
	count = int(input('Digite o número de vezes que a mensagem deve repetir na linha : '))
	repeat = int(input('Digite o número de linhas: '))
	input('Aperte enter se já foi escaneado o QR code')
	
	for x in range(0, repeat):
		
		if (x == 0):
			senderNewMessage(name,msg,count)
		else:
			sender(name,msg,count)

			
def senderNewMessage(name,msg,count):
	
	pesquisaContato = driver.find_element_by_id('input-chatlist-search')
	pesquisaContato.send_keys(name)
	
	
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('input-container')
	
	for i in range(count):
		msg_box.send_keys(msg)
	driver.find_element_by_class_name('compose-btn-send').click()

def sender(name,msg,count):
	
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	time.sleep(0.5)
	user.click()

	msg_box = driver.find_element_by_class_name('input-container')
	
	for i in range(count):
		msg_box.send_keys(msg)
	driver.find_element_by_class_name('compose-btn-send').click()

# main	
repetir = True
while (repetir == True):
	opcao = input('Você deseja que o envio seja Automático ou Manual? (A/M): ')
	if(opcao == 'A'):
		sendAutomatic()
	else:
		sendManual()
	sair = input('Você deseja sair? (S/N) : ')
	if (sair == 'S'):
		repetir = False
	else:
		repetir = True
	