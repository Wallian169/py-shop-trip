from __future__ import annotations
from datetime import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return f"{self.name}"

    def print_check(
            self,
            customer_name: str,
            product_cart: dict,
    ) -> None:
        print(datetime.now().strftime("Date: %m/%d/%Y %H:%M:%S"))
        print(f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought:")
        total = 0
        for product, quantity in product_cart.items():

            if product in self.products:
                summary = quantity * self.products[product]
                print(f"{quantity} {product}s for {summary} dollars")
                total += summary
        print(f"Total cost is {total} dollars\n"
              f"See you again!\n")

    @classmethod
    def from_dict(cls, shop: dict) -> Shop:
        return cls(
            shop.get("name"),
            shop["location"],
            shop.get("products")
        )
