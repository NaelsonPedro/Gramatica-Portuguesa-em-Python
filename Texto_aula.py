letrasEfonemas = {
    "letra": """
    ---------------------------------------------------------------------------------------------------------\n
    \033[0;34mLetra\033[m é o sinal que representa na escrita o sistema sonoro.

    Uma letra pode representar um fonema, mais de um fonema ou pode apenas ajudar na pronúncia de um fonema.
    Sendo assim, o número de letras de uma palavra não será, necessariamente, o número de fonemas.

    \033[0;34mFonema\033[m é a unidade de som.

    Quando produzimos sons, o ar que vem dos pulmões pode passar totalmente pela boca (fonemas orais) ou pela boca
    e pelo nariz (fonemas nasais).
    """,

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "inicio": """Os sons linguísticos classificam-se em \033[0;34mvogais\033[m \033[0;33mconsoantes\033[m e \033[0;31msemivogais\033[m.\n
    -----------------------------------------------------------------------------------------------------------------------------------
    """,

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "vogais": """-\033[0;34mVogais\033[m: São, em lingua portuguesa, o centro da sílaba.
    -São Fonemas produzidos livremente, sem obstrução na boca (boca aberta);
    -Podem ser orais (abertas ou fechadas) ou nasais (indicadas pelo til, 'm', 'n');

    exemplos:
    taxa(oral) / mãe(nasal)
    pé(oral - aberta) / vespa(oral - fechada) / lenda(nasal)
    vida(oral) / lindo(nasal)
    baú(oral) / mundo(nasal)\n
    -----------------------------------------------------------------------------------------------------------------------------------
    """,

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "consoantes": """\033[0;33mConsoantes\033[m: São fonemas marginais, que só aparecem, na sílaba com vogais. 
    -As Consoantes são: B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Z.\n
    -----------------------------------------------------------------------------------------------------------------------------------
    """,

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "semivogais": """-\033[0;31mSemivogais\033[m: Os fonemas /i/ e /u/ são semivogais quando formam uma sílaba com uma vogal.
    -Fonemas com som menos forte do que as vogais;
    -Aparecem sempre com uma vogal na mesma sílaba;
    -Também são semivogais as letras (E/O/M/N/W/Y), pois essas letras podem ter som de I ou U, de acordor com o contexto.

    exemplos:
    VESTIDO
    ves-ti-do  ->Vogais(e,i,o) Não temos semivogais.

    PAIXÃO
    pai-xão    ->Vogais(a,ã), Semivogais(i,o)

    PODEM
    po-dem     ->Vogais(o,e), Semivogais(m)

    SAGUÕES
    sa-guões    ->Vogais(a,õ),Semivogais(u,e)\n
    -----------------------------------------------------------------------------------------------------------------------------------
    """,

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "exercicio01": "Identifique as \033[0;34mvogais\033[m na palavra: Livro R->",

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "exercicio02": "Identifique as \033[0;33mconsoantes\033[m na palavra: Janela",

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "exercicio03": "Identifique as \033[0;31msemivogais\033[m nas palavras: Feira e Seu",

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "nova_sem": "São semivogais: IU(representadas pelas letras I,U,E,O,M,N,W,Y)",

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        "exercicio04": "Indentifique as \033[0;31msemivogais\033[m: \nFaixa - Pouco - Saguões - Mão \nPodem - Hífen - Show - Motoboy"
}

encontros_vocalicos = {
    "enc_voc": """\n
-----------------------------------------------------------------------------------------------------------------------------------

\033[0;32mDitongo\033[m: Encontro de \033[0;34mvogal\033[m e \033[0;31msemivogal\033[m. \n Crescente: \033[0;31msemivogal\033[m + \033[0;34mvogal\033[m. \n Quase(oral) - Tranquilo - Quando(nasal) - água(oral)
\n Decrescente: \033[0;34mvogal\033[m + \033[0;31msemivogal\033[m 
Pai(oral) - Muito - Céu(oral) - hífen(nasal)\n

Obs: em \033[0;33m"am","em" e "en",\033[m no final das palavras, as letras \033[0;31m"m" e "n"\033[m são consideradas semivogais, pois produzem som de "u" e "i".\n
-----------------------------------------------------------------------------------------------------------------------------------
""",

    ##################################################################################################################################

    "oral": """\033[0;36mOral:\033[m na pronúncia, o ar passa apenas passa pela boca. \n Mãe - Cãibra - Põe - Muito - Vejam - Vem - Benzinho \n \033[0;31mObs:\033[m am e em en 
posição final de palavras e en no interior de palavras derivadas são considerados ditongos nasais.\n
-----------------------------------------------------------------------------------------------------------------------------------
""",

    ##################################################################################################################################

    "tritongo": """\033[0;35mTritongo\033[m: Encontro de semivogal + vogal + semivogal. \n Oral: na pronuncia o ar passa apenas pela boca. \n Uruguai - Enxaguei - Quaisquer 
\n Nasal: durante a pronúncia o ar passa pela boca e pelo nariz. \n Saguão - Enxáguam - Quão \n Obs: Palavras como queijo não formam \033[0;35mtritongo\033[m, uma vez que não 
ha presença de três sons vocálicos. Palavras como \033[0;33mmeia\033[m não formam \033[0;35mtritongo\033[m porque os três sons vocálicos não estão na mesma silába.\n
-----------------------------------------------------------------------------------------------------------------------------------
""",

    ##################################################################################################################################

    "hiato": """
\033[0;33mHiato\033[m: encontro de duas \033[0;34mvogais\033[m em sílabas diferentes \n Pais - Baú - Poesia - Saida\n
-----------------------------------------------------------------------------------------------------------------------------------
""",

    ##################################################################################################################################

    "exe01": """
Identifique as vogais crescente nas palavras: Rua - Cárie - Maria
R->""",

    #################################################################################################################################

    "exe02": """
Indentifique as vogais decrescente nas palavras: Mangueira - Amam - Véia
R->""",
}

