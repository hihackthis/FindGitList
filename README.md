# Find-Tool-GitHub


### **Descrição**
---

> This program searches for a keyword in the title on a GitHub page.

Escrito em Python3 e somente executado no Linux (Debian).

Este programa serve para procurar o nome e ou descrição de uma ferramenta publicada aqui no GitHub e que você favoritou em um arquivo de texto pessoal, o qual contem URLs. O programa irá procurar por esta palavra na `tag title` do URL, note: o programa irá procurar **uma**, e somente **uma**, palavra por vez.

### **Requerimentos**
---

##### Modules:

- [x] re (RegEx, or Regular Expression)
- [x] requests (Dealing with HTTP requests)
- [x] lxml (To offer support for XPath, RelaxNG, XML Schema etc)

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

4. Digite a palavra que procura **ENTER**
5. Adicione o caminho do arquivo **ENTER**

![](https://live.staticflickr.com/65535/49353145058_97e62450f9_b.jpg)

PS: Caso o arquivo esteja localizado na mesma pasta do programa, então basta escrever o nome do arquivo

### **Propósito**
---

Eu criei esta ferramenta para resolver um problema pessoal: facilitar minhas pesquisas nos Meus Favoritos.

Eu não sou programador profissional, eu sou um entusiasta em Python e eu estou de mente aberta para receber qualquer opinião.
