import struct

E_SIZE = 8 + 4
D_SIZE = 4 + 2 * 7
C_SIZE = 4 + 4 + 2
B_SIZE = 4 + 4 + 2 + 2 + 2 + 4
A_SIZE = 4 + 2 + 4 + 8 * 6 + 1 + 4


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset:offset + E_SIZE]
    e_parsed = struct.unpack('<Qf', e_bytes)

    return {
        'E1': e_parsed[0],
        'E2': e_parsed[1]}


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('<iHHHHHHH', d_bytes)

    return {
        'D1': d_parsed[0],
        'D2': list(d_parsed[1:])
    }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('<iIH', c_bytes)
    c2_parsed = struct.unpack('<' + 'I' * c_parsed[1], byte_string[c_parsed[2]:c_parsed[2] + c_parsed[1] * 4])
    c2_list = [parse_d(addr, byte_string) for addr in c2_parsed]

    return {
        'C1': c_parsed[0],
        'C2': c2_list
    }


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('<iiHHHI', b_bytes)
    b5_bytes = byte_string[b_parsed[5]:b_parsed[5] + b_parsed[4]]
    b5_parsed = struct.unpack('<' + 'b' * b_parsed[4], b5_bytes)

    return {
        'B1': b_parsed[0],
        'B2': b_parsed[1],
        'B3': parse_c(b_parsed[2], byte_string),
        'B4': b_parsed[3],
        'B5': list(b5_parsed)
    }


def parse_a(offset, byte_string):
    a_bytes = byte_string[offset:offset + A_SIZE]
    a_parsed = struct.unpack('<IHIddddddBI', a_bytes)
    a2_bytes = byte_string[a_parsed[2]:a_parsed[2] + a_parsed[1] * 2]
    a2_parsed = struct.unpack('<' + 'H' * a_parsed[1], a2_bytes)

    return {
        'A1': parse_b(a_parsed[0], byte_string),
        'A2': list(a2_parsed[0:]),
        'A3': list(a_parsed[3:9]),
        'A4': a_parsed[9],
        'A5': parse_e(a_parsed[10], byte_string)
    }


def f31(byte_string):
    return parse_a(4, byte_string)


f31(b'GUMZ{\x00\x00\x00\x06\x00\x8d\x00\x00\x00xez\xbb\x9fR\xcb\xbf\xd6\xb8;M\xef]'
b"\xef?\xc6f_\xfc\x97\xc7\xe1\xbf\xd4'\x1c\x96\xd5?\xee\xbf\x08\x1e\xc4\x85fK"
b'\xed?\xfaH\t\xcc1\x04\xe1\xbf\t\x99\x00\x00\x00N\xeaA\\\xb66-\xd9\x10'
b'\xbfH\xe1\xf5\xb1\xc1\xa5\x06\\R\n\xad\xd0\xaa\xe6\xe0K\xfcg\xad'
b'(\x93\x99\xc7\x9b\xbf\xacC\x00\x00\x00U\x00\x00\x00\xcf)+\x9b\x02'
b'\x00\x00\x00g\x00)\xc8K\x8c\x94\xc2\x1a\x98\xca?o\x00\xb3\x0f\x02'
b'\x00y\x00\x00\x00\xb8o\x8f\xb1\x08\x9a*\xbb\x0e+mY\xcf-\xca\xef\xf2tM3X`\xf7'
b'>')