encontros_consonantais = {
    "enc_con": """
    ----------------------------------------------------------------------------------------------------------
    Agrupamento de consoantes em um vocábulo. \n \033[0;31mobs:\033[m Não ocorre encontro consonantal em palavras como Campo e Lenda, já que 
    as letras \033[0;32mM\33[m e \033[0;32mN\033[m assumem o papel de semivogais, produzindo sons vocálicos.\n
    ----------------------------------------------------------------------------------------------------------""",
    "exe01": "Encontre as \033[0;32mconsoantes\033[m nas palavras: \n Vidro - Plano - Flor - Psicólogo - Pneu \n R->"
}

digrafos = {
    "inicio": """
----------------------------------------------------------------------------------------------------------
\033[0;31mDígrafos\033[m são grupos de letras que representam um único som. \n 
    exemplos:
    \033[0;31mCh\033[muva - Ve\033[0;31mlh\033[mo - Gali\033[0;31mnh\033[ma - Ca\033[0;31mrr\033[mo - \n
    Pa\033[0;31mss\033[mo - Gue\033[0;31mrr\033[ma - \033[0;31mQu\033[milo - Cre\033[0;31msc\033[mer \n 
    De\033[0;31msç\033[ma - E\033[0;31mxc\033[meder - C\033[0;31mam\033[mpo - T\033[0;31mem\033[mpo \n 
    L\033[0;31min\033[mdo - P\033[0;31mom\033[mbo - Mu\033[0;31mnd\033[mo \n
    Obs: AM,AN,EM,EN,IM,IN,OM,ON,UM,UN serve para representar as vogais nasais.
    ----------------------------------------------------------------------------------------------------------""",

    "digrafos_consonantais": """
-----------------------------------------------------------------
\033[0;32mDígrafos consonantais:\033[m CH, GU, LH, NH, QU, RR, SS, SC, SÇ, XC, XS
chave   banho   pássaro
gueto   queijo  descente
alho    carro   cresça
-----------------------------------------------------------------
""",

    "digrafos_vocálicos": """\033[0;33mDígrafos vocálicos ou nasais:\033[m AM, AN, EM, EN, IM, OM, ON, UM, UN, na mesma sílaba no interior da palavra.
campo   tempo   limpo
canto   lenda   lindo
""",

    "exe01": """Indentifique os dígrafos consonantais nas palavras: Exceção - Cresça - Carro
R->""",

    "exe02": """Identifique os dígrafos vocálicos nas palavras: Umbigo - Mundo - Tombo
R->"""
}

