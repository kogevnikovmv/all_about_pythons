class Doska():
    def __init__(self):
        doska=[[1,8,"empty"],[2,8,"empty"],[3,8,"empty"],[4,8,"empty"],[5,8,"empty"],[6,8,"empty"],[7,8,"empty"],[8,8,"empty"],
        [1,7,"empty"],[2,7,"empty"],[3,7,"empty"],[4,7,"empty"],[5,7,"empty"],[6,7,"empty"],[7,7,"empty"],[8,7,"empty"],
        [1,6,"empty"],[2,6,"empty"],[3,6,"empty"],[4,6,"empty"],[5,6,"empty"],[6,6,"empty"],[7,6,"empty"],[8,6,"empty"],
        [1,5,"empty"],[2,5,"empty"],[3,5,"empty"],[4,5,"empty"],[5,5,"empty"],[6,5,"empty"],[7,5,"empty"],[8,5,"empty"],
        [1,4,"empty"],[2,4,"empty"],[3,4,"empty"],[4,4,"empty"],[5,4,"empty"],[6,4,"empty"],[7,4,"empty"],[8,4,"empty"],
        [1,3,"empty"],[2,3,"empty"],[3,3,"empty"],[4,3,"empty"],[5,3,"empty"],[6,3,"empty"],[7,3,"empty"],[8,3,"empty"],
        [1,2,"empty"],[2,2,"empty"],[3,2,"empty"],[4,2,"empty"],[5,2,"empty"],[6,2,"empty"],[7,2,"empty"],[8,2,"empty"],
        [1,1,"empty"],[2,1,"empty"],[3,1,"empty"],[4,1,"empty"],[5,1,"empty"],[6,1,"empty"],[7,1,"empty"],[8,1,"empty"]]

        self.doska=doska

    def smena_hoda(self, color):       
        if color=="black":  
            return "white"
        else:
            return "black"



        
    def move(self, color):
        ABV=["a","b","c","d","e","f","g","h"]
        klon_doski=self.doska
        correct_hod=None    
        while correct_hod!=True: # Если ввести две буквы или цифра+буква - то ошибка
            correct_figura=None
            while correct_figura!=True:
                xyOLD=input("Выберите фигуру которую хотите переместить, формат БУКВА+ЦИФРА:\n")
                if xyOLD[0] not in ABV: # Если ввести две буквы или цифра+буква - то ошибка
                    correct_figura=False
                    print("Вы выбрали фигуру 'вне поля'...")
                    break
                xOLD=int(ABV.index(xyOLD[0]))+1
                yOLD=int(xyOLD[1])
                if 8<xOLD or yOLD>8:
                    correct_figura=False
                    print("Вы выбрали фигуру 'вне поля'...")
                    break
                for i in self.doska:
                    if xOLD==i[0] and yOLD==i[1]:    
                        if i[2]=="empty":
                            correct_figura=False
                            print("вы выбрали пустую клетку")
                        elif i[2].color!=color:
                            print("Вы выбрали фигуру не вашего цвета")
                            correct_figura=False
                        elif i[2].color==color: #Вы выбрали вашу фигуру
                            correct_figura=True
                            figura=i[2] # теперь figura как бы у вас в руках)
                        else:
                            print("Произошла неведомая хрень при выборе фигуры, которую хотите переместить")
                    else:
                        continue

            correct_figura=None
        
            while correct_figura!=True:
                print("Для отмены хода введите 'отмена'.")
                xyNEW=input("Введите ваш ход в формате БУКВА(ENG)+ЦИФРА:\n")
                if xyNEW=="отмена":
                    print("Отмена хода")
                    correct_hod=False
                    correct_figura=True
                else:
                    xNEW=int(ABV.index(xyNEW[0]))+1
                    yNEW=int(xyNEW[1])
                    if 8<xNEW or yNEW>8:
                        correct_figura=False
                        print("Вы выбрали фигуру 'вне поля'...")
                        break
                    for i in self.doska:
                            if xNEW==i[0] and yNEW==i[1]:
                                if i[2]=="empty" or i[2].color!=color:
                                    correct_figura=figura.hod(xOLD, yOLD, xNEW, yNEW, klon_doski)
                                    correct_hod=True
                                    if correct_figura==None:
                                        print("не верный ход)")
                                elif i[2].color==color:
                                     correct_figura=False
                                     print("вы выбрали клетку со своей фигурой")
                                else:
                                    print("Произошла неведомая хрень при выборе фигуры, которую хотите переместить")
                            else:
                                continue
        
                        
        for i in self.doska:                   
                if xOLD==i[0] and yOLD==i[1]:   
                    i[2]="empty"               
                else:
                    continue
        for i in self.doska:
                if xNEW==i[0] and yNEW==i[1]:
                    i[2]=figura
                else:
                    continue
        
    def __str__(self):
        rep=self.doska
        return rep

    def rasstanovka(self):
        color="black"
        for i in range(8):
            for kv in self.doska[8:16]:
                kv[2]=Peshka(color)
        
        self.doska[0][2]=Lada(color)
        self.doska[7][2]=Lada(color)
        self.doska[1][2]=Kon(color)
        self.doska[6][2]=Kon(color)
        self.doska[2][2]=Slon(color)
        self.doska[5][2]=Slon(color)
        self.doska[3][2]=Dama(color)
        self.doska[4][2]=Korol(color)
        
        color="white"
        for i in range(8):
            for kv in self.doska[48:56]:
                kv[2]=Peshka(color)
      
        self.doska[56][2]=Lada(color)
        self.doska[63][2]=Lada(color)
        self.doska[57][2]=Kon(color)
        self.doska[62][2]=Kon(color)
        self.doska[58][2]=Slon(color)
        self.doska[61][2]=Slon(color)
        self.doska[59][2]=Dama(color)
        self.doska[60][2]=Korol(color)
        
    def display(self):
        rep="8|"
        count=0
        aa=["7","6","5","4","3","2","1"]
        for kvadrat in self.doska:
            if count==8:
                rep=rep+"\n"+aa[0]+"|"
                aa=aa[1:]
                count=0
            if "empty" in kvadrat:
                    rep+="_|"
                    
            else:   
                rep+=str(kvadrat[2])
            count+=1
        print(rep)
        print(" |a|b|c|d|e|f|g|h")

