def decorador_mio(function):
    def agregar_capsula():
        print("=======================================================")
        function()
        print("=======================================================")
    return agregar_capsula