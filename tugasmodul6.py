import math 

#parent class kalkulator

class Kalkulator: 

    def __init__(self, numbers): 

        self.numbers = numbers 

 
    def calculate(self): 

        pass 

 
    def clear(self): 

        self.numbers = None 

 
    def get_numbers(self): 

        return self.numbers 

 
    def set_numbers(self, numbers): 

        self.numbers = numbers 

 
#Sub Class "Kalkulator Biasa" 

#Untuk Abstraction : proses dimana kita menghilangkan atau menghapus karakteristik dari sesuatu untuk mengurangi kompleksitasnya, menjadi seperangkat karakteristik penting. 

#Untuk Polymorfism : Pendefinisian Method pada Subclass dan pendefinisiannya sama dengan SuperClassnya

#Untuk Encapsulation : peroses pemaketan / penyatu data bersama metode – metodenya, dimana hal ini bermanfaat untuk menyembunyikan rincian – rincian implementasi dari pemakai. Sebagai seperti pembentukan class-class, sehingga data pada class 1 tidak akan diakses oleh data 2

class KalkulatorBiasa(Kalkulator): 

    def __init__(self, numbers): 

        super().__init__(numbers) 

 
    def calculate(self, operator): 

        result = 0 

        if operator == "+": 

            result = self.Pertambahan() 

        elif operator == "-": 

            result = self.Pengurangan() 

        elif operator == "*": 

            result = self.Perkalian() 

        elif operator == "/": 

            result = self.Pembagian() 

        else: 

            print("Operator tidak dikenal") 

        return result 

 
    def Pertambahan(self): 

        result = 0 

        for number in self.numbers: 

            result += number 

        return result 
 

    def Pengurangan(self): 

        result = self.numbers[0] 

        for i in range(1, len(self.numbers)): 

            result -= self.numbers[i] 

        return result 


    def Perkalian(self): 

        result = 1 

        for number in self.numbers: 

            result *= number 

        return result 


    def Pembagian(self): 

        result = self.numbers[0] 

        for i in range(1, len(self.numbers)): 

            if self.numbers[i] != 0: 

                result /= self.numbers[i] 

            else: 

                print("Pembagian dengan nol kaga bisa") 

                result = 0 

                break 

        return result 

 
#Kelas Anakan "Kalkulator Scientific"

class ScientificCalculator(Kalkulator): 

    def __init__(self, numbers): 

        super().__init__(numbers) 

 
    def calculate(self, operator): 

        result = 0 

        if operator == "+": 

            result = self.Pertambahan() 

        elif operator == "-": 

            result = self.Pengurangan() 

        elif operator == "*": 

            result = self.Perkalian() 

        elif operator == "/": 

            result = self.Pembagian() 

        elif operator == "sqrt": 

            result = self.Akar_Pangkat_Dua() 

        elif operator == "^": 

            result = self.Pangkat() 

        elif operator == "!": 

            result = self.factorial() 

        else: 

            print("Operatornya salah cuy") 

        return result 
    
    

 
    def Akar_Pangkat_Dua(self): 

        return math.sqrt(self.numbers[0]) 

    def Pertambahan(self): 

        result = 0 

        for number in self.numbers: 

            result += number 

        return result 
 

    def Pengurangan(self): 

        result = self.numbers[0] 

        for i in range(1, len(self.numbers)): 

            result -= self.numbers[i] 

        return result 


    def Perkalian(self): 

        result = 1 

        for number in self.numbers: 

            result *= number 

        return result 


    def Pembagian(self): 

        result = self.numbers[0] 

        for i in range(1, len(self.numbers)): 

            if self.numbers[i] != 0: 

                result /= self.numbers[i] 

            else: 

                print("Pembagian dengan nol kaga bisa cuy") 

                result = 0 

                break 

        return result 
    
    

 
    def Pangkat(self): 

        return math.pow(self.numbers[0], self.numbers[1]) 

 
    def factorial(self): 

        num = int(self.numbers[0]) 

        result = 1 

        for i in range(1, num+1): 

            result *= i 

        return result 

 
# penggunaan kalkulator 

print(" _____Tugas Kalkulator_____ ") 

print("Pilihan Kalkulator:") 

print("1. Basic Calculator") 

print("2. Scientific Calculator") 

calculator_type = input("Pilihan Kalkulator yang Diinginkan : ") 


if calculator_type == "1": 

    numbers = list(map(float, input("Masukkan bilangan yang akan dihitung (pisahkan dengan spasi): ").split())) 

    operator = input("Masukkan operator (+, -, *, /): ") 

    basic_calculator = KalkulatorBiasa(numbers) 

    result = basic_calculator.calculate(operator) 

    print("Hasil : ", result) 


elif calculator_type == "2": 

    numbers = list(map(float, input("Masukkan bilangan yang akan dihitung (pisahkan dengan spasi): ").split())) 

    operator = input("Masukkan operator (sqrt,^,!,+, -, *, /) :") 

    ScientificCalculator = ScientificCalculator(numbers) 

    result = ScientificCalculator.calculate(operator) 

    print("Hasil : ", result)