#    def screen(self): #очистка экрана после хода, не работает в IDLE
#        import os
#        os.system('cls')

        #[["a","8","empty"],["b","8","empty"],["c","8","empty"],["d","8","empty"],["e","8","empty"],["f","8","empty"],["g","8","empty"],["h","8","empty"]],
        #[["a","7","empty"],["b","7","empty"],["c","7","empty"],["d","7","empty"],["e","7","empty"],["f","7","empty"],["g","7","empty"],["h","7","empty"]],
        #[["a","6","empty"],["b","6","empty"],["c","6","empty"],["d","6","empty"],["e","6","empty"],["f","6","empty"],["g","6","empty"],["h","6","empty"]],
        #[["a","5","empty"],["b","5","empty"],["c","5","empty"],["d","5","empty"],["e","5","empty"],["f","5","empty"],["g","5","empty"],["h","5","empty"]],
        #[["a","4","empty"],["b","4","empty"],["c","4","empty"],["d","4","empty"],["e","4","empty"],["f","4","empty"],["g","4","empty"],["h","4","empty"]],
        #[["a","3","empty"],["b","3","empty"],["c","3","empty"],["d","3","empty"],["e","3","empty"],["f","3","empty"],["g","3","empty"],["h","3","empty"]],
        #[["a","2","EMPTY"],["b","2","empty"],["c","2","empty"],["d","2","empty"],["e","2","empty"],["f","2","empty"],["g","2","empty"],["h","2","empty"]],
        #[["a","1","empty"],["b","1","empty"],["c","1","empty"],["d","1","empty"],["e","1","empty"],["f","1","empty"],["g","1","empty"],["h","1","empty"]]

class Peshka():
    def __init__(self, color):
        self.color=color
        self.first_hod=False #первый ход
        
    def __str__(self):
        if self.color=="white":
            rep="П|"
            return rep
        else:
            rep="P|"
            return rep
    def hod(self, xOLD, yOLD, xNEW, yNEW, klon_doski):
        if self.color=="white":
            yOLD=-yOLD
            yNEW=-yNEW
        if xOLD==xNEW and 8>=abs(yNEW)==abs(yOLD-2) and self.first_hod==False:
            for i in klon_doski:                   
                if xNEW==i[0] and abs(yOLD-1)==i[1] and i[2]=="empty":
                    print("перемещаю фигуру")
                    self.first_hod=True
                    return True
                elif xNEW==i[0] and abs(yOLD-1)==i[1] and i[2]!="empty":
                    print("не первый ход или на рути другая фигура")
                    return False
        elif xOLD==xNEW and 8>=abs(yNEW)==abs(yOLD-1):
            for i in klon_doski:                   
                if xNEW==i[0] and abs(yNEW)==i[1] and i[2]=="empty":
                    print("перемещаю фигуру")
                    self.first_hod=True
                    return True
        elif abs(xNEW-xOLD)==1 and 1<=xNEW<=8 and 8>=abs(yNEW)==abs(yOLD-1):
            for i in klon_doski:
                if xNEW==i[0] and abs(yNEW)==i[1] and i[2].color!=self.color:
                    self.first_hod=True
                    print("атакую!")
                    return True             
        else:
            print("Не верный ход")
            return False
         

