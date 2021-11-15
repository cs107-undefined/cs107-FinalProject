import numpy as np
# TODO: add summary in docstring
class UDFunction:
    #constructor that sets the value of the function and derivative
    def __init__(self, val, der=1):
        """[summary]

        Args:
            val (numeric or numpy ndarray): value of function
            der (int, optional): derivative of function. Defaults to 1.
        """
        self._val = val
        self._der = der
        if hasattr(self._val, 'shape'):
            self._shape = self._val.shape
        else:
            self._shape = 1
        self._left_child = None
        self._right_child = None

    @property
    def val(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if isinstance(self._val, float):
            return round(self._val, 2)
        else:
            return self._val

    @property
    def der(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if isinstance(self._der, float):
            return round(self._der, 2)
        else:
            return self._der
            
    def __str__(self):
        return f"value: {self.val} \n" + f"derivative: {self.der}"

    #overloading add method
    def __add__(self, other):
        """[summary]

        Args:
            other (UDFunction or numeric): object to add with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val + other.val
            new_der = self._der + other.der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val + other
            new_der = self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    #overloading multiplication method
    def __mul__(self, other):
        """[summary]

        Args:
            other (UDFunction or numeric): object to multiply with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val * other.val
            new_der = self._der * other.val + self._val * other.der
        elif isinstance(other, (int, float, np.ndarray)):
            # TODO: check for vectors
            new_val = self._val * other
            new_der = self._der * other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    #overloading radd method
    def __radd__(self, other):
        """[summary]

        Args:
            other (UDFunction or numeric): object to add with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val + other.val
            new_der = self._der + other.der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val + other
            new_der = self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    #overloading rmul method
    def __rmul__(self, other):
        """[summary]

        Args:
            other (UDFunction or numeric): object to multiply with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val * other.val
            new_der = self._der * other.val + self._val * other.der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val * other
            new_der = self._der * other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __neg__(self):
        """[summary]

        Returns:
            UDFunction: object with neg value
        """
        return -1 * self

    def __sub__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(other, UDFunction):
            new_val = self._val - other.val
            new_der = self._der - other.der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val - other
            new_der = self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rsub__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(other, UDFunction):
            new_val = other.val - self._val
            new_der = other.der - self._der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other - self._val
            new_der = - self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
        
    def __truediv__(self, other): # bc - ad / c**2
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(other, UDFunction):
            new_val = self._val / other.val
            new_der = (self._der * other.val - self._val * other.der) / (other.val * other.val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val / other
            new_der = self._der / other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rtruediv__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(other, UDFunction):
            new_val = other.val / self._val
            new_der = (self._val * other.der - self._der * other.val) / (self._val * self._val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other / self._val
            new_der = - 1 * other * self._der / (self._val * self._val)
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __floordiv__(self, other): # self // other
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(other, UDFunction):
            new_val = self._val // other.val
            new_der = (self._der * other.val - self._val * other.der) // (other.val * other.val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val // other
            new_der = self._der // other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rfloordiv__(self, other): # other // self
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(other, UDFunction):
            new_val = other.val // self._val
            new_der = (self._val * other.der - self._der * other.val) // (self._val * self._val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other // self._val
            new_der = - 1 * other * self._der / (self._val * self._val)
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __pow__(self, degree):
        """[summary]

        Args:
            degree ([type]): [description]

        Returns:
            [type]: [description]
        """
        udf = self
        for d in range(degree - 1):
            udf = udf * self
        return udf

if __name__ == "__main__":
    a = 2.0
    x = UDFunction(a)
    y = 1//x
    print(y)



