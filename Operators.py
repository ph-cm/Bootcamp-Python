# Operators are simbols that represents operations with one or more values

# Aritmetricos
x = 5 + 2 # Add
y = 5 - 2 # Sub
z = 5 * 2 # Multiplication
a = 5 / 2 # Div
b = 5 % 2 # Module
c = 5 ** 2 # Exponential
d = 5 // 2 # Int Div

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)

print("________________________________")

#Comparativos/Relacionais
print(5 == 5) # Equal
print(5 != 4) # Diferent
print(5 > 4) # Bigger
print(4 < 5) # Smaller
print(5 >= 5) # Bigger or equal
print(5 <= 4) # Smaller or Equal

print("_______________________________")

# #Boolean/Logicos
# AND -> just if all the expressions here true, its gonna be true
# OR  -> if at least one expression here true, its gonna be true
# NOT -> invert the boolean value
age = 21
permition_drive = True

print(age > 18 and permition_drive)
print(age < 18 or permition_drive)
print(not permition_drive)

print("_____________________________")

# #Bitwise/Bit a Bit
# operar nos bits individuais de numeros inteiros. Excencial em criptografia, graficos e otimizacao de baixo nivel.
#& -> AND bit a bit
# ` -> OR bit a bit
# ^ -> XOR bit a bit
# ~ -> NOT bit a bit
# << -> Deslocamento a esqueda bit a bit
# >> -> Deslocamento a direita bit a bit
print(5 & 3) # 1 em decimal
print(5 ^ 3) # 6 em decimal
print(~5)    # inverte todos os bits
print(5 << 1)# 0101 -> 1010 = 10
print(5 >> 1)# 0101 -> 0010 = 2

print("___________________________")

# #is & in 
# is -> Identity: verifies if 2 operands are the same object in the memory, not just
# has the same value. Similar to "===" on JS

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)

a = None
print(a is None) # A way to test if something is None

# in -> verifies if a value is in a sequence(string, list, tuple, set) or if 
# an key is in a dictionary

fruit = ["apple", "banana", "orange"]
print("apple" in fruit)
print("grape" in fruit)

text = " Hello World"
print("Hello" in text)
print("java" in text)

dictionary = {"name": "Pedro", "idade": 22}
print("name" in dictionary)
print("Pedro" in dictionary)
print("Pedro" in dictionary.values())

print("__________________________")

#Ternary
# if-else in a unique line
# value_if_true if condition else value_if_false

age = 17
status = "maior de idade" if age >= 18 else "menor de idade"
print(status)

temp = 25
climate = "hot" if temp > 20 else "cold"
print(climate)

print("_________________________")
