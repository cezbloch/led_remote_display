class BinaryEncoder(object):
    @staticmethod
    def encode_bytes(data):
        return data.encode('base64')

    @staticmethod
    def decode_bytes(data):
        return data.decode('base64')
