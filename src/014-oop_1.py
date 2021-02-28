# imports as needed

class MyRouter(object):
    """Represents a Router"""
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manufac_date):
        print(f"Router Name: {self.routername}")
        print(f"Router Model: {self.model}")
        print(f"Router Serial Number: {self.serialno}")
        print(f"Router's Firmware Version:{self.ios}")
        print(f"Created in: {manufac_date}")

def main():
    mr = MyRouter("R1", "2600", "12345", "12.4")
    mr.print_router(2012)

if __name__ == '__main__':
    main()
