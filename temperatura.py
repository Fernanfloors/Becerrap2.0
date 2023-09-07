def celcius_a_fahrenheit(celcius): 
    return (celcius *9/5)+ 32 

def fahrenheit_a_celcius(fahrenheit):
    return (fahrenheit -32)*5/9

if __name__ == "__main__": 
    celcius = 25
    fahrenheit = celcius_a_fahrenheit(celcius)
    print(f"{celcius} grados celcius equivalen a {fahrenheit} grados fahrenheit")

    fahrenheit = 25
    celcius = fahrenheit_a_celcius(fahrenheit)
    print(f"{fahrenheit} grados fahrenheit equivalen a {celcius} grados celcius")       