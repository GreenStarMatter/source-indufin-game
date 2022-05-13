# Project Log

## Introduction

I call this an introduction, but it could also be seen as a statement of purpose.  This is simply a free form of what I was thinking when I was thinking, or perhaps what I was planning to do.  The goal of this document is to communicate my thought process rather than the correctness of the end result.  I will accomplish this by only editing the small section I'm working on until I've concretely decided to move on.  My coding process strongly relies on writing in my notebook by hand; I hope this log will bridge the difficulty in sharing my thoughts which I have previously encountered.


## Project Summary
The goal of this project is to show my programming ability through the creation of a game.  I identified some operations processes which I believe could easily be gamified, are suitable to be easily learned, and can offer a rewarding complex experience by combination of the atomic elements.  The game will consist of a factory which will hold a money balance that will interact with external vendors to reach capital objectives.  I see this as a four phase game: phase 1 will allow the players to purchase and place in their factories, phase 2 will allow their factories to process, phase 3 will allow them to sell/collect new materials, and phase four will evaluate the consequences of their decisions externally.

For capital, my vision is:

- +Starting capital
- +Capital by selling materials/materials processors (machines)
- -Capital by purchasing materials/materials processors (machines)
- +Capital by loan
- -Capital by interest
- -Capital by overhead expenses

For processes, my vision is:

- Process materials
- Process materials processors
- Allocate maintainers
- Remove processors

For vendors, my vision is:

- Find buyer
- Get order
- Acquire/lose buyer
- Acquire/lose order
- Advertise
- Find seller
- Acquire/lose seller


For this project, I'd like to have multiple players, multiple objectives, and multiple play modes (e.g. cooperative, competitive, unknown).  However, I first want to create the skeleton of the game without the additional complexity.  Therefore, I have decided to start with an easy mode (or better yet a tutorial) which will allow me to get up and running as quickly as possible.  I believe the skeleton will be most easily completed by implementing the phasing of turns with only a few options.

Easy Mode Tutorial:

- Single players
- Only one buying vendor
- Only one materials selling vendor
- Three material types
- Three machine types
- Three machine variants
- Demand from vendor is infinite
- No loans
- No repairs
- No maintainers


## Code Goals

To achieve this, I will break the problem down accordingly:

- Money making system
 - Money in
 - Money out
 - Balance
 - Capital types
- Machine processing system
 - Machine functions
 - Machine variants
 - Machine costs
- Machine placement grid system
 - Grid size
 - Machine size
 - Materials size
 - Add/remove items to/from grid
- Play conditions
 - Lose condition (balance below 0)
 - Win condition (At least $XXX)
 - Turn counter
 - Implement phases

## Analysis

I would like to add an analysis aspect to this project.  Primarily I will focus on turns to victory/loss condition, money spent, cumulative profits, placement heat maps, and machine usage.

### Plan

From here, the documentation may become much more free-form.  I had approximately a week of consideration before writing the before hand; the time of which I used to write in my notebook where I am generally very organized.  Below is my first set of steps which I will complete the creation of the Easy Mode Tutorial mode.

1. Identify best project set-up
1. Identify best test suite
1. Create project and upload to GitHub
1. Start Test Driven Development (TDD) of Code Goals
1. At each step evaluate code quality/style adherence (Likely through use of linter, Pylint)
1. Implement analytics after core mechanics

#### Progress 4/30/2022 12:33 pm

I have chosen Anaconda to manage my Python packages as I am very familiar with it (~7 years experience).  However, I set my original environment up as a toy environment which I haphazardly maintained over the past years whenever I needed to see how a function works or to pull quickly pull a library in to see if it might be useful for a work environment.  To rectify this, I simply exported my environment into a .yml file using (conda env export > environment.yml) and renamed the name in the .yml file to **old_environment**.  I then updated to the newest version of Anaconda with simple conda update commands.  I then pointed to the old_environment .yml and created a virtual environment using (conda env create -f environment.yml).  This allowed me to clean-up my environment without losing any of my other work; though they are generally disorganized non-version controlled scripts I still love them.  Personally I tend to be an over-worker that is constantly reading and learning; however, I tend not to make cohesive engineering level side-projects as that is what I do at work.  So unfortunately that means work before starting to do meaningful work.

#### Progress 4/30/2022 12:54 pm
I just realized that when going to create a new virtual environment for this game that I have not named it yet.  I probably should do that so the environment name is easier to remember, though I could just rename it later I suppose.  I'm choosing source_indufin (source, industry, finance) because it is what it is and it sounds funny when said quickly.  The command to create this environment is conda create -n source_indufin python=3.7.10.  I prefer to work in Python 3.7.10 as I'm familiar with it and I'm fairly certain will contain more than enough capability to implement this project.

#### Progress 4/30/2022 1:00 pm
Installed numpy, pandas, pylint, and pytest to conda environment.  These will hopefully make development much easier.  Next goal is to set-up GitHub environment.

#### Progress 4/30/2022 1:18 pm

I already have a GitHub account to the basic set-up won't be necessary.  I will just need to create a new environment which I think I will just use the GUI to do so.  Project is now a GitHub repository.  Project log has been added, tests directory, and an empty ReadMe as well.  I think it would be good to establish a simple process loop.

### Process Loop

I generally use different style guides and coding processes when working so I think it is important at this early stage to set-up a flow.

1. Identify next feature that will be created/changed (i.e. work scope).
1. Make sure on correct GitHub branch and on a new commit
 - Don't load to much change into a single commit
