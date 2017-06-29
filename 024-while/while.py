print("Commencing obnoxious drinking song:")
print("")

bottles_of_beer = 99
while bottles_of_beer > 0:
    beer_str = str(bottles_of_beer)

    if bottles_of_beer == 1:
        beer_str = beer_str + " bottle"
    else:
        beer_str = beer_str + " bottles"

    print(beer_str + " of beer on the wall!")
    print(beer_str + " of beer!")
    print("Take one down, pass it around,")
    bottles_of_beer = bottles_of_beer - 1
    beer_str = str(bottles_of_beer)

    if bottles_of_beer == 1:
        beer_str = beer_str + " bottle"
    elif bottles_of_beer == 0:
        beer_str = "No more bottles"
    else:
        beer_str = beer_str + " bottles"
        
    print(beer_str + " of beer on the wall!")
    print("")
