# Importando os módulos corretamente
from TextoAulas import letrasEfonemas, encontros_vocalicos, encontros_consonantais, digrafos, silaba_tonica, hifen, consonantalXdigrafo, substantivos

# from TextoAulas import

print('Gramática Portuguesa')
nome = input('Qual é o seu nome? ')


# Função para continuar ou não
def continuar():
    cont = str(input('Quer continuar? [S/N] R-> '))
    
    if cont in 'Ss':
        return True
    elif cont in 'Nn':
        return False




while True:
    opcao_escolhida = int(input(f"""
    ------------------------------------
        Sr(a) {nome} escolha um módulo.
        [1] Letras e Fonemas
        [2] Encontros Vocálicos
        [3] Encontros Consonantais
        [4] Dígrafos
        [5] ConsonantalXdígrafo
        [6] Sílaba Tônica
        [7] Hífen
        [8] Substantivos
        [9] Verbos
    ------------------------------------
    R-> """))
    while True:
        if opcao_escolhida == 1:
            print(letrasEfonemas["letra"])
            print(letrasEfonemas['inicio'])

            cont = continuar()
        
            print(letrasEfonemas['vogais'])
            cont = continuar()
            
            print(letrasEfonemas['consoantes'])

            cont = continuar()
            
            print(letrasEfonemas['semivogais'])
            exe = input(letrasEfonemas['exercicio01']).upper()

            if exe == 'OA':
                print('Resposta correta!')

                cont = continuar()
                
                exe = letrasEfonemas['exercicio02']
                print(exe)
                ex = input('R->').upper()

                if ex == 'JNL':
                    print('Resposta correta!')

                    cont = continuar()
                    
                    exe = letrasEfonemas['exercicio03']
                    print(exe)
                    ex = input('R->').upper()

                    if ex == 'IU':
                        print('Resposta correta!')
                        print(f'\033[0;32mParabéns Sr(a) {nome}! Você concluiu esse módulo.\033[m')
                        break
                                     
                    else:
                        print('Resposta errada!')
                        break
                else:
                    print('Resposta errada!')
                    break
            else:
                print('Resposta errada!')
                break
            

        elif opcao_escolhida == 2:
            print(f'''\nSr(a) \033[0;33m{nome}\033[m, iniciaremos os estudos sobre:\n
                Encontros vocálicos''')
            print(encontros_vocalicos['enc_voc'])
            cont = continuar()
            
            print(encontros_vocalicos['oral'])
            cont = continuar()
            
            print(encontros_vocalicos['tritongo'])
            cont = continuar()
            
            print(encontros_vocalicos['hiato'])
            cont = continuar()
            
            exe = input(encontros_vocalicos['exe01']).upper()

            if exe == 'AEA':
                print('Resposta correta!')
                cont = continuar()
                
                exe = input(encontros_vocalicos['exe02']).upper()

                if exe == 'UMA':
                    print('Resposta correta')
                    print(f'\033[0;32mParabéns sr(a){nome}! Você concluiu esse módulo.\033[m')
                    break
                else:
                    print('\033[0;31mResposta errada!\033[m')
                    break
                        
            else:
                print('\033[0;31mResposta errada!\033[m')
                break


        elif opcao_escolhida == 3:
            print(encontros_consonantais["enc_con"])
            cont = continuar()
            
            exercicio = input(encontros_consonantais['exe01']).upper()
            if exercicio in "VDRPLNFLRPSCLGPN":
                print('\033[0;32mResposta correta! Você concluiu esse módulo.\033[m')
                break
            else:
                print('Resposta errada!')
                break
          

        elif opcao_escolhida == 4:
            print(digrafos['inicio'])
            cont = continuar()
            
            print(digrafos['digrafos_consonantais'])
            cont = continuar()
            
            print(digrafos['digrafos_vocálicos'])
            cont = continuar()
            
            exercicio = input(digrafos['exe01']).upper()
            if exercicio in 'XCSÇRR':
                print('\033[0;33mResposta Correta!\033[m')
                cont = continuar()
                
                exercicio = input(digrafos['exe02']).upper()
                if exercicio in 'UMUNOM':
                    print(f'\033[0;32mParabéns sr(a){nome}! Você terminou esse módulo.\033[m')
                    break
                else:
                    print('\033[0;31mResposta errada!\033[m')
                    break
            else:
                print('\033[0;31mResposta errada!\033[m')
                break


        elif opcao_escolhida == 5:
            print(consonantalXdigrafo["encontro_consonantal"])
            cont = continuar()
            
            exe = input(consonantalXdigrafo["exe01"]).upper()
            if exe == "FVVV":
                print('\033[0;33mVocê acertou, parabéns!\033[m')
                cont = continuar()
                
                print(consonantalXdigrafo["digrafo"])
                cont = continuar()
                
                exe = input(consonantalXdigrafo['exe02']).lower()
                if exe in "chexmpgrndfrng":
                    print('\033[0;33mResposta correta!\033[m')
                    cont = continuar()
                    
                    print(consonantalXdigrafo["consonatalXdigrafo"])
                    cont = continuar()
                    
                    exe = input(consonantalXdigrafo["exe03"]).upper()
                    if exe == 'VV':
                        print('Resposta correta!')
                        print(f'\033[0;32mParabens {nome} Você terminou o curso\033[m')
                        break
                    else:
                        print('\033[0;31mResposta errada!\033[m')
                        break           
                else:
                    print('\033[0;31mResposta errada!\033[m')
                    break             
            else:
                print('\033[0;31mResposta errada!\033[m')
                break


        elif opcao_escolhida == 6:
            print(silaba_tonica['inicio'])
            cont = input('Quer continuar? [S] [N] R->')
            
            print(silaba_tonica['proparoxitonas'])
            cont = input('Quer continuar? [S] [N] R->')
            
            exe = input(silaba_tonica['exe01']).upper()
            if exe in 'IAAOOI':
                print('Resposta Correta!')
                cont = input('Quer continuar? [S] [N] R->')
                
                print(silaba_tonica['paroxitonas'])
                exe = input(silaba_tonica["exe02"]).upper()
                if exe in 'EAIIAA':
                    print('Resposta correta')
                    print(f'\033[0;32mParabéns sr(a){nome}, você concluiu esse módulo.\033[m ')
                    break
                else:
                    print('\033[0;31mResposta errada!\033[m')
                    break
            else:
                print('\033[0;31mResposta errada!\033[m')
                break


        elif opcao_escolhida == 7:
            print(hifen['hifen'])
            cont = continuar()
            
            exe01 = input(hifen['exe01']).upper()
            if exe01 == 'VVF':
                print('Resposta correta!')
                print("""
                    # a) Correto: Amor-de-mãe (ligação entre elementos)
                    # b) Correto: Agora-ou-nunca (ligação entre elementos)
                    # c) Incorreto: Infelizmente (não requer hífen)""")
                cont = continuar()
                
                exe02 = input(hifen['exe02'])
                if exe02 in ['trar-te-ei', 'mos-trou', 'con-taram']:
                    print('Resposta correta!')
                    cont = continuar()
                    
                    print(hifen["usa_hifen"])
                    exe03 = input(hifen['exe03']).upper()
                    if exe03 == 'VVV':
                        print('Resposta correta!')
                        cont = continuar()
                        
                        exe04 = input(hifen['exe04']).upper()
                        if exe04 in 'FFF':
                            print('Resposta correta!')
                            cont = continuar()
                            
                            exe05 = input(hifen['exe05'])
                            if exe05 in ['Rio-mineiro', 'São-paulino', 'Belo-horizontino']:
                                print('Resposta correta!')
                                cont = continuar()
                                
                                print(hifen['não_hifen'])
                                cont = continuar()
                                
                                exe06 = input(hifen['exe06'])
                                if exe06 in 'Bb':
                                    print('Resposta correta!')
                                    cont = continuar()
                                    #
                                    exe07 = input(hifen['exe07'])
                                    if exe07 in ['Pontapé', 'Girassol', 'Infraestrutura']:
                                        print('Resposta correta!')
                                        cont = continuar()
                                        
                                        print(hifen['observações'])
                                        exe08 = input(hifen['exe08']).upper()
                                        if exe08 in 'FVF':
                                            print('Resposta correta!')
                                            cont = continuar()
                                            
                                            exe09 = input(hifen['exe09'])
                                            if exe09 in ['Bem-bom','Sub-Região','Bem-educada']:
                                                print(f'\033[0;32mParabéns Sr(a){nome}, você concluiu esse módulo.\033[m')
                                                break
                                                                           
                                        else:
                                            print('\033[0;31mResposta errada!\033[m')
                                            break
                                else:
                                    print('\033[0;31mResposta errada!\033[m')
                                    break
                        else:
                            print('\033[0;31mResposta errada!\033[m')
                            break
                else:
                    print('\033[0;31mResposta errada!\033[m')
                    break


        elif opcao_escolhida == 8:
            print(substantivos['inicio'])
            cont = continuar()
            
            print(substantivos['ConcretosOuAbstratos'])
            cont = continuar()
            
            print(substantivos['ComunsOuProprios'])
            cont = continuar()
            
            print(substantivos['SimplesOuCompostos'])
            cont = continuar()
            
            print(substantivos['PrimitivosOuDerivados'])
            cont = continuar()
            
            print(substantivos['SubstantivosColetivos'])
            cont = continuar()
            
            print('Resolva os exercícios:')
            resp = input(substantivos["Identificacao"]).upper()
            if resp == 'ACACA':
                print('resposta correta!')
                print(substantivos['ind_resp'])
                cont = continuar()
                
                resp = input(substantivos["Classificacao"]).upper()
                if resp == 'CPCPC':
                    print('Resposta correta!')
                    print(substantivos['class_exe'])
                    cont = continuar()
                    
                    resp = input(substantivos["FormacaoPalavras"]).upper()
                    if resp == 'CSCCS':
                        print('Resposta correta!')
                        print(substantivos['for_exe'])
                        cont = continuar()
                        
                        resp = input(substantivos['Derivacao']).upper()
                        if resp == 'DPDDDP':
                            print('Resposta correta!')
                            print(substantivos["der_exe"])
                            cont = continuar()
                            
                            resp = input(substantivos['Sub_col']).upper()
                            if resp == '54321':
                                print('Resposta correta!')
                                print(substantivos['sub_exe'])  

                                print(f'\033[0;32mParabéns sr(a){nome}, Você terminou esse módulo.\033[m')
                                break
                            else:
                                print('\033[0;31mResposta errada!\033[m')
                                break
                        else:
                            print('\033[0;31mResposta errada!\033[m')
                            break
                    else:
                        print('\033[0;31mResposta errada!\033[m')
                        break
                else:
                    print('\033[0;31mResposta errada!\033[m')
                    break
            else:
                print('\033[0;31mResposta errada!\033[m')
                break
                                                


        else:
            print("--------------------------------------------------------------------")
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3, 4, 5).")
            print("--------------------------------------------------------------------")
            break
