matrix = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, "G"],
    [0, 1, 0, 1, 0],
    ["I", 1, 1, 1, 0]
]

# opou to I h arxh mas kai opou to G o prorismos mas
# Me ton 1 simbolizoume ta tetragonakia pou exoume prosbasi kai opou 0 ta tetragwnakia opou den exoume prosbasi
u=0
CurrentCost = 0
BestCost = 100  # ena BestCost pou sigoura 8a allaksei
BestState = []  # To BestState tha periexei thn diadromh me to ligotero kostos
CurrentState = []  # To CurrentState einai h pio prosfath diadromh
CurrentStates = []
ChildrenStates = []  # h pi8anes pories mas
tempChildrenstates= []




for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "I":
            StartX = i
            StartY = j

while True:


    if StartY + 1 <= 4:

        if matrix[StartX][StartY + 1] == "G" or matrix[StartX][StartY + 1] == 1:

            Potitions = [StartX, StartY + 1]
            tempChildrenstates.append(Potitions)



    if StartY - 1 >= 0:

        if matrix[StartX][StartY - 1] == "G" or matrix[StartX][StartY - 1] == 1 :

            Potitions = [StartX, StartY - 1]
            tempChildrenstates.append(Potitions)




    if StartX - 1 >= 0:

        if matrix[StartX - 1][StartY] == "G" or matrix[StartX - 1][StartY] == 1:

            Potitions = [StartX - 1, StartY]
            tempChildrenstates.append(Potitions)



    if StartX + 1 <= 3:

        if matrix[StartX + 1][StartY] == "G" or matrix[StartX + 1][StartY] == 1 :

            Potitions = [StartX + 1, StartY]
            tempChildrenstates.append(Potitions)



    for i in CurrentState:
        if (i in tempChildrenstates):
            tempChildrenstates.remove( i )

    ChildrenStates = tempChildrenstates.copy()
    tempChildrenstates.clear()
    
    if len(ChildrenStates) == 0 :
        if len(CurrentStates) !=0:
            if CurrentCost < BestCost:
                BestState.clear()
                BestState = CurrentState.copy()
                BestCost = CurrentCost
                CurrentState.clear()
                CurrentState = CurrentStates.pop()
                ChildrenStates.append( CurrentState[-1].copy() )
                CurrentState = CurrentState[:-1]
                CurrentCost = len( CurrentState )
            else:
                CurrentState.clear()
                CurrentState = CurrentStates.pop()
                ChildrenStates.append( CurrentState[-1].copy() )
                CurrentState = CurrentState[:-1]
                CurrentCost = len( CurrentState )


    if len( ChildrenStates ) > 1:
        temp = CurrentState.copy()

        for i in range(len(ChildrenStates)):

            temp.append(ChildrenStates.pop())
            CurrentStates.append(temp.copy())
            temp.clear()
            temp = CurrentState.copy()


        CurrentState.clear()
        CurrentState = CurrentStates.pop()
        ChildrenStates.append(CurrentState[-1].copy())
        CurrentState = CurrentState[:-1]

        CurrentCost = len( CurrentState )


    if  len(CurrentStates) == 0 and len(ChildrenStates) == 0:

        if CurrentCost < BestCost:
            BestState.clear()
            BestState = CurrentState.copy()
            BestCost = CurrentCost
        break

    if len(ChildrenStates) != 0 :

        Positions = ChildrenStates.pop()
        CurrentState.append(Positions)

        StartX = Positions[0]
        StartY = Positions[1]
        CurrentCost = CurrentCost + 1

print("H kaliteri diadromh",BestState,"to kostos tis ",BestCost)
