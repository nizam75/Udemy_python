from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokeman Name", ["Picachu", "squirtle", "charmander"])
table.add_column("type", ["electric", "water", "fire"])
table.align = "l"
print(table)