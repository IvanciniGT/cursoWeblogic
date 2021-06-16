def solicitar_dato (dato, valor_por_defecto, valor_actual):
    if len(valor_actual) == 0 :    
        valor_actual = raw_input( "Dame " + dato + " [" + valor_por_defecto + "]: " )
        if len(valor_actual) == 0 :
            valor_actual=valor_por_defecto
    return valor_actual
    
                                                        # valor por defecto
def super_connect( usuario="" , password="" , server_ip="localhost",  port="7001" , protocolo="t3" ):
    
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
super_connect( usuario="admin" ) # Se solicitaría contarseña por pantalla
#super_connect( usuario="admin" , server_ip="" ) # Se solicitaría contarseña por pantalla y además servidor
                                                # Si no me dan un servidor por pantalla... se toma localhost

# Aqui hariamos muchas cosas !!!