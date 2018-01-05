# Author: Samuel Brati Favarin
# GitHub: @SamuelBFavarin
# AUTOMATIC WHATSAPP MESSENGER SENDER
# Language: Python
#
# Functions:
# send messages with text and images
# for send automatic you need:
#	-> insert the contacts in contacts.txt
#	-> insert the message in messages.txt
#	-> insert the image path in pathImage.txt

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import os
import time

# Path for chrome driver
driver = webdriver.Chrome('chromedriver')
# Open Whatsapp Web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Send message automatic from text files content contacts and messages
def sendAutomatic():
	# flagContact
	emptyContact = False

	# get contacts
	with open('contacts.txt', 'r') as arq:
		contacts = arq.read().splitlines()

	# get messages
	with open('messages.txt', 'r') as arq:
		messages = arq.read().splitlines()

	#get images
	with open('pathImage.txt', 'r') as arq:
		url = arq.read().splitlines()

	count = 1
	i =0;
	input('Aperte enter se já foi escaneado o QR code')

	#loop in contatcts->message
	for name in contacts:
		for message in messages:
			# in first time send new message
			if(i == 0):
				emptyContact = senderNewMessage(name,message,count)
			else:
				emptyContact = sender(name,message,count)
			i = i+1
		# test if exist image and contact
		if (fileEmpty('pathImage.txt') == False and emptyContact == False):
			sendImage(url)
		i = 0
		emptyContact == False

#send manual message, input is contact name, message, repetition message in line, row number for repetition
def sendManual():
	name = input('Digite o nome do usuário ou do grupo: ')
	msg = input('Digite a mensagem: ')
	count = int(input('Digite o número de vezes que a mensagem deve repetir na linha: '))
	repeat = int(input('Digite o número de linhas: '))

	#get images
	with open('pathImage.txt', 'r') as arq:
		url = arq.read().splitlines()


	input('Aperte enter se já foi escaneado o QR code')

	# loop for do repetition
	for x in range(0, repeat):
		#in first time send new message
		if (x == 0):
			senderNewMessage(name,msg,count)
		else:
			sender(name,msg,count)
		# test if exist image for send
		if (fileEmpty('pathImage.txt') == False):
			sendImage(url)

#send new message search in all contacts
def senderNewMessage(name,msg,count):

	# get input for contacts and insert contact name in input
	pesquisaContato = driver.find_element_by_id('input-chatlist-search')
	pesquisaContato.send_keys(name)
	#try do send messa for contact
	try:
		# get contact card and enter in chat
		time.sleep(2)
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()
		# send message in number of repetition line message
		msg_box = driver.find_element_by_class_name('input-container')
		for i in range(count):
			msg_box.send_keys(msg)
		driver.find_element_by_class_name('compose-btn-send').click()
		return False
	# if contact not found
	except NoSuchElementException:
		print("Contato não encontrado.")
		driver.find_element_by_xpath('//*[@id="side"]/div[2]/div/button').click()
		return True

# send message when chat is open
def sender(name,msg,count):
	# for prevention get card element again end enter in chat
	# try send message for contact
	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		time.sleep(0.5)
		user.click()
		# send message in number of repetition line message
		msg_box = driver.find_element_by_class_name('input-container')
		for i in range(count):
			msg_box.send_keys(msg)
		driver.find_element_by_class_name('compose-btn-send').click()
		return False
	# if contact not found
	except NoSuchElementException:
		print("Contato não encontrado.")
		return True

# send image message from path
def sendImage(path):
        pathImage = path
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input').send_keys(pathImage)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]').click()

# test if pathImage isn't empty
def fileEmpty(path):
    return os.stat(path).st_size==0

# Main Menu
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
