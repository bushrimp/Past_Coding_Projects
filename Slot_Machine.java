/*
------------------------------------------------------------------------------
   Name:     Slot_Machine
   Author:   Bushra Ibrahim
   Date:     Mar 3, 2022
   Language: Java
   Purpose:  The purpose of this program is to simulate a simple slot machine.
             If the user chooses to play, it'll roll out 3 random numbers within
             0-9 (inclusive) and if 2 or 3 of them match, they've "won." The 
             user can play again if they choose, or end the program by saying
             "No". (See PP 5.8)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 3, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package slot_machine;

import java.util.Random;
import java.util.Scanner;

public class Slot_Machine 
{
    public static void main(String[] args) 
    {
        Scanner scnUserInput = new Scanner(System.in);

        String strUserAnswer = "";
        
        System.out.println("Do you want to use this slot machine? (yes or no)");
        strUserAnswer = scnUserInput.nextLine();
        
        if (strUserAnswer.equals("no"))
            {System.out.println("Aww, too bad. Maybe next time!");}
        
        while (strUserAnswer.equals("yes"))
        {   
            System.out.println("And your 3 numbers are... ");
            
            Random randGen = new Random();
            int intRand1 = randGen.nextInt(10);
            int intRand2 = randGen.nextInt(10);
            int intRand3 = randGen.nextInt(10);
            
            System.out.println(intRand1 + ", " + intRand2 + ", " + intRand3);
            
            if (intRand1 == intRand2 && intRand1 == intRand3 && intRand2 == intRand3)
            {
                System.out.println("Congratulations! All three numbers match! You've won.\n");
                
            }
            
            if (intRand1 == intRand2 || intRand1 == intRand3 || intRand2 == intRand3)
            {
                System.out.println("Wow! Two numbers match! You're lucky!\n");
                
            }
            
            if (intRand1 != intRand2 && intRand1 != intRand3 && intRand2 != intRand3)
            {
                System.out.println("Aww, you've lost! None of your three numbers match.\n");
                
            }
            
        System.out.println("Thanks for playing!\n");
        
        System.out.print("Do you want to play again? (yes or no) \n");
        strUserAnswer = scnUserInput.next();     
        
        }
    }
}
