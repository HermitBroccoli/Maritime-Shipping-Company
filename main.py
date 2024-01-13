from shipping_company import Route, Ship, Captain, ShippingCompany


ship1 = Ship(
    name="Аврора",
    capacity=5000,
    year_built=2003,
    current_location="Москва",
    speed=20
)

route1 = Route(
    departure_point="Москва",
    destination="Южно-Сахалин",
    distance=1092.75
)

capitan1 = Captain(
    name="Григорий",
    surname="Дмитрович",
    experience=20,
    qualification="Капитан первого ранга"
)

company1 = ShippingCompany(name_company="ООО 'Круиз'")

company1.add_ship(ship=ship1)
company1.add_route(route=route1)
company1.hire_capitan(captain=capitan1)

ship1.load_cargo(cargo=500)
ship1.change_location(new_location="Владивосток")
ship1.speed = 35.7
