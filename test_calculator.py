from calculator.calculator import Calculator
import pytest 

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self): 

        # arrange 

        a = 2500 
        b = 1500 
        cal = Calculator() 

        result = cal.subtract(a, b) 

        expected = 1000
        assert result == expected 



    def test_multiply(self): 

        # arrange 

        a = 8 
        b = 5 
        cal = Calculator() 
 
        result = cal.multiply(a, b) 

        expected = 40 
        assert result == expected 


    def test_divide(self): 

        a = 160 
        b = 20 
        cal = Calculator() 

        result = cal.divide(a, b) 

        expected = 8 
        assert result == expected 

 

    def test_divide_by_zero(self): 

        a = 100 
        b = 0 
        cal = Calculator() 
 

        with pytest.raises(ZeroDivisionError): 
            cal.divide(a, b) 

 