1. Set-up/Validate environment changes
 - If new step requires an environment or version change to project, then it is important to first update documentation.  I'm a firm believer that if in the past you promise to go back and document that you are just making a liar out of your future self.
1. Quick reminder step of current style guide
 - Style guide chosen is PEP-8. I normally do not use this so I will leverage pylint to help.
1. Determine if new test file is needed
 - Is this feature distinct enough from old test files to require new set?
1. Create new tests if needed.
 - If feature is new then tests will be needed to verify functionality.  If this is a feature change, then no new tests may be needed.
1. Verify tests by using pytest.
 - Verify that tests are set-up correctly before moving to actually coding of logic.
1. Code logic
1. Run tests to verify that logic is correct
 -If any tests fail, step back to rework code logic
1. Use pylint to verify that PEP-8 was followed
 - If any updates are made to code, then step back to running tests
1. Locally commit files
1. Push to origin.
1. Compare to existing branch on GitHub
1. Follow best practice GitHub merging.

#### Progress 4/30/2022 1:42 pm

Updated project log and merged to GitHub.  Now project is established, process is established, logic has been broken up into steps.  Next step is to implement logic.


#### Progress 4/30/2022 5:17 pm

Installed Spyder IDE to conda environment.  I prefer to use this as I like to have an R like set-up where I can run commands to verify the behavior in an almost instant feedback system and I can easily track variables.  Got the package and sub-package hierarchy set-up.  Added a first set of basic existence tests.  Added in some account addition by overwriting dunder methods.  Also adding some assignment abilites.  Class looks pretty solid to start with.  I need to run a linter on it and then reverify tests.  Pylint was rolled over code and some minor corrections were made.  Some renaming completed, restructured the directory, and obliterated 100 white space characters injected by Spyder IDE.  Reran all tests, time for first GitHub push!  Next step is to add industry to project.  I'm seeing that I forgot to add in materials to the original industry development plan.  Fortunately, these should be fairly similar to the machine processing system so I don't believe this will be too much additional work.  I also need to remember to instance the ReadME when I get to the end of the Easy Mode Tutorial.  I'll tuck that into each progress check.

#### Progress 4/30/2022 7:30 pm
NOTE: Don't forget to create ReadME!
NOTE: Don't forget materials class!

Had a typo in the first line of the ReadME. Typical.
Just worked through the machines class.  This caused some flair-ups which I had not thought of yet.  I am going to need a processor class which takes the machine and material in to validate and create new objects from them.  This will hopefully prevent my machine and materials classes from becoming monolithic.  Other than that I have tested, linted, retested, and am ready to move this class to the repository!



#### Progress 4/30/2022 10:50 pm
- NOTE: Don't forget to create ReadME!
- NOTE: Don't forget processor class!
- NOTE: Don't forget factory/grid class!
- NOTE: Don't forget vendor class!
- NOTE: Don't forget turn phase logic!

Noticed better name for CreatedMachine class. Will go back and fix after materials are finished in different commit.  Also noticed minor error in __repr__ of machines, kept some of naming from money.  Also likely kept only money naming convention in __repr__ of MoneyAccount.  Finished materials class, testing,  and linting.  Going back for minor errors/updates.


#### Progress 4/30/2022 10:57 pm
- NOTE: Don't forget to create ReadME!
- NOTE: Don't forget processor class!
- NOTE: Don't forget factory/grid class!
- NOTE: Don't forget vendor class!
- NOTE: Don't forget turn phase logic!

Went back through for minor errors/updates and corrected.  Reran all tests and linted to make sure nothing was injected.  Pushing to GitHub.

#### Progress 5/1/2022 12:44 am
- NOTE: Don't forget to create ReadME!
- NOTE: Don't forget factory/grid class!
- NOTE: Don't forget vendor class!
- NOTE: Don't forget turn phase logic!

Considering changing language in machines and materials to align.  One calls it an augmentation and the other form.  Both make sense and are slightly different; however, it may flow better if they are named the same or more similarly.  Also just noticed a lapse in the testing docustrings, think I'm getting a bit tired.  Noticed some holes in testing, I'm not bounding input... very much assuming fair players.  I need to go back and create restraints, this may be more appropriate as integration level testing now that I have a better idea of how the game will play.  This was difficult at the beginning because a lot of this game is made up on the spot.  These started to get more noticeable at the processor class which is an integration of machines and materials.  I was also thinking I may need a palette class, though I think I can make it work with a processor unit.  The machine would be the palette and the material would be the held material.  The processor would have an infinite clock and would be destroyed on command.  Only difficulty would be handling the amount of material that could be held in palette.  Just noticed that I need to rename all internal methods with leading underscore, bad habit crept in.


Finished first pass at processors.  I think there may be more to do once I start getting the turns up and running.  Seems like it would be good to get a decrement for the turns to finish.  Also would seem good to manage the material/machine quality from an external source.  I may have this initialize every game in an environment type object.  That could lead to easy randomization as well as set game types that could be stored in data structures.  Need to finish documentation, lint, and retest.  Then I can check this in.  All tests passed, linted, and retested.  Turning in and turning myself in to bed.

#### Progress 5/1/2022 10:39 am
- CREATE: Don't forget to create ReadME!
- CREATE: Don't forget factory/grid class!
- CREATE: Don't forget vendor class!
- CREATE: Don't forget turn phase logic!
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)

