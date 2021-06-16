Aplicaciones en Weblogic:
    
    Desarrolladas en JAVA que sigan el estandar JEE
    
    - Como se escribe el código:
        - Jsp
        - Servlet
        - Jfc <<< similar al JSP
        
    - Empaquetamiento de la aplicación:
        
    
# CODIGO FUENTE

Al escribir código en JAVA generamos unos ficheros con extensión .java <<< Librerias o Servlets
                  También podemos generar ficheros con extensión .jsp  <<< JSP: Combinación de código HTML + Java
                  
Los archivos JAVA se deben compilar antes de poder ejecutarse. Esto lo hace el desarrollador: javac
    .java   --->   .class

Esto se empaqueta en un archivo ZIP, al cual le cambiamos la extensión .jar 

Los archivos .jar conienen en JAVA: 
    - Librerias:   Un conjunto de funciones NO pensadas para ejecutarse de forma AUTONOMA, sino para ser utilizadas desde otro programa.
    - Programas standalone: Programas que no requieren de un servidor de aplicaciones <<<< ESTOS NO NOS INTERESAN
    
# APLICACIONES WEB, el estandar JEE

ME debes entregar un archivo ZIP, que en este caso llevará la extensión .war
Ese archivo debe contener una carpeta denominada "WEB-INF". 
    Dentro de esa carpeta debe existir un archivo llamado "web.xml"   <<< Este archivo continie información de CONFIGURACION de la applicación web
    Además, dentro de esta carpeta también deben incluirse otras librerias que pueda necesitar la aplicación WEB, dentro de una carpeta llamada "lib"
    Además, los fichero java propios de la aplicación, deben entregarse compilados (.class) dentro de una carpeta llamada "classes"
Fuera de la carpeta WEB-INF podemos añadir ficheros .jsp, junto con otro tipo de ficheros accesible por el usuario final


Al trabajar con WEBLOGIC y realmente con cualquier Servidor de Aplicaciones JAVA.... esos servidores de apps... en qué lenguaje están desarrollados?
    JAVA
Para ejecutar un servidor de aplicaciones JAVA necesitamos tener instalada una máquina virtual java
Los archivos JSP son compilados por el propio servidor de aplicaciones .jsp >>>> .class . ESTA OPERACION REQUIERE DEL PROGRAMA javac

Los instaladores de JAVA siempre me dan a elegir entre 2 opciones:
    JRE: Java Runtime edition
        java <<<<<  JVM
    JDK: Java development Kit
        java <<<<< JVM
        javac <<<< Compilador de java


Para generar un proyecto APLICACION de prueba:
$ mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-webapp -DarchetypeVersion=1.4

PAQUETE: es.caixa.nominas
Mo codigo va a estar dentro de las carpetas : es\caixa\nominas\ CODIGO (a lo mejor estructurado en más carpetas)   <<<< GROUPID



Pre peticion: RAM Usando 100kb
          Request                                                                 Response
Cliente     >>>>>    peticion.jsp   >>>>>> crear un monton de cosas en la RAM      >>>>>>    Cliente
                                                    VVVVVVVVV
                        Nadie tiene ninguna variable que apunte a la tabla que tiene los objetos 50Kb

Al acabar la petición... la cosa es que nos queda un monton de basura en la RAM (toda esa tabla de objetos que ya no necesito para nada)

HEAP : EDEN > SURVIVOR > OLD GEN
Post peticion: RAM Usando 150kb -- A borrar   
Post peticion: RAM Usando 200kb -- A borrar
Post peticion: RAM Usando 250kb -- A borrar
Post peticion: RAM Usando 300kb -- A borrar
Post peticion: RAM Usando 350kb -- A borrar
Post peticion: RAM Usando 400kb -- A borrar
Petición en curso: lleva creados 40Kbs de cosas  -- No se puede borrar. Las mantengo ----> Las paso a otra zona de memoria RAM: SURVIVOR

