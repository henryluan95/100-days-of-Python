from art import logo

print(logo)
bidding_log = {}
continue_bidding = True
while(continue_bidding):
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: "))
    bidding_log[user_name] = user_bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if(other_bidders == "no"):
        continue_bidding = False

highest_bidder = ""
highest_bid = 0
for bidder in bidding_log:
    if(bidding_log[bidder] > highest_bid):
        highest_bidder = bidder
        highest_bid = bidding_log[bidder]

print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')