Picking up where I left off yesterday.  Going to review log first so I don't lose any musings I made, but didn't record well.  I think I can finish the Basic Tutorial mode.  Biggest challenges will be the grid logic and the turn/phase logic.  I think I just solved the palette issue.  If I extend the machine class to have a "capacity" attribute, then I could multi-process materials.  This would also allow me to put multiple materials into a holding space.  The only difference is that the materials will inherit their form and form strength from themselves rather than the machine.  I also see processed materials being stuck in a processor/machine if there is no room to put them into a palette, this would be mitigated by placing a palette and designating a landing spot.

#### Progress 5/1/2022 12:11 pm
- CREATE: Don't forget to create ReadME!
- CREATE: Don't forget factory/grid class!
- CREATE: Don't forget vendor class!
- CREATE: Don't forget turn phase logic!
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)

Implement vendors class.  This will consist of both sellers and buyers.  I'm thinking a catalogue type system where sellers and buyers have set lists of things they will purchase/sell with a corresponding price point.

During implementation of vendor class, catalogue feels a bit complex.  Nested structure with a lot of info.  May be wise to break this down in the near future.  Managing this data with nested dict structure is already feeling like a hassle, my gut tells me a RDBMS would be best.  I may be able to get away with managing this in a .csv structure for now or setting up a postgreSQL DB.  Whatever the decision is, this feels like a tabular form that Pandas could easily process.  Now that I think a bit more, Pandas could probably tackle this completely for the Basic Tutorial version.  I could go bigger with a Relational DB as needed in future versions if the data storage facet gets large enough.  I was trying to stay in Python's standard library for as long as possible, but Pandas is pretty ubiquitous.  Looking like a good decision, this is minimizing my tests by allowing me to keep a single simple catalogue instead of multiple smaller dictionaries... I work in this everyday, probably should have seen that one earlier.  Pride. Or perhaps I need to slow down a bit and make sure I have this logic flushed out. Or both.  I'm thinking that I'm now at the integration level and I don't have this as well thought out as I did the general structure.


Need to finish the product, account, and status add/subtract.  Then I need to code the actual function.  Then I need to finish the grid class.  After this point I will regroup before doing the phase logic as this will be the integration between all of these objects.  It would be a good idea to revisit everything I've learned or thought of during this process.  I've been revisiting the idea if I want objects to own objects or just references to those objects.  I think I've been implicitly assigning these on intuition, but I need to make a concrete decision soon.  Probably will revisit at end of first development round.

#### Progress 5/1/2022 4:04 pm
- CREATE: Don't forget to create ReadME!
- CREATE: Don't forget factory/grid class!
- CREATE: Don't forget vendor class!
- CREATE: Don't forget turn phase logic!
- CREATE: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.


Idea to create a general purpose ledger.  This would make it easier to manage all of the games assets in a single location.  Thinking that if there are a lot of ledger writes that may cause I/O slowdowns and interpret the pace of the game.  I don't think the ledger will be large enough to cause that, but it's worth keeping an eye on.  I could also manage everything with ledgers of ledgers which would likely keep my I/O latency low, but may cause some integration issues if I'm not careful with processing steps and validation.

Tests appear to be completed for vendors, now moving on to creating vendor class.  Noticed minor error in machines, remove processable material added item instead of removing.  Fixed this as it was a one liner that was obviously wrong.  Starting to struggle a little bit, I have outpaced my original plan and am finding new functionality questions I didn't think of... would've been easier to implement an existing game instead of making one up on the fly.

Vendor logic nearing completion, catalogue handling turned out to be a bit more complex than I thought it would be.  Taking my time on it so it doesn't explode code size.  Feeling a bit unproductive, I think I'm going to re-diagram the code as it has changed pretty significantly in a short period of time.  I'm trying to implement the entirety of a catalogue instead of the MVP which will get me to the Basic Tutorial. Stop it.


#### Progress 5/1/2022 5:07 pm
- CREATE: Don't forget to create ReadME!
- CREATE: Don't forget factory/grid class!
- CREATE: Don't forget vendor class!
- CREATE: Don't forget turn phase logic!
- CREATE: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Writing this down in my notebook, I have essentially doubled the amount of objects I originally planned for.  I had planned to be done by now with simpler plan.  Writing everything down is helping.  I'm thinking I over-engineered the MVP which will be helpful down the line but is wearing on my patience now.  I've found a shortcut for now.  In Basic Tutorial I will assume infinite supply and demand.  This will allow for purchases/sales if the player has enough capital and will give me a good framework for the future.  I will manually set the vendors amounts so I don't have to worry about any transfers besides accounts.  Realized biggest issue I'm getting stumped on is how to transfer new items to player.  Removal is easy, but I'm thinking maybe a temporary holding list within the player industry phase would be best.  If they move to the next phase with items in here, this is essentially throwing them away (valid move if factory space is too small).  So I'm struggling with the grid and play handler.  I'm just going to simplify the vendor catalogues to only focus on if inventory in catalogue and if player can afford transaction.  This is going to be easier if I only allow single edits in Pandas to start.


#### Progress 5/1/2022 11:37 pm
- CREATE: Don't forget to create ReadME!
- CREATE: Don't forget factory/grid class!
- CREATE: Don't forget vendor class!
- CREATE: Don't forget turn phase logic!
- CREATE: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

