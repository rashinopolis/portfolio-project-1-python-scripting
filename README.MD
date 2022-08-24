# Morse Code Converter

![Morse Code](/static/morse_code.jpg)

Capable of converting text to or from morse code. Just start the program, select
to convert to or from, and input desired text:

### To Morse Code:

```linux
$ python index.py
>>> 1
>>> hello world
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### From Morse Code:

```linux
$ python index.py
>>> 2
>>> .... . .-.. .-.. --- / .-- --- .-. .-.. -..
hello world
```

- Exception handling for non-alphanumeric values when converting to morse
- Exception handling for non-morse characters when converting to alphanumeric
- Documentation for all methods in the class