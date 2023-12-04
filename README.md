# Food Truck Order Menu

   ### CONTENTS
**[The Challenge](#the-challenge)**<br>
**[Starter Code](#starter-code)**<br>
**[Getting Ahead Perhaps](#getting-ahead-perhaps)**<br>
**[Challenge Checklist](#challenge-checklist)**<br>
**[Suggested Additions for Use-Case](#suggested-additions-for-use-case)**<br>

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
- [x] Match item and prompt for quanity
- [x] Request user for continuation of order
- [ ] Iterate customer order
- [ ] Set variables
- [ ] Calculate spaces for clean output :frowning:
- [ ] Create space strings for clean output :frowning:
- [ ] Print the order list in a nice table format
- [ ] Calculate and print total cost

## Getting Ahead Perhaps

Some of the suggested steps seem poorly thought out, even for a beginner class. Surely it is better to teach string handling up front rather than overburdened code. There are several better solutions to creating a clean output for a table on the screen than creating a set of strings to add whitespace. Such solutions would cut out some of the checklist items. My code will match the requested checklist, but comments will indicate a better solution.

## Suggested Additions for Use-Case

### Order Edits/Confirmation

In a use-case scenario, the user should be prompted if they want to edit their order by either removing items or changing quantities. And to confirm their final order before printing.

### Tax

In a use-case scenario, tax should be calculated and included on the receipt.