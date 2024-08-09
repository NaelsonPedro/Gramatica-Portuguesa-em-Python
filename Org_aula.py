# Importando os módulos corretamente
from Texto_aula import letrasEfonemas, encontros_vocalicos, encontros_consonantais, digrafos, silaba_tonica, hifen, consonantalXdigrafo, substantivos, Verbos
# from TextoAulas import

print('Gramática Portuguesa')
nome = input('Qual é o seu nome? ')

#   Areas especiais!
def cont():
    conti = input('Quer continuar? [S/N] R->')
    if conti in 'Ss':
        return True
    elif conti in 'Nn':
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
    ------------------------------------
    R-> """))
    while True:
        if opcao_escolhida == 1:
            print(letrasEfonemas["letra"])
            print(letrasEfonemas['inicio'])

            continuar = cont()
            if continuar:
                print(letrasEfonemas['vogais'])
                continuar = cont()
                if continuar:
                    print(letrasEfonemas['consoantes'])

                    continuar = cont()
                    if continuar:
                        print(letrasEfonemas['semivogais'])
                        exe = input(letrasEfonemas['exercicio01']).upper()

                        if exe == 'IO':
                            print('Resposta correta!')

                            continuar = cont()
                            if continuar:
                                exe = letrasEfonemas['exercicio02']
                                print(exe)
                                ex = input('R->').upper()

                                if ex == 'JNL':
                                    print('Resposta correta!')

                                    continuar = cont()
                                    if continuar:
                                        exe = letrasEfonemas['exercicio03']
                                        print(exe)
                                        ex = input('R->').upper()

                                        if ex == 'IU':
                                            print('Resposta correta!')
                                            print(f'\033[0;32mParabéns Sr(a) {nome}! Você concluiu esse módulo.\033[m')
                                            break
                                        else:
                                            break
                                    else:
                                        break
                                else:
                                    break
                            else:
                                break
                        else:
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
            cont = input('Quer continuar? [S/N] R->')
            if cont in 'Ss':
                print(encontros_vocalicos['oral'])
                cont = input('Quer continuar? [S/N] R->')
                if cont in 'Ss':
                    print(encontros_vocalicos['tritongo'])
                    cont = input('Quer continuar? [S/N] R->')
                    if cont in 'Ss':
                        print(encontros_vocalicos['hiato'])
                        cont = input('Quer continuar? [S/N] R->')
                        if cont in 'Ss':
                            exe = input(encontros_vocalicos['exe01']).upper()

                            if exe == 'AEA':
                                print('Resposta correta!')
                                cont = input('Quer continuar? [S/N] R->')
                                if cont in 'Ss':
                                    exe = input(encontros_vocalicos['exe02']).upper()

                                    if exe == 'UMA':
                                        print('Resposta correta')
                                        print(f'\033[0;32mParabéns sr(a){nome}! Você concluiu esse módulo.\033[m')
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

        elif opcao_escolhida == 3:
            print(encontros_consonantais["enc_con"])
            cont = input('Quer continuar? [S/N] R->')
            if cont in 'Ss':
                exercicio = input(encontros_consonantais['exe01']).upper()
                if exercicio in "VDRPLNFLRPSCLGPN":
                    print('\033[0;32mResposta correta! Você concluiu esse módulo.\033[m')
                    break
                else:
                    print('Resposta errada!')
                    break
            else:
                print('Resposta errada!')
                break

        elif opcao_escolhida == 4:
            print(digrafos['inicio'])
            cont = input('Quer continuar? [S/N] R->')
            if cont in 'Ss':
                print(digrafos['digrafos_consonantais'])
                cont = input('Quer continuar? [S/N] R->')
                if cont in 'Ss':
                    print(digrafos['digrafos_vocálicos'])
                    cont = input('Quer continuar? [S/N] R->')
                    if cont in 'Ss':
                        exercicio = input(digrafos['exe01']).upper()
                        if exercicio in 'XCSÇRR':
                            print('\033[0;33mResposta Correta!\033[m')
                            cont = input('Quer continuar? [S/N] R->')
                            if cont in 'Ss':
                                exercicio = input(digrafos['exe02']).upper()
                                if exercicio in 'UMUNOM':
                                    print(f'\033[0;32mParabéns sr(a){nome}! Você terminou esse módulo.\033[m')
                                    break
            else:
                print('Resposta Errada!')
                break

        elif opcao_escolhida == 5:
            print(consonantalXdigrafo["encontro_consonantal"])
            continuar = cont()
            if continuar:
                exe = input(consonantalXdigrafo["exe01"]).upper()
                if exe == "FVVV":
                    print('\033[0;33mVocê acertou, parabéns!\033[m')
                    continuar = cont()
                    if continuar:
                        print(consonantalXdigrafo["digrafo"])
                        continuar = cont()
                        if continuar:
                            exe = input(consonantalXdigrafo['exe02']).lower()
                            if exe in "chexmpgrndfrng":
                                print('\033[0;33mResposta correta!\033[m')
                                continuar = cont()
                                if continuar:
                                    print(consonantalXdigrafo["consonatalXdigrafo"])
                                    continuar = cont()
                                    if continuar:
                                        exe = input(consonantalXdigrafo["exe03"]).upper()
                                        if exe == 'VV':
                                            print('Resposta correta!')
                                            print(f'Parabens {nome} Você terminou o curso')
                                else:
                                    break
                            else:
                                print('Resposta errada!')
                                break
                else:
                    print('\033[0;31mVocê errou! tente novamente!\033[m')
                    break             
            else:
                break


        elif opcao_escolhida == 6:
            print(silaba_tonica['inicio'])
            cont = input('Quer continuar? [S] [N] R->')
            if cont in 'Ss':
                print(silaba_tonica['proparoxitonas'])
                cont = input('Quer continuar? [S] [N] R->')
                if cont in 'Ss':
                    exe = input(silaba_tonica['exe01']).upper()
                    if exe in 'IAAOOI':
                        print('Resposta Correta!')
                        cont = input('Quer continuar? [S] [N] R->')
                        if cont in 'Ss':
                            print(silaba_tonica['paroxitonas'])
                            exe = input(silaba_tonica["exe02"]).upper()
                            if exe in 'EAIIAA':
                                print('Resposta correta')
                                cont = input('Quer continuar? [S] [N] R->')
                            else:
                                print('Resposta errada!')
                                break

        elif opcao_escolhida == 7:
            print(hifen['hifen'])
            cont = input('Quer continuar? [S/N] R->')
            if cont in 'Ss':
                exe01 = input(hifen['exe01']).upper()
                if exe01 == 'VVF':
                    print('Resposta correta!')
                    cont = input('Quer continuar? [S/N] R->')
                    if cont in 'Ss':
                        exe02 = input(hifen['exe02'])
                        if exe02 in ['trar-te-ei', 'mos-trou', 'con-taram']:
                            print('Resposta correta!')
                            cont = input('Quer continuar? [S/N] R->')
                            if cont in 'Ss':
                                print(hifen["usa_hifen"])
                                exe03 = input(hifen['exe03']).upper()
                                if exe03 == 'VVV':
                                    print('Resposta correta!')
                                    cont = input('Quer continuar? [S/N] R->')
                                    if cont in 'Ss':
                                        exe04 = input(hifen['exe04']).upper()
                                        if exe04 in 'FFF':
                                            print('Resposta correta!')
                                            cont = input('Quer continuar? [S/N]')
                                            if cont in 'Ss':
                                                exe05 = input(hifen['exe05'])
                                                if exe05 in ['Rio-mineiro', 'São-paulino', 'Belo-horizontino']:
                                                    print('Resposta correta!')
                                                    cont = input('Quer continuar? [S/N] R->')
                                                    if cont in 'Ss':
                                                        print(hifen['não_hifen'])
                                                        cont = input('Quer continuar? [S/N]')
                                                        if cont in 'Ss':
                                                            exe06 = input(hifen['exe06'])
                                                            if exe in 'Bb':
                                                                print('Resposta correta!')
                                                                cont = input('Quer continuar? [S/N] R->')
                                                                if cont in 'Ss':
                                                                    exe07 = input(hifen['exe07'])
                                                                    if exe07 in ['Pontapé', 'Girassol', 'Infraestrutura']:
                                                                        print('Resposta correta!')
                                                                        cont = input('quer continuar? [S/N] R->')
                                                                        if cont in 'Ss':
                                                                            print(hifen['observações'])
                                                                            exe08 = input(hifen['exe08'])
                                                                            if exe08 in 'FVF':
                                                                                print('Resposta correta!')
                                                                                cont = input('Quer continuar? [S/N] R->')
                                                                                if cont in 'Ss':
                                                                                    exe09 = input(hifen['exe09'])
                                                                                    if exe09 in ['Bem-bom','Sub-Região','Bem-educada']:
                                                                                        print(f'\033[0;32mParabéns Sr(a){nome}, você concluiu esse módulo.\033[m ')
                                                                                    else:
                                                                                        print('Resposta errada!')
                                                                                        break
                                                                            else:
                                                                                print('Resposta errada!')
                                                                                break
                                                                    else:
                                                                        print('Respota errada!')
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
                                else:
                                    print('Resposta errada!')
                                    break
                        else:
                            print('Resposta errada!')
                            break
                else:
                    print('Resposta errada!')
                    break

        elif opcao_escolhida == 8:
            print(substantivos['inicio'])
            cont = input('Quer continuar? [S/N] R->')
            if cont in 'Ss':
                print(substantivos['ConcretosOuAbstratos'])
                cont = input('Quer continuar? [S/N] R->')
                if cont in 'Ss':
                    print(substantivos['ComunsOuProprios'])
                    cont = input('Quer continuar? [S/N] R->')
                    if cont in 'Ss':
                        print(substantivos['SimplesOuCompostos'])
                        cont = input('Quer continuar? [S/N] R->')
                        if cont in 'Ss':
                            print(substantivos['PrimitivosOuDerivados'])
                            cont = input('Quer continuar? [S/N] R->')
                            if cont in 'Ss':
                                print(substantivos['SubstantivosColetivos'])
                                cont = input('Quer continuar? [S/N] R->')
                                if cont in 'Ss':
                                    print('Resolva os exercícios:')
                                    resp = input(substantivos["Identificacao"]).upper()
                                    if resp == 'ACACA':
                                        print('resposta correta!')
                                        print(substantivos['ind_resp'])
                                        cont = input('Quer continuar? [S/N] R->')
                                        if cont in 'Ss':
                                            resp = input(substantivos["Classificacao"]).upper()
                                            if resp == 'CPCPC':
                                                print('Resposta correta!')
                                                print(substantivos['class_exe'])
                                                cont = input('Quer continuar? [S/N] R->')
                                                if cont in 'Ss':
                                                    resp = input(substantivos["FormacaoPalavras"]).upper()
                                                    if resp == 'CSCCS':
                                                        print('Resposta correta!')
                                                        print(substantivos['for_exe'])
                                                        cont = input('Quer continuar? [S/N] R->')
                                                        if cont in 'Ss':
                                                            resp = input(substantivos['Derivacao']).upper()
                                                            if resp == 'DPDDDP':
                                                                print('Resposta correta!')
                                                                print(substantivos["der_exe"])
                                                                cont = input('Quer continuar? [S/N] R->')
                                                                if cont in 'Ss':
                                                                    resp = input(substantivos['Sub_col']).upper()
                                                                    if resp == '54321':
                                                                        print('Resposta correta!')
                                                                        print(substantivos['sub_exe'])  

                                                                        print(f'\033[0;32mParabéns sr(a){nome}, Você terminou esse módulo.\033[m')
                                                                        break
                                                                    else:
                                                                        print('Resposta errada!')
                                                                        break
                                                            else:
                                                                print('Resposta errada! Tente novamente!')
                                                                break
                                                    else:
                                                        print('Resposta errada! Tente novamente!')
                                                        break


                                            else:
                                                print('Respota errada! Tente novamente!')
                                                break

                                    else:
                                        print('Resposta errada! Tente novamente!')
                                        break


        else:
            print("--------------------------------------------------------------------")
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3, 4, 5).")
            print("--------------------------------------------------------------------")
            break
