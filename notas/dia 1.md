# Contenedores <<< Imágen de contenedor (Desarrollador o Fabricante)

docker image list         >>> docker images
docker container list     >>> docker ps 

Docker <<< Docker compose


docker login (en concreto esto es por usar una imagen de oracle... si fuera otra no haría falta)
docker pull NOMBRE DE IMAGEN  <<<< descargar una imagen de contenedor en mi maquina

!!!! docker container create \
    -p 8080:7001 -p 8081:9002 \
    -v $PWD:/u01/oracle/properties \
    -e DOMAIN_NAME=base_domain \
    --name miweblogic \
    store/oracle/weblogic:12.2.1.4-dev-200117

!!!! docker start miweblogic

docker logs miweblogic

docker stop miweblogic 

docker restart miweblogic 

docker rm miweblogic

docker system prune --all

----------------------------------------------

docker run \
    -d \
    -p 7001:7001 -p 9002:9002 \
    -v $PWD:/u01/oracle/properties \
    -e DOMAIN_NAME=base_domain \
    --name miweblogic \
    store/oracle/weblogic:12.2.1.4-dev-200117

docker run = docker pull + docker container create + docker start + docker attach

docker inspect miweblogic
docker exec -it miweblogic bash





-------------------------------------------------
# WEBLOGIC

## Dominio

Agrupación lógica de objetos dentro de un cluster de weblogic




Producción:
- Alta disponibilidad:    Tiene que ver con conseguir que mi app o servicio esté funcionando la mayor parte posible del tiempo
- Escalabilidad           Capacidad de adapar el entorno a las necesidades de cada momento

Los resolvemos mediante el concepto de cluster:

                DOMINIO   PRINCIPAL
-----------------------------------------------------------------------------------------------------------------------------                
Maquina 1       Servidor de Weblogic 1-App1
Maquina 2       Servidor de Weblogic 2-App2
                Servidor de Weblogic 3-App3
Maquina 3       Servidor de Weblogic 4-App4
...
Maquina n       Servidor de Weblogic 5-AppN                                                            Sistemas de Mensajería
                IP1: Servidor C1 - AppC                   Cluster1 - AppC - Plantilla de servidor      Conexiones a BBDD
                IP2: Servidor C2 - AppC                   
                IP3: Servidor C3 - AppC                   
                IP4: Servidor C4 - AppC                   
Maquina n+1     IP5: Servidor C5 - AppC


Que IP le doy al cliente?
    Balanceador de carga, que distribuye el trafico entre los servers que haya por detrás.



App 
dia 1 - 10000   Black friday
dia 2 - 20                              <<<<< Cuantos ordenadores 2
dia 10 - 250000  Ciber Monday           <<<<< Cuantos ordenadores 15
dia 50 - 1000

                            Dias normal             Atentado
App emergencias                 0-10                1M

De donde saco esos 15 ordenador: Alquilo por minutos : Amazon AWS, GCL, AZURE, IBM Cloud <<<<< 

4 clusters de Kubernetes 50 maquinas






