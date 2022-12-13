''' balkezesek.csv
név;első;utolsó;súly;magasság
 0    1    2     3      4
Jim Abbott;1989-04-08;1999-07-21;200;75
'''

# 2.
class Versenyző:
    def __init__(self,sor):
        s = sor.strip().split(';')
        self.név      = s[0]
        self.első     = s[1]
        self.utolsó   = s[2]
        self.súly     = int(s[3])
        self.magasság = int(s[4])

with open('balkezesek.csv', 'r', encoding='latin2') as forrás:
    fejléc = forrás.readline()
    mátrix = [ Versenyző(sor) for sor in forrás ]

print(f"3. feladat: {len(mátrix)}")

print(  f"4. feladat:")
[ print(f"        {sor.név}, {sor.magasság*2.54:.1f} cm") for sor in mátrix if sor.utolsó[:7] == '1999-10']

print(f"5. Feladat:")

while True:
    év = input('Kérek egy 1990 és 1999 közötti évszámot:')
    if ('1990' <= év <= '1999'):
        break
    else:
        print('Hibás adat!', end='')

súlyok = [ sor.súly for sor in mátrix if (sor.első[:4] <= év <= sor.utolsó[:4]) ]
átlag = sum(súlyok) / len(súlyok)

print(f"6. feladat: {átlag:.2f} font")