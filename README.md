What is it?
--------------

Dijkstrapy is a command line reverse polish notation calculator written in python. The purpose of this tool
is to simulate the experience of an rpn calculator on pc by minimising the number of keys required for input. NOTE: Software is experimental, pre-release

Features
-------

  - Full rpn experience
  - Real time input. No need to press enter unneccesarily
  - Supports a wide array of math functions that can be called with short keywords
  - Easily enter constants
  - Manage stacks with builtin commands
  - Extensible. Add your own math functions (mathfuncs)
  - Different modes (ie scientific notation)
  - Argument form. Pass an expression as arguments to djkstrapy
  - Inbuilt function help
  - Inbuilt manual
  - Configuration file
  - Colour output

Upcoming features:
-----------------

  - Ability to add user defined constants. **Done!**
  - Npr function
  - Apply operation recursively. Done!
  - More colour options
  - Vim like set command
  - rewrite with classes
  - command line arguments mode **Done!**
  - Add ability to change the trigger key for any function


Install & Run
-----------------

  For now simply clone and run: python dijstrapy.

  pip support is being developed

Platform
--------

Tested on GNU/Linux and Microsoft Windows.

Known issues
------------

  - Unexpected results due to floating point behaviour (e.g 1.2+ 2.2 = 4.4000000004). Can be mitigated by turning on decimal option in config.ini
  - All text can be erased (including stack info)
  - Some incorrect input is still not handled correctly
  - Recursion feature has a bug
  - ~~Backspace in GNU/Linux does not work. Use ; function instead~~
  - ~~Some characters from previous operation show up before printing of result in GNU\Linux~~

Documentation
-------------

Documentation on the use of this application is available by typing 'man' in the main program or by starting program with --help argument. 

#### Simple operations:
+, - ,\*,\\

#### Stack operations:

| Command | Action                     |
| ------- | -------------------------- |
| rm      | remove stack member        |
| \#      | swap the last two stacks   |
| \'      | drops highest stack member |

#### Math functions:
| Command | Action                                   |
| ------- | ---------------------------------------- |
| $       | invert sign of operand                   |
| ^       | Return x\*\*y (x to the power of y).     |
| !       | Return factorial(x)                      |
| srt     | Return the square root of x.             |
| log     | If the base not specified, returns the natural logarithm (base e of x |
| tlog    | Return the base 10 logarithm of x.       |
| sin     | Return the sine of x (measured in radians). |
| cos     | Return the cosine of x (measured in radians). |
| tan     | Returns the tangent of x (measured in radians) |
| crt     | Return the cube root of x                |
| epow    | Return e raised to the power of x.       |
| ncr     | n Choose r function                      |

#### Conversions:
| Command | Action                                   |
| ------- | ---------------------------------------- |
| ra      | Convert angle x from degrees to radians. |
| deg     | Convert angle x from radians to degrees. |

#### Number:

| Command | Action                                   |
| ------- | ---------------------------------------- |
| &       | finds a fractional approximation to a given floating point number |
| E       | scientific notation                      |
| dp      | changes the decimal precision of a floating point number |
| rnd     | rounds to given precision                |

#### Constants

| Command | Action     |
| ------- | ---------- |
| pi      | returns pi |
| eu      | returns e  |

#### System operations:

| Command | Action                                   |
| ------- | ---------------------------------------- |
| man     | opens full documentation                 |
| ?fnc    | opens documentation for function         |
| ;       | clears input (not including stack members) |
| ver     | displays dijkstrapy version              |
| q       | quit                                     |

#### Other features

##### Recursion

Apply the operation recursively on stack. For now only +,-,*,/ operators are supported. 

Syntax:

​	n@o - where n is the number of times operation should be repeated and o is the operator

​	@ao - a is parameter all. Hence operation is replied recusively to last stack member

For developers
-------------

Below is a list of the functions that each module contains

- mathfuncs (additional math functions) = [cube_root, sci_notation, invert_sign, decimal_places, rnd, fract, ncr]
- stackop (stack operations) = [two_pop, operate, append_rogue, adv_operate_double, adv_operate_single, adv_operate_none]
- screen (drawing operations)= [clear, return_custom,  write_custom, draw]
- sysfuncs (system functions) = [clear_line, delete_stack, drop, swap, assist, newline, backspace, leave, catch_inline_help, inline_help, display_version, set_precision]
- handler (input handling functions) = [num_handle, match_and_operate, operator_handler, character_handler]
- readconfig(str2bool, check_colour, reset_colours, check_precision, load_config, read_argv)

Bug reporting && Suggestions
------------

When you find a bug, which you are almost certain of doing, please open an issue on Github.

I welcome any suggestions as I am a newbie

Credits
-------

Danny Yoo

Licensing
---------

Please see the LICENSE file
