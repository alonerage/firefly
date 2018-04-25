﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("Я")
define ma = Character(_("Маша"), color="#db1717")
define ba = Character(_("Бабушка"), color="#db1717")
define ssl = Character(_("Сестра"), color="#008080")


##glass-smash

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg domleto
    
    play music "sound/summer01.ogg"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

 
    
    "Такой воздух бывает только в детстве. Густой как патока. Пахнет травой, нагретой землей и приключениями, которые ждут за каждым поворотом."
 
    "Каждое лето я проводил у бабушки в Журавлином Холме. Это совсем не далеко от Города. Меньше часа на электричке, или машине. Но как будто-бы совсем другой мир. Нет суеты, машин, уроков. Тут не слышны гудки кораблей и почти не пахнет морем. "
 
    "Даже фонарей почти нет. Когда идешь по улице, дорога освещается светом из окон низеньких домов. Если хозяева не легли спать, а если легли, то луной и звездами. Немного страшно и в то же время красиво. Нигде больше не видел таких ярких звезд."
 
    "В то утро я сидел на лавочке которую смастерил дед. Это было задолго до моего рождения. Доски стали серыми от времени, что никак не сказалось на надежности этой монументальной конструкции. "
 
    "Это было, как будто вчера. Я грелся на солнышке и думал куда пойти. На луг, или пройтись по улице."
    
    #play sound "sound/creakydoor"
    
  

    menu:
      "На луг":
       $dir = 'left'
      "На улицу":
       $dir = 'right'
    
    if dir == 'left': 
     play sound "sound/dundun.ogg"    
     show baba
     ba "Андрей! Ты куда собрался!?!"
     "Это была Бабушка..."
     me "Да вот, решил погулять немного. По улице пройдусь, может до Луга дойду. Я не на долго, бабуль."
     ba "Хорошо. Иди конечно. Только сестру возьми, а то путается под ногами"
     show ssl at right
     show baba at left
     "Это был конец. Надо было что-то срочно предпринять. Мелкая будет постоянно ныть, мешаться под ногами, а потом еще бабушке пожалуется. С другой сторны, если спорить, то могут и вовсе не отпустить."
     
     # menu:
      "Убежать!":
        $dir = 'pobeg'
      "Взять сестру с собой":
        $dir = 'zabratss'
    
    #if dir == 'pobeg': 
    play sound "sound/run.wav"   
     scene bg  street
    "Я рванул с места, что было сил. Ломая кусты и ветки, перепрыгнул через забор полисадника. Ударился коленом и потянул ногу, но не остановился. Позади я слышал сердитый голос бабушки и расстроенное хныканье сестры."
          
    
    #else:
     show ssl at right
     show baba at left
     "Решив, что не буду лишний раз расстраивать бубушку, я вздохнул и посмотрел на сестру"  
    me "Ну что. Пойдем Мелкая"
     ssl "Ты чего вздыхаешь?"
     "Она надула губы и как будто-то бы обиделась."
     me "Просто так. Пойдем, только веди себя хорошо. Договорились?"
     ssl "Ну даже не знаю..."
     ba "Надя! Это что такое?"
     ssl "Да пошутила я!"
     play sound "sound/ssl-laughter.wav"
     scene bg  street
  

     
    else:
      "Бабушка что-то делала в доме. Надо бы ей сказать, что я ухожу."
      me "Бабуль! Я пойду погуляю!"
      ba "На долго?"
      "Её голос доносился из глубины дома и сопровождался звоном посуды. Наверное она готовила обед."
      me "Нет!"
      play sound "sound/creakydoor.wav"
      "Она что-то говорила мне в догонку. Её голос заглушил звук старой калитки."
      "Я вышел на улицу"
     #This ends the game.
    
    
#show madam blush

    # These display lines of dialogue.
  
    #me "Маша я предлагаю тебе свою руку, сердце и прочие  органы!"
    #ma "Наверняка обманешь."
    #me "Нет! Ты будешь моим Цветочком, а я твоим Андрейкой!"

    #menu:
      #"Наебать и пойти на лево":
       # $dir = 'left'
      #"Честность и преданность":
      #  $dir = 'right'
    
    #if dir == 'left': 
    ##play sound "sound/glass-smash.ogg"   
    # show madam angry at left
    # ma "Ну ты и мудак!"
        
      
    #else:
    #  ma "Дай поцелую."
    # This ends the game.

    #return