---- Llega un límite que JAVA (JVM) determina que es necesario hacer un gc()
El gc de entrada libera el EDEN
La basura es eliminada----> Con cuanta RAM me quedaría en uso en este punto? 100Kb
(^ Situación ideal)
(v Situación real)
La basura es eliminada----> Con cuanta RAM me quedaría en uso en este punto? 140Kb
---- Acaba el GC

Petición en curso: crea otro 10Kb de cosas   ---- Se borran
Post peticion: RAM Usando 150kb              ---- Se borra
Post peticion: RAM Usando 200kb              ---- Se borra
Post peticion: RAM Usando 250kb              ---- Se borra
Post peticion: RAM Usando 300kb              ---- Se borra
Petición en curso: lleva creados 30Kbs de cosas - Al survivor 

---- Llega un límite que JAVA (JVM) determina que es necesario hacer un gc()
El gc de entrada libera el EDEN
---- termina el GC. La RAM Está en ?      170Kb

--- Llega un momento que el survivor se peta... se llena... que pasa ahí? Todo lo que hay en el survivor (1,2) ---> OldGen

--- Llega un momento que el old gen se llena ----- JAVA llama de nuevo al GC, pero en esta ocasión le llama sobre el EDEN + OLD GEN (tarda la vida)

--- Al acabar este proceso... en cuanto se quedaría la RAM? 100Kbs


                        
Garbage collector
System.gc();        <<        PROHIBIDO EN JAVA 




Programa en C   (mucho más eficiente en cuanto a la gestión de la RAM)                        JAVA (más sencillo y más productivo)
    Reservar un trozo de RAM    ---    malloc                                       <<<<<<      No se hace
    Poner lo que quiera en la RAM
    Sobreescribirlo si me interesa                                                  <<<<<<<     No se puede
    Leerlo las veces que necesite
    Al finalizar tendria YO como desarrollador que Liberar ese espacio de memoria.  <<<<<<      La hace el GC (con cierta periodicidad / cuando la memoria se va llenando)
                                                                                                Es un proceso pesado (hay 2 tipos)

Quien crea las conexiones con MariaDB o la base de datos que sea?
    Weblogic / O el servidor de apps de turno
    
Quien REALMENTE crea las conexiones con MariaDB o la base de datos que sea?
    Driver de base datos
    
Para cada BBDD que quiera utilizar necesito un driver de base de datos

Ese driver en que lenguaje está desarrollado? JAVA
Como me lo van a dar ese programa: .jar   <<<<<< Que viene ahí dentro?
    Librerias / Driver.... eso es compuesto de?
    Tenemos un ZIP (jar) ... ahi dentro vamos tener el que ?
        Una estructura de carpetas con archivos .class   
        
        De entro los MUCHOS archivos que habrá allí dentro, SOLO 1 es el que Weblogic debe utilizar
        Driver Class Name


En Weblogic tenemos que configurar la CADENA DE CONEXION a la base de datos:
URL
protocolo: maquina : puerto / base de datos
jdbc(dialecto)://maquina:3306/testDB
Weblogic construye esta URL pero SOLO para bases de datos que el conozca de antemano




----------------

# Conexiones a la base de datos

Son gestionadas a través de Weblogic... que internamente usa un driver especifico para cada BBDD

## Cada vez que un usuario de nuestra apliación (la que tenemos en weblogic) necesita una coexión a la BBDD, weblogic crea una?

No... esto se gestiona a través de un pool de conexiones, esto es:
- Un conjunto de conexiones preestablecido (aunque dinámico) que nuestro usuarios (thread... ejecutor) usarán para comunicarse con la BBDD.


## Que implica abrir una nueva conexión a una base de datos?
Esto implica un coste tanto a nivel de Weblogic como a nivel de BBDD <<< La peor parte se la lleva la BBDD






Usuarios >>>> Navegador    >>>>>  APP   >>> Respuesta al usuario
                                | + Weblogic atender la petición http(s)
                                |    > La petición que hace un usuario es pasada a través de una cola a un determinado ejecutor (Thread)
                                |    > Esos hilos (ejecutores) se obtienen de un poll de ejecutores (poll de hilos)
                                |    > Ese poll esstá predefinido (aunque es dinámico)
                                
                                        ____________________________________________  Ratio Cuantas conexiones necesitas por thread
                                        V                                          V
        >>>>     Weblogic           THREADS                                       BBDD                  |       Servidor BBDD
