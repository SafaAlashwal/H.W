
info={"safa":444444,"ahmed":145622,"mohemmed":12345668}
#-----------------------------------------------------
#update
def update():
    up=input("enter the name you want change his numper:")
    upp=input("enter new numper:")
    int(upp)
    info.update({up:upp})
#-----------------------------------------------------
#add
def add():
    addname=input("add name:")
    addnum=input("add number:")
    info[addname]=addnum

#-----------------------------------------------------
#remove
def remove():
    removename=input("enter the name you want remove:")
    info.pop(removename)
#---------------------------------------------------------------------
def view():
    print(info)
#---------------------------------------------------------------------
listoption=["1-add","2-updat","3-delete","4-view"]
print(f"{listoption[0]}\n{listoption[1]}\n{listoption[2]}\n{listoption[3]}")
#---------------------------------------------------------------------

canedit=0
#ifcondation
while   canedit<=3:
    canedit+=1
    useroption=input("enter number the option or the option:")

    if  "add"== useroption or "1" == useroption:
        add()
        print (info)
    else:
        print("")
    if  "updat" == useroption or "2" == useroption :
        update()
        print(info)
    elif "delete" == useroption or "3" == useroption:
        remove()   
        print(info)
    elif "view" == useroption or "4" == useroption:
        view()
        print(info)
    
 
    else:
        print(f" error {useroption} out option")


 
