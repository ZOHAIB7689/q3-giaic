text: str = "hello world"
numbers: int= 1234
decimal: float = 3.12
boolean: bool = True 
collection_of_data:list[int] =[1,2,3,4,5 ]
# print(collection_of_data[1])
immutable_collection_of_data:tuple[int,str,float]= (1,"hello",3.14)
object_data : dict[str] ={"name":"john","age":"29 "}

# print(object_data["name"])

unique_values:set[int] ={1,1,5,6,2,3,34,545,6,445} 
# print(unique_values)


numbers_list:list[int] =range(1,20)
# print(numbers_list) 
# for num in range(1,20):

# byte: bytes = b"hello"
# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Comparison Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

# Logical Operators
x = True
y = False