connect("admin","password1","localhost:7001")

print "El nombre de mi servidor es:" + cmo.getServers()[0].getName()

print ("El puerto de mi servidor es:" + str(cmo.getServers()[0].getListenPort()))
