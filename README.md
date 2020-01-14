# Find-Tool-GitHub


# Find-Tool-GitHub


### **Description**
---

> This program searches for a keyword in the title on a GitHub page.

This program is for looking up the name and description of a tool published here on GitHub that you favored in a personal text file, which contains URLs. The program will search for this word in the `title tag` of the URL. Note: the program will look for **one**, and only **one**, word at a time.

### **Requirements**
---

##### Modules:

- [x] colorama (Colored text using ANSI sequences)
- [x] lxml (To offer support for XPath, RelaxNG, XML Schema etc)
- [x] re (RegEx, or Regular Expression)
- [x] requests (Dealing with HTTP requests)

### **Run**
---

1. Create a file containing GitHub URLs one below the other.
2. Like this:

        GitHub_URL1
        GitHub_URL2
        GitHub_URL3
        GitHub_URL4

3. At Terminal run the command:

    > python3 findGit.py

4. Choose option 1 to search **ENTER**
5. Type the file path **ENTER**
6. Enter a word to search **ENTER**

![](https://live.staticflickr.com/65535/49381495197_22ee314c39_b.jpg)

PS: If the file is located in the same folder as the program, then just type the file name.

### **Purpose**
---

I created this tool in Python 3 to solve a personal problem: facilitate my searches in My Favorites.

Developed and testing on Debian with a black wallpaper, see the image above.

**Note**: program colors can be easily changed in code, for example, if it is written RED, replace with BLUE (capital letter). More info: 

###### [Colorama Homepage](https://pypi.org/project/colorama/ "Colorama Homepage")

I'm not a professional programmer, I'm Python enthusiast and I'm open-minded (and code hahaha) to receive any feedback.
