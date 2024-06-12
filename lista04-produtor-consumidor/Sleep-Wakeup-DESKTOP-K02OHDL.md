# Soluções de dormir e acordar

Essencialmente, um processo é colocado para dormir quando a região crítica está ocupada. Analogia: Se o banheiro ta ocupado, o cliente que queria usar é colocado para dormir, no momento que o banheiro é desocupado, esse cliente é acordado para usá-lo.

* Um a chamada para o processo dormir e uma chamada para ele acordar.

## Revisão exclusão mútua

p1 & p2 } recurso compartilhado

Se o p1 já ta na RC (região crítica), então o p2 não deverá entrar.

## Soluções com Dormir/ Acordar

* par de primitivas - Sleep e Wake-up - é utilizado.

* São chamadas ao sistema para bloqueio e desbloqueio de processos

* Sleep bloqueia o processo que a chamou.

* Suspende a execução até que outro processo o acorde.

* A primitiva Wake-up "acorda" um determinado processo, evitando espera-ocupada.

Então, qual a principal diferença entre o sleep-wakeUp com espera-ocupada?

* Ao invés do p1 verificar se a RC está cheia constantemente (igual no espera-ocupada), o p1 é colocado para dormir, ou seja, ele fica desativado. o p1 não fica consultando a RC o tempo todo, pois quando o processo p2 finalizar, ele envia um sinal de "acorda" para o p1.

## Problema do Consumidor e Produtor

* Dois processos compartilham um buffer de tamanho fixo.

* O processo produtor coloca os dados no buffer 

* Consumidor retira dados do buffer.

_Problema:_ O produtor deseja colocar dados e o buffer está cheio; enquanto o consumidor deseja retirar dados quando o buffer está vazio.

### Solução

1. Colocar os processos para "dormir", até que eles possam ser executados;

2. Produtor colocado para dormir, quando o buffer estiver cheio;

3. Consumidor colocado para dormir, quando o buffer estiver vazio;

### Implementando

Buffer
* Uma variável count controla a quantidade de dados presente no buffer.

Produtor
* Antes de colocar dados no buffer, o produtor checa o valor de count.
* if count == cheio, processo-produtor == sleep
* if count != cheio, processo-produtor Wake-up, count ++ (produtor coloca dados no buffer e incrementa count)

Consumidor

* Antes de retirar dados no buffer, checa se count == 0; if count == 0, processo-consumidor == sleep
* If count != 0, processo-consumidor == Wake-up




