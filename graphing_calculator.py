### PLEASE NOTE: All variables with the name “equation” are list structures. All variables of a single
### letter are counting variables (for while loops).

### This initializes the lineEquation variable.
lineEquation = ''

### This function compiles the graph for printing. It does this by iterating through each ‘point’ or square
### on the 21 x 21 graph, calling interpretEquation(equation,column) to retrieve a modified ‘x’ (column)
### value, and comparing it to the y value (row). The result of this comparison determines what object will
### be appended to rowList (a temporary list for each row of the graph). If the modified ‘x’ value and ‘y’
### values are the same or similar, an ‘X’ or ‘O’ will be appended accordingly. If the function call for ‘x’
### returns None, then a blank square will be appended. If the values of either ‘y’ or the unmodified ‘x’
### are 0, then it appends a black square (to represent the axis of the coordinate plane). Finally, if none
### of these conditions are met, then a blank square will be appended. This occurs 21 times for each
### column in the row of the graph. rowList is then joined together and printed on one line. This occurs 21
### times for each row in the graph.
def graphPrinter(equation):
    graphList = []
    for row in range(11,-12,-1):
        rowList = []
        for column in range(-11,12,1):
            output = interpretEquation(equation,column)
            if row == output:
                rowList.append("\033[31mX\033[30m")
            elif output == None:
                if row == 0:
                    rowList.append('■')
                elif column == 0:
                    rowList.append('■')
                else:
                    rowList.append('□')
            elif row == round(float(output)):
                rowList.append("\033[31mO\033[30m")
            elif row == 0 or column == 0:
                rowList.append('■')
            else:
                rowList.append("□")
        graphList.append(rowList)
        print(''.join(rowList))

