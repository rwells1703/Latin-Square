def generate_square(size):
    latin_square = []

    i = 0
    while i < size:
        j = 0
        latin_square.append([])
        
        while j < size:
            value = j+i+1
            
            while value > size:
                value -= size
                
            latin_square[i].append(value)
            j += 1
        i += 1
        
    return latin_square

def display_square(square):
    for line in square:
        for char in line:
            print(char,end=" ")
        print()
        
def display_ascii_wave(square):
    i = 30
    while True:
        if i == 255:
            i = 30
        for line in square:
            for char in line:
                print(chr(char+i),end="")
            print()
        i += 1
        
square = generate_square(9)

display_square(square)
print()
display_ascii_wave(square)
