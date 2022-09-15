/*
------------------------------------------------------------------------------
   Name:     Average
   Author:   Bushra Ibrahim
   Date:     Feb 28, 2022
   Language: Java
   Purpose:  The purpose of this program is to take integers from the user
             and keep track of the sum of those integers, and return their
             average once 0 is entered. If 0 is entered as the very first 
             entry, the program simply stops as no "values" were entered.
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 28, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package average;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Average 
{

    public static void main(String[] args) 
            
    {
      int sum = 0, value, count = 0;
      double average;
      Scanner scan = new 
      Scanner(System.in); 
      System.out.print("Enter an integer (0 to quit): "); 
      value = scan.nextInt();

      while (value != 0) 
      {
         count++;
         sum += value;
         System.out.println("The sum so far is " + sum);
         System.out.print("Enter an integer (0 to quit): ");
         value = scan.nextInt();
      }
      
      System.out.println();
      if (count == 0)
         System.out.println("No values were entered.");
      
      else
      {
         average = (double)sum / count;
         DecimalFormat fmt = new DecimalFormat("0.###");
         System.out.println("The average is " + fmt.format(average));
      }
      
      System.out.println("The sum was " + sum);
    }

}
