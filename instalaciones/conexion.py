from java.io import FileInputStream

def solicitar_dato (dato, valor_por_defecto, valor_actual):
    if len(valor_actual) == 0 :    
        valor_actual = raw_input( "Dame " + dato + " [" + valor_por_defecto + "]: " )
        if len(valor_actual) == 0 :
            valor_actual=valor_por_defecto
    return valor_actual
    
                                                        # valor por defecto
def super_connect( usuario="" , password="" , server_ip="localhost",  port="7001" , protocolo="t3" ):
    
    ## Revisar si se han puesto datos en la llamada al script
    for indice in range(1,len(sys.argv)):
        
        if sys.argv[indice] == "--password" or sys.argv[indice] == "-p":
            password=sys.argv[indice+1]  # Tomo como password el valor del siguiente argumento
    
        elif sys.argv[indice] == "--user" or sys.argv[indice] == "-u":
            usuario=sys.argv[indice+1]  
    
        elif sys.argv[indice] == "--server" or sys.argv[indice] == "-s":
            server_ip=sys.argv[indice+1]  
    
        elif sys.argv[indice] == "--port" or sys.argv[indice] == "-P":
            port=sys.argv[indice+1]  
    
        elif sys.argv[indice] == "--protocol" or sys.argv[indice] == "-t":
            protocolo=sys.argv[indice+1]  
    
        elif sys.argv[indice] == "--connection-properties" or sys.argv[indice] == "-c":
            fichero_parametros=sys.argv[indice+1]  

            fichero = FileInputStream( fichero_parametros )
            propiedades = Properties()
            propiedades.load(fichero)
            
            if propiedades.get("usuario") is not None:
                usuario=propiedades.get("usuario")
            if propiedades.get("password") is not None:
                password=propiedades.get("password")
            if propiedades.get("usuario") is not None:
                usuario=propiedades.get("usuario")
            if propiedades.get("servidor") is not None:
                server_ip=propiedades.get("servidor")
            if propiedades.get("puerto") is not None:
                port=propiedades.get("puerto")


    while True: 
        # Verificar si me han suministrado una contraseña
        # Si no, voy a solicitarla
        while len(usuario) == 0 :    # No tengo contraseña.. No hay caracteres
            usuario = raw_input( "Dame el usuario: " )
        
        while len(password) == 0 :    
            password = raw_input( "Dame la contraseña: " )
        
        server_ip=solicitar_dato("el servidor", "localhost", server_ip)        
        port=solicitar_dato("el puerto", "7001", port)        
        protocolo=solicitar_dato("el protocolo", "t3", protocolo)        
        
        try:                                
            connect( usuario , password , protocolo + "://" + server_ip + ":" + port)
            print("INFO: Conectado correctamente con el servidor")
            return 
        except:
            print("ERROR. No se ha podido conectar con el server. Revise los datos")
            usuario=""
            password=""
            server_ip=""
            port=""
            protocolo=""
            
## Aqui acaba la funcion super_connect    
    
#super_connect( usuario="admin" , password="password1" )
#super_connect( usuario="admin" ) # Se solicitaría contarseña por pantalla
#super_connect( usuario="admin" , server_ip="" ) # Se solicitaría contarseña por pantalla y además servidor
                                                # Si no me dan un servidor por pantalla... se toma localhost


def create_datasource(nombre, jndi, driver, url, usuario, password):
    cd('/')
    nuevoRecurso=cmo.createJDBCSystemResource(nombre)
    
    #    nuevoRecurso.getJDBCResource().setName(nombre)
    
    #    nuevoRecurso.getJDBCResource().getJDBCDataSourceParams().setJNDINames(jarray.array([String(jndi)], String))
        
    #    nuevoRecurso.getJDBCResource().getJDBCDriverParams().setUrl(url)
    #    nuevoRecurso.getJDBCResource().getJDBCDriverParams().setDriverName(driver)
    #    nuevoRecurso.getJDBCResource().getJDBCDriverParams().setPassword(password)
    #    nuevoRecurso.getJDBCResource().getJDBCDriverParams().createProperty('user')
    #    nuevoRecurso.getJDBCResource().getJDBCDriverParams().setUser(usuario)
        
    #    nuevoRecurso.getJDBCResource().getJDBCConnectionPoolParams().setTestTableName('SQL SELECT 1 \n')

    recurso='/JDBCSystemResources/' + nombre + '/JDBCResource/' + nombre
    cd(recurso)
    cmo.setName(nombre)
    
    cd(recurso + '/JDBCDataSourceParams/' + nombre)
    set('JNDINames',jarray.array([String(jndi)], String))
    
    cd(recurso + '/JDBCDriverParams/' + nombre)
    cmo.setUrl(url)
    cmo.setDriverName(driver)
    set('Password', password)
    
    cd(recurso + '/JDBCConnectionPoolParams/' + nombre)
    cmo.setTestTableName('SQL SELECT 1 \n')
    
    cd(recurso + '/JDBCDriverParams/' + nombre + '/Properties/' + nombre)
    cmo.createProperty('user')
    
    cd(recurso + '/JDBCDriverParams/' + nombre + '/Properties/' + nombre + '/Properties/user')
    cmo.setValue(usuario)


#### PROGRAMA: 


super_connect()

# Activar el modo edición
edit()
startEdit()

# Aqui hago cambios !!!
create_datasource("miDatasource1", "jndi/miDatasource", "com.mysql.jdbc.Driver" ,"jdbc:mysql://34.252.101.176:3307/miTestDB","usuario","password")

# Aqui guardo los cambios
save()
activate()

# Me desconecto
disconnect()