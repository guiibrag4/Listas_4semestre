import asyncio
import websockets
import aioconsole

async def iniciar_Cliente(endereco_url):
    async with websockets.connect(endereco_url) as websocket:
        mensagem = ''
        while mensagem.lower() != 'sair':
            mensagem = await aioconsole.ainput("Entre com a mensagem: ")
            if mensagem.lower() != 'sair':
                await websocket.send(mensagem)
                resposta = await websocket.recv()
                print("Resposta: ", resposta)

endereco_servidor = "ws://localhost:80"
asyncio.run(iniciar_Cliente(endereco_servidor))