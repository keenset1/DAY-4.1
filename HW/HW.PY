# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.

#Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.

#This project will be completed individually, though you can feel free to share ideas with your fellow students.

#Once completed, commit the project to github and submit the link to this assignment.
Investment = 500000
Rent = 7500
Loss = 200

def ROI(Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment)*100
    print(ROI)
    
ROI(Investment, Rent, Loss)