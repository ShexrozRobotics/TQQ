# Tosh - Qaychi - Qog'oz o'yini
import random
while True:
    print("""
    Keling o'ynaymiz!
    Istagan ishorani kiriting>>
    1 - Tosh
    2 - Qaychi
    3 - Qog'oz
    """)
    ishora = ["Tosh", "Qaychi", "Qog'oz"]
    user = int(input("Marhamat raqam kiriting: "))
    machine = int(random.randint(1,3))

    if(user>=0 and user<4 or user==int()):
        user_in = ishora[user-1]
        machine_in = ishora[machine-1]
        print(f""""
        Siz : {user_in}
        Kompyuter : {machine_in}
        """)
        if(user == machine):
            print("O'yin durang!")
        else:
            if(user==1 and machine==2 or user==2 and machine==3 or user==3 and machine==1):
                print(f"Tabriklayman siz G'olibsiz!")
            elif(user==1 and machine==3 or user==2 and machine==1 or user==3 and machine==2):
                print(f"Afsus! Omadingiz kelmadi.")
    else:
        print("Xatolik!")

    print("Keling yana o'ynab ko'ramiz!")