I took a pretty long break today and came back to this.  Definitely was overcomplicating things because I'm tired.  I simplified back down and have essentially completed the vendor class.  I need to increase the test coverage before I'll comfortably say that, but otherwise the vendors appear to have the correct logic.  I was going to put the accounts in the ledger, but I think I will give them to the vendors.  This would make things a lot easier.  Maybe the ledger can do things like consolidate accounts and return them to vendors as well as keeping external track of all finances.


#### Progress 5/2/2022 7:19 pm
- TODO: Don't forget to create ReadME!
- TODO: Don't forget factory/grid class!
- TODO: Don't forget vendor class!
- TODO: Don't forget turn phase logic!
- TODO: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK:  Change MoneyAccount to use objects on dunder methods
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Noticed minor error in MoneyAccounts.__repr__, didn't have f on f string.  Also noticed that all functions work between a MoneyAccount object and a number, thinking I want to change this to work between two MoneyAccounts instead.  It would be very useful to implment a buy transaction from an object.  This would be very similar to vendor catalogue processing.  Really starting to feel like I need a catalogue class and an assets class.  Something which can store multiple of the subclasses and makes aggregation of them easier.  I should have only allowed a single account per vendor to start for simplicity, now having to compensate for logic which won't be in the Basic Tutorial.  Simplified down to one account.  I think this would be much easier with a transaction object.  I've caught myself pasting the same Pandas structure to multiple files.  I think I can do without for now, but this would be a useful expansion.

Just made update to accounts to be able to process transactions.


#### Progress 5/1/2022 11:37 pm
- CREATE: Don't forget to create ReadME!
- CREATE: Don't forget factory/grid class!
- CREATE: Don't forget vendor class!
- CREATE: Don't forget turn phase logic!
- CREATE: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

I took a pretty long break today and came back to this.  Definitely was overcomplicating things because I'm tired.  I simplified back down and have essentially completed the vendor class.  I need to increase the test coverage before I'll comfortably say that, but otherwise the vendors appear to have the correct logic.  I was going to put the accounts in the ledger, but I think I will give them to the vendors.  This would make things a lot easier.  Maybe the ledger can do things like consolidate accounts and return them to vendors as well as keeping external track of all finances.


#### Progress 5/2/2022 8:06 pm
- TODO: Don't forget to create ReadME!
- TODO: Don't forget factory/grid class!
- TODO: Don't forget vendor class!
- TODO: Don't forget turn phase logic!
- TODO: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK:  Change MoneyAccount to use objects on dunder methods
- REWORK:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

FINALLY FINISHED VENDOR CLASS!! (first version)...  As soon as I added Pandas in, I went to implement everything I could do with it instead of what needed to be done.  After revisiting requirements and simplifying down I have the necessary play functionality.  I can always update the other stuff as I like, but for now I need to focus on the MVP.

Just went through and linted code.  Looks satisfactory!  Reran tests and everything still passes.  Time to upload to GitHub and then start on the grid class.

#### Progress 5/2/2022 8:15 pm
- TODO: Don't forget to create ReadME!
- TODO: Don't forget factory/grid class!
- TODO: Don't forget turn phase logic!
- TODO: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK:  Change MoneyAccount to use objects on dunder methods
- REWORK:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.


Starting grid class.  I'm thinking that everything is going to be a square to start with, that way I don't have to worry about orientation at the beginning.  I think I potentially need a loading bay class.  This would be a simple place to hold objects that were purchased before placing them on the grid.  This would also help with selling items so the player can see what the grid could place things that we already sold.  I was going to do the array in numpy, but I think I want to represent items as strings and that would be easier to manage in a list of lists.  I could always do numerical placeholders, but I feel like I would be constantly translating items to better represent them.

#### Progress 5/2/2022 9:54 pm
- TODO: Don't forget to create ReadME!
- TODO: Don't forget factory/grid class!
- TODO: Don't forget turn phase logic!
- TODO: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK:  Change MoneyAccount to use objects on dunder methods
- REWORK:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Most of the way done with grid class.  This has been surprisingly straight forward, though I finally got to sleep this afternoon so most of these problems were probably sleep deprivation in the first place.  I see a minor issue with the MachineUnit, the size is only a single list and should be a list of lists.  I will go back through and fix this once I have wrapped up my work in the grid class.  I'll do that and then make some integration level tests between machines and the grid.  Went back and fixed machine class, fix looks a little odd but works for now.  Had some integration level tests fail, but new updates passed after changes.

#### Progress 5/2/2022 11:04 pm
- TODO: Don't forget to create ReadME!
- TODO: Don't forget factory/grid class!
- TODO: Don't forget turn phase logic!
- TODO: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND: Add capacity attribute to machines
- EXPAND: Add palette logic to processors
- EXPAND: Add transfer logic to processors
- EXPAND: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK: Replace Pandas catalogue with named tuple, may do this in conjunction with
- REWORK: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK:  Change MoneyAccount to use objects on dunder methods
- REWORK:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- NOTE: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Grid very close to completion.  I need to implement remove from grid and I need to clean-up grid placement function.  Iteration is ugly and confusing right now.  May offload iteration to another value.  Could make a coordinate method and a flip value method.  Calling these from place/remove could get the desired affect. Almost forgot to add/remove objects to grid defaultdict!  Now that I've thought about it, I think Pandas was overkill for the catalogue and updates.  I think a named tuple would have been more appropriate.  I'm already treating the transactions like immutable data, where I search, remove, and replace them.  Also the data shouldn't be more than 100 items.  I think if the catalogue is too large it would detract from gameplay.  Adding this as a REWORK item.  Also going to add index numbers to projectlog, TODO list is getting too long.

