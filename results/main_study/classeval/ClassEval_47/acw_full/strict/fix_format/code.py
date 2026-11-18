class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def is_valid(self):
        octets = self.ip_address.split(".")
        if len(octets) != 4:
            return False
        return not any(
            not octet.isdigit() or int(octet) < 0 or int(octet) > 255
            for octet in octets
        )

    def get_octets(self):
        return self.ip_address.split(".") if self.is_valid() else []

    def get_binary(self):
        if self.is_valid():
            binary_octets = [format(int(octet), "08b") for octet in self.get_octets()]
            return ".".join(binary_octets)
        else:
            return ""
