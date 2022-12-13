'''  balkezesek.csv
 0    1    2     3      4
név;első;utolsó;súly;magasság
Jim Abbott;1989-04-08;1999-07-21;200;75
'''

# 2.
with open('balkezesek.csv', 'r', encoding='latin2') as forrás:
    forrás.readline()
    mátrix = [sor.strip().split(';') for sor in forrás ]

# 3. 
print(f"3. feladat: {len(mátrix)}")

# 4.
print(  f"4. feladat:")
[ print(f"        {sor[0]}, {int(sor[4]) * 2.54:.2f} cm") for sor in mátrix if sor[2][:7] == '1999-10' ]

# 5.
print(f"5. Feladat:")

while True:
    év = input('Kérek egy 1990 és 1999 közötti évszámot:')
    if ('1990' <= év <= '1999'):
        break
    else:
        print('Hibás adat!', end='')

súlyok = [ int(sor[3]) for sor in mátrix if (sor[1][:4] <= év <= sor[2][:4]) ]
átlag = sum(súlyok)/ len(súlyok)

# 6.
print(f"6. feladat: {átlag:.2f} font")
