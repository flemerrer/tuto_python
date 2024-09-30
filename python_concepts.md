### Numbers and math operators

division
> > > 7 / 5
> > > 1.4

euclidian div
> > > 7 // 5
> > > 1

modulo
> > > 7 % 5
> > > 2

power
> > > 2 ** 3
> > > 8

absolute value
> > > abs(-1.2)
> > > 1.2

round
> > > round(1/3, 4)
> > > 0.3333

minimum
> > > min(1.5, -6, 3.7)
> > > -6

maximum
> > > max(1.5, -6, 3.7)
> > > 3.7

division and rest
> > > divmod(7, 5)
(1, 2)

binary value
> > > bin(42)
'0b101010'

octal value
> > > oct(42)
'0o52'

hexadecimal value
> > > hex(42)
'0x2a'

It's also possible to do binary operations and access the Python infiniite value

### Strings

It's possible to crawl through a list from the end
> > > 'hello world'[-3]
'r'

Slicing allows to parametrize String operations [beginning:end:step]

*in* operator allows easy locating of specified chars in a String
> > > 'la' in 'hello'
> > > False

*index* and *find* return the index of specified characters

*count*, *removeprefix*, *removesuffix*, *startswith* and *endswith* are self explanatory

*lstrip*, *rstrip* and *strip* allow removal of spaces around a String
They also accept a parameter to delete specified char instead of spaces

*upper*, *lower*, *capitalize* and *title* change the case of the Str

Then you have *replace*, *join*, *split* ; join can be used with an empty Str to concatenate :
> > > ''.join(['h', 'e', 'l', 'l', 'o'])
'hello'

### Dictionnaries

Access data from a dict using a loop :
> > > for name in phonebook:
> > > ... print(name, ':', phonebook[name])
> > > ...
> > > Alice : 0633432380
> > > Bob : 0663621029
> > > Alex : 0714381809

Converting the dict to a list to get a list of the keys :
> > > list(phonebook)
['Alice', 'Bob', 'Alex']

Get only the values and not the keys :
> > > for phone in phonebook.values():
> > > ... print('Numéro de téléphone :', phone)
> > > ...
> > > Numéro de téléphone : 0633432380
> > > Numéro de téléphone : 0663621029
> > > Numéro de téléphone : 0714381809

*dict.keys()* is a method used to get all the keys as a list and is **de facto** iterable 

*.items()* returns the values as a list of n-uplets. You can iterate on it with multiple *for* parameters :
>>> for name, phone in phonebook.items():
...     print(name, ':', phone)

### Other

There's a whole array of operators to manipulate lists

*is* operator allows to check if two objects have the same identity
It doesn't check the value but the memory space value (check validity)

*None* is a singleton and shouldn't be used with a *==* but called with *is (not) None*

Convert an iterable as a tuple : 
>>> tuple('abcd')
('a', 'b', 'c', 'd')