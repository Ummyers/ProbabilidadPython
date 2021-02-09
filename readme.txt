El repositorio llamado ProbabilidadPythonYR contiene ejercicios en Python y nada en R, el plan inicial del curso era que nos enseñaran R pero no fue así.
Es por ello que el repositorio contiene simulaciones de experimentos "aleatorios" utiles para entender conceptos de probabilidad. Se anexan además las tareas del curso con el profesor Julio César Galindo López y Guillermo Garro Gómez (Memo) quien llevó la parte de Jypyter y Python, es decir, las simulaciones.

>>Para la instalación de Anaconda en Ubuntu se siguieron las instrucciones del siguiente enlace:

https://phoenixnap.com/kb/how-to-install-anaconda-ubuntu-18-04-or-20-04 
O una versión en español: https://www.digitalocean.com/community/tutorials/como-instalar-anaconda-en-ubuntu-18-04-quickstart-es

Para verificar la correcta instalación lo podrás hacer con el siguiente comando:

$conda --version

Debería devolverte algo como: conda 4.8.3 (Según la versión que manejes) 

Sin embargo, en mi caso al terminar de realizar las instrucciones, debido a unas configuraciones para el proyecto del Framework Ligra 
tuve que añadir el siguiente comando:

$ export PATH=~/anaconda3/bin:$PATH

Si al momento de ejecutar el comando $conda --version no obtuviste respuesta puedes intentar realizar el comando anterior. 

Para inicializar Anaconda desde la terminal se usa el siguiente comando:

$ anaconda-navigator
