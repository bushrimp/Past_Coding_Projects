/*
------------------------------------------------------------------------------
   Name:     Slot_Machine_Jackpot
   Author:   Bushra Ibrahim
   Date:     Mar 9, 2022
   Language: Java
   Purpose:  The purpose of this program is to simulate slot machine, enhanced
             with additonal conditions.
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 9, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package slot_machine_jackpot;

import java.util.Scanner;
import java.util.Random;

public class Slot_Machine_Jackpot 
{
    static Scanner scan1 = new Scanner(System.in);
    
    public static void main(String[] args) 
    {
        boolean yesPlay = true;
        
        int looper = 0;
        
        while (yesPlay)
        {
            looper +=1;
            
            System.out.print("Do you want to play slots? (Y/N):  ");
            
            String userResp = scan1.next();
            
            switch(userResp.toLowerCase())
            {
                case "n","no","nah":
                    System.out.println("Thanks for stopping by!");
                    yesPlay = false;
                    break;
                    
                case "y","yes","yeah":
                    System.out.println("Great! Let's play!\n");
                    playSlots();
                    break;

                default:
                    System.out.println("Invalid response. Try again.\n");
                    break;
                  
            }
            
        }
    
    }
    
    public static void playSlots()
    {
        boolean Jackpot = false;
        
        int looper = 0;
        
        while (!Jackpot)
        {
            looper += 1;
            Random gen = new Random();

            int intOne = gen.nextInt(10);
            int intTwo = gen.nextInt(10);
            int intThree = gen.nextInt(10);

            System.out.println("Your slots: | " + intOne + " | " + intTwo + " | " + intThree + " | \n");

            if (intOne == intTwo && intOne == intThree && intTwo == intThree)
            {   
                System.out.println("*".repeat(50));
                System.out.println("J A C K P O T !");
                System.out.println("*".repeat(50) + "\n");
                System.out.println("It took you " + looper + " spins to hit the jackpot!\n");
                System.out.println("You're " + (looper < 50 ? "lucky" : "unlucky") + "!\n");
                Jackpot = true;
            }

            else if (intOne == intTwo || intOne == intThree || intTwo == intThree)
            {
                System.out.println("So close! I will see you on the other side.\n");
            }    

            else
            {
                System.out.println("You lost! Sucks to suck, I guess. \n");
            }
            
        }    
       
    }

}
