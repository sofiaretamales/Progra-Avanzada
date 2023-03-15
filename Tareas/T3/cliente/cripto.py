def encriptar(msg : bytearray) -> bytearray:
    # Completar con el proceso de encriptación
    if msg:
        A = bytearray()
        B = bytearray()
        C = bytearray()
        msg_encriptado = bytearray()
        for n in range(len(msg)):
            if n % 3 == 0:
                A.append(msg[n])
            elif n % 3 == 1:
                B.append(msg[n])
            elif n % 3 == 2:
                C.append(msg[n])
        primer_byte_A = A[0]
        if len(B) % 2 == 0:
            byte_central_B = B[int(len(B)/2)] + B[int((len(B)/2) - 1)]
        else:
            byte_central_B = B[len(B)//2]
        ultimo_byte_C = C[len(C)-1]
        suma = primer_byte_A + byte_central_B + ultimo_byte_C
        if suma % 2 == 0:
            msg_encriptado.append(0)
            msg_encriptado += C
            msg_encriptado += A
            msg_encriptado += B
        else:
            msg_encriptado.append(1)
            msg_encriptado += A
            msg_encriptado += C
            msg_encriptado += B
        return msg_encriptado
    else:
        return b''


def desencriptar(msg : bytearray) -> bytearray:
    # Completar con el proceso de desencriptación
    if msg:
        A = bytearray()
        B = bytearray()
        C = bytearray()
        msg_desencriptado = bytearray()
        if msg[0] == 0: #nCAB
            msg.pop(0)
            largo_msg = len(msg)
            for _ in range(int(largo_msg / 3)):
                C.append(msg.pop(0))
            if largo_msg % 3 == 0:
                for _ in range(len(C)):
                    A.append(msg.pop(0))
            else:
                for _ in range(len(C)+1):
                    A.append(msg.pop(0))
            B = msg
            for _ in range(largo_msg//3 + 1):
                if A:
                    msg_desencriptado.append(A.pop(0))
                if B:
                    msg_desencriptado.append(B.pop(0))
                if C:
                    msg_desencriptado.append(C.pop(0))
        elif msg[0] == 1: #nACB
            msg.pop(0)
            largo_msg = len(msg)
            if largo_msg % 3 == 0:
                for _ in range(int(largo_msg/3)):
                    A.append(msg.pop(0))
            else:
                for _ in range(int(largo_msg/3)+1):
                    A.append(msg.pop(0))
            for _ in range(int(largo_msg/3)):
                C.append(msg.pop(0))
            B = msg
            for _ in range(largo_msg//3 + 1):
                if A:
                    msg_desencriptado.append(A.pop(0))
                if B:
                    msg_desencriptado.append(B.pop(0))
                if C:
                    msg_desencriptado.append(C.pop(0))
        return msg_desencriptado
    else:
        return b''

if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')

    msg_encriptado = encriptar(msg_original)
    print(msg_encriptado)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    print(msg_desencriptado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
