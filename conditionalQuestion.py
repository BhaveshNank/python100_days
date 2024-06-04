'''
write a program where you are purchasing apples and you have a fix buget in which you
have to buy it. If after deducting that apple price from the money you have, you are left with 50
rupees in your pocket then you can tell alexa to add 1kg of apple to your cart, if you have 70 
rupees left in your pocket after deducting the apple price then you can consider adding it to your
cart otherwise you tell alexa not to add any to your cart. 
'''
applePrice = 10 
budget = 80 
if ((budget-applePrice) > 70 ):
    print("Its okay ill manage, alexa add 1kg apples to my cart")
elif ((budget-applePrice) > 50):
    print("Alexa add 1kg apples to my cart")
else:
    print("No, i do not have the buget to buy an apple")