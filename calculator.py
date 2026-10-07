HISTORY_FILE="history.txt"

def save_to_history(equation , result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()
        

def show_history():
    file = open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines)==0:
        print("No History Found")
    else :
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("History cleared")

def calculate(user_input):
    parts = user_input.split()
    if len(parts)!= 3:
        print("Invalid input, Use format: num operator num (e.g 8 + 8)")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op =="+":
        result = num1 + num2
    elif op =="-":
        result = num1 - num2
    elif op =="*":
        result = num1 * num2  
    elif op =="/":
        if num2 == 0:
            print("Not divisible by 0")
            return
        result = num1 / num2          
    else:
        print("Invalid operatorn, Use only + - * /")
        return
    
    if int(result)==result:
        result = int(result)
    print("Result",result)    
    save_to_history(user_input,result)

def main():
    print("---SIMPLE CALCULATOR THAT SAVES HISTORY")    
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear, exit)")
        if user_input=="exit":
            print("GOOD BYE")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)        
main()