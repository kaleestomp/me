TODO: Reflect on what you learned this week and what is still unclear.

exercise 1 word pyramid: do i have to convert url to json

why can't I .json() some of the urls (word pyramid url for example)

what is a binary object?

after .open(), what if I want to keep .read()/readline()/readlines(). (after the first one) (the text gets removed after being read?)

def get_some_details() - this function didn't .close()?

I think there's an error with word pyramid (longest word not 20)

def smallPokedex(low=1, high=5):
"""Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.

    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """

    pokedex = []
    for i in range(low, high, 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        r = requests.get(url)
        if r.status_code is 200:  # if the request comes back...
            print(r)
            data = r.json()
            pokedex.append(
                {
                    "name": data["name"],
                    "weight": data["weight"],
                    "height": data["height"],
                }
            )
    highiest = -1.0
    tallestPoke = "kyle"
    for p in pokedex:
        if p["height"] > highiest:
            highiest = p["height"]
            tallestPoke = p

    return tallestPoke
