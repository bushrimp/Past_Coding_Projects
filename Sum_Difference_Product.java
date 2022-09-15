/*
------------------------------------------------------------------------------
   Name:     Sum_Difference_Product
   Author:   Bushra Ibrahim
   Date:     Feb 9, 2022
   Language: Java
   Purpose:  The purpose of this program is to take 2 floating point variable
             values from the user (which will look just like inputting integers)
             and returning their sum, difference, and product. (see PP 2.3)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 9, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package sum_difference_product;

import java.util.Scanner;

public class Sum_Difference_Product {


    public static void main(String[] args) {
        Scanner scnKey = new Scanner (System.in);
        
        System.out.println("Hello. This program takes 2 numbers from you" +
                          " and prints back their sum, difference, and product" +
                          " as floating point variables. Please enter your" +
                          " first number.");
        float fltOne = scnKey.nextInt();
        scnKey.nextLine();
        System.out.println("Please enter your second number.");
        float fltTwo = scnKey.nextInt();
        scnKey.nextLine();
        System.out.println("Thank you. Here are the sum, difference, and"
                +          " product of the 2 numbers you entered.");
        float fltSum = (fltOne + fltTwo);
        System.out.println("Sum: " + fltSum);
        float fltDiff = (fltOne - fltTwo);
        System.out.println("Difference: " + fltDiff);
        float fltProd = (fltOne * fltTwo);
        System.out.println("Product: " + fltProd);
    }

}
