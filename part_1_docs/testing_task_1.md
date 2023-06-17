### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # the CardGame class is empty 



  def check_for_ace(self, card):
    # on the line below, there is an '=' missing from the statement, so we are assigning card.value with the value of 1 rather than checking if it is equal to '== 1'
    if card.value = 1:
      return True
      # below there's a colon missing from else 
    else
      return False
   
# on the line below, there is a spelling error on 'def' 
# inside the parentheses there is a comma missing from between two parameters 'card1, card2'
  dif highest_card(self, card1 card2):
  # on the line below there is no indentation so the if statement is not within the function being defined. 
  if card1.value > card2.value:
    # below it is returning the wrong variable name, should be returning card1 instead of just card
    return card
  else:
    return card2
  

# the indentation of the function below is outside of the CardGame class, so therefore isn't a method recognised within the class.
def cards_total(self, cards):
  # the total variable below hasn't been assigned a value 
  total
  for card in cards:
    total += card.value
  # the problem below is the indentation of the return, where it currently is placed it would only return the value for the first iteraton done within the loop and then stop the loop entirely.
    return "You have a total of" + total

  
```
