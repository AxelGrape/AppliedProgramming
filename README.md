# AppliedProgramming
För kursen tillämpad programmering sommarterminen 2020

En parser för Pascal som kommer kunna användas på en sida skapad med Django.

Testkörning av systemet:

Installering av Django:
```
$ sudo apt install python3-pip -y # Om pip saknas
$ pip install django
```

Förutsatt att Django är installerat.
```
$ bash runscript
```

För att endast köra parserdelen

1: from interface_module import parse_file

2: #För att parsa en fil, skriv output = parse_file(filnamn)
   #Alla tokens som matchas skrivs ut och output blir en sträng med alla eventuella felmeddelanden. "testok1.pas" är en fil som kan testas, finns med i repo.
