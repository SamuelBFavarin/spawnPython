# Author: Samuel Brati Favarin
# GitHub: @SamuelBFavarin
# AUTOMATIC WHATSAPP MESSENGER SENDER
# Language: Portuguese

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#path for chrome driver
driver = webdriver.Chrome('chromedriver') 
#link of Whatsapp Web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

#Send message automatic from text files content contacts and messages
def sendAutomatic():
	# get contacts 
	with open('contacts.txt', 'r') as arq:
		contacts = arq.read().splitlines()

	# get messages
	with open('messages.txt', 'r') as arq:
		messages = arq.read().splitlines()	
	
	count = 1
	i =0;
	input('Aperte enter se já foi escaneado o QR code')

	#loop in contatcts->message
	for name in contacts:
		for message in messages:
			# in first time send new message
			if(i == 0):
				senderNewMessage(name,message,count)
			else:
				sender(name,message,count)
			i = i+1
		i = 0

#send manual message, input is contact name, message, repetition message in line, row number for repetition
def sendManual():
	name = input('Digite o nome do usuário ou do grupo : ')
	msg = input('Digite a mensagem : ')
	count = int(input('Digite o número de vezes que a mensagem deve repetir na linha : '))
	repeat = int(input('Digite o número de linhas: '))
	input('Aperte enter se já foi escaneado o QR code')
	
	# loop for do repetition
	for x in range(0, repeat):
		#in first time send new message
		if (x == 0):
			senderNewMessage(name,msg,count)
		else:
			sender(name,msg,count)


#send new message search in all contacts			
def senderNewMessage(name,msg,count):
	
	# get input for contacts and insert contact name in input
	pesquisaContato = driver.find_element_by_id('input-chatlist-search')
	pesquisaContato.send_keys(name)
	
	# get contact card and enter in chat
	time.sleep(2)
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	# send message in number of repetition line message
	msg_box = driver.find_element_by_class_name('input-container')
	for i in range(count):
		msg_box.send_keys(msg)
	driver.find_element_by_class_name('compose-btn-send').click()

# send message when chat is open
def sender(name,msg,count):
	# for prevention get card element again end enter in chat
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	time.sleep(0.5)
	user.click()

	# send message in number of repetition line message
	msg_box = driver.find_element_by_class_name('input-container')
	for i in range(count):
		msg_box.send_keys(msg)
	driver.find_element_by_class_name('compose-btn-send').click()

# main	
repetir = True
while (repetir == True):
	opcao = input('Você deseja que o envio seja Automático ou Manual? (A/M): ')
	if(opcao == 'A' or opcao == 'a'):
		sendAutomatic()
	else:
		sendManual()
	sair = input('Você deseja sair? (S/N) : ')
	if (sair == 'S' or sair == 's'):
		repetir = False
	else:
		repetir = True
	
