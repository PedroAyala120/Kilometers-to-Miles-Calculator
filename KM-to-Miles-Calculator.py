#The user will enter kilometers and the program will calculate the miles
#Pedro Ayala

#definition of main
def main():
   kilometers = float(input('Input the kilometers:'))  #User input for kilometers

   show_miles(kilometers)      #call function to calculate and print miles

#definition of the function to calculate and print miles
def show_miles(kilometers):
   miles = kilometers * 0.6214     #formula for miles conversion

   print(kilometers, 'km is: ', miles, 'mi')   #print miles

main()  #return to main
