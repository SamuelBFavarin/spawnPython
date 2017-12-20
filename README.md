# Spawn Python Whatsapp (version 0.2)

Sistema de envio de mensagem automática via Whatsapp WEB. Desenvolvido com Python e biblioteca Selenium.
Utiliza-se o navegador Chromium e seu driver.

Baseado no projeto de [umangahuja1](https://github.com/umangahuja1/Scripting-and-Web-Scraping/blob/master/Whatsapp/message.py)

# Instalação

Segue abaixo o ambiente necessário para execução do programa.

### Instalação do Python
  
  * Python 3.6.4 - [Download](https://www.python.org/) 
  
  Geralmente o PIP é instalado com o Python, porém caso você não instalou basta escrever o código abaixo no Console
  
  ```
  python get-pip.py
  ```

### Instalação do Selenium

```
pip install selenium
```

### Instalação do Navegador

* Chromium - [Download do navegador](https://download-chromium.appspot.com/) 
* Driver - [Drive do navegador](https://chromedriver.storage.googleapis.com/index.html?path=2.25/)

# Executando

 * Execute o arquivo spawn.py no console
 * Entre no whatsapp web gerado pelo programa
 * Siga o menu do console
 
### Envio de menssagens manualmente

Você pode enviar menssagens manualmente para cada contato, basta escolher a opção de envio manual.
Segue os parâmetros pedidos pelo programa:
 
 * Nome do grupo ou contato (Caso seja contato pode ser também enviado o número de telefone)
 * Mensagem (Deve-se usar apenas caracteres suportados pelo console)
 * Número de vezes a repetir a mensagem dentro da linha
 * Número de vezes a repetir a mensagem
 
### Envio de menssagens automáticas

Você pode enviar menssagens automáticas para uma lista de contatos. Você também pode definir uma lista de mensagens.
Para o funcionamento deve-se inserir os contatos separados por linha no arquivo 'contacts.txt', do mesmo modo deve-se inserir as mensagens no arquivo 'messages.txt'

# Futuras Implementações

* Interface gráfica
* Envio de mensagens programadas
* Integração com banco de dados




