def reject():
    Input_array = ["impolite", "cows","partner", "undress", "rule","chop", "moor", "hunt", "pack", "old-fashioned"]
    rejected_items=["cows", "partner", "wonderful", "rainstorm", "painful","undress","hunt"]
    for x in rejected_items:
        for y in Input_array:
            if x==y:
                Input_array.remove(x)
    print(Input_array)

reject()
