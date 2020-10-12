## saudar + solicitar +confirmar
* saudar
  - utter_saudar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm  
    - form{"name":"jogoForm"}
    - form{"name":null} 
    - utter_confirmar_pedido
*confirmar
    - utter_confirmar
    - utter_despedir
    
## saudar+ solicitar + negar
* saudar
  - utter_saudar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm  
    - form{"name":"jogoForm"}
    * negar
    - utter_negar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm
    - form{"name":"null"}
    - utter_confirmar_pedido
*confirmar
    - utter_confirmar
    - utter_despedir
    
## pedido+confirmar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm  
    - form{"name":"jogoForm"}
    - form{"name":null} 
    - utter_confirmar_pedido
*confirmar
    - utter_confirmar
    - utter_despedir
    
    
## solicitar + negar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm  
    - form{"name":"jogoForm"} 
* negar
    - utter_negar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm
    - form{"name":"null"}
    - utter_confirmar_pedido
*confirmar
    - utter_confirmar
    - utter_despedir
 
 ## despedir
* despedir
    - utter_despedir

## saudar+ despedir
* saudar
  - utter_saudar
* despedir
    - utter_despedir
    
## saudar+pedido+negar+negar
* saudar
  - utter_saudar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm  
    - form{"name":"jogoForm"}
    - form{"name":null} 
    - utter_confirmar_pedido
* negar
    - utter_negar
* negar
    - utter_despedir
 
## negar+negar
* negar
    - utter_negar
* negar
   - utter_despedir
   
   
## jogo não encontrado
* saudar
  - utter_saudar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
*jogo_nao_encontrado
    - utter_jogo_nao_encontrado
    - utter_despedir
    
## jogo confirmar+ não+ não encontrado
* saudar
  - utter_saudar
* solicitar
    - utter_solicitar
    - utter_jogos
    - utter_selecionar
* confirmar_pedido
    - jogoForm  
    - form{"name":"jogoForm"}
    - form{"name":null} 
    - utter_confirmar_pedido
* negar
    - utter_negar
*jogo_nao_encontrado
    - utter_jogo_nao_encontrado
    - utter_despedir