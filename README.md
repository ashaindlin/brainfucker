## about

`brainfucker` is a Brainfuck interpreter written in Python. The interpreter itself was written in one sitting (about 3 hours, hence the lack of a long commit history); everything else (verbose mode, etc.) is just tweaks.

## usage

``` python
>>> import brainfucker
>>> bf = brainfucker.Brainfucker(useASCII=True)
>>> bf.interpret("++++++ [ > ++++++++++ < - ] +++++ .") # print 'A'
A
>>> bf.resetEnv()
>>> bf.useASCII = False
>>> #read two numbers and multiply them
... bf.interpret(",>,< [ > [ >+ >+ << -] >> [- << + >>] <<< -] >>.")
bf> 12345
bf> 2
24690
>>> bf.resetEnv()
>>> bf.verbose = True
>>> bf.interpret("++ [> ++ < -]")
 v
[0]
 v
[1]
 v
[2]
    v
[2, 0]
    v
[2, 1]
    v
[2, 2]
 v
[2, 2]
 v
[1, 2]
    v
[1, 2]
    v
[1, 3]
    v
[1, 4]
 v
[1, 4]
 v
[0, 4]
>>> print bf.cells[0:4]
[0, 4, 0, 0]
```

## resources

[standards for "nice" brainfuck](http://www.muppetlabs.com/~breadbox/bf/standards.html) - helped greatly with laying out the details

[learn x in y minutes where x = brainfuck](http://learnxinyminutes.com/docs/brainfuck/) - short programs for testing the interpreter (shown in `usage` section)

## to do

- write unit tests
- optimize away long strings of `+` and `-`
- add a compiler (maybe?!)