class Lada():
    def __init__(self, color):
        self.color=color
        
    def __str__(self):
        if self.color=="white":
            rep="Л|"
            return rep
        else:
            rep="L|"
            return rep
    def hod(self, xOLD, yOLD, xNEW, yNEW, klon_doski):
        if 1<=yNEW==yOLD<=8 and 1<=xNEW<=8: # ход по иксу\горизонтали
            lada_kol_hodov=abs(xNEW-xOLD)
            if xNEW>xOLD: # ход направо по горизонтали
                z=xOLD
                while lada_kol_hodov!=0:
                    lada_kol_hodov=lada_kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z+1 and fig[1]==yOLD:
                            z=z+1
                            if fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура)")
                                return False
            elif xNEW<xOLD: # ход налево по горизонтали
                z=xOLD
                while lada_kol_hodov!=0:
                    lada_kol_hodov=lada_kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z-1 and fig[1]==yOLD:
                            z=z-1
                            if fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура)")
                                return False
        elif 1<=xNEW==xOLD<=8 and 1<=yNEW<=8: # ход по игрику\вертикали
            lada_kol_hodov=abs(yNEW-yOLD)
            if yNEW>yOLD: # вверх
                z=yOLD
                while lada_kol_hodov!=0:
                    lada_kol_hodov=lada_kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==xOLD and fig[1]==z+1:
                            z=z+1
                            if fig[1]!=yNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура)")
                                return False
            elif yNEW<yOLD: # ход вниз
                z=yOLD
                while lada_kol_hodov!=0:
                    lada_kol_hodov=lada_kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==xOLD and fig[1]==z-1:
                            z=z-1
                            if fig[1]!=yNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
        else:
            print("ошибка, дааааа")

    def deystvie(self, xNEW, yNEW, klon_doski): # проверяет конечную точку пустая/враг/свой и пременяет соответствующее действие
        for it in klon_doski:
            if it[0]==xNEW and it[1]==yNEW and it[2]=="empty":
                print("пермещаю фигуру")
            elif it[0]==xNEW and it[1]==yNEW and it[2].color!=self.color:
                print("атакую!")
            else:
                continue




class Kon():
    def __init__(self, color):
        self.color=color
        
    def __str__(self):
        if self.color=="white":
            rep="к|"
            return rep
        else:
            rep="K|"
            return rep
    def hod(self, xOLD, yOLD, xNEW, yNEW, klon_doski):
        if abs(yOLD-yNEW)==3 and abs(xOLD-xNEW)==1:
            self.deystvie(xNEW, yNEW, klon_doski)
            return True
        elif abs(yOLD-yNEW)==1 and abs(xOLD-xNEW)==3:
            self.deystvie(xNEW, yNEW, klon_doski)
            return True
        else:
            print("ошибка в hod")
    def deystvie(self, xNEW, yNEW, klon_doski): # проверяет конечную точку пустая/враг/свой и пременяет соответствующее действие
        for it in klon_doski:
            if it[0]==xNEW and it[1]==yNEW and it[2]=="empty":
                print("пермещаю фигуру")
            elif it[0]==xNEW and it[1]==yNEW and it[2].color!=self.color:
                print("атакую!")
            else:
                continue
            

    
class Slon():
    def __init__(self, color):
        self.color=color
        
    def __str__(self):
        if self.color=="white":
            rep="С|"
            return rep
        else:
            rep="S|"
            return rep
    def hod(self, xOLD, yOLD, xNEW, yNEW, klon_doski):
        if abs(xNEW-xOLD)==abs(yNEW-yOLD):
            kol_hodov=abs(xNEW-xOLD)
            if xNEW>xOLD and yNEW>yOLD: # направо вверх
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z+1 and fig[1]==v+1:
                            z=z+1
                            v=v+1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
            elif xNEW>xOLD and yNEW<yOLD: # направо вниз
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z+1 and fig[1]==v-1:
                            z=z+1
                            v=v-1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
            elif xNEW<xOLD and yNEW<yOLD: # налево вниз
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z-1 and fig[1]==v-1:
                            z=z-1
                            v=v-1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False

            elif xNEW<xOLD and yNEW>yOLD: # налево вверх
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z-1 and fig[1]==v+1:
                            z=z-1
                            v=v+1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False

        else:
            print("Вы выбрали неверный ход")
            return False

    def deystvie(self, xNEW, yNEW, klon_doski): # проверяет конечную точку пустая/враг/свой и пременяет соответствующее действие
        for it in klon_doski:
            if it[0]==xNEW and it[1]==yNEW and it[2]=="empty":
                print("пермещаю фигуру")
            elif it[0]==xNEW and it[1]==yNEW and it[2].color!=self.color:
                print("атакую!")
            else:
                continue






        
