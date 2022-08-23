# CODE CHALLENGE #2 09/08/2022 - WITCHCRAFT, HERESY, AND PERMUTATION!

For this challenge, you need to build an app that can output all the possible permutations of witchcraft potion recipes using the ingredients list that each witch provides you with:

- You need to write a program that reads in a list of witches and their list of ingredients.
- You can use any language and framework you want but make sure it can read in a JSON file.
- You will need to output, in any way you like, a list of possible recipes for each witch based on their ingredients. This will require recursing through the ingredients and generating recipes each end loop.
- The order of the ingredients matters and some ingredients don’t play well before or after each other and should be avoided lest you risk blowing up the cauldron.
- The JSON file with all the witches and their ingredients list will be provided (`witch-data.json`).

_An example: Hermione has red apple, green apple, eye of newt, squid ink and tree sap. Red apple cannot go before green apple, squid ink cannot go after tree sap, otherwise cauldron go boom. So the possible permutations are:_

- _Red apple_
- _Green apple_
- _Eye of newt_
- _Squid ink_
- _Tree sap_
- _Red apple, Eye of newt_
- _Red apple, Eye of newt, Green apple_
- _Red apple, Eye of newt, Green apple, Squid ink,_
- _…_
- _and so on_

_Each of those count as 1 recipe and every witch will have a total number of recipes they can craft from the ingredients they own_

Bonus points if you can also output all the permutations that would cause an explosion and separate them from the safe recipe permutations, that way the witch knows which permutations to avoid.
Also extra bonus point if you can name the code challenge title reference.

You will be marked on whether the program meets the criteria, the quality, readability, and performance of the code, and any testing you include.

Good luck
