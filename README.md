# CSC 104 Lecture Notes

LaTeX sources for the Lecture Notes for CSC 104 at Nassau Community College.

First, make sure you have the fonts installed:
* [Fira Sans](https://fonts.google.com/specimen/Fira+Sans)
* [Fira Mono](https://fonts.google.com/specimen/Fira+Mono)
* [Fira Math](https://github.com/firamath/firamath)

Then, make sure that [Pygments](http://pygments.org/download/) is installed.  You will probably have to have Python 3 installed first, so that you can use the pip3 tool to install Pygments.

Once that's all done, you should be able to compile everything with this command:

```
xelatex -synctex=1 -shell-escape -interaction=nonstopmode CSC104LectureNotes.tex
```