consonantalXdigrafo = {
    "encontro_consonantal": """
\033[0;34mEncontro consonantal\033[m é o encontro de consoantes em uma palavra. No encontro consonantal, as 
consoantes são pronunciadas separadamente.

- Encontros consonantais inseparáveis
\033[0;31mpr\033[mato           \033[0;31mcl\033[maro       \033[0;31mps\033[micólogo
a\033[0;31mpr\033[movado        \033[0;31mfl\033[mora       \033[0;31mgn\033[momo

- Encontros consonantais separáveis
pa\033[0;31mst\033[mo           a\033[0;31mpt\033[midão     é\033[0;31mtn\033[mico
cu\033[0;31mrt\033[mo           a\033[0;31mbr\033[mu\033[0;31mpt\033[mo     a\033[0;31mmn\033[mésia
""",
    "digrafo": """
\033[0;34mDígrafo\033[m é a união de duas letras representando um só fonema, ou seja, um único som.

- Dígrafos consonantais
\033[0;31mgu\033[merra          \033[0;31mch\033[mave       gali\033[0;31mnh\033[ma     pá\033[0;31mss\033[maro         cre\033[0;31msç\033[ma      e\033[0;31mxs\033[mudar
\033[0;31mqu\033[meijo          fi\033[0;31mlh\033[mo       ca\033[0;31mrr\033[mo       de\033[0;31msc\033[mer          e\033[0;31mxc\033[meto

- Dígrafo vocálicos
Dígrafo vocálico: \033[0;34ma, e, i, o, u\033[m seguidos de m ou n no interior da palavra e na mesma sílaba.

c\033[0;31mam\033[mpo       t\033[0;31mem\033[mpo       l\033[0;31mim\033[mpo       l\033[0;31mom\033[mbo       ch\033[0;31mum\033[mbo
\033[0;31man\033[mdar       l\033[0;31men\033[mda       l\033[0;31min\033[mdo       t\033[0;31mon\033[mto       m\033[0;31mun\033[mdo

Quando aparecem no final da palavra, não são dígrafos. Exemplos: hifén, amam
""",
    "consonatalXdigrafo": """
\033[0;34mEncontro consonantal:\033[m as duas letras são pronunciadas (dois fonemas)
\033[0;31mfl\033[more\033[0;31mst\033[ma
li\033[0;31mvr\033[mo

Dígrafo: as duas letras produzem um único som (um fonema)
o\033[0;31mlh\033[mo
\033[0;31mon\033[mda

Não é encontro consonantal, já que a letra "n" não é considerada consoante nesse contexto; apenas contribuiu para nasalização da vogal anterior.
""",

    "exe01":"""
\033[0;32mPara cada palavra a seguir, identifique se há encontro consonantal inseparável com (F) ou separável com (V):\033[m
"gramado" [V/F]
"fruta"   [V/F]
"plantação" [V/F]
"transporte" [V/F]
Escreva a sequência correta das regras gramaticais com [V/F]
R->""",


# ////////////////////////////////////////////////
# Identificação de Encontros Consonantais:

# "gramado": Encontro consonantal inseparável (gr + m), porque as consoantes "gr" são pronunciadas juntas.
# "fruta": Encontro consonantal separável (fr + t), pois as consoantes "fr" são pronunciadas separadamente.
# "plantação": Encontro consonantal separável (pl + t), porque as consoantes "pl" são pronunciadas separadamente.
# "transporte": Encontro consonantal separável (tr + ns), pois as consoantes "tr" são pronunciadas separadamente.

# Resposta correta! FVVV

    "exe02":"""
\033[0;32mEncontre e destaque os dígrafos consonantais nas seguintes palavras:\033[m
"chaveiro"
"exemplo"
"grandeza"
"frango"
Digite os digrafos consonantais encontrados nas palavras acima:
\033[0;31mobs:(não utilize virgula ou espaços em branco)\033[m
R->""",


# ////////////////////////////////////////////    
#     Dígrafos Consonantais e Vocálicos:

# Dígrafos consonantais nas palavras:
# "chaveiro" (ch)
# "exemplo" (ex, mp)
# "grandeza" (gr, nd)
# "frango" (fr, ng)
# Dígrafo consonantal: é a união de duas consoantes que representam um único fonema, como "ch" em "chaveiro".
# Dígrafo vocálico: é a união de uma vogal com "m" ou "n" que representa um único fonema, como "am" em "campo".
    
# Resposta correta! R->chexmpgrndfrng

    "exe03":"""
Analise as palavras "chuva" e "canto" quanto à presença de encontros consonantais e dígrafos.

"Chuva" Possui digrafo consonantal? [V/F]
"Canto" É um digrafo vocalico? [V/F]
R->""",

# //////////////////////////////////////////
# Análise de Palavras:

# "chuva": Não possui encontro consonantal nem dígrafo consonantal, apenas a vogal "u" com "v" formando uma semivogal "w".
# "canto": Não possui encontro consonantal nem dígrafo consonantal, apenas a vogal "a" com "n" formando uma nasalização.
# Essas análises mostram como os encontros consonantais e os dígrafos se manifestam em diferentes palavras e como isso afeta a pronúncia e a escrita em português.
# Resposta correta! VV

}

silaba_tonica = {
    "inicio": """\nAs palavras quanto á posição da sílaba tônica.\n
    Classificação  |   Sílaba tônica   |   Exemplos \n
    \033[0;34mProparoxitonas\033[m |   Antepenúltima   |   Sábado, fenômeno \n
    \033[0;33mParoxítonas\033[m    |   Penúltima       |   Janela, caráter \n
    \033[0;31mOxítonas\033[m       |   Última          |   Jacaré, Itu""",

    "proparoxitonas": """TODAS as \033[0;34mproparoxítonas\033[m são acentuadas.\n
    Pêssego     Vírgula     Último\n
    Ótimo       Máximo      Óculos""",

    "exe01": """Quais letras precisam ser acentuadas?:\n
    Principe    Aspero      Rapido\n
    Proximo     Folego      Minimo\n
    R->""",

    "paroxitonas": """Acentuam-se as \033[0;33mparoxitonas\033[m terminadas em. \n
    terminação| \n
    \033[0;32mr\033[m         |açucar, éter, carater   |\033[0;32mã(s)\033[m    ímã, órfãs \n
    \033[0;32mi(s)\033[m      |táxi, lápis, tênis      |\033[0;32mão(s)\033[m   Órfão, órfão \n
              |hífen, próton, Pólen \n                            
        """,

    "exe02": """Quais letras precisam ser acentuadas?:
    Regua    | Lapis   | Uisque
    Virus    | facil   | Alcool
    R->""",

    "oxitonas": """As \033[0;31moxítonas\033[m terminadas em:
    Terminação|  Exemplos
    as(s)     |  Paraná, Cajá
    e(s)      |  Café, Chulé, Você
    o(s)      |  Vovô, vovó, cipó
    em, en    |  também, ninguém, parabéns, armazém
""",

    "exe03": """Quais letras precisam ser acentuadas?:
    Sofa     | Jacare  | Irmaos
    Fregues  | Adeus   | Parabens
    R->""",

    "monossilabos": """Os monossílabos tônicos terminados em:
    Terminação|  Exemplos
    a(s)      |  Pá, Lá, Fá
    e(s)      |  Fá, Lê
    o(s)      |  Nó, Pó, Nós
""",

    "ditongos_abertos": """é, éu, ói tônicos em oxitonas e monossílabas
    Herói
    Anéis
    Céu
    Chapéu
""",

    "i_u": """Quando formam hiato com vogal anterior.
    Baú(ba-ú)
    País(Pa-ís)
    Saí(Sa-í)
    Jacareí(Ja-ca-re-í)

    Exceções:
    -i seguido de nh na sílaba seguinte não é acentuado.
    (rainha, coroinha)
    -u tônico antecedido por um ditongo não é acentuado.
    (feiura, Bocaiuva)

    Itu
    Itu é uma oxítona terminada em U
    Jaú também é uma oxítona, mas tem um hiato.
""",

    'exe_07': 'AAA'
}

