data={
    "143141":{'balance':10000,'pin':14141,'History':[]},
    "143142":{'balance':20000,'pin':14142,'History':[]},
    "143143":{'balance':30000,'pin':14143,'History':[]},
    "143144":{'balance':40000,'pin':14144,'History':[]},
    "143145":{'balance':50000,'pin':14145,'History':[]},
    "143146":{'balance':60000,'pin':14146,'History':[]},
    "143147":{'balance':70000,'pin':14147,'History':[]},
}

acc_num=None
loign_status=False

def welcome():
    print("Welcome to the ATM").center(40,"-")

def menu():
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.View Transation")
    print("5.Exit")


def login_account(acc,pin):
    if acc in data:
        if data[acc]['pin']==pin:
            acc_num=acc
            print("Login successful")
        else:
            print("Invalid pin")
    else:
        print("Invalid Account number")
        
