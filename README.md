# Compilers Project One

I've chosen to do the option based on a finite state
automata. Instead of using a table, I've chosen a functional
paradigm, because I think it's easier to follow as a programmer.

Note that we have line number, as well as additional data.

There are a few things that are worth refactoring. For example, I
probably wouldn't stack generators. 

## Keywords:
 - Can be added trivially by updating keywords.kwds.
 - Can split by any white space character.

## Usage
scanner filename

Don't use the filepath. File must have .sp2020 path. 