from collections import OrderedDict

print("Demonstrating the iteration behavior of an ordered dictionary:")
print("")

waldorf_salad = OrderedDict()
waldorf_salad['celery']     = 'vegetable'
waldorf_salad['apples']     = 'fruit'
waldorf_salad['walnuts']    = 'nut'
waldorf_salad['grapes']     = 'fruit'
waldorf_salad['mayonnaise'] = 'condiment'

for ingredient, kind in waldorf_salad.items():
    print("A waldorf salad has " + ingredient + ", which is a " + kind + ".")
