from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
print("welcome to the silent auction")

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  #{"Suruchi" : 123, "James" : 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is the {winner} with a bid of ${highest_bid}")

bids = {}
bidding_finished = False
while not bidding_finished:
  name = input("What's your name?")
  price = int(input("What's your bid? $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == 'yes':
    clear()
  


# silent_auction = {}

# again = True
# while again:
#   silent_auction["name"] = input("What's your name?:")
#   silent_auction["bid"] = input("What's your bid?:")
#   answer = input("Are there any other users who want to bid?yes or no ").lower()
#   #clear()
#   if answer == "yes":
#     again = True
#   else:
#     again = False
# highest = 0
# for i in range(1, len(silent_auction)):
#   if silent_auction['bid'][i] > silent_auction['bid'][i-1]:
#     highest = silent_auction['bid'][i-1]
#   else:
#     highest = silent_auction['bid'][i]
# print(f"The highest bid is {highest} and the winner is {silent_auction['bid'][highest]}")

#print(silent_auction)