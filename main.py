def direction(facing, turn):
    directions_dict = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}

    # перевірка значення "turn" на попадання в заданий проміжок і кратність 45 градусам
    if turn not in range(-1080, 1081, 45):
        return "ERROR: input value of 'turn' is too big or not multiple of 45!"
    else:
        turn_degrees = directions_dict[facing] + turn

    direction_after_turn = turn_degrees - (turn_degrees // 360) * 360
    # (turn_degrees // 360) >> визначаємо к-сть кіл в заданих координатах
    # * 360 >> к-сть повних кіл
    # turn_degrees - >> отриманий залишок співпадатиме з градусами зі словнику

    # Визначення напрямку по отриманих значеннях в градусах
    for k, v in directions_dict.items():
        if v == direction_after_turn:
            return k

"""
print(direction("S", 180))      # N
print(direction("SE", -45))     # E
print(direction("W", 495))      # NE

print(direction("E", -135))     # NW
print(direction("N", -720))     # N
print(direction("E", -855))     # NW
print(direction("E", 1035))     # NE
"""