hifen = {
    "hifen": """
-------------------------------------------------------------------------------
    HÍFEN
O hífen (-) é usado para:
a) ligar os elementos das palavras compostas:
couver-flor     bem-te-vi

b) unir prefixos a radicais:
ex-marido       pós-graduação

c) Ligar verbos a pronomes oblíquos átonos, quando há ênclise ou mesóclise:
pediram-me      enviar-te-ei

d) Passar de uma linha para outra uma palavra, dividindo-a:
Os candidatos ao proces-        O resultado estará disponível
so seletivo devem acom-         a partir das 10h de segunda-
panhar o Diário Oficial.        -feira.
-------------------------------------------------------------------------------
""",

    "exe01": """Identifique se o uso do hífen está correto nas seguintes palavras compostas:
a) Amor-de-mãe      [V/F]
b) Agora-ou-nunca   [V/F]
c) Infelizmente     [V/F] 

Digite a sequência correta: R->""",

    # a) Correto: Amor-de-mãe (ligação entre elementos)
    # b) Correto: Agora-ou-nunca (ligação entre elementos)
    # c) Incorreto: Infelizmente (não requer hífen)

    "exe02": """
Complete as frases com o verbo e o pronome oblíquo, utilizando o hífen corretamente:
a) Eu _______________ a casa. (trazer)
b) Ela _______________ o livro. (mostrar)
c) Eles _______________ as novidades. (contar)

Qual a sequência correta? R->""",

    # a) Eu trar-te-ei a casa.
    # b) Ela mos-trou o livro.
    # c) Eles con-taram as novidades.

    "usa_hifen": """
------------------------------------------------------------------------------
Usa-se hífen:

1. Após os prefixos: ex, sem, além, aquém, recém, para, vice, pós, pré e pró
ex-marido       para-raios
sem-teto        vice-presidente
além-mar        pós-graduando
aquém-oceano    pré-escola
recém-casado    pró-forma

EXCEÇÕES:
-Na palavra paraquedas e seus derivados, não há hífen;

-Quando a pronúncia dos prefixos pos, pre e pro é atóna:
posfácio, preconceito, prociar

2. Entre vogais iguais:
anti-inflamatório
contra-atacar
micro-ondas

EXCEÇÃO:
-Com os prefixos co e re:
    coordernadora reeleição

3. Entre consoantes iguais:
inter-racial
sub-bibliotecário
super-resistente

4. Antes de apalavra iniciada por H:
super-homem
anti-higiênico
sobre-humano
sub-humano

EXCEÇÕES:
-com os prefixos co, des, in e re:
coerdeiro       inábil
desumano        reabilitar

-com prefixo sub, há duas possibilidades:
o emprego do hífen ou a palavra perde o H se junta ao prefixo:
sub-humano        subumano

5. Palavras composta por justaposição que apresentam uma unidade semântica:
Segunda-feira
Guarda-chuva
Arco-Íris

6. Em palavras compostas devivadas de topônimos:

belo-horizontino
sul-mineiro
pouso-alegrense

7. Em palavras compostas que designam espécies animais e botânicas:
erva-doce
couve-flor
bem-te-vi
pimenta-do-reino
-------------------------------------------------------------------------------
""",

    "exe03": """
Indique se o uso do hífen está correto nas seguintes palavras:
a) Vice-diretor [V/F]
b) Pré-escolar  [V/F]
c) Recém-nascido [V/F]

Digite a sequência correta: R->""",

    # a) Correto: Vice-diretor (após o prefixo "vice")
    # b) Correto: Pré-escolar (após o prefixo "pré")
    # c) Correto: Recém-nascido (após o prefixo "recém")

    "exe04": """
Identifique se as palavras estão corretamente formadas por justaposição ou se precisam de hífen:
a) Segundafeira     [V/F]
b) Guarda chuva     [V/F]
c) Arcoiris         [V/F]

R->""",

    # a) Incorreto: Segundafeira (deve ser "Segunda-feira") [V/F]
    # b) Incorreto: Guarda chuva (deve ser "Guarda-chuva")  [V/F]
    # c) Incorreto: Arcoiris (deve ser "Arco-Íris")         [V/F]

    "exe05": """
Complete as palavras compostas derivadas de topônimos com o hífen correto:
a) Rio-________________ (para um residente do Rio de Janeiro)
b) São-________________ (para um residente de São Paulo)
c) Belo-________________ (para um residente de Belo Horizonte)

R->""",

    # a) Rio-mineiro
    # b) São-paulino
    # c) Belo-horizontino

    "não_hifen": """
-------------------------------------------------------------------------------
Não se usa hífen:

1. Quando o prefixo termina em vogal e a palavra começa com consoante (exceto R e S):
autopeça
seminovo
ultramoderno

2. Quando o prefixo termina em vogal eo segundo elemento começa com R ou S. Nesse caso, duplicam-se essas letras:
antissocial
contrarregra
minissaia

3. Entre vogais diferentes:
autoescola
infraestrutura
semianalfabeto

4. Quando o prefixo termina em consoante, e o segundo elemento começa em vogal:
hiperativo
interestadual
superinteressante

5. Entre palavras que perderam a noção de composição:
girassol
paraquedas
pontapé

6. Em palavras compostas que apresentam elementos de ligação dia a dia
pé de moleque
fim de semana
pão de ló

EXCEÇÕES:
-água-de-colônia, arco-da-velha, cor-de-rosa, mais-que-perfeito, queima-roupa, pé-de-meia;

-espécies botânicas e animais.
-------------------------------------------------------------------------------
""",

    "exe06": """
Indique qual das seguintes palavras compostas está correta de acordo com as regras apresentadas:
a) Ultramoderno
b) Superinteressante
c) Contrarregra
d) Interessante
e) Arco-íris

Qual alternativa é a correta? R->""",

    # Resposta correta: b) Superinteressante
    # Explicação: Nesse caso, o prefixo "super" termina em "r" e a palavra seguinte começa com "i", então não há necessidade de hífen.

    "exe07": """
Complete as seguintes frases com a palavra correta, de acordo com as regras apresentadas:
a) Ele comprou um ________ de chocolate para a festa.
b) O ________ é uma planta muito bonita.
c) A ________ da cidade está em obras.
""",

    # a) Ele comprou um pontapé de chocolate para a festa.
    # Explicação: "Pontapé" é uma palavra composta que perdeu a noção de composição, por isso não leva hífen.
    # b) O girassol é uma planta muito bonita.
    # Explicação: "Girassol" é uma exceção, pois se refere a uma espécie botânica, que não segue as regras de hifenização.
    # c) A infraestrutura da cidade está em obras.
    # Explicação: "Infraestrutura" segue as regras de hifenização entre vogais diferentes.

    "observações": """
-------------------------------------------------------------------------------
Observações:

-Com prefixo sub, usa-se hífen também diante das palavras iniciadas por R:
sub-região

-Com os prefixos circum e pam, usa-se hífen antes de palavras iniciadas por M, N e vogal:
circum-meridiano
circum-navegação
pan-americano

-Com mal, usa-se hífen apenas quando o segundo elemento começar por H, L ou vogal:
maç-humano      mal-limpo       mal-educado
mal-acostumado  mal-estar       mal-olhado

-Com bem, usa-se hífen diante das vogais A, E, I e O e das consoantes B,C,D,F,H,M,N,P,Q,S,T,V:
bem-amado           bem-bom         bem-humorado        bem-querer
bem-educado         bem-casado      bem-merecido        bem-sucedido
bem-intencionado    bem-dotado      bem-nascido         bem-talhado
bem-ordenado        bem-fazer*      bem-posto           bem-vindo

Mas: benfeito, benfeitoria, benfeitor
(segundo o VOLP - Vocabulário Ortográfico da Lingua Portuguesa)
-------------------------------------------------------------------------------
""",

    "exe08": """Determine se as palavras estão corretamente escritas com ou sem hífen de acordo com as regras apresentadas:
a) Malnascido   [V/F]
b) Bem-estar    [V/F]
c) Submarinho   [V/F]

R->""",

    # a) Malnascido - Incorreto. De acordo com as regras, "mal" não requer hífen antes de "n".
    # b) Bem-estar - Correto. O prefixo "bem" exige hífen antes de "e".
    # c) Submarinho - Incorreto. Com o prefixo "sub" diante de palavras iniciadas por R, é necessário usar hífen: submarinho.

    "exe09": """
Preencha as lacunas nas seguintes frases com a palavra correta, de acordo com as regras apresentadas:
a) Ele comprou um ________ na feira.
b) A ________ está localizada no sub-região.
c) Ela é uma pessoa ________.
""",

    # a) Ele comprou um bem-bom na feira. ("Bem" exige hífen antes de vogais.)
    # b) A sub-região está localizada no sub-região. (Com "sub" diante de palavras iniciadas por R, usa-se hífen.)
    # c) Ela é uma pessoa bem-educada. ("Bem" exige hífen antes de consoantes.)
}