#### Progress 5/3/2022 5:30 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 2: Add capacity attribute to machines
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Change grid coordinate placement.  These nested loops are pretty messy.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Did a very quick run through on the last of last functions in grid.  This is done well enough for a first run.  I really want to rework the double nested list before uploading this.  That's nasty enough that I don't want anyone to see it.  Only two more items to complete!  The play handler will make the game functional, but I'd like to store the moves of each session.  That will make a pretty good analysis angle I think.


#### Progress 5/3/2022 6:32 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 2: Add capacity attribute to machines
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Change grid coordinate placement.  These nested loops are pretty messy.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Made a much cleaner implementation of grid.  This is still not where I want it, I'm heavily considering going to numpy for better indexing.  Just need to write docustrings for grid_test.py, fix the \_\_str\_\_ method of grid,  lint, retest and I'm done with this one!  Finished docustrings and lint of test function.  Finished \_\_str\_\_ methods, linted, and retested.  Everything looks good!  On to the phase logic and this will finally be playable!

#### Progress 5/4/2022 10:01 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 2: Add capacity attribute to machines
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Change grid coordinate placement.  These nested loops are pretty messy.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.

Looking back at development queue, I think there are going to be some key updates I need to make before this game is really playable.  I need to be able to transfer to/from processors and add capacity to machines.  These shouldn't be overwhelming updates, but I think they will be vital.  I'm going to do these first.  Capacity update to machines was very quick.  I need to implement some protection logic in processors to limit from too much material being placed in a processor.  Need to do this by having an input_payload size.  I was going to add in processor logic to pass to next processor; however, I think I should just make a "move" function which the player is in control of.  The processor can just have a flag which indicates that the output material is ready (probably should destroy the input material at that time).

The following four items need to be completed to wrap up the processor class.
- Need to verify tests in processor_test.  Need to set flag that says output_payload is ready (start processing/stop processing).
- Need to make a collect payload method which will wipe output_payload, the input_payload, and set the flag to stop processing.
- Need to make a start processing method which takes the machines turns to produce as an internal variable which indicates whether the output_payload is ready.
- Need to make a simple counter function which decrements the internal variable which keeps track of the turns until the output is ready (4,3,2, 1 = Next, 0 = Now, -1 = Empty).

#### Progress 5/5/2022 6:43 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 2: Add capacity attribute to machines
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Change grid coordinate placement.  These nested loops are pretty messy.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am having fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Looking back at development queue, I think there are going to be some key updates I need to make before this game is really playable.  I need to be able to transfer to/from processors and add capacity to machines.  These shouldn't be overwhelming updates, but I think they will be vital.  I'm going to do these first.  Capacity update to machines was very quick.  I need to implement some protection logic in processors to limit from too much material being placed in a processor.  Need to do this by having an input_payload size.  I was going to add in processor logic to pass to next processor; however, I think I should just make a "move" function which the player is in control of.  The processor can just have a flag which indicates that the output material is ready (probably should destroy the input material at that time).

The following four items need to be completed to wrap up the processor class.
- Need to verify tests in processor_test.
- Need to set flag that says output_payload is ready (start processing/stop processing).
- Need to make a collect payload method which will wipe output_payload, the input_payload, and set the flag to stop processing.
- Need to make a start processing method which takes the machines turns to produce as an internal variable which indicates whether the output_payload is ready.
- Need to make a simple counter function which decrements the internal variable which keeps track of the turns until the output is ready (4,3,2, 1 = Next, 0 = Now, -1 = Empty).


I think turns to produce should be an attribute of machines which is passed to the processor.  Realizing that I'm struggling with a lot of integration... these are from poorly defined and flushed out requirements from the stakeholder who is also me.  Next time it will be easier if I spend a bit more time thinking through the early design steps, but then again I've never developed a game before and I'm trying to work as quickly as possible.  I think it's still going well all things considered.

- Need to verify tests in processor_test.
- Need to add processing time to machines, and worm this back through to the processor and the vendor catalogue (would be a vital decision in picking a machine).
- Need to update testing for new attribute.


Just finished adding processing time to machines and updating machine testing.  Need to update vendor and vendor testing, need to update processor and processor testing.  Finished adding to catalogue and updating tests.  Updated processor with new logic.  Need to add processing tests to better get handle on logic.

#### Progress 5/5/2022 7:31 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Testing for processor has been updated!  Just need to relint project and retest before pushing to GitHub!  Linted and retested, pushing to GitHub!  Finally ready for the turn phase logic.


#### Progress 5/5/2022 10:01 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

NOTICED ANOTHER ERROR.  Starting to feel like my process was sloppy.  I don't think I took enough up front time on the tests.  This would have helped me flush out the code a little better, but I was trying to push to get this mostly done within a week.  This one is pretty easy to fix, just need to flip/flop the buy/sell from a vendor.  When a buy is initiated, I need to look for the corresponding selling line.  Currently buy looks for other buys... this would be equivalent to going to an auction and asking whoever just bid if you could buy the auction item they just bid on from them... probably not going to work.  Also realized when writing the player logic that I'll need to override the inventory match for the player.  Basically the player is in charge of what they may buy, buyer beware.

#### Progress 5/6/2022 6:43 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.