class Dama():
    def __init__(self, color):
        self.color=color
        
    def __str__(self):
        if self.color=="white":
            rep="Д|"
            return rep
        else:
            rep="D|"
            return rep
    def hod(self, xOLD, yOLD, xNEW, yNEW, klon_doski):
        if abs(xNEW-xOLD)==abs(yNEW-yOLD):
            kol_hodov=abs(xNEW-xOLD)
            if xNEW>xOLD and yNEW>yOLD: # направо вверх
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z+1 and fig[1]==v+1:
                            z=z+1
                            v=v+1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
            elif xNEW>xOLD and yNEW<yOLD: # направо вниз
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z+1 and fig[1]==v-1:
                            z=z+1
                            v=v-1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
            elif xNEW<xOLD and yNEW<yOLD: # налево вниз
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z-1 and fig[1]==v-1:
                            z=z-1
                            v=v-1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False

            elif xNEW<xOLD and yNEW>yOLD: # налево вверх
                z=xOLD
                v=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z-1 and fig[1]==v+1:
                            z=z-1
                            v=v+1
                            if fig[1]!=yNEW and fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW and fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
        elif 1<=yNEW==yOLD<=8 and 1<=xNEW<=8: # ход по иксу\горизонтали
            kol_hodov=abs(xNEW-xOLD)
            if xNEW>xOLD: # ход направо по горизонтали
                z=xOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z+1 and fig[1]==yOLD:
                            z=z+1
                            if fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура)")
                                return False
            elif xNEW<xOLD: # ход налево по горизонтали
                z=xOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==z-1 and fig[1]==yOLD:
                            z=z-1
                            if fig[0]!=xNEW and fig[2]=="empty":
                                continue
                            if fig[0]==xNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура)")
                                return False
        elif 1<=xNEW==xOLD<=8 and 1<=yNEW<=8: # ход по игрику\вертикали
            kol_hodov=abs(yNEW-yOLD)
            if yNEW>yOLD: # вверх
                z=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==xOLD and fig[1]==z+1:
                            z=z+1
                            if fig[1]!=yNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура)")
                                return False
            elif yNEW<yOLD: # ход вниз
                z=yOLD
                while kol_hodov!=0:
                    kol_hodov=kol_hodov-1
                    for fig in klon_doski:
                        if fig[0]==xOLD and fig[1]==z-1:
                            z=z-1
                            if fig[1]!=yNEW and fig[2]=="empty":
                                continue
                            if fig[1]==yNEW:
                                self.deystvie(xNEW, yNEW, klon_doski)
                                return True
                            else:
                                print("не верный ход(мешает фигура на пути)")
                                return False
        else:
            print("Вы выбрали неверный ход")
            return False

    def deystvie(self, xNEW, yNEW, klon_doski): # проверяет конечную точку пустая/враг/свой и пременяет соответствующее действие
        for it in klon_doski:
            if it[0]==xNEW and it[1]==yNEW and it[2]=="empty":
                print("пермещаю фигуру")
            elif it[0]==xNEW and it[1]==yNEW and it[2].color!=self.color:
                print("атакую!")
            else:
                continue
class Korol():
    def __init__(self, color):
        self.color=color
        
    def __str__(self):
        if self.color=="white":
            rep="К|"
            return rep
        else:
            rep="k|"
            return rep
    def hod(self, xOLD, yOLD, xNEW, yNEW, klon_doski):
        if abs(xNEW-xOLD)==1 and abs(yNEW-yOLD)==1:
            self.deystvie(xNEW, yNEW, klon_doski)
            return True
        elif xNEW==xOLD and abs(yNEW-yOLD)==1:
            self.deystvie(xNEW, yNEW, klon_doski)
            return True
        elif abs(xNEW-xOLD)==1 and yNEW==yOLD:
            self.deystvie(xNEW, yNEW, klon_doski)
            return True
        else:
            print("не верный ход")
            return False

    def deystvie(self, xNEW, yNEW, klon_doski): # проверяет конечную точку пустая/враг/свой и пременяет соответствующее действие
        for it in klon_doski:
            if it[0]==xNEW and it[1]==yNEW and it[2]=="empty":
                print("пермещаю фигуру")
            elif it[0]==xNEW and it[1]==yNEW and it[2].color!=self.color:
                print("атакую!")
            else:
                continue
        
        

def main():
    doska1=Doska()
    doska1.rasstanovka()
    doska1.display()
    color="black"
    end=None
    while end!=1:
        doska1.move(color)
        doska1.display()
        color=doska1.smena_hoda(color)

            

            
        


main()
input("exit")