### This function is called for each point on the 21x21 graph. It uses the cleaned user-inputted equation
### as input. It first checks if the equation list has any embedded lists (which represent parentheses or
### absolute value functions). If an embedded list is detected in the list, the function is recursively called
### with the embedded list used as input in place of the equation. This occurs for each embedded list
### inside the equation, and each embedded list inside each embedded list (crazy, right?). Once each list
### has been isolated, the function evaluates the equation. It first searches for each mathematical
### function present (multiplication, division, exponents, addition, subtraction), and adds that functions’
### position, priority (in accordance with PEMDAS), and functional operation as a list to a list called
### priorityList. Once each function inside the equation list has been detected, the list is sorted in order
### of increasing priority and increasing position (from left to right) in that order. This is done by calling
### dualSort function. Once sorted, this function runs through each item, and evaluates the constants
### (usually number floats) to the left and right of the function by the function. Finally, it replaces these
### three items with the result of the mathematical function (i.e: the equation list [2.5,*,2,-,1] will be
### [5,-,1] after the first iteration of priorityList. This repeats for each item in priorityList. Once the list is
### exhausted (or if there never was anything in the list to begin with), the expected result of the equation
### list should be a single value. This value is returned as the modified ‘x’ value.
def interpretEquation(equation,column):
    lineEquation = list(equation)
    for i in range(len(lineEquation)):
        if isinstance(lineEquation[i],list):
            if lineEquation[i][len(lineEquation[i])-1] == '&':
                lineEquation[i] = lineEquation[i][:len(lineEquation[i])-1]
                lineEquation[i] = abs(interpretEquation(lineEquation[i],column))
            else:
                lineEquation[i] = interpretEquation(lineEquation[i],column)
        elif lineEquation[i] == 'x':
            lineEquation[i] = column
    priorityList = []
    for i in range(len(lineEquation)):
        if lineEquation[i] == '^':
            priorityList.append([1,i,1])
        elif lineEquation[i] == '*':
            priorityList.append([2,i,2])
        elif lineEquation[i] == '/':
            priorityList.append([2,i,3])
        elif lineEquation[i] == '+':
            priorityList.append([3,i,4])
        elif lineEquation[i] == '-':
            priorityList.append([3,i,5])
    priorityList = dualSort(priorityList)
    for i in range(len(priorityList)):
        if priorityList[i][1]!=0:
            if priorityList[i][1]<len(lineEquation):
                if isinstance((lineEquation[(priorityList[i][1])-1]),float) or isinstance((lineEquation[(priorityList[i][1])-1]),int):
                    if isinstance((lineEquation[(priorityList[i][1])+1]),float) or isinstance((lineEquation[(priorityList[i][1])+1]),int):
                        if priorityList[i][2]==1:
                            temp = []
                            for f in range(len(lineEquation)):
                                if f != (priorityList[i][1])-1 and f != (priorityList[i][1])+1:
                                    if f == (priorityList[i][1]):
                                        try:
                                            temp.append((lineEquation[(priorityList[i][1])-1])**(lineEquation[(priorityList[i][1])+1]))
                                        except NegativePowerError:
                                            return
                                    else:
                                        temp.append(lineEquation[f])
                            lineEquation = list(temp)
                            for u in range(i,len(priorityList)):
                                if priorityList[i][1]<priorityList[u][1]:
                                    priorityList[u][1] = priorityList[u][1]-2
                        elif priorityList[i][2]==2:
                            temp = []
                            for f in range(len(lineEquation)):
                                if f != (priorityList[i][1])-1 and f != (priorityList[i][1])+1:
                                    if f == (priorityList[i][1]):
                                        temp.append((lineEquation[(priorityList[i][1])-1]*lineEquation[(priorityList[i][1])+1]))
                                    else:
                                        temp.append(lineEquation[f])
                            lineEquation = list(temp)
                            for u in range(i,len(priorityList)):
                                if priorityList[i][1]<priorityList[u][1]:
                                    priorityList[u][1] = priorityList[u][1]-2
                        elif priorityList[i][2]==3:
                            temp = []
                            for f in range(len(lineEquation)):
                                if f != (priorityList[i][1])-1 and f != (priorityList[i][1])+1:
                                    if f == (priorityList[i][1]):
                                        try:
                                            temp.append((lineEquation[(priorityList[i][1])-1]/lineEquation[(priorityList[i][1])+1]))
                                        except ZeroDivisionError:
                                            return
                                    else:
                                        temp.append(lineEquation[f])
                            lineEquation = list(temp)
                            for u in range(i,len(priorityList)):
                                if priorityList[i][1]<priorityList[u][1]:
                                    priorityList[u][1] = priorityList[u][1]-2
                        elif priorityList[i][2]==4:
                            temp = []
                            for f in range(len(lineEquation)):
                                if f != (priorityList[i][1])-1 and f != (priorityList[i][1])+1:
                                    if f == (priorityList[i][1]):
                                        temp.append((lineEquation[(priorityList[i][1])-1]+lineEquation[(priorityList[i][1])+1]))
                                    else:
                                        temp.append(lineEquation[f])
                            lineEquation = list(temp)
                            for u in range(i,len(priorityList)):
                                if priorityList[i][1]<priorityList[u][1]:
                                    priorityList[u][1] = priorityList[u][1]-2
                        elif priorityList[i][2]==5:
                            temp = []
                            for f in range(len(lineEquation)):
                                if f != (priorityList[i][1])-1 and f != (priorityList[i][1])+1:
                                    if f == (priorityList[i][1]):
                                        temp.append((lineEquation[(priorityList[i][1])-1]-lineEquation[(priorityList[i][1])+1]))
                                    else:
                                        temp.append(lineEquation[f])
                            lineEquation = list(temp)
                            for u in range(i,len(priorityList)):
                                if priorityList[i][1]<priorityList[u][1]:
                                    priorityList[u][1] = priorityList[u][1]-2
    return lineEquation[0]

### This is a sorting algorithm that sorts a list of lists. The embedded lists are sorted by their first value
### and their second value, in that order of priority. This function is called in interpretEquation and returns
### a sorted list as described above.
def dualSort(array):
    Swapped = False
    for n in range(len(array)-1):
        if array[n][0]>array[n+1][0]:
            array[n],array[n+1] = array[n+1],array[n]
            Swapped = True
        elif array[n][0]==array[n+1][0]:
            if array[n][1]>array[n+1][1]:
                array[n],array[n+1] = array[n+1],array[n]
                Swapped = True
    if Swapped == True:
        return dualSort(array)
    else:
        return array

