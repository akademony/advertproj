import tkinter
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Baseball Statkeeper+')
root.grid()

def IntegerMaker():

    strPlayername = playerName.get()
    intG = int(G.get())
    intAB = int(AB.get())
    intR = int(R.get())
    intSingles = int(Singles.get())
    intDoubles = int(Singles.get())
    intTriples = int(Triples.get())
    intHR = int(Hr.get())
    intRbi = int(rbi.get())
    intSB = int(SB.get())
    intBB = int(bb.get())
    intSacf = int(SACF.get())
    intHbp = int(HBP.get())
    intFc = int(Fc.get())


    H = intSingles+intDoubles+intTriples+intHR
    OBP = (H+intBB+intHbp)/(intAB+intBB+intHbp+intSacf)
    OBP = round(OBP, 3)
    BA = H/intAB
    BA = round(BA, 3)
    SLG = (intSingles + (intDoubles * 2) + (intTriples * 3) + (intHR * 4)) / intAB
    SLG = round(SLG, 3)
    OPS = OBP + SLG
    OPS = round(OPS, 3)

    fh = open(f'Stats_{strPlayername}.txt', 'w')
    fh.write(f'Player Name: {playerName.get()}\nGames Played: {intG}\nBatting Average: {BA}\nOn Base %: {OBP}\nSlugging %: {SLG}'
             f'\nOPS: {OPS}\nAt Bats: {intAB}\nRuns: {intR}\nHits: {H}\nSingles: {intSingles}\nDoubles: {intDoubles}'
             f'\nTriples: {intTriples}\nHomeruns: {intHR}\nReached on Error/Fielders Choice: {intFc}'
             f'\nRuns batted in: {intRbi}\nStolen Bases: {intSB}\nWalks: {intBB}\nSacrifice Flies: {intSacf}'
             f'\nHit By Pitch: {intHbp}'
             )
    fh.close()


playerName = Entry(root, width=50)
playerName.grid(row=1, column=1)
playerNameLabel = Label(root, width=50, text="Player's Name:")
playerNameLabel.grid(row=1, column=0)


G = Entry(root, width=50)
G.grid(row=2, column=1)
gLabel = Label(root, width=50, text='Games:')
gLabel.grid(row=2, column=0)

AB = Entry(root, width=50)
AB.grid(row=3, column=1)
abLabel = Label(root, width=50, text='At Bats:')
abLabel.grid(row=3, column=0)

R = Entry(root, width=50)
R.grid(row=4, column=1)
rLabel = Label(root, width=50, text='Runs:')
rLabel.grid(row=4, column=0)

Singles = Entry(root, width=50)
Singles.grid(row=5, column=1)
singlesLabel = Label(root, width=50, text='1B:')
singlesLabel.grid(row=5, column=0)

Doubles = Entry(root, width=50)
Doubles.grid(row=6, column=1)
doublesLabel = Label(root, width=50, text='2B:')
doublesLabel.grid(row=6, column=0)

Triples = Entry(root, width=50)
Triples.grid(row=7, column=1)
triplesLabel = Label(root, width=50, text='3B:')
triplesLabel.grid(row=7, column=0)

Hr = Entry(root, width=50)
Hr.grid(row=8, column=1)
hrLabel = Label(root, width=50, text='HR:')
hrLabel.grid(row=8, column=0)

rbi = Entry(root, width=50)
rbi.grid(row=9, column=1)
rbiLabel = Label(root, width=50, text='RBI:')
rbiLabel.grid(row=9, column=0)

SB = Entry(root, width=50)
SB.grid(row=10, column=1)
sbLabel = Label(root, width=50, text='SB:')
sbLabel.grid(row=10, column=0)

bb = Entry(root, width=50)
bb.grid(row=11, column=1)
bbLabel = Label(root, width=50, text='BB:')
bbLabel.grid(row=11, column=0)

SACF = Entry(root, width=50)
SACF.grid(row=12, column=1)
sacfLabel = Label(root, width=50, text='SACF:')
sacfLabel.grid(row=12, column=0)

HBP = Entry(root, width=50)
HBP.grid(row=13, column=1)
hbpLabel = Label(root, width=50, text='HBP:')
hbpLabel.grid(row=13, column=0)

Fc = Entry(root, width=50)
Fc.grid(row=14, column=1)
fcLabel = Label(root, width=50, text='FC:')
fcLabel.grid(row=14, column=0)

Label(root, width=50, text='Instagram: @michael.antooo').grid()
ListButton = Button(root, width=50, text='Download as .txt file', command=IntegerMaker).grid(row=15, column=1)

title = Label(root, text='Baseball Player Stat Keeper+', font=190)
title.grid(row=0, column=0)


root.resizable(0, 0)
root.mainloop()