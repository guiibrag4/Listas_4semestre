from xmlrpc.server import SimpleXMLRPCServer

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

server = SimpleXMLRPCServer(('localhost', 8000))

server.register_function(somar, 'somar')
server.register_function(subtrair, 'subtrair')
server.register_function(multiplicar, 'multiplicar')
server.register_function(dividir, 'dividir')

print ("Servidor RPC está disponível na porta 8000...")
server.serve_forever()


