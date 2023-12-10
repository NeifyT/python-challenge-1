# Food Truck Order Menu

   ### CONTENTS
**[The Challenge](#the-challenge)**<br>
**[Starter Code](#starter-code)**<br>
**[Getting Ahead Perhaps](#getting-ahead-perhaps)**<br>
**[Challenge Checklist](#challenge-checklist)**<br>
**[Graded Assignment](#graded-assignment)**<br>
**[Suggested Additions for Use-Case](#suggested-additions-for-use-case)**<br>
**[Rewriting for Additional Practice](#rewriting-for-additional-practice)**<br>

## The Challenge

Provide a continuous food order system for a food truck. The system should include a main menu of categories and associated submenus for each category. The main menu categories are printed on the screen, requesting the user to input a number from the main menu to view the submenus. The submenu is then printed on the screen, asking the user to input a number to order a specific item. Upon successful option input for an item, the user is prompted to indicate the quantity of the order (with a default of 1).

Following an initial order, the user is prompted if they would like to continue ordering (‘y’ or ‘Y’ for yes and ‘n’ or ‘N’ for no). The process is repeated if they answer yes. If they answer no, then a receipt is printed with a list of all the order items, their price, the quantity ordered, and the total cost.

Error checking of user input is paramount. Except for the quantity of items (which defaults to 1), other inputs should be re-prompted for any incorrect entries.

## Starter Code

The starter code is provided by the course creators. It contains a simple menu consisting of 28 distinct items within four main food categories, with some items as categories with even more items. These items are contained in nested dictionaries, with the price being the ultimate value and the item name as the key.

The code contains initial looping structures that print the main menu items with an associated menu item number that will be used to match user input. It also contains the first set of input and checks for main menus for looping and printing submenus. Note that the submenus of submenus are concatenated into a single submenu.

The code also contains comments indicating what portions of the program must still be completed. See [Challenge Checklist](#challenge-checklist) for paraphrased steps.

## Challenge Checklist

- [x] Initialize an empty order list (dictionaries)
- [x] Request user input of menu item number
- [x] Validate user input
- [x] Match item and prompt for quantity
- [x] Request user for continuation of order
- [x] Iterate customer order
- [x] Set variables
- [x] Calculate spaces for clean output :frowning:
- [x] Create space strings for clean output :frowning:
- [x] Print the order list in a nice table format
- [x] Calculate and print total cost

## Getting Ahead Perhaps

Some of the suggested steps seem poorly thought out, even for a beginner class. Surely it is better to teach string handling[^1] up front rather than overburdened code. There are several better solutions to creating a clean output for a table on the screen than creating a set of strings to add whitespace. Such solutions would cut out some of the checklist items. My code will match the requested checklist, but comments will indicate a better solution.

 [^1]: I note that formatted strings were taught in the first class and reiterated in the other two. Could easily have covered padding within just another minute or two.

## Graded Assignment

The graded assignment (menu.py) should be run from the command line:

```
python menu.py
```

## Suggested Additions for Use-Case

### Order Edits/Confirmation

In a use-case scenario, the user should be prompted if they want to edit their order by either removing items or changing quantities. And to confirm their final order before printing.

### Subtotals

Subtotals or amounts for each item are usually displayed when there is a quantity of those items to be calculated.

### Tax

In a use-case scenario, tax should be calculated and included on the receipt.

### Kiosk

Generally an automated food order machine would never exit. It just start back at the beginning after a patron places their order so the next patron can place an order.

## Rewriting for Additional Practice

Not intended to be graded but for my own practice the advancedmenu.py demonstrates the same type of system done my way with only the menu dictionary as a starter.  This could be run from the command line:

```
python advancedmenu.py
```

This will prompt the owner to enter the current tax rate, and then enter a Kiosk mode (or continuous loop) that must be exited with a keyboard interrupt (Ctrl + C). It will then allow a patron to place an order of one or more items, until the patron is done.  It will output the totals for the order, and cycle back to the start for the next patron.