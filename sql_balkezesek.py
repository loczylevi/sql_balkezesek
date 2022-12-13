''' balkezesek.csv
n�v;els�;utols�;s�ly;magass�g
Jim Abbott;1989-04-08;1999-07-21;200;75
Kyle Abbott;1991-09-10;1996-08-24;200;76
Joel Adamson;1996-04-10;1998-04-26;185;76
'''
import sqlite3


conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# 2.

class Balkezesek:
  def __init__(self,sor):
    nev,elso,utolso,weight,magassag = sor.strip().split(";")
    self.nev = nev
    self.elso = elso
    self.utolso = utolso
    self.weight = int(weight)
    self.magassag = int(magassag)

with open('balkezesek.csv', encoding='latin2') as f:
  fejlec = f.readline()
  lista = [Balkezesek(sor) for sor in f]



cur.execute(" DROP TABLE IF EXISTS balkezesek ")
cur.execute("""
    CREATE TABLE IF NOT EXISTS balkezesek
    (nev    TEXT,
    elso  TEXT,
    utolso    TEXT,
    weight      INTEGER,
    magassag     INTEGER)
    """)
conn.commit()


for i in lista:
    lista = [(i.nev,i.elso,i.utolso,i.weight,i.magassag)]
    cur.executemany("INSERT INTO balkezesek VALUES (?,?,?,?,?) ", lista)
    
conn.commit()
msg = cur.execute("SELECT * FROM balkezesek")

#for row in cur.execute("SELECT * FROM balkezesek"):
    #print(row)


# 3. Hány sornyi adat van a forrásállományban?

darab = cur.execute(" SELECT COUNT() FROM balkezesek  ")    
print( f'3. feladat: { darab.fetchall()[0][0] } ' )
# 4. 
print("4.feladat:")
lekeres = cur.execute("SELECT nev,magassag*2.54 FROM balkezesek WHERE utolso LIKE '1999-10%'")
for sor in lekeres:
  finomitas = f"{sor[1]:.1f}"
  finomitas =str(finomitas).replace(".",",")
  print(f'\t{ sor[0] }, {finomitas} cm' )


#5.

bekeres = int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
while True:
  if 1990 <= bekeres <= 1999:
    break
  else:
    bekeres = int(input("Hibás adat, kérek egy 1990 és 1999 közötti évszámot!: "))

#6#

atlag = cur.execute(f"SELECT AVG(weight) FROM balkezesek WHERE utolso LIKE '{bekeres}%'")

eredmeny = f"{atlag.fetchall()[0][0]:.2f}"

eredmeny =str(eredmeny).replace(".",",")

print(f"6.feladat: {eredmeny} font")