### This function is called in the start function. It takes in the raw user-inputted equation, and returns a
### cleaned/uniform version of the equation for interpretation. First, it searches the list for spaces, and
### removes any it finds by the initialization of a new list and selectively appending non-space values
### the inputted list into the new one. Next, it checks if the length of the list is greater than two, and calls
### the start function again if not (to restart the program for a new list). It then checks if the list starts with
### the values ‘y’ and ‘=‘, and calls the start function if not. After this, it replaces all uppercase ‘X’s with ‘x’
### for consistency, and begins iteration. It first checks if the i value of the list is a digit. If it is, it continues
### to search the next items in the list until the item is not a number. Once this is found, it appends all
### these numbers together, and adds them to the new equation list as a single item. If the item found is
### a mathematical function (*,/,^,-,+), it adds that to the new list (on the rare case that this function is
### the first item in the list, it will append a ‘1’ before appending the function). Next, if the item found is a
### ‘(‘ or a ‘{‘, it will search the next items in the list until a ‘)’ or ‘}’ is found. When that occurs, all the items
### between are appended to the new list as an embedded list to represent parentheses and absolute
### value function respectively. In the case of the later, a ‘&’ is appended to the end of that list to identity
### that it is an absolute value function. Finally, if the input list is exhausted, the function returns the new
### equation list.
def equationClean(equation):
    equationNew = []
    for i in range(len(equation)):
        if equation[i] != ' ':
            equationNew.append(equation[i])
    if len(equationNew) < 2:
        print('\nSyntax Error\n')
        start()
    if (equationNew[0] == 'y' or equationNew[0] == 'Y') and equationNew[1] == '=':
        equation = equationNew[2:]
        equation.append(" ")
        newEquation = []
        for i in range(len(equation)):
            if equation[i] == 'X':
                equation[i] = 'x'
        i=0
        while i < len(equation):
            if equation[i].isdigit() == True:
                tempVar = [equation[i]]
                b=1
                l=1
                while b > 0:
                    if equation[i+b].isdigit() == True:
                        tempVar.append(equation[i+b])
                        b += 1
                    elif equation[i+b] == '.':
                        if l < 2:
                            tempVar.append(equation[i+b])
                            b += 1
                            l += 1
                        else:
                            print("\nSyntax Error\n")
                            start()
                    else:
                        if l == 2:
                            tempVar.append('0')
                        tempVar = ''.join(tempVar)
                        newEquation.append(float(tempVar))
                        equation = equation[b-1:]
                        b=0
                        if equation[i] == '.':
                            equation[i] = '0'
                i+=1
            elif equation[i] == '+' or equation[i] == '-' or equation[i] == '*' or equation[i] == '/' or equation[i] == '^':
                if len(newEquation) == 0 or equation[i-1] == '+' or equation[i-1] == '-' or equation[i-1] == '*' or equation[i-1] == '/' or equation[i-1] == '^':
                    if equation[i] == '-':
                        newEquation.append(float('-1'))
                        newEquation.append('*')
                    else:
                        print('\nSyntax Error\n')
                        start()
                elif equation[i+1]==' ':
                    print("\nSyntax Error\n")
                    start()
                else:
                    newEquation.append(equation[i])
                i+=1
            elif equation[i] == 'x':
                if i == 0:
                    if equation[i+1].isdigit()==False and not(equation[i+1]==')') and not(equation[i+1]=='x'):
                        newEquation.append(equation[i])
                    else:
                        newEquation.append(equation[i])
                        newEquation.append('*')
                        equation[i] = 'X'
                elif equation[i-1].isdigit()==False and not(equation[i-1]==')') and not(equation[i-1]=='x') and equation[i+1].isdigit()==False and not(equation[i+1]=='x') and not(equation[i+1]==')'):
                    newEquation.append(equation[i])
                elif equation[i-1].isdigit() or equation[i-1]==')' or equation[i-1]=='x':
                    newEquation.append('*')
                    newEquation.append(equation[i])
                    if equation[i+1].isdigit() or equation[i+1]==')' or equation[i+1]=='x':
                        newEquation.append('*')
                    equation[i] = 'X'
                else:
                    newEquation.append(equation[i])
                    newEquation.append('*')
                    equation[i] = 'X'
                i+=1
            elif equation[i] == '(':
                j=1
                u=0
                tempVar = []
                try:
                    while j > 0:
                        if i+j>len(equation):
                            print('\nSyntax Error\n')
                            start()
                        elif equation[i+j] == '(':
                            tempVar.append(equation[i+j])
                            u+=1
                            j+=1
                        elif equation[i+j] != ')':
                            tempVar.append(equation[i+j])
                            j+=1
                        elif equation[i+j] == ')':
                            if u <= 0:
                                parEquation = ['y','=']
                                for o in range(len(tempVar)):
                                    parEquation.append(tempVar[o])
                                parEquation = equationClean(parEquation)
                                if len(newEquation) != 0:
                                    if str(newEquation[-1]).isdigit() or (str(newEquation[-1]) =='x') or isinstance((newEquation[-1]),list) or isinstance((newEquation[-1]),float):
                                        newEquation.append("*")
                                newEquation.append(parEquation)
                                equation = equation[i+j-1:]
                                i=1
                                j=0
                            else:
                                tempVar.append(equation[i+j])
                                u = u-1
                                j+=1
                except IndexError:
                    print('\nSyntax Error\n')
                    start()
                i+=1
            elif equation[i] == '{':
                j=1
                u=0
                tempVar = []
                try:
                    while j > 0:
                        if i+j>len(equation):
                            print('\nSyntax Error\n')
                            start()
                        elif equation[i+j] == '{':
                            tempVar.append(equation[i+j])
                            u+=1
                            j+=1
                        elif equation[i+j] != '}':
                            tempVar.append(equation[i+j])
                            j+=1
                        elif equation[i+j] == '}':
                            if u <= 0:
                                parEquation = ['y','=']
                                for o in range(len(tempVar)):
                                    parEquation.append(tempVar[o])
                                parEquation = equationClean(parEquation)
                                if len(newEquation) != 0:
                                    if str(newEquation[-1]).isdigit() or (str(newEquation[-1]) =='x') or isinstance((newEquation[-1]),list) or isinstance((newEquation[-1]),float):
                                        newEquation.append("*")
                                parEquation.append('&')
                                newEquation.append(parEquation)
                                equation = equation[i+j-1:]
                                i=1
                                j=0
                            else:
                                tempVar.append(equation[i+j])
                                u = u-1
                                j+=1
                except IndexError:
                    print('\nSyntax Error\n')
                    start()
                i+=1
            elif equation[i] == " ":
                return newEquation[:len(newEquation)]
            else:
                print("\nSyntax Error\n")
                start()
    else:
        print("\nEquation must be in the format 'y='\n")
        start()

### This function is called when the program needs to be restarted and at the start of the run. This
### function takes in user input for the equation, calls equationClean to clean that equation, and then
### calls graphPrinter to print the graph. At the end, the function calls on itself again to ask for another
### user input.
def start():
    lineEquation = input("Please enter an equation: ")
    lineEquation = equationClean(lineEquation)
    print('\n')
    graphPrinter(lineEquation)
    print('\nGraph of your equation centered at (0,0)')
    print('\n\n\n')
    start()

### This contains the user instructions and the initial call of the start function
if __name__ == "__main__":
    print("Note:\n- Decimals MUST start with a number (.5 is unacceptable)\n- Use '{' and '}' to indicate absolute value\n- Use '^' to indicate exponents\n- The equation must be in the form y=___\n- No other variables than x and y acceptable\n- Spaces are irrelevant\n- 'O' represents approximate solutions\n- 'X' represents exact solutions\n")
    start()
