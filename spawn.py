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
	# vetor com os nomes dos contatos
	contacts = ['BUG DO MILÊNIO', 'Robert Metzler']
	messages = ['*Olá, boa tarde!!!*','Obrigado por estar conosco, te espero ano que vem!!!','*Feliz natal e boas Festas*', '_Não esqueça de responder nossa pesquisa_', 'https://goo.gl/forms/vW7CdRGJWoTdvi1C3','_RISEUP VENHA SER EXCLUSIVO!!!_']
	count = 1
	input('Aperte enter se já foi escaneado o QR code')
	for name in contacts:
		time.sleep(1)
		for message in messages:
			time.sleep(1)
			sender(name,message,count)

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
	