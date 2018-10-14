antonyms=dict({'Hi':'Bye','Bye':'Hi'})
while True:
     current_word=input("please enter a word:")
     if current_word in antonyms:
         print(antonyms[current_word])
     else:
         ask=True
         while ask:
            ask=True
            print("i dont know the antonym of "+current_word)
            cont=input("do you want to teach it to me?(y\\n)")
            if cont =='y':
                ant=input("please enter the antonym of "+current_word+":")
                antonyms[current_word]=ant
                antonyms[ant]=current_word
                ask=False
                print("thanks,i've learned it!")
            elif cont =='n':
                print("ok!")
                ask=False
