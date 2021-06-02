from art import logo
from replit import clear
print(logo)
def cal(no1,op,no2):
  if(op=="+"):
    return no1+no2
  elif(op=="-"):
    return no1-no2
  elif(op=="*"):
    return no1*no2
  else:
    return no1/no2
def calculator():
  a=float(input("What's the first number: "))
  print("+\n-\n*\n/\n")
  ends=True
  while ends:
    b=input("Pick an operation: ")
    c=float(input("What's the next number: "))
    d=cal(a,b,c)
    print(f"{a} {b} {c} = {d}")
    e=input(f"Type 'y' to continue calculating with {d} or type 'n' to start a new calculation and press any key for exit: ").lower()
    if (e=="y"):
      a=d
    elif(e=="n"):
      ends=False
      clear()
      calculator()
    else:
      ends=False
calculator()
   




"""another way to make calculator using dictionary

from art import logo
from replit import clear


def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

operations={
"+":add,
"-":sub,
"*":mul,
"/":div
}
def calculator():
  print(logo)
  num1=float(input("What's the first number: "))

  for k in operations:
    print(k)

  a=True
  while a:
    symbol=input("pick an opaeration: ")
    num2=float(input("What's the next number: "))
    function=operations[symbol]
    ans1=function(num1,num2)
    print(f"{num1} {symbol} {num2} = {ans1}")
    k=input(f"Type 'y' to continue with {ans1} , or type 'n' to start a new calculation: ")
    if k=="y":
      num1=ans1
    else:
      a=False
      clear()
      calculator()
calculator()

"""


