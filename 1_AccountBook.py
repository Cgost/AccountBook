'''
項目
account_name
收入 支出
money
結餘
total
備註
comment
'''
import os
import datetime

ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
total = 0
class AccountBill():
    """docstring for AccountBill"""
    def __init__(self, date, name):
        self.date   = date
        self.name   = name
        self.bill   = 0
        self.note   = "no comment"
        
    def money(self, amount):
        self.bill += amount

    def comment(self, text):
        if text == none:
            self.note = "no comment"
        else:
            self.note = text


# ex:
'''
acct1 = AccountBill("90/11/30", "Justing")

acct1.money(100)
acct1.comment()

print("number:", acct1.number)
print("name:", acct1.name)
print("money:", acct1.blance)
'''
def ReadRecord(account_name):
    account_name += ".txt"
    f = open("Saved/" + account_name, "r", encoding="utf-8")
    account_record = f.read()
    f.close()

def SaveRecord(account_name, date, bill, comment, mode):
    dname = "Saved"
    if not os.path.exists(dname):
      os.makedirs(dname)
    f = open(dname + "/" + account_name + ".txt", "w+")
    #f.write("時間:" + date + "\n金額:" + str(bill) + "\n備註:" + comment + "\n")
    f.write("%10s |%8d  | %s \n" %(date, bill, comment))
    f.close()
    if bill>=0:
        f = open(dname+"/"+account_name+"_expense.txt", "w+")
        f.write("0")
        f.close()
        f = open(dname+"/"+account_name+"_income.txt", "w+")
        f.write(str(bill)+"\n")
        f.close()
    else:
        f = open(dname+"/"+account_name+"_income.txt", "w+")
        f.write("0")
        f.close()
        f = open(dname+"/"+account_name+"_expense.txt", "w+")
        f.write(str(bill)+"\n")
        f.close()
    if mode == 0:
        if not os.path.exists("account_list.txt"):
            f = open("account_list.txt", "a")
            f.write(account_name)
            f.close()

        else:
            f = open("account_list.txt", "a")
            f.write("\n" + account_name)
            f.close()

def show_list():
    print("+----------+")
    print(" 1.列出項目")
    print(" 2.查詢項目")
    print(" 3.新增項目")
    print(" 4.修改項目")
    print(" 5.所有項目")
    print("+----------+")

def show_account():
    account_list = []
    if not os.path.exists("account_list.txt"):
        print("尚無紀錄項目")
    else:
        f = open("account_list.txt", "r", encoding="utf-8")
        s = f.read()
        f.close()
        string = ""
        for i in s:
            if i == "\n":
                account_list.append(list(string))
                string = ""
            else:
                string += i
        account_list.append(list(string))
        for name in account_list:
            for word in name:
                print(word, end="")
            print()

    
    return account_list

def search_account():
    account_name = input("請輸入項目名稱:")
    if not os.path.exists("Saved/"+account_name+".txt"):
        print("查無此項目")
    else:
        f = open("Saved/"+account_name+".txt", "r")
        s = f.read()
        f.close()
        account_list = []
        string = ""
        for i in s:
            if i == "\n":
                account_list.append(list(string))
                string = ""
            else:
                string += i
        account_list.append(list(string))

        print("=======[時間]=======|==[金額]==|=========[備註]=========\n", end="")
        for name in account_list:
            for word in name:
                print(word, end="")
            print()


def creat_account():
    account_name = ""
    date = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    bill = 0
    comment = ""
    mode = 0

    account_name = input("項目:")
    if os.path.exists("Saved/"+account_name+".txt"):
        print("\n項目已存在")
    else:
        bill     = int(input("金額:"))
        comment      = input("備註:")
        SaveRecord(account_name, date, bill, comment, mode)

def modify_account():
    account_name = ""
    date = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    bill = 0
    comment = ""
    mode = 1
    account_name = input("項目:")
    if not os.path.exists("Saved/"+account_name+".txt"):
        print("查無此項目")
    else:
        bill         = int(input("金額:"))
        comment          = input("備註:")
        SaveRecord(account_name, date, bill, comment, mode)    

def all_account():
    account_list = []
    if not os.path.exists("account_list.txt"):
        print("尚無紀錄項目")
    else:
        f = open("account_list.txt", "r", encoding="utf-8")
        s = f.read()
        f.close()
        print("%5s   |%10s        |   %-4s |   %s    |" %("項目", "時間", "金額", "備註"))
        string = ""
        for i in s:
            if i == "\n":
                f = open("Saved/"+string+".txt", "r")
                s2 = f.read()
                f.close()
                #print("========="+string+"=========\n"+s2)
                print("%-10s %s" %(string, s2))
                string = ""
            else:
                string += i
        f = open("Saved/"+string+".txt", "r")
        s2 = f.read()
        f.close()
        #print("========="+string+"=========\n"+s2)
        print("%-10s %s" %(string, s2))
        get_money(s)

def get_money(s):
    account_name = s
    income       = 0
    expense      = 0
    blance       = 0
    string = ""
    for i in s:
        if i == "\n":
            f = open("Saved/"+string+"_income.txt", "r")
            bill = f.read()
            f.close()
            income += int(bill)
            f = open("Saved/"+string+"_expense.txt", "r")
            bill = f.read()
            f.close()
            expense += int(bill)
            string = ""
            blance += int(bill)
        else:
            string += i
    f = open("Saved/"+string+"_income.txt", "r")
    bill = f.read()
    f.close()
    income += int(bill)
    f = open("Saved/"+string+"_expense.txt", "r")
    bill = f.read()
    f.close()
    expense += int(bill)
    string = ""
    blance += int(bill)

    print("\n\n總收入: %10d" %(income))
    print("總支出: %10d" %(expense))
    print("=======================")
    print("淨額:   %10d" %(blance))


def main():
    account_list = []

    show_list()
    list_num = int(input("choose action:"))
    os.system("cls")
    if list_num == 1:
        show_account()
    elif list_num == 2:
        search_account()
    elif list_num == 3:
        creat_account()
    elif list_num == 4:
        modify_account()
    elif list_num == 5:
        all_account()

while True:
    os.system("cls")
    main()
    print()
    os.system("pause")
