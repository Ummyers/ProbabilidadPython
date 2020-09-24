Para la instalación de Anaconda en Ubuntu se siguieron las intrucciones del siguiente enlace

Para verificar la correcta instalación lo podrás verificar con el siguiente comando:

$conda --version

Lo que debería devolverte algo como: conda 4.8.3

Sin embargo, en mi caso al terminar de realizar las instrucciones, debido a unas configuraciones para el proyecto del Framework Ligra 
tuve que añadir el siguiente comando

$ export PATH=~/anaconda3/bin:$PATH
