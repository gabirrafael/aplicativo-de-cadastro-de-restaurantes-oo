from modelos.restaurantes import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

#Central Perk
restaurante_central_perk = Restaurante('Central Perk', 'Cafeteria')
prato_pave_da_rachel = Prato('Pavê da Rachel', 15.0, 'O pavê de bife original da Rachel Green!')
prato_pave_da_rachel.aplicar_desconto()
bebida_cafe_expresso = Bebida('Expresso Central Perk', 5.0, 'Pequeno')
bebida_cafe_expresso.aplicar_desconto()
restaurante_central_perk.adicionar_no_cardapio(bebida_cafe_expresso)
restaurante_central_perk.adicionar_no_cardapio(prato_pave_da_rachel)

#Outros restaurantes
restaurante_ichiraku = Restaurante('Ichiraku','Japonesa')
restaurante_siri_cascudo = Restaurante('Siri Cascudo', 'Lanche')

def main():
    restaurante_central_perk.exibir_cardapio

if __name__ == '__main__':
    main()