Did a quick fix on vendor logic.  Everything appears to be working correctly now.  Noticed minor error where accounts are not assigned to vendors.  This could be rectified very quickly, but will have no impact on the Basic Tutorial.  Upon testing transaction logic, it appears multiple purchases are not working for buyer catalogue though they do appear to work for the seller as well as both accounts. Indexing may be off on stock update for buyer

Use update_catalogue(self, method = "Sell", update_df) to remove items from player without having to actually Sell them.  This will decrement from the player catalogue.  Then I can verify the catalogue is empty down to the placeholder line.

Was testing something else and actual bug may be more nefarious.  Sell didn't find a matching counterpart so it just injected at index 1... YIKES!  Definitely need to fix this.  I've been lax on these things because I really want to move away from my catalogue system.  This would be much better with a shared ledger I think.  Exactly what I thought it was... weird internal index storage is coming back to bite me.  I didn't want to do multiple filters in Pandas so I just tried to hold the relevant index data in a variable.  This data is very small so re-filtering is not the end of the world and will result in more consistent performance.  All that's left is:

- Finish 7 transactions
- Implement play flow
- Print help methods and improve playability
- Perform Testing
- Clean-up code
- ADVANCED: Add more features such as
 - randomness
 - more play modes
 - more money types
 - better graphics/charm
 - more players
 - computer players  

 #### Progress 5/7/2022 4:38 pm
 - TODO 1: Don't forget to create ReadME!
 - TODO 3: Don't forget turn phase logic!
 - TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
 - EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
 - EXPAND 3: Add palette logic to processors
 - EXPAND 4: Add transfer logic to processors
 - EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
 - EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
 - EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
 - EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
 - REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
 - REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
 - REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
 - REWORK 4:  Change MoneyAccount to use objects on dunder methods
 - REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
 - REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
 - NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
 - IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.


 Finally got some sleep... everything is pretty clear now.  Blazed through updating temporary index in vendor so that those variables were local or passed through as inputs to methods.  ALSO, the root cause of the selling issue is that the Pandas dataframes were improperly indexing.  When adding new items to the catalogue, the player frame is keeping an index of 0... so when the index is reset, the new index is correct but the new column representing the old index is wrong.  This will be a quick fix likely, but annoying.  Super fast fix here, just put a reset_index on the concat.  This was caused from the Pandas concat on a new catalogue item which keeps the original index.  Actually thought about this and that should be a default option for Pandas concat method, by passing the argument ignore_index = True gets same result and is more inline with how the method was supposed to be used.

Boiled game down into 7 fundamental transactions.  Completed all 7 already.  Pretty straight-forward.  Had some minor bugs creep in though:
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.

All that's really needed to do is to formalize the transaction logic and create a play flow around it!

#### Progress 5/7/2022 5:35 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.


Almost finished this... have to remove all of the references since the functions are in the same subpackage.  Transaction logic formalized!  All I need to do is get the play flow logic and minor bugs down and I'm done!

#### Progress 5/8/2022 1:00 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Decided to close out Spyder and re-open.  It gets weirdly buggy when it's been running for too long.  I think it just tries to keep up with all of the annotating and it's too much animation when new code is added or removed.  Going through the player decision flow.  This was becoming highly nested if statements and while loops.  I decided to break this down into functions.  This won't reflect in my GitHub pushes, but I am building a branch of the while loop all the way down.  Then I move from the end of the decision branches and roll the logic into a function.  I continue to roll up at every branch decision to get the functional framework which makes a lot of the other coding much easier for me.  I chose this method because I wasn't really sure what the branches would look like.  I could have worked backwards from the transaction I wanted to complete, but I wanted to work forwards from what the player would do to achieve the action.  I'm sure this will change once I start playing and finding things that annoy me/hamper the UX but I'd rather experience those things in motion.  This is also helping me keep the base logic more readable.



#### Progress 5/8/2022 4:53 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.


I've decided to rename the functions to be more expressive.  They will indicate a player decision (or not) and the branch that was created.  Completed the buy/sell branch!  Last main branch to complete are the player/grid interactions!!  Already have the machine placement done.  Had a slight snag with materials and processing, I don't have a flag for if the processor is ready to accept new input.  Very simple fix, but right now I'm using an internal variable as a placeholder, putting in as REWORK 9.

I finally got the game into a semi-working state!!!  I have some bad input handling, but that is easily fixable.  I've done some quick fixes just to see the logic flow and it appears to be working the way I intended.  Next I will develop some scrubbing functions for input and then I'll be ready to do a full play test and some UX!
#### Progress 5/8/2022 10:00 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Reviewing through and collecting BUGS.  Also keeping command strings to easily retest values:
- COMMAND 1 (Buy Machine 5): 0,1,5,1
- COMMAND 2 (Place Machine at Origin): 1,1,1,00
- COMMAND 3 (Remove Machine at Origin): 1,2,0
- COMMAND 4 (Sell Machine to Vendor): 0, 2, 5
- COMMAND 5 (Buy 10 Units of Material 0): 0,1,0,10
- COMMAND 6 (Place 10 Units of Material 0 into Machine 5 at Origin): 1,1,2,0,10

Knocked down most bugs! Almost done with the Basic Tutorial!!  I just need to calculate what a semi-challenging game is and set all of the starting assets.  I have some wants to add on.  I really got on a roll and deviated from TDD.  I started a lot of functional programming as opposed to OOP and wanted to go really fast.  Bug hunting is going to get a little bit difficult from here so I'm going to develop a test suite... going to be a while to do that because I doubled the code size after writing all of these functions.  So finally here are my lists of wants:

