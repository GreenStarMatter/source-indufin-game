# source-indufin-game
 Source Indufin is a game which involves sourcing materials, processing them, and managing capital.  The player must carefully manage their operating capital when purchasing materials from selling vendors, lock machines into their factory while controlling shrinking free space, process materials to keep an assembly line running, and sell the outputs to stay afloat.

---

## Environment

This project was created using a virtual Anaconda environment with Python 3.7.10.  An **environment.yml** file has been included which will build the complete environment necessary to run this module.

The following command will create this virtual environment.  Replace environment.yml with the full path to where ever you are storing the .yml file.

**conda env create -f environment.yml**

---

## Run Instructions

1. Start the virtual environment from the *Environment* section.
1. Run the command python basic_tutorial.py
1. Follow prompts to complete the objective!

---
## Introduction/Basic Tutorial
An image of the starting board can be found in the top level directory (PlayingBoard.png).


Hello, welcome to the source-indufin game!
Currently you are in a basic tutorial mode.  You have been given
some capital ($150) to start.  Your objective is to raise more
than a threshold ($2500).  You can do this by purchasing
materials and machines, running a factory, and selling processed
materials.  The actions you can perform are:

- BUY: Purchase machines or materials so you can place them in your
factory.
- SELL: Sell machines or processed materials to make money.
- PLACE IN FACTORY:  Place machines on factory floor grid or place
materials in available machines
- REMOVE FROM FACTORY: Remove materials or machines from factory
floor.
- END TURN: End the day and allow machines to process materials.


A normal progression would be to:
1. Buy a machine from a seller
2. Buy material which matches the machine input payload
3. Place the machine in your factory
4. Place the material in your factory
5. Pass turns until the material is ready to be harvested
6. Harvest material into your catalogue
7. Sell material to buyer
8. Determine how to spend your profit!

Bonus actions can be performed to make turns more efficient:

- Harvest All Machines allows the player to automatically harvest all
machines which have fully processed materials instead of having to
individually pull from each one.
- Set Priority Queue allow the player to arrange machines on the grid
so that they can be autofilled.
- Autofill Priority Queue automatically allocates materials to
machines based on how the player previously set-up.

These 3 actions are very helpful for mature factories.  For example,
a factory with 10 machines would take approximately 80 commands to
process.  However, this can be minimized to just 3 top level options.

Currently the game is in a tutorial level stage.  The interface is bare bones with just enough information to make decisions.  The logic is primarily focused on protecting user actions and has some conveniences added in, but still has some progress to be made before the game plays at a good pace.

---

## Vision
The vision for this game is a full fledged resource managing factory board game.

#### Mechanics
Non-symmetrical factory machines will cause players to have to carefully manage board space.  Materials will take-up space if they are not being held by a machine, so the player will have to be wary of processing materials without an exit strategy.  Some materials will require multiple machines to process, which makes a prime opportunity for bottlenecks and mid-process storage issues.  Buyer/Seller prices may fluctuate and can be dependent on order sizes.  Randomness is always present and fluctuations can appear in the amount of turns it takes to process, prices, and the amount of yield of a process.  Everything not properly stored when a turn ends must be thrown away because storage is limited!  All of these machines and movements need to be accomplished by a work force.  Some game modes may have other conditions or story elements which a player must achieve to progress, while other elements may cause the player to lose (i.e. taking too many turns, losing all money).

#### Story
For a story element, I'm thinking of drawing plot lines in a manner similar to The Goal by Eliyahu Goldratt and Death by Meetings by Patrick Lencioni.  I think having problems come up in an organic manner with other characters trying to influence the player would be interesting.  My first thought goes to The Goal, a high-level corporate office could keep urging the player to keep the factory running at full efficiency while another character could suggest that the goal is to make money.  This would probably make the point of The Goal pretty obvious.  I could set-up a series of these scenarios (taking over a failing factory, volatile product type and amount demand, consistent seasonal demand, other factories using the player factory as a storage facility, etc.)  These would all encourage different play styles and could allow for emotional slants in the game.

---

## Analytics

The game includes analytic capability which is currently fully external.

#### Game Set-Up
The script **\analysis\calculate_fair_game.py** accesses the .csv **\analysis\data\ConfigurationCalculations.csv** to aid in the calculation of a fair game.  The basic idea of this was to determine how productive machine/set of machines would be when operating at max efficiency. The net gain of processing can be seen by graphing these values over processing turns.  This helped to inform what purchase cost, processing time, selling cost, and scaling between different sized machines should be to make a fair game.  The script creates a useful visual for setting these values.  The turn 0 value shows how much capital is required to create a configuration and the slopes show how quickly a configuration can produce income.  Different combinations of the machines can be interpolated from these lines.

