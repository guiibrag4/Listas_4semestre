import asyncio
import websockets

# O python inicializa um conjunto vazio de conexoes
conexao_clientes = set()

# Quando um cliente estabelece uma conexão utiliza dessa função, de forma assíncrona
async def responder_Cliente(websocket, endereco):
  conexao_clientes.add(websocket)
  try: 
    async for mensagem in websocket:
      print (mensagem)
      for clientes in conexao_clientes:
        if(clientes != websocket):
          await clientes.send(f"{mensagem}")
  except Exception as e:
    print(f"Erro ao processar mensagem: {e}")
# No finally do try catch, ele garante obrigatoriamente que o que ta dentro de finally será executado.
  finally:
    conexao_clientes.remove(websocket)
    
async def main():
  async with websockets.serve(responder_Cliente, '0.0.0.0', 80):
    print("Servidor rodando")
    # Para conexão ficar estabelecida e não encerrar na primeira vez
    await asyncio.Future()

asyncio.run(main())
    