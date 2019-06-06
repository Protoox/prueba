print("Bienvenido al combate pokemon del momento, tu pokemon es Pikachu")
print("Pikachu tiene 100HP y dos ataques, Impactrueno:10 de Daño y Bola voltio:12")
print("A cual de los siguientes contrincantes te quieres enfrentar?")
print("Charmander 120HP 10 Daño")
print("Squirtle 80HP 15 Daño")
print("Bulbasur 100HP 12 Daño")
pokemon = input("Escribe el nombre de charmander, squirtle o bulbasur para enfrentarte a alguno de ellos: ").upper()

pikachu_hp = 100
pikachu_a1 = 10
pikachu_a2 = 20

if pokemon == "CHARMANDER":
    pokemon = 1
    pokemonhp = 120
    pokemondmg = 10
    pokemon_name = "Charmander"
    pokemon_a = "Ascuas"

elif pokemon == "SQUIRTLE":
    pokemon = 2
    pokemonhp = 80
    pokemondmg = 15
    pokemon_name = "Squirtle"
    pokemon_a = "Pistola Agua"

elif pokemon == "BULBASUR":
    pokemon = 3
    pokemonhp = 100
    pokemondmg = 12
    pokemon_name = "Bulbasur"
    pokemon_a = "Latigo Cepa"

print("Perfecto, lucharas contra {}".format(pokemon_name))
while pokemonhp >= 0 and pikachu_hp >= 0:
    pikachuattq = input("Tu atacas, elige Impactrueno o Bola Voltio").upper()

    if pikachuattq == "IMPACTRUENO":
                pokemonhp -= pikachu_a1
                print("Pikachu ha usado Impactrueno")
                print("La vida de {} ha bajado a {}".format(pokemon_name, pokemonhp))
    elif pikachuattq == "BOLA VOLTIO":
                print("Pikachu ha usado Bola Voltio")
                print("La vida de {} ha bajado a {}".format(pokemon_name, pokemonhp))
                pokemonhp -= pikachu_a2

    pikachu_hp -= pokemondmg
    print("{} ha usado {}".format(pokemon_name, pokemon_a))
    print("La vida de Pikachu ha bajado a {}".format(pikachu_hp))
if pokemonhp <= 0:
    print("Felicidades, {} ah sido derrotado".format(pokemon_name))
elif pikachu_hp <= 0:
    print("Pikachu ha sido derrotado! Te has pegado un tiro al ver como sufria tu pikachu")