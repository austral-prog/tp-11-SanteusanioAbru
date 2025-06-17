def read_file_to_dict(filename):
    print(f"Intentando abrir {filename}...")  # solo informativo
    data = {}
    with open(filename, "r") as file:
        line = file.readline().strip()
        ventas = line.split(";")
        for venta in ventas:
            if venta:
                producto, valor = venta.split(":")
                if producto not in data:
                    data[producto] = []
                data[producto].append(float(valor))
    return data

def process_dict(data):
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
