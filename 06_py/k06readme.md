K06 README
Cool Dogs
Ishraq Mahid, Ivan Mijacika, Gavin McGinley
To read the CSV we used a CSV reader from the csv library, which generates an iterable object of tuples, where each row is a tuple, and each comma separated phrase is a different string. We read this into a dictionary. The dictionary is extremely useful because it allows us to store a reference in relation to certain jobs in bulk, in this case the occupations. We can assign all of these occupations a float, and easily access it later by simply calling the dictionary and the desired key.
**MARKDOWN**
*They're all listed online*
* In markdown you can do *italics* and **bold**
* In mark down you can make lists, like this list of what we can do in markdown
* You can also do block quotes:
> Which isn't very useful in our opinion
* You can also do syntax highlighting 
```python
def foo(x):
	print(x)

```
**WEIGHTED PROBABILITY**
The way weighted probability works in our program is that first, a random integer from 1-998 is generated (occupations only total 99.8%). Then the dictionary storing the occupations and their percentages is iterated through. For every item, the percentage(times 10) is added to a total counter. If total exceeds the randomly generated integer, the occupation is printed. For any item the chance of it passing the random integer on its turn is proportional to its share of the 99.8%.
