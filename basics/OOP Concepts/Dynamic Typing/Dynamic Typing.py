"""
One of the standout features of Python language is that it is a dynamically typed language. The compiler-based languages C/C++, Java, etc. are statically typed. Let us try to understand the difference between static typing and dynamic typing.

In a statically typed language, each variable and its data type must be declared before assigning it a value. Any other type of value is not acceptable to the compiler, and it raises a compile-time error.

Let us take the following snippet of a Java program −

public class MyClass {
   public static void main(String args[]) {
      int var;
      var="Hello";

      System.out.println("Value of var = " + var);
   }
}
Here, var is declared as an integer variable. When we try to assign it a string value, the compiler gives the following error message −

/MyClass.java:4: error: incompatible types: String cannot be converted to int
   x="Hello";
     ^
1 error
"""