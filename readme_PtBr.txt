# Find-Git-List


### **Descrição**
---

> This program searches for a keyword in the title on a GitHub page.

Este programa serve para procurar o nome e ou descrição de uma ferramenta publicada aqui no GitHub e que você favoritou em um arquivo de texto pessoal, o qual contem URLs. O programa irá procurar por esta palavra na `tag title` do URL Note: o programa irá procurar **uma**, e somente **uma**, palavra por vez.

### **Requerimentos**
---

##### Modules:

- [x] colorama (Colored text using ANSI sequences)
- [x] lxml (To offer support for XPath, RelaxNG, XML Schema etc)
- [x] re (RegEx, or Regular Expression)
- [x] requests (Dealing with HTTP requests)

### **Execução**
---

1. Crie um arquivo contendo URLs, um abaixo do outro, do GitHub
2. Desta forma:

        GitHub_URL1
        GitHub_URL2
        GitHub_URL3
        GitHub_URL4

3. No Terminal execute o comando:

    > python3 findGit.py

4. Escolha a opção 1 para pesquisar <**ENTER**>
5. Adicione o caminho do arquivo <**ENTER**>
6. Digite uma palavra a ser pesquisada <**ENTER**>

![](https://live.staticflickr.com/65535/49381495197_22ee314c39_b.jpg)

PS: Caso o arquivo esteja localizado na mesma pasta do programa, então basta escrever o nome do arquivo

### **Propósito**
---

Eu criei esta ferramenta em Python 3 para resolver um problema pessoal: facilitar minhas pesquisas nos Meus Favoritos.

Desevolvido e testando em Debian com um plano de fundo da cor preto. 

**Note**: as cores do programa podem ser alteradas facilmente no código, por exemplo, se estiver escrito RED, substitua por BLUE (tudo maísculo). Veja: 

###### [Colorama Homepage](https://pypi.org/project/colorama/ "Colorama Homepage")

Eu não sou programador profissional, eu sou um entusiasta em Python e eu estou de mente aberta (e código) para receber qualquer opinião.
