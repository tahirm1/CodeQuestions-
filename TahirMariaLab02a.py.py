#first python program
#you will be able to enter the temperature in F and see what that converts to in C

def main():
    #Enter your first and last name
    firstName= input("Type your first name")
    lastName= input("Type your last name")

    #Enter the temperature in F
    farenheit= (int)(input("What is the current temperature in farenheit?"))

    #equation to convert Farenheit to Celsius
    celsius=(farenheit-32)*(5/9)
    
    for x in range (0, 10):
        print(firstName," ", lastName, "The temperature in celsius is", celsius+x,"degrees")


    
