from fastmcp import FastMCP
mcp = FastMCP("food-mcp")

FOOD_DB = [
    {"name": "Paneer Tikka", "veg": True, "price": 150, "rating": 4.5},
    {"name": "Chicken Biryani", "veg": False, "price": 250, "rating": 4.8},
    {"name": "Dal Makhani", "veg": True, "price": 120, "rating": 4.2},
    {"name": "Veg Burger", "veg": True, "price": 90, "rating": 3.8},
    {"name": "Mutton Rogan", "veg": False, "price": 300, "rating": 4.6},
]


@mcp.tool()
def find_veg_food()->str:
    """ find veg food items """
    return [f for f in FOOD_DB if f["veg"]]


@mcp.tool()
def find_nonveg_food()->str:
    """ find nonveg food items """
    return [f for f in FOOD_DB if not f["veg"]]

@mcp.tool()
def find_under_price(max_price: int)-> str:
    """find food items under a specific price"""
    return [f for f in FOOD_DB if f["price"] <= max_price]

@mcp.tool()
def find_above_rating(min_rating: int)-> str:
    """find food items with the ratings above the specified ratings"""
    return [f for f in FOOD_DB if f["rating"] >= min_rating]


if __name__ == "__main__":
    mcp.run()