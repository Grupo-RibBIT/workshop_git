palavras_possívei = [ "tamandua"]

palavra = input("Digite uma palavra: ")



#teste teste test teste
<<<<<<< HEAD
#deve dar conflito com oque vc escreveu
=======
#outro teste kkkk
>>>>>>> 334f3db0f0ff6b0e6439589695a5e4bc9c54ae2f

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