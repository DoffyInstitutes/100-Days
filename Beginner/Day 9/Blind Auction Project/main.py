from art import logo
print(logo)

bids = {}
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def bidding():
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

def continueBid():
    response = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if response == "no":
        return False
    else:
        return True

def checkWinner():
    initial=0
    highest_bidder=""
    for bidder in bids:
        if bids[bidder]>initial:
            initial=bids[bidder]
            highest_bidder=bidder
    print(f"The winner is {highest_bidder} with a bid of {initial}")

bidding()
continueBidding = continueBid()
while continueBidding:
    print("\n" * 20)
    bidding()
    continueBidding = continueBid()

checkWinner()

#max function python - max(fruits, key=fruits.get)