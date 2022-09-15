/*
------------------------------------------------------------------------------
   Name:     Fraction_To_Decimal
   Author:   Bushra Ibrahim
   Date:     Feb 9, 2022
   Language: Java
   Purpose:  The purpose of this program is to take 2 integer inputs from the
             user, which represent the numerator and the denominator of a
             fraction (respectively), and return the decimal version of
             that fraction. (see PP 2.13)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 9, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package fraction_to_decimal;

import java.util.Scanner;

public class Fraction_To_Decimal {


    public static void main(String[] args) {
        Scanner scnKey = new Scanner (System.in);
        
        System.out.println("Hello. This program takes 2 integers from you" +
                          " that represent the numerator and denominator");
        System.out.println(" of a fraction, respectively, and prints back" +
                          " the decimal equivalent of that fraction.");
        System.out.println(" Please enter your first integer.");
        int intNum = scnKey.nextInt();
        scnKey.nextLine();
        System.out.println("Please enter your second integer.");
        int intDen = scnKey.nextInt();
        scnKey.nextLine();
        System.out.println("Thank you. Here is your fraction as a decimal.");
        float fltNum = intNum;
        float fltDen = intDen;
        float fltDec = fltNum/fltDen;
        System.out.println("Decimal version of your fraction: " + fltDec);
    }

}
