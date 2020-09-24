Para la instalación de Anaconda en Ubuntu se siguieron las intrucciones del siguiente enlace:

https://phoenixnap.com/kb/how-to-install-anaconda-ubuntu-18-04-or-20-04 
O una versión en español: https://www.digitalocean.com/community/tutorials/como-instalar-anaconda-en-ubuntu-18-04-quickstart-es

Para verificar la correcta instalación lo podrás verificar con el siguiente comando:

$conda --version

Lo que debería devolverte algo como: conda 4.8.3

Sin embargo, en mi caso al terminar de realizar las instrucciones, debido a unas configuraciones para el proyecto del Framework Ligra 
tuve que añadir el siguiente comando

$ export PATH=~/anaconda3/bin:$PATH
