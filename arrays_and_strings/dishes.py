#dishes


def groupingDishes(dishes):
    grouped = {}
    for dish in dishes:
        for i in range(1, len(dish)):
            if dish[i] not in grouped:
                grouped[dish[i]] = []
            
            ings = grouped[dish[i]]
            ings.append(dish[0])
            grouped[dish[i]] = ings


    result = []
    for ing in sorted(grouped.keys()):
        if len(grouped[ing]) >= 2:
            row = sorted(grouped[ing])
            row.insert(0, ing)
            result.append(row)
    return result

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
print(groupingDishes(dishes))