substantivos = {
    "inicio": """
    -Palavras que dão nome às coisas (objetos, seres, ações, sentimentos, lugares, etc.)

    celular         professora      corrida
    ansiedade       Minas Gerais

    - São variáveis em gênero, número e grau.

    aluna / aluno
    livro / livros
    carrão / carrinhos

    Os \033[0;34msubstantivos\033[m podem ser:

    - Concretos ou Abstratos;
    - Comuns ou Próprios;
    - Simples ou Compostos;
    - Primitivos ou Derivados;
    - Coletivos.
    """,

        "ConcretosOuAbstratos": """
    Concretos ou Abstratos

    SUBSTANTIVOS                        CONCEITOS                           EXEMPLOS
    Concretos           geralmente designam pessoas, animais, plantas,      cantora / gato / Brasil
                        coisas, lugares, seres fantásticos                  flor / mesa / anjo

    Abstratos           palavra com que se nomeia uma ação, qualidade,      corrida / timidez
                        estado ou sentimento dos seres sem os quais         morte / saudades
                        não poderia existir

    Os \033[0;34msubstantivos concretos\033[m nomeiam seres que têm existência própria, reais ou imaginários.

    - Pessoas, animais, insetos, plantas:
    \033[0;31mMaria\033[m, \033[0;31mirmão\033[m, \033[0;31mprofessora\033[m, \033[0;31mmenino\033[m, \033[0;31mgato\033[m, \033[0;31mcoelho\033[m, \033[0;31mformiga\033[m, \033[0;31mpernilongo\033[m, \033[0;31mmargarida\033[m

    - Coisas, lugares:
    \033[0;31mmesa\033[m, \033[0;31mcomputador\033[m, \033[0;31mlivro\033[m, \033[0;31mSão Paulo\033[m, \033[0;31mescola\033[m, \033[0;31mBrasil\033[m

    - Seres fantásticos
    \033[0;31mfada\033[m, \033[0;31manjo\033[m, \033[0;31mbruxo\033[m, \033[0;31mdeuses\033[m, \033[0;31mdiabo\033[m

    Os \033[0;34msubstantivos abstratos\033[m existem como resultado de ação, de estado, de qualidade.

    - \033[0;34mSubstantivos abstratos \033[m
    derivados de ação: \033[0;31mcorrida\033[m (correr); \033[0;31mbrincadeira\033[m (brincar); \033[0;31msaída\033[m (sair); \033[0;31mbeijo\033[m (beijar).

    \033[0;34mSubstantivos abstratos derivados de estado:\033[m
    \033[0;31mtriste\033[m (triste); \033[0;31memoção\033[m(emocionado).

    - Substantivos abstratos derivados de qualidade:
    \033[0;31mlargura\033[m(largo); \033[0;31mrapidez\033[m(rápido); \033[0;31mgentileza\033[m(gentil); \033[0;31mbeleza\033[m(belo).
    """,

        "ComunsOuProprios": """
    SUBSTANTIVOS        CONCEITOS                                                       EXEMPLOS
    Comuns              nomeiam seres e grupos de seres da mesma \033[0;31mespécie\033[m, que têm       casa, desenho, computador
                        características em comum, \033[0;31mmas\033[m não são tratados como             
                        \033[0;31mindividuais\033[m                                                     

    Próprios            nomeiam serres específicos, de determinada \033[0;31mespécie\033[m(nomes de     Pedro, São Paulo, Minas Gerais
                        pessoas, cidades, estados,\033[0;31metc.\033[m) 
    """,

        "SimplesOuCompostos": """
    SUBSTANTIVOS        CONCEITOS                                       EXEMPLOS
    Simples             são formados por \033[0;31mapenas\033[m um radical              flor, couve, chuva
                        
                  
    Compostos           apresentam mais de \033[0;31mmais\033[m de um radical           beija-flor, couve-flor, guarda-chuva
    """,

        "PrimitivosOuDerivados": """
    SUBSTANTIVOS    CONCEITOS                                                     EXEMPLOS
    Primitivos      Não são formados a partir de outras palavras da língua         barco, pedra,casa

                        
    Derivados       São formados a partir de outras palavras da lingua             embarcação, casebre               
    """,

        "SubstantivosColetivos": """
        -Os \033[0;34msubstantivos coletivos\033[m designam um conjunto ou uma coleção de elementos considerados a sua totalidade.

    Exemplos:
    \033[0;31mfolhagem\033[m(folhas)            \033[0;31mcaravana\033[m(viajantes)
    \033[0;31mCongresso\033[m(parlamentares)    \033[0;31melenco\033[m(atores)
    \033[0;31mcardume\033[m(peixes)""",

    #exercicios
    "Identificacao": """
    1. Identificação de Substantivos:
    Leia as seguintes palavras e diga se são substantivos concretos (C) ou abstratos (A):
    a) Amor        
    b) Cachorro    
    c) Felicidade  
    d) Árvore      
    e) Coragem 

    \033[0;32mHelp: Escreva a resposta juntas com letra maiúsculas ou minúsculas como no exemplo: (caaca)\033[m
    R->""",

    "ind_resp":"""
        # A (Amor é um sentimento, uma qualidade abstrata)
        # C (Cachorro é um ser concreto, um animal)
        # A (Felicidade é um estado emocional, uma abstração)
        # C (Árvore é um ser concreto, um objeto físico)
        # A (Coragem é uma qualidade abstrata, um estado mental)
    """,

    "Classificacao": """
    2. Classificação de Substantivos:
    Classifique os seguintes substantivos como comuns (C) ou próprios (P):
    a) Rio      
    b) Brasil   
    c) Cachorro 
    d) João     
    e) Mar      

    \033[0;32mHelp: Escreva a resposta juntas com letra maiúsculas ou minúsculas como no exemplo: (PCPCPC)\033[m
R->""",

    'class_exe':"""
    # C (Rio é um substantivo comum, não se refere a um nome específico)
    # P (Brasil é um substantivo próprio, refere-se a um país específico)
    # C (Cachorro é um substantivo comum, não se refere a um indivíduo específico)
    # P (João é um substantivo próprio, refere-se a uma pessoa específica)
    # C (Mar é um substantivo comum, não se refere a uma entidade específica)
""",

    "FormacaoPalavras": """
    3. Formação de Palavras:
    Indique se os seguintes substantivos são simples (S) ou compostos (C):
    a) Beija-flor   
    b) Cachorro     
    c) Guarda-chuva  
    d) Couve-flor   
    e) Flor         

    \033[0;32mHelp: Escreva a resposta juntas com letra maiúsculas ou minúsculas como no exemplo: (SCSCSC)\033[m
R->""",

    'for_exe':"""
    # C (Beija-flor é um substantivo composto, formado por duas palavras)
    # S (Cachorro é um substantivo simples, formado por uma única palavra)
    # C (Guarda-chuva é um substantivo composto, formado por duas palavras)
    # C (Couve-flor é um substantivo composto, formado por duas palavras)
    # S (Flor é um substantivo simples, formado por uma única palavra)
""",

    "Derivacao": """
    4. Derivação de Substantivos:
    Encontre a palavra primitiva (P) ou a palavra da qual a palavra derivada (D) foi formada:
    a) Pedreiro    
    b) Casa  
    c) Corrida      
    d) Casebre     
    e) Embarcação  
    f) Barco    

    \033[0;32mHelp: Escreva a resposta juntas com letra maiúsculas ou minúsculas como no exemplo: (PDPDPD)\033[m
    R->""",

    'der_exe':"""
    a) ("Pedreiro" é uma palavra derivada da palavra primitiva "pedra")
    b) (Casa é uma palavra primitiva, não é derivada de outra palavra)
    c) (Corrida é derivada de Correr)
    d) (Casebre é formado a partir da palavra primitiva 'casa')
    e) (Embarcação é formada a partir da palavra primitiva 'barco')
    f) (Barco é uma palavra primitiva, não é derivada de outra palavra)
""",

    "Sub_col": """
    5. Substantivos Coletivos:
    Associe os seguintes substantivos coletivos aos seus respectivos grupos de elementos:
    a) Cardume      1 - Livros
    b) Enxame       2 - Porcos
    c) Ramalhete    3 - Flores
    d) Vara         4 - Abelhas
    e) Biblioteca   5 - Peixes

    \033[0;32mHelp: Escreva os números em sequência correspondente, sem vírgulas ou espaços, como no exemplo: (12345)\033[m
R->""",

    'sub_exe':"""
    # 1 (Cardume se refere a um grupo de peixes)
    # 2 (Enxame se refere a um grupo de abelhas)
    # 3 (Ramalhete se refere a um grupo de flores)
    # 4 (Vara se refere a um grupo de porcos)
    # 5 (Biblioteca se refere a um grupo de livros)
"""
}