Ivan                 |                 E1                       |                  C1       >>>>        |           Ejecutores - Procesos a nivel de SO
Iñaki                |___              E2                       |___               C2       >>>>        |
Jose Manuel          Dispatcher        E3      >>>>>            Dispatcher         C3       >>>>        |
Eva                  |---              E4                       |---                                            Servicio BBDD (proceso a nivel de SO)



Al configurar el poll de conexiones a BBDD en Weblogic, estará influenciado por:
    - En función del número de ejecutores que tenga (THREADS)
    - El tiempo empleado por esos ejecutores total y en acceder a BBDD   // Naturaleza de las operaciones que se hacen en la app.
A su vez... tods estos datos (# ejecutores - # conexiones) están limitados a los recursos de mi máquina    

Saber Un determenidao servidor que ye levante: Cuanta RAM - CPU - Para atender un determinado numero X de peticiones (Ejecutores, Coneciones)
    Cuando necesite procesar más peticiones: ESCALAR... más servidores 


Despues de realizar 10000 operaciones, hemos tardado de media 400 ms por petición    |
Despues de realizar 10000 operaciones, los hilos han usado de media 100 ms de bbdd   |   100/400 = 25% del tiempo del ejecutor es empleado en BBDD de media
      VVVVVVVVV
    MONITORIZACION
    
    
Si tengo 200 ejecutores... cuantas conexiones necesito a BBDD? 50+(10%-15%) extras

Que pasa si configuro un número de conexiones a BBDD Mucho más grande del que necesito? Eso es un problema?
    Innecesario (Muchas conexiones que no se usen...) Ni siquiera se abren
    Abre entre 20 y 200 conexiones
     A priori parece que no es un problema... Hasta que venga un pico de carga. Si en un instante T entran 180 peticiones, se genera cola?
        No... se abren más coexiones... Abrir las conexiones tendrá un coste...> Tiempo 0.5-2 seg
        Si le abro demasiadas xonexiones a la BBDD la puedo petar... y entonces cuantas peticiones atiendo: CERO !!!!
Que pasa si abro un número más pequeño de conexiones del que necesito?
    Cola que se va a ir poniendo muy grande.... llegara a infinito TIMEOUTS

E1 ----> Analizarla la petición HTTP que se está recibiendo (CPU / RAM)           50ms
    ---> Query a BBDD                                       (-Sleep, cafe-)      100ms
     --> Componer un HTML                                   (CPU / RAM)          150ms
      -> Mandar el HTML por la red                          (RED...)              50ms
                                                    -------------------------
                                                        400 ms                     25% del tiempo en BBDD
                  |          |        |
                  V          V        V
       100ms    200ms    300ms     400ms   500ms                                                     
E1   >*****++++++++++********************<*****++++++++++********************<*****++++++++++********************<*****++++++++++********************<
E2          >*****   ++++++++++********************<*****++++++++++********************<*****++++++++++********************<*****++++++++++********************<
E3    >*****                   +++++++++++********************<*****++++++++++********************<*****++++++++++********************<*****++++++++++********************<
E4                   >*****               ++++++++++********************< *****++++++++++********************<*****++++++++++********************<*****++++++++++********************<

1 conexion a BBDD



Memoria JAVA  >>>>>     minimo/inicial memoria     ---    maximo de memoria      <<<<<<      Inicial = maximo   (RECOMENDACION)
----
App (se usa de dia)             2Gb - 4Gb      6Gb RAM
App (que se usa de noche)       2Gb - 4Gb
---
100 usuario   ---- App A    
              ---- App B



El servidor de BBDD va a ofrecer un nñumero máximo de conexiones global --- 200 conexiones entre todo el mundo
    App 1  ---- 50-70
    App 2  ---- 100-120
    App 3  ---- 25-50




Que pasa si tengo una máquina / servidor... que está al:    

ESCENARIO 1.... Esta guay o es RUINA? GUAY
    CPU: 60%
    RAM: 60%
    Presion de disco: 60%
    Aprovechamiento de recursos: BUENO !!!!
    Capacidad de absorción de trabajo: BUENA !!!!
    
ESCENARIO 2.... Esta guay o es RUINA?  RUINA
    CPU: 90%
    RAM: 90%
    Presion de disco: 90%
    
    Aprovechamiento de recursos: GENIAL !!!!
    Capacidad de absorción de trabajo: MUY MALA !!!!   <<< Problema? NO
        Si viene más trabajo: Escalo (para eso está un cluster)
    HA: Que pasa si se cae esta máquina? Donde va ese 90% de trabajo que se está realizando... Son capaces de asumirlo?

ESCENARIO 3.... Esta guay o es RUINA? 
    CPU: 30%
    RAM: 60% + RAM
    Presion de disco: 60%
    
    Sistema desbalanceado en su configuración: Tengo más CPU que la que necesito en función de la RAM que me has dado
    

En el caso de añadir un hierro extra al cluster    
    1 Servidor 16 Gbs de RAM JAVA y 4 cores.... -----> 10  Gb libres para operar
    2 Servidores 8 Gbs RAM JAVA y 2 Cores       -----> 2 Gbs libres x 2 Maquinas= 4 Gbs libres para operar
    
1 unica aplicación

RAM: App:
    CACHE : PUEDE ocupar un monton !!!! MONTON !!! 6 Gbs    <<<<<<    Linea base de uso de memoria   < Cache
    

Como funciona una app en cluster      <<<<<




                                            StickySessions                                      INSTANCIAS
Cliente: Manolo             >>>>>           Balanceador      >>>>>>             Nodo 1 - Servidor Weblogic - App   XXXX
                                                                                            Datos asociados a la sesión de manolo   XXXX
                                                                                Nodo 2 - Servidor Weblogic - App
                                                                                            En ese ordenador ... en su RAM estarian los datos de Manolo
                                                                                Nodo 3 - Servidor Weblogic - App

Weblogic: Tener una sesión distribuida entre los servidores

Que es una sesión  <<<<  JEE <<<<< La funcionalidad de replicar las sesiones en servidores
    Tiene un identificador  >>> Se le hace llegar a Manolo: Cookie
    Un espacio de almacenamiento en RAM disponible para un usuario/conexión


Servidores de app de clase web              - TOMCAT
Servidores de apss de clase empresarial     - WEBLOGIC - WAS


25% CAPACIDAD Me la juego a que se caigan el 75% Nodos sería capaz de seguir trabajando
La replicacion la tengo que hacer en el 75% de los servidores

Independientemente de lo que haya configurado o no el desarrollador, se hace persistencia de SESION: Oracle Coherence

Spring
Hibernate


Timeout de sesión: Cuenta desde la ultima vez que el usuario conecto: 30 minutos:
        Si el usuario conecta a los 29 minutos... tiene otros 30 disponibles.
        
        
Queries y JAVA

Statement: QUERY 
En java existe un tipo de Query Especial PreparedStatements ~ Dentro de una BBDD un procedimiento almacenado

QUERY --- SQL ---> Analisis sintactico de la QUERY... y extraer los componentes principales de ese texto <<<< Parser SQL
              ---> Analizar la mejor forma de ejecutar esa query. Optimozadores de ejecución de las query -> Planes de ejecución
              
              
Cluster Weblogic
AdminServer 
    /console
    API de Weblogic
    

El puerto de administracion se abre en todos los servidores de weblogic: 9002


El puerto 7001 es el puerto con el que conectar con cada servidor de weblogic por http
El puerto 7002 es el puerto con el que conectar con cada servidor de weblogic por https


AdminServer
    7001
    7002
    /console
    
Worker1
    7001
    7002
    
Worker2
    7001
    7002
    /app1
    
    
    
    http://IPWORKER1:7001/app1
    https://IPWORKER1:7002/app1
    http://IPADMINSERVER:7001/console
    √ OPCIONALMENTE https://ANY_IP:9002/console

