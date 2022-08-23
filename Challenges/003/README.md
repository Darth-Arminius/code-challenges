# CODE CHALLENGE #3 23/08/2022 - In space no-one can hear you meme!

In this challenge you will need to create a working playable board game based on a set of rules outlined and with as many of the below features as you can integrate. You can use any language or framework you want. Bonus points may be awarded for a fancy UI but one is not required, a console/terminal output works just fine too.

You work for a board game company and you’ve just been asked to create a digital “space race” board game that contains dank memes for some reason. The goal of the game is to get your spacecraft to the finish first, utilising beneficial meme zones to boost you ahead and avoiding hazardous ones that hold or pull you back.

Rules and requirements:

- The board consists of an 8 x 8 grid of squares or “zones” starting with zone 1 in the bottom left corner and finishing with zone 64 in the top left corner of the board. The zones follow a “snake-like” path starting from left to right, then going up to the next row, then right to left, then up again, left to right, etc. You can find a quick diagram of the board (`board.png`)
- Each player’s spacecraft piece starts on zone 1
- Player’s get one turn per round unless stated otherwise
- Each round each player rolls a 6 sided die and moves the number of spaces they rolled
- A round ends when all players have finished their turn(s)
- The order of player turns goes from Player 1, Player 2, …, to the last Player, then back to Player 1 again at the start of the next round and repeat
- If the player lands on a “meme zone” the meme is displayed (can be text, can be an image, can be a video, can be a link to the meme) and the effect(s) take(s) effect (list of memes and their effects below). Passing over/by a meme zone should not trigger it. Meme zones remain in place throughout the game
- If the player lands on a zone that already contains a player, the player that just moved gets to “bounce” off of the stationary player and move up one space (i.e. Player 2 rolls a 4 and lands on a zone that already contains Player 1, Player 2 then gets to “bounce” off of Player 1 and move up 1 more space for free). This does not trigger at the start as all players are on zone 1
- If a player rolls a ‘6’ they get another turn that round
- Any extra turns a player receives they must take immediately after completing their last turn
- If a player rolls a ‘6’ three times in a row their spacecraft blows up and they are sent back to zone 1 on the board
- A player must roll the exact amount needed to reach the finish, rolling more than is needed counts as a “bust” and the player doesn’t move that turn i.e. Player 1 is 4 zones away from the finish but rolls a 5, Player 1 busts and doesn’t move that turn having to wait until their next turn/next round to try again

Features (implement as many as you can, you don’t need to add all of them but the more you add the higher your submission will be marked):

- A start “screen” allowing you to select the number of players
- The ability to input the name for each player
- The ability to play with at least 1 other human player
- The ability to play with at least 1 computer controlled player
- A way, chosen by you, to distinguish the human players from the computer controlled players (can be colours, icons, images…)
- The ability to randomise or choose the order players take their turns
- An input command the player needs to perform to roll the die (e.g. Pressing the spacebar to roll, clicking a button on screen, etc.)
- The ability to let the computer play by itself/against itself
- The ability to cheat the number rolled by the die (mainly used to test the roll a ‘6’ three times rule)
- The ability to cheat the zone a player is on (allowing a player to win instantly by teleporting their piece to the finish zone, or to test certain meme zone effects)
- A leaderboard allowing you to input your name and telling you how many dice rolls it took to finish, the lower the number of dice rolls the higher you are on the leaderboard
- Randomly generated game boards. The start should still be zone 1 and the finish should be zone 64 but the locations of the meme zones, the types of meme zone, and even the direction of board travel can be randomised
- The ability to select a custom board size (e.g. 4 x 4, 11 x 7). Can also allow random sized boards
- The ability to turn on “moving meme zones” which makes meme zones change position randomly each round. If a meme zone moves to a zone with a player already on that zone that meme effect does not trigger for that player
- A fancy UI with colours, images, animations, sound effects, etc. designed however you want

Meme zones (the effects trigger when a player lands on the meme zone):

- “Change my mind” = Go back to the zone you came from
- “Success kid” = Success! You get another turn this round
- “Shut up and take my money” = Skip your next turn as you stop to buy the latest iPhone
- “That escalated quickly” = Escalate up to the zone directly above the zone you are on (1 row up)
- “Distracted boyfriend” = You get distracted by that spacecraft’s sleek fuselage, skip your next turn
- “The most interesting man in the world” = You don’t always roll dice but when you do you roll sixes, your next roll is automatically a 6
- “Strutting Leo” = You go for a joyous stroll, your next roll is automatically a 1
- “Facepalm” = Patrick Stewart is disappointed, skip your next 2 turns as you sort your bridge crew out
- “Good guy Greg” = You’re feeling especially generous today, every other player gets 1 extra turn while you skip your next turn
- “Scumbag Steve” = You’ve stolen everyone else’s turn, every other player skips a turn while you get an extra turn
- “One does not simply” = One does not simply fly their spacecraft at a gentle place into the next zone, if you roll anything but a 6 next turn it doesn’t count and you lose that turn
- “First World Problems” = Oh no! Rolling a 1 makes you upset, if you roll a 1 next turn it doesn’t count and you lose that turn
- “What if I told you” = Plans within plans, turns out there’s a game within the game, landing on this special meme zone starts a brand new game from the beginning played with the same rules, once complete the old game returns and the winner of the new game goes next and gets 5 extra turns (**NOTE**: This is a bonus meme zone that you don’t need to add but will give you a ton of extra marks if you do)

You will be marked on whether the game meets the criteria, the quality, readability, and performance of the code, and any testing you include.

Good luck