In one scenario, setting the ratio of starting income and early machine configurations incorrectly can leave the player stranded in the early game.  In another, if a beginning option is severely better than future options, then the player will have no incentive to change their factory configuration.  The shapes of the machines were picked to allow for a "foldable" configuration which would make these calculations and comparisons easier (4 T1s takes up as much space as 1 T2, 4 T2s takes up as much space as 1 T3, etc.).  With oblong shapes, the classic paper cutting optimization would need to come into play and would make this much more complex than a basic level game (This is definitely on the table for future iterations though).

#### Post-Game Analysis
Each transaction within the game is recorded into a ledger.  When the player either quits or finishes the game, the ledger is uniquely indexed and written to a .csv in **\analysis\session_data**.  This will act as a convenient vehicle to analyze placement patterns, financial transactions, and player preference.

A Tableau workbook was created as a one-shot analysis of a play through.  The data structure will likely change so I only spent 5-10 minutes on this, but it does give insight on how the game was playing.  There is an image included of the dashboard as well.  Purchasing from the seller happened in very erratic intervals in a guess and check manner so the player could perform actions which they knew fit their factory and then use the left overs to potentially perform secondary purchases.  Selling to the buyer was fairly uniform, there were no decisions to make here so output was unloaded in a single transaction each time.  I'm really regretting not storing the turn in the data ledger because the pacing is not apparent from this visual.  It can be interpreted from the seller/player capital transaction, the first 100 transactions were very flat compared to the last 350.  This informed me to raise the starting capital and to extend the length of the game.  The bulk of the transactions were with the grid, but this data did not capture the fact that the user never had to or wanted to remove a machine from the grid.  That aspect also went into the changing of the game structure.  Without this, a lot of the board economics are removed from the game.  I don't want the player to be overwhelmed in the tutorial, but I'd like them to experience a decision point on what to do when they run out of space and start to flat-line.

---
## Additional Considerations

Included is a project log which I detailed my development process.  This is to give an insight into how I think about problems and how I come to solutions.  It's fairly colloquial and includes a lot of me talking to myself.  This project was made from scratch partially as an exercise to work some of the more intermediate to advanced functionality of python.  I loosely thought it would end up at about 1000 rows of code; however, it ended up being about 3x as large as I though it was going to be.

---
## Next Steps

I believe the long term vision of this game would not take much longer; however, I cannot keep working at the pace that I am.  I would estimate that each feature would take at max a week and in total ~2 months to complete.

- I would really like to clean this project up.  I wanted to get this to a playable level, but I left behind some engineering structure in order to do that.  There are quite a few items which should be managed as objects and code redundancies in the basic tutorial.  This got me to a product faster, but in the end I gave up a lot of code cleanliness to achieve this.  I also felt naming conventions slipping on me near the end.  I got a bit caught up in deciding how the game would play that I got excited and shot to the end of development... the analytics and design parts were too enticing.  I'm also a sucker for workability (in this case playability), but I'm going to have to root back through this and make some changes to make this more engineered.  Very much a case of stick and carrot encouraging away from strong engineering principles.
- In the near term I'd like to focus on the post-game analytics as I'd like to show-off some of the stuff I did in my master's.
- I'd then like to add more data engineering fundamentals to the project.  Those aspects were after thoughts because the data size was so small and infrequent that a lot of it could be safely ignored.  Although the ledger formation is giving me heart palpitations, but I set a hard stop and I need to honor that to.  If anything, I can simulate results from existing sessions and pass those through some cloud services.  I could also sparkify some of the analytics I create.  It would be pretty self-indulgent, but it's good to keep these skills sharp.
- I think it would also be cool to push this into a web-app with Django.  I don't think it would be too much extra effort if I keep the amount of players to only 1.  I originally shirked from this because it seemed like a complexity explosion, but I may be able to keep it under control with only one user per session.  This would make the data engineering side much more interesting.
- Increasing UX will be a core facet of this development, I really want to avoid a pure simulation feel... I could see this becoming "work the game" if I'm not careful.

###### Completed Next steps
-  Game was sped up with the priority queue listed in the project log.  I would like the tutorial to play in about 5 minutes if possible.
---
