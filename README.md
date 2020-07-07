# AppliedProgramming
För kursen tillämpad programmering sommarterminen 2020

En parser för Pascal som kommer kunna användas på en sida skapad med Django.

# Testkörning av systemet:
Django krävs för att starta hemsidan, är det redan installerat så är det bara att köra scriptet.

## Installering av Django:
```
$ sudo apt install python3-pip -y # Om pip saknas
$ pip install django
```
[Mer info](https://www.howtoforge.com/tutorial/how-to-install-django-on-ubuntu/)
## Provkörning.
```
$ bash runscript
```

## Testning av endast parserdelen

1: from interface_module import parse_file

2: #För att parsa en fil, skriv output = parse_file(filnamn)
   #Alla tokens som matchas skrivs ut och output blir en sträng med alla eventuella felmeddelanden. "testok1.pas" är en fil som kan testas, finns med i repo.
