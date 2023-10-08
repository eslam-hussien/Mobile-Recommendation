# co B and C
# len each group
# how much medium how much low and etc
# get data from user
def split(interests, levels):
    groups = [([x for x in interests if x["level"] == level[0]], level[1])
              for level in levels]
    return list(filter(lambda g: len(g[0]) > 0, groups))

# col D
# groups = counter of intersts in each level


def calc_weights(groups, total):
    return [{"g": group[0], "w": len(group[0])/total*group[1]} for group in groups]

# col f


def calc_percentages(groups):
    total = 0
    for g in groups:
        total += g["w"]
    return [{"g": group["g"], "p":group["w"]/total*100} for group in groups]

# col h


def calc_x_value(group):
    n = len(group["g"])
    c = (n/2)*(n-1)
    if n > 0:
        x = (group["p"]-c)/n
    else:
        x = 0
    return {"g": group["g"], "x": x}

# sorting choices (b)


def sort_group(group):
    return sorted(group["g"], key=lambda i: i['order'])

# score of each interst in each level
# col I


def clac_interests_score(groups):
    interests = []
    for group in groups:
        max = len(group["g"])-1
        group["g"] = sort_group(group)
        x = group['x']
        for interest in group["g"]:
            if(max < 0):
                exit(1)
            interest['score'] = max+x
            max -= 1
        interests += group["g"]

    return interests
# match level with interst and interst with mapping
# inial mapping with algorithm


def process_interests(interests, levels):
    groups = split(interests, levels)
    groups = calc_weights(groups, len(interests))
    groups = calc_percentages(groups)
    groups = [calc_x_value(group) for group in groups]
    return clac_interests_score(groups)

# row 7 (total)


def process_components(mapping, interests):
    output = {}
    for interest in interests:
        components = mapping[interest['id']]
        for k, v in components.items():
            if k in output:
                output[k] += v*interest['score']
            else:
                output[k] = v*interest['score']

    return output

# row 18 (totals)


def product_score(product, comps):
    product['score'] = 0
    for k, v in comps.items():
        if k in product:
            product['score'] += product[k]*v
        else:
            print(f"this {k} is not found")
    return product

# if less than 10 get them if more get only 10


def get_recommended(products):
    products = sorted(products, key=lambda i: i['score'], reverse=True)
    print(products)
    if len(products) <= 10:
        return products
    else:
        return products[:10]

# rendering recomended mobiles


def alg(interests, products, levels, mapping):
    interests = process_interests(interests, levels)
    comps = process_components(mapping, interests)
    products = [product_score(p, comps) for p in products]
    recommended = get_recommended(products)
    return recommended
