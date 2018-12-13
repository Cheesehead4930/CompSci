import pyautogui as pg
import webbrowser as wb
import time as t

points = 0
            
food= pg.prompt ("what is your favorite food? ")
    
if food == "pizza":
    points += 10
    wb.open("https://www.youtube.com/watch?v=sv3TXMSv6Lw")
    t.sleep(5)
    pg.alert ("good")

elif food== "pasta":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=YNHqjFyk5gU")
    t.sleep(5)
    pg.alert ("gross!")

elif food== "cereal":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=Ay31lOZHTNE")
    t.sleep(5)
    pg.alert ("good with milk")

elif food== "chips":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=DbadNY-NCwc")
    t.sleep(5)
    pg.alert ("decent")
  
elif food== "soup":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=GojmNjoTaTg")
    t.sleep(5)
    pg.alert ("good")

elif food== "yogurt":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=jEn_vMhrhTk")
    t.sleep(5)
    pg.alert ("yogurt is good")

else:
    pg.alert ("your favorite food is " + food)

show = pg.prompt ("what is your favorite show?")

if show == "parks and rec":
    points += 10
    wb.open("https://www.youtube.com/watch?v=AMlyrdR1Uwg")
    t.sleep(5)
    pg.alert ("Great show")

elif show == "friends":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=6CHUaxeasEQ")
    t.sleep(5)
    pg.alert ("good show")
              
elif show == "riverdale":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=PmufRC4BV9E")
    t.sleep(5)
    pg.alert ("basic")
              
elif show == "rick and morty":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=cffSbDucnrM&t=19s")
    t.sleep(5)
    pg.alert("good")

elif show == "how i met your mother":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=cffSbDucnrM&t=19s")
    t.sleep(5)
    pg.alert ("i dont even know that show")

elif show == "the simpsons":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=lm5o50ICyMQ")
    t.sleep(5)
    pg.alert ("bruh")
else:
    pg.alert ("your favorite show is " + show)
    

game= pg.prompt ("what is your favorite game? ")
    
if game== "fortnite":
    points += 10
    wb.open("https://www.youtube.com/watch?v=MXgdV_cJuTg")
    t.sleep(5)
    pg.alert ("so fun")

elif game== "COD":
    points += 7
    wb.open ("https://www.youtube.com/watch?v=dJO9H9RQINY")
    t.sleep(5)
    pg.alert ("boring game!")

elif game== "Csgo":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=qu3buoRyd6k")
    t.sleep(5)
    pg.alert ("old and a bad game")

elif game== "pub g":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=H4mNboC-Cqk")
    t.sleep(5)
    pg.alert ("BORING")
  
elif game== "overwatch":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=KebJNcfus-c")
    t.sleep(5)
    pg.alert ("we cant be friends")

elif game== "minecraft":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=s-9GtrKuT4M")
    t.sleep(5)
    pg.alert ("you are a meme")

else:
     pg.alert ("your favorite game is " + game)


team = pg.prompt ("what is your favorite team? ")
    
if team == "packers":
    points += 10
    wb.open("https://www.youtube.com/watch?v=nX2KJVS8fsI")
    t.sleep(5)
    pg.alert ("PACKERS ARE THE BEST TEAM IN THE NFL")

elif team == "bears":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=Z13-znp08rs")
    t.sleep(5)
    pg.alert ("u are literal garbage")

elif team == "vikings":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=uJle7UP1OKg")
    t.sleep(5)
    pg.alert ("nobody likes you")

elif team == "patriots":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=AxbE48WDNTk")
    t.sleep(5)
    pg.alert ("bandwagon")
  
elif team == "steelers":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=KOG_k1vJPmY")
    t.sleep(5)
    pg.alert ("why dude why")

elif team == "browns":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=kN8p4rWbo08")
    t.sleep(5)
    pg.alert ("i am truly sorry for you")

else:
     pg.alert ("your favorite team is " + team)


movie = pg.prompt ("what is your favorite movie? ")
    
if movie == "finding nemo":
    points += 10
    wb.open("https://www.youtube.com/watch?v=-OzyIioc4T0")
    t.sleep(5)
    pg.alert ("good movie")

elif movie == "avengers":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=H-sZBlwK5h0")
    t.sleep(5)
    pg.alert ("not very good")

elif movie == "deadpool":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=ONHBaC-pfsk")
    t.sleep(5)
    pg.alert ("good movie")

elif movie == "mighty ducks":
    points += 10
    w.open ("https://www.youtube.com/watch?v=GoZCITtz-WI")
    t.sleep(5)
    pg.alert ("no idea what that is")
  
elif movie == "the elf":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=CQ8y0qso06w")
    t.sleep(5)
    pg.alert ("funny")

elif movie == "ghost busters":
    points += 10
    wb.open ("https://www.youtube.com/watch?v=eXI-9p7CUN0")
    t.sleep(5)
    pg.alert ("great")

else:
     pg.alert ("your favorite movie is " + movie)

pg.alert("u made " +  points)
