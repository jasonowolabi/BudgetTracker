from openpyxl import *
import time

date = time.strftime("%m/%d")
currTime = time.strftime("%I:%M %p")

wb = load_workbook('db.xlsx')
ws = wb.active

balance = ws['B2'].value

def update(item, price):
    item = input("Item> ")
    price = int(input("Price> "))
    ws.append(date, item, price)
    ws['B2'].value = balance - price

def currBalance():
    return balance

wb.save('db.xlsx')

