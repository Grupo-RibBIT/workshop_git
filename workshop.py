palavras_possíveis = ["arroz", "tamandua"]

def forca(palavra):
    sorteio = random.int()
    palavra_sorteada = palavra[sorteio]
    while True:
        chute = int(input("Chute uma letra:"))
        if len(chute) > 1:
            print('Digite apenas uma letra')
        else:
            if chute in palavra_sorteada:
                print("Você achou uma letra!")
                palavra_oculta = ''
                for letra not in palavra_sorteada:
                    palavra_oculta = palavra_sorteada.replace(letra, *)
            print("Status:", palavra_oculta)
    


#Tatu bola
forca(palavras_possívei[1])