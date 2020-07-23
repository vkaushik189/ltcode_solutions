class Solution:
    def defangIPaddr(self, address: str) -> str:

        """
        new_address = address.replace(".", "[.]")
        return new_address
        """
        new_message = ''
        for char in address:
            if char != '.':
                new_message = new_message + char
            else:
                new_message = new_message + "[.]"
        return new_message