Verbos = {
    'verbos_conjugacao':"""

    Verbos são palavras variáveis que podem exprimir ação, estado, fenomeno ou fato situado no tempo.
    ASSUNTOS DESTA AULA
        Conjugações, do verbo, Flexões do verbo, Formas nominais do verbo.
    
        A professora /explicou/ a matéria.
        As professoras /explicaram/ a matéria.
        anotações:
            A palavra sublinhada é um verbo, pois exprime uma ação;
            O verbo vai variar de acordo com as palavras/sujeito;
            explicou = releva que a ação ocorreu no passado.
            
        
        Os estudantes /ficarão/ animados com a notícia.
        O estudante /ficará/ animado com a notícia.
        anotações:
            ficarão = É o verbo e estar no futuro;
            não expressa uma ação, mas sim um estado.
        
        
        Aqui /venta/ muito.
        anotações:
            o verbo ventar não exprime nem ação, nem estado, mas um fenômeno da natureza.
            
            
        Aconteceu um acidente na estrada.
        anotações:
            aconteceu = Indica um fato;
            Está situado no passado.
            
                                
        Conjugações do verbo
            1ª conjugação | -ar | cantar, amar, dançar, brincar
            2ª conjugação | -er | comer, beber, fazer, saber
            3ª conjugação | -ir | sair, partir, sorrir, mentir
        
            
            Obs:
                Verbo "pôr" é conjugado como "er" por vir do antigo verbo "poer";
                Pertence a segunda conjugação;
                Também vale para seus derivados: propor, repor, dispor, compor...
                

""",

    "flexoes":"""
    
    anotações: 
        verbo é a classe de palavra que mais pode se flexionar, não apenas em
        singular em plural, mas também em:
        -Pessoa(1ª, 2ª, 3ª), 
        -Número(singular, plural), 
        Tempo(indicativo, subjuntivo, imperativo), 
        -Voz(ativa, passiva, reflexiva)
        

    Flexão de número e pessoa:
        NÚMERO   | PESSOA   | EXEMPLOS
                    | 1ª pessoa| Eu estudo
        singular | 2ª pessoa| Tu estudas
                    | 3ª pessoa| Ele estuda
                
                    | 1ª pessoa| Nós estudamos
        plural   | 2ª pessoa| Vós estudais
                    | 3ª pessoa| Eles estudam
                
                *Vós vem de você				
				 
    Flexão de modo e tempo:
        MODOS   | 			TEMPOS			 | EXEMPLOS
            In	| Presente					 | Eu viajo
            Di  | Pretérito perfeito         | Eu viajei
            Ca  | Pretérito imperfeito		 | Eu viajava
            Ti  | Pretérito mais-que-perfeito| Eu viajara
            Vo  | Futuro do presente		 | Eu viajarei
                |  Futuro do pretérito		 | Eu viajaria
                        
            Sub	| Presente		 			 | (Que) eu viaje
            Jun	| Pretérito imperfeito		 | (Se) eu viajasse
            Tivo| Futuro		 			 | (Quando) eu viajar
            
            IMPE| Afirmativo				 | Viaje (você)
            RATI| Negativo	 				 | Não viaje (você)
            Vo  |  		 					 | 
            
            anotações:
                    Pretérito imperfeito = Indica algo que ocorria no passado, de forma recorrente;
                    Pretérito mais-que-perfeito = Indica um passado anterior a outro passado;
                    exemplo: tinha/havia viajado
                        Quando /você chegou em casa/ eu já viajara.
                        Quando /você chegou em casa/ eu já tinha viajado.
                
        Futuro do pretérito = Futuro do passado, algo que já tinha planejado, e naquele momento no passado era o futuro;
            
        *O modo Indicativo expressa certezas/fatos, coisas que aconteceram, acontece ou aconteceram;
            O modo Subjtuntivo expressa desejos, possibilidades, coisas que podem ou não acontecer;
            O modo Imperativo expressa ordens, conselho, pedido.
            
                
    Flexão de voz
        VOZ		|EXPLICAÇÃO					EXEMPLOS
        Voz		|O sujeito pratica a ação	|O menino machucou a criança.
        Ativa	 expressa pelo verbo			
        Voz		|O sujeito recebe a ação	|A criança foi machucada pelo menino.
        Passiva	 expressa pelo verbo
        Voz 	|O sujeito pratica e recebe	|A criança machucou-se.
        refle	 a ação expressa pelo
        xiva	 verbo
                
        Observação:
            Quanto à flexão, o verbo pode ser:		
            Regular: flexiona-se de acordo com o modelo comum da conjugação.
                Eu comi, tu comeste, ele comeu
            
            Irregular: flexiona-se de modo diferente do modelo.
                Eu fiz, tu fizeste, ele fez

            Defectivo: não possui certas formas.
                Eu ---, tu colores, ele colore
        
            Abundante: possui mais de uma forma equivalente no particípio.
            Ele tinha /entregado/ a mercadoria. (forma regular - ter/haver)
            A mercadoria foi /entregue/. (forma irregular - ser/estar)""",
            
    
    
    
    
    
    
    
    
    'Formas_nominais_do_verbo':"""

                    estudar		Você terá de estudar bastante.
        INFINITIVO	beber		Locução verbal (auxiliar + infinitivo)
                    dormir
                    estudando	Você anda estudando corretamente.
        GERÚNDIO	bebendo		Locução verbal (auxiliar + gerúndio)
                    dormindo
                    estudando	Eu nunca tinha estudado tanto antes.
        PARTICÍPIO	bebido		Tempo composto (ter + particípio)
                    dormindo	- pretérito mais-que-perfeito
                    
                    
            anotação:
            infinitivo
                Está relacionado a estruturas que expressam o futuro
                    Tempos composto = Quando tem mais de um verbo;
                    Locução verbal = ter de fazer alguma coisa, pois expressa obrigação;
                    verbos = andar e estudar formam uma locução verbal, pois formam mais de um verbo par expressar uma ação.
                    
            Gerúndio
                Expressa algo que está acontecendo, pois o gerúndio está bastante relacionado com o presente.
                
            Particípio
                Expressa o tempo mais-que-perfeito."""
}

 

