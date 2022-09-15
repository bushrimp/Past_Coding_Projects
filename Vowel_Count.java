/*
------------------------------------------------------------------------------
   Name:     Vowel_Count
   Author:   Bushra Ibrahim
   Date:     Mar 9, 2022
   Language: Java
   Purpose:  The purpose of this program is to take an input string from 
             the user and print back how many vowels that string had, as well
             as how many of each vowel, and how many nonvowel characters.
             The program said only "lowercase vowels" but then the nonvowel 
             characters would also include capitalized vowels, so I chose to
             ignore that, and just have my program count all vowels, capital
             or not. (See PP 6.9)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 9, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package vowel_count;

import java.util.Scanner;

public class Vowel_Count 
{
    public static void main(String[] args) 
    {
        int intA = 0, intE = 0, intI = 0, intO = 0, intU = 0, intOther = 0;
        String strUserString;
        Scanner scnScanKybd = new Scanner (System.in);
        
        System.out.println("Enter a string, and I'll give you\n" 
                            + "your vowel stats (inclusive of capital and lowercase vowels):  ");
        strUserString = scnScanKybd.nextLine();
        
        for (int intUserStringLength = 0; 
             intUserStringLength < strUserString.length(); 
             intUserStringLength ++)
        {
            char charCurrentCharacter = strUserString.charAt(intUserStringLength);
            
            switch(charCurrentCharacter)
            {
                case 'a', 'A':
                    intA ++;
                    break;
                case 'e','E':
                    intE ++;
                    break;
                case 'i','I':
                    intI ++;
                    break;
                case 'o','O':
                    intO ++;
                    break;
                case 'u','U':
                    intU ++;
                    break;
                default:
                    intOther ++;
                    break;   
            }
                
        }
        
        System.out.println("\nHere are your vowel stats!\n");
        System.out.println("Total number of vowels in your string: " + (intA + intE + intI + intO + intU));
        System.out.println();
        System.out.println("Number of A's: " + intA);
        System.out.println("Number of E's: " + intE);
        System.out.println("Number of I's: " + intI);
        System.out.println("Number of O's: " + intO);
        System.out.println("Number of U's: " + intU);
        System.out.println();
        System.out.println("Number of nonvowel characters: " + intOther);
    }

}
