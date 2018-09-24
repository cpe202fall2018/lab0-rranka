def weight_on_planets():
  # weight = input("What do you weigh on Earth? ")
 #  weightFloat = float(weight) #float casting
  
# marsWeight = weightFloat * 0.38
 #  jupiterWeight = weightFloat * 2.4
   
   weight = input("What do you weigh on earth? ")
   weightFloat = float(weight) #casting
   print ("\nOn Mars you would weigh ", weightFloat*0.38, " pounds.\n" + "On Jupiter you would weigh ", weightFloat*2.34, " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()
