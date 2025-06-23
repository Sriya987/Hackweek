import argparse
# to convert the given celsius temp to fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
# to convert the given fahrenheit temp to celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def main():
    # initializing a parser
    parser = argparse.ArgumentParser(description='Temperature Converter: Celsius <-> Fahrenheit')
    group = parser.add_mutually_exclusive_group(required=True)
    # adding the input arguments (celsius and fahrenheit)
    group.add_argument('-c', '--celsius', type=float, help='Temperature in Celsius to convert to Fahrenheit')
    group.add_argument('-f', '--fahrenheit', type=float, help='Temperature in Fahrenheit to convert to Celsius')
    # to parse the args in the command
    args = parser.parse_args()
    # if arg is celsius,convert to fahrenheit
    if args.celsius is not None:
        result = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C is {result:.2f}°F")
    # else if arg is fahrenheit, convert to celsius
    elif args.fahrenheit is not None:
        result = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit}°F is {result:.2f}°C")

if __name__ == '__main__':
    main()
