# ' ' ' ' ' ' Hello and welcome to My Program ' ' ' ' ' ' ' ' '



print("\n\n\n          Hello And Welcome To My Calculator\n ")
print('\n               Choose YOUR Method ')


count=0
total=0

print("For Multiplication  [m]\n")
print("For Subtraction   [s]\n")
print("FOR Division  [d]\n")
print("For Addtion  [a]\n")
print("\nFor Average  [A]\n")
print("For ALL IN ONR Calculator [ALL]\n\n")


while True:

    user = input("\n\n\n            ENTER YOUR METHOD  (*_*) = ")

    total = 0
    count = 0
    if user == 'm':
        while True:

            inp = input('\n\n\n          ENTER YOUR NUMBER = ')
            if inp == 'done': break

            try:
                k = float(inp)
                print('Good')

                total = total * k
                count = count + 1

                print("Enter values ", count)
                print("YOUR MULTIPLICATION = ", total)

            except:
                print('sorry invalid enter  ')


    elif user == 'a':
        count=0
        total=0
        while True:

            inp = input('\n\n\n          ENTER YOUR NUMBER =  ')
            if inp == 'done': break


            try :
                j = float(inp)
                total = total+j
                count = count+1
                print('This is your sum = ',total)
                print('You enter values ',count)
            except :
                print('please try again')



    elif user=='s' :
        while True:
            inp = input("\n\n\n           Enter your Number =  ")
            if inp == 'done': break
            try:
                f =int(inp)
                total = total - f
                count = count +1
                print('DONE =',total)
                print("total value you Enter = ")
            except:
                print('sorry i dont undersatand')


    elif user=='d':
        while True:
            inp =input("\n\n\n            ENTER your Number =  ")
            xinp = input("\n\n           Enter your second Number ")
            if inp =='done': break

            try:
                v =float(inp)
                b =float(xinp)

                print('done! ', v/b)
            except:
                print('try again ')

    elif user =='A':

        while True:
            count = 1
            total = 0
            inp = input("\n\n\n          ENTER YOUR NUMBER = ")
            if inp == 'done': break
            try:
                n = float(inp)
                count = count + 1
                total = total + inp
                print("Your Enter Values ", count)
                print("Average = ", total / count)
            except:
                print('please try Again ')

    elif user == 'ALL':
        while True:
            count = 0
            total = 0
            inp = input("\n\n\n          ENTER YOUR NUMBER = ")
            if inp == 'done': break
            try:
                all=float(inp)
                count = count+1
                total = all/count
                atotal = total+all

                print('done',total)
                print('done',atotal)
                print('done',count)

            except:
                print('\nTry Again\n ')

    elif user =='exit':
        print('\n\n            Thank You For Using\n')
        break

    else:print('\nPlease Try Again\n ' )




























































































