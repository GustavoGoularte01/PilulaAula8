def atender_paciente(fila):
    if len(fila) == 0:
        print('fila vazia')
        return fila
    paciente = fila.pop(0)
    print(f'atendendo: {paciente}')
    return fila

def main():
    fila = ['Gabriel','Beatriz', 'Carlos', 'Ana', 'Alcides']
    print (f'fila inicial {fila}')
    fila = atender_paciente(fila)
    print(f'fila atualizada {fila}')
    
main()