- Pretty prints where ever there are player options.  Right now a player would have to remember quite a bit and there isn't any real charm to the game.
- Balance game.  I need to change the starting assets to have some sort of difficulty/flow.  I have some generic calculations (starting capital, win condition capital, machine size, machine cost, grid size) that I can set up some mathematical functions to calculate some generic strategies
- Test suite for basic tutorial.  This is something I skipped past which I probably should not have.  I only did this because I thought I would fumble around with completing the transactions if I tried to go too granular to start.  Gotta pay the piper now.

#### Progress 5/9/2022 7:00 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Though I had finished this... added in analytic capabilities to determine if gameplay will be entertaining and complicated enough to not have a straight forward answer.  Determined balanced assets and was updating the functional code when I realized that the catalogue won't distinguish between different capacities.  This is a bear of a change because the transactions were not pushed into an object and therefore are not centralized in the code.  This is going to be a sprawling change and it will have to be made like 50 times.  OUCH!  Pay the piper 2x for speeding in a construction zone.  Changes were actually pretty harmless, though I'm running into some floating issues within the actual game now where the catalogue needs the new update.  Instead of tracking down each instance of this, I'm just going to create the test suite.  I'm going to have to comb through anyway, this will hopefully get the bugs out of the way and upgrade my test coverage at the same time.

#### Progress 5/9/2022 9:23 pm
- TODO 1: Don't forget to create ReadME!
- TODO 3: Don't forget turn phase logic!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Just went back through all functions and arranged them into groups.  I am now going through the process of transforming these groups into a test suite.  I've identified 3 primary bugs I need to squash while performing this testing; hopefully they will be very apparent while I make my way through the branching logic.  I have already created the asset creation tests.  Since most of the creation logic is stored within these, the tests primarily detect if the functions run.  In the future I would consider storing these assets in a data file and reading them in, though I have put that beyond the scope of the basic tutorial. 39 to go, the ledger, and then another round of clean-up on this script.  I'm happy with where the logic is and I that I got to balance the game play, sometimes you've got to do the fun parts to keep going strong.  Pushing to GitHub because I've done a ton of work and would hate to lose it.

- Bugs (0/3)
- Gameflow Help Functions (0/12)
- Asset Creation Functions (7/7)
- Transactions (0/6)
- Update Data Helper Functions (0/4)
- Player Decision Tree (0/11)
- Game (0/3)

===== Total (7/46) =====

#### Progress 5/10/2022 5:30 pm
- TODO 1: Don't forget to create ReadME!
- TODO 4: Create a ledger class, this was going to be a bank; however, I believe this can be more general purpose for tracking machines and materials as well.
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 4: Add transfer logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 9: I have abstracted a lot of transactional inputs by just supplying an update_df.  I will need to create this each time with inputs.  Will be a series of functions, but otherwise will be very easy.  This is natural stuff I was planning on doing in the play flow.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
- REWORK 6: Fix improper sell injection when no match is found.  May only happen in the case that a Buy is found with no Sell in the catalogue.
- REWORK 7: 0 stock items are causing difficulty with existence function as the line technically exists, but the vendor has no stock
- REWORK 8: I think a weird buy/sell bug is lingering with multiple similar purchases for the player.  Some testing will be needed to verify, but it's worth tracking as it would cause multiple catalogue items containing the same category of data.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.


Having some trouble implementing monkeypatch for testing user inputs.  I'm going to leave this for later as I have run through the game and it is operating as intended.  I have successfully finished a balanced game!  There were some annoyances that I had that I want to patch up, mainly that the assignment/removal action is a bit cumbersome when there are 3 or more machines.  I have identified some small button-ups which will round out the first phase of this project:

- BUG: The shape for the machines is not correct since I changed the catalogue.
- IMPROVE: Improve the UX, sometimes I find myself swimming through a wall of text.  Need to shrink this and make player action/reaction more tactile.
- IMPROVE: Put a safety on machine removal.  Right now a machine can be yanked off the grid even if it contains a material.  The material is destroyed in the process which is the correct behavior, but I need to warn the user about that first.
- IMPROVE: I want a collect all button on the main menu... this could minimize like 50 button pushes later in the game and greatly speed up the harvesting phase.  I would like a similar action for speed placing, but that one isn't as obvious to me.
- IMPROVE: Once the game has decent pace and can be finished in ~5-10 minutes, I'd like to create a ledger which records all of the game's transactions.  I think I could do some cool analytics on the game results once that is implemented.
- IMPROVE: Need to do something with the NONE line in the player catalogue.  This is a good place holder, but I need to suppress it when the player has other items and I need to protect that the player cannot choose it in transactions.

#### Progress 5/11/2022 7:30 pm
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 10: Use priority queue so player can set-up an auto-fill option.  This would greatly speed up processing and would have some associated automation costs to the user (Is the time to set stuff up worth the minor improvements they may get from the manual placements every turn)? If a factory is semi-mature it could easily have 6 machines.  Each machine requires 5 selections to place into resulting in 30 selections per turn to run at maximal efficiency.  This could be reduced to a single click once the queue is set.  If each selection speed is 2-5 seconds, then this will save a range of 1-2.5 minutes per turn in a semi-mature factory... that is a lot.
- EXPAND 11: Have a turn limit and small interactions between other "characters", this could add a little flavor to the game every couple turns and reinforce whether or not the player is on track.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- REWORK 10: Move ledger to write only text file.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

This is a good place holder, but I need to suppress it when the player has other items and I need to protect that the player cannot choose it in transactions.

Solved shape bug.  Noticed that I can still place when an inventory is at 0.  I thought I had ironed this out, but I need to handle the 0 stock issue.  This would likely fix the None line issue as well which is good.  I really would like to close this first round out, but I a lot of my updates are UX oriented which are bottomless pits.  I think I have to accept this for what it is at this point and start closing out if even if stuff isn't looking perfect.

Moved priority queue improvement to full list of actions.  Just had a great idea which would give this game some character and player motivation.  Added this to EXPAND 11.  Squashed 0 stock placement bug! Turns out I made a method in the vendor class when I made the class just to deal with this exact situation... go figure. DOWN TO LAST UPDATE!!  Game flow is actually looking okay now.  I think small flavor additions would take this a long way.  Definitely would need the ledger first though.  In addition to analytics at the end, I could push interesting patterns back into the game and have characters be aware of play styles and performance.  This iteration would certainly be beyond the basic tutorial scope.  Finally finished coding!!!!!!!!!!!!!  Looking back; REWORK 6, REWORK 7, REWORK 8, EXPAND 4, EXPAND 9 as these are now obsolete with the current project progress.


Things left to do to finish the Basic Tutorial are to lint the project, complete the ReadME, and push to GitHub!  Linted this about as well as it's going to go.  Big difficulty is the declaration of global variables controlling the ledger writes.  This could be easily circumvented by opening a write only file and dumping results in which is what; however, that was out of scope for this iteration.  I set the data up to be a structured .csv which is not necessary in this case but was convenient.  Fixing this would make this code a lot cleaner and more idiomatically correct, but I put a deadline on myself to finish this by today because I only planned for this portion to take a week and I've already overrun by 3 days.

Had a quick play test and definitely experienced menu fatigue.  Lots of repeated actions... that indicates that I should implement the priority queue.  This is on the edge of complexity I'm willing to take in,  it's not bad on its own but combined with other things the player can do and the amount of control I want to give to them is what really worries me.  This could be a lot more work than I'm willing to do.  Buttoning up the ReadMe now!

#### Progress 5/12/2022 8:30 pm
- EXPAND 1: Expand test suite and restrict object inputs!  Also upgrade docustrings when back in test scripts.  It will be easier to write documentation because I will have a better idea of how to distinguish/categorize them
- EXPAND 3: Add palette logic to processors
- EXPAND 5: Add consolidate method which moves all accounts held into one account.  Potentially put this in a new bank object.
- EXPAND 6: Add ability to remove sell/buy transactions from vendor.  Likely won't be extremely necessary, as right now I can just deplete their stocks.  It may be useful during gameplay to see what actions they can perform at a glance to avoid clutter.
- EXPAND 7: Add transaction class.  This would standardize the transaction form and make the updates to other class objects much more clean.
- EXPAND 8: Add catalogue class.  This would take complexity away from vendor classes and make it easier to track items.
- EXPAND 11: Have a turn limit and small interactions between other "characters", this could add a little flavor to the game every couple turns and reinforce whether or not the player is on track.
- REWORK 1: Replace Pandas catalogue with named tuple, may do this in conjunction with EXPAND 8
- REWORK 2: Rename internal methods with leading underscore (machines, accounts, and all testing)
- REWORK 3: Decide if objects should be held by other objects or just references.  So far vendors are more of references as they are mimicking a catalogue (wouldn't actually have the item, but could source it).  The accounts probably should be direct references to objects as they are being held by each vendor.
- REWORK 4:  Change MoneyAccount to use objects on dunder methods
- REWORK 5:  Move non-self-referential functions out of classes (vendor).  This may be easier accomplished by making the catalogue and transaction classes.  This is a workable short term solution.
-  REWORK 9:  Put in is_processor_ready_for_input() method. Update corresponding logic in basic_tutorial.py in get_all_available_machines_for_placement.
- REWORK 10: Move ledger to write only text file.
- NOTE 1: I have decided to keep the player as a vendor, but will afford them special abilities to make decisions.  This will hopefully cut down on needed code.  May just extend the vendor class to accept user input and allow factory interaction.
- IDEA 1: I am fumbling a bit when looking back through my tests, this feels much more manual than it should be.  It would be great if I could pull all the docustrings and file directories into a relational data structure for a quick view and indexing.  I think this would greatly help with globally scrolling through quickly summarizing the test suite.

Alright... I said I was done, but the priority queue was too good to pass up.  It has been implemented and it makes playing so much more intuitive and responsive.  Probably by the end of the week I'll recreate the ledger writes as well... that way I can get interrupted game sessions and can potentially rework some streaming analysis into this.  This would also be very beneficial if I decided to move this to a web app.  Just got a play test all the way through!  The beginning of the game was difficult, but at the end the tester started to really flow.  I got some good suggestions such as an unlock system for higher level machines.  Even though the barrier could be small, this would likely give more incentive to experiment.  I could also use this mechanic to improve existing machines.  I'm creating a quick Tableau dashboard of the play throughs so I can analyze what people are doing fairly quickly.  I made a Tableau dashboard which isn't too in-depth but is a good starting point.  I need to better engineering the data before I'll spend an appreciable time on a proper dashboard, I'm not fond of analytics in shifting sand data environments.
