# ML PeopleCounter
*   Preliminares:
    *   Se debe de tener anaconda con dos ambientes listos. (pueden llamarse labelImg y tfodapi, ambas con python 3.7)
    *   Se debe de tener una carpeta donde se pondrán todos los archivos (acá la llamaremos devFolder) 


## Instalación de la api de tensorflow



*   Las siguientes instrucciones se deben de realizar en el ambiente de tfodapi.
*   NOTA (se debe de instalar la version 1.14 de tensor flow y la version 1.17 de numpy).
*   Se clona el repositorio de tensor flow object detection api en devFolder
    *   _git clone [https://github.com/tensorflow/models.git](https://github.com/tensorflow/models.git)_
*   Se instala tensorflow en tfodapi
    *   _pip install tensorflow _->_ _para CPU
    *   _pip install tensorflow-gpu _-> para GPU
*   Se procede a instalar más librerías de python necesarias en tfodapi
    *   _pip install pillow_
    *   _pip install lxml_
    *   _pip install jupyter_
    *   _pip install matplotlib_
*   Se instala la api de COCO modificada para windows en tfodapi
    *   _pip install git+[https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI](https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI)_
    *   _Para mas informacion de esta version, consultar [https://github.com/philferriere/cocoapi](https://github.com/philferriere/cocoapi)_
*   Dado que la api usa archivos formato .proto que necesitan ser compilados a archivos .py, se descarga la versión 3.4.0 de windows de protobuf, que permite esta compilación.
    *   _Descargar la versión indicada en [https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0](https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0)_
    *   _Extraer el archivo zip en devFolder_
    *   _Ejecutar el archivo protoc.exe de la carpeta extraida en \models\research\object_detection\protos de la siguiente manera:_
        *   _{ruta a protoc.exe}\protoc.exe {ruta a devFolder}\models\research\object_detection\protos\*.proto --python_out=._
    *   _Se debe de poder ver los archivos .py compilados en la carpeta de protos_
*   Luego se añaden las librerías de la api de tensorflow a la variable del sistema PYTHONPATH. directorios a añadir:
    *   {ruta a devFolder}\models
    *   {ruta a devFolder}\models\research
    *   {ruta a devFolder}\models\research\slim
    *   {ruta a devFolder}\models\research\object_detection
*   Esto terminaria la instalacion, para mas información de detalles o posibles errores, consultar [https://medium.com/@marklabinski/installing-tensorflow-object-detection-api-on-windows-10-7a4eb83e1e7b](https://medium.com/@marklabinski/installing-tensorflow-object-detection-api-on-windows-10-7a4eb83e1e7b). 


## Instalación labelimg



*   Las siguientes instrucciones se deben de realizar en el ambiente de labelImg.
*   Clonar repositorio de labelimg (https://github.com/tzutalin/labelImg) en devFolder
    *   git clone [https://github.com/tzutalin/labelImg.git](https://github.com/tzutalin/labelImg.git)
*   En el ambiente de labelImg ejecutar los siguientes comandos en el repositorio clonado:
    *   _conda install pyqt=5_
    *   _conda install -c anaconda lxml_
    *   _pyrcc5 -o libs/resources.py resources.qrc_
*   La instalación está completada, para abrir el software de etiquetación, solo basta con ejecutar el siguiente comando en el repositorio clonado:
    *   _python labelImg.py_


## Instalación proyecto ML PeopleCounter

Este es el repositorio donde se tiene los datos divididos en sus respectivos sets, y se guarda todos los archivos necesarios para desarrollar nuevos modelos, entrenarlos, evaluarlos, extraer los grafos de inferencia para posteriormente probarlos con archivos de video o imágenes y visualizar los resultados.



*   Para la instalacion de ML PeopleCounter, solo basta con clonar el repositorio en devFolder e instalar opencv para python en el ambiente de tfodapi
    *   _git clone [https://gitlab.com/metrocali/ml-peoplecounter.git](https://gitlab.com/metrocali/ml-peoplecounter.git)_
    *   _pip install opencv-python_
