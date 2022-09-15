/*
------------------------------------------------------------------------------
   Name:     Number_Guessing_Game
   Author:   Bushra Ibrahim
   Date:     Mar 3, 2022
   Language: Java
   Purpose:  The purpose of this program is to play a random number guessing 
             game with the user (Hi-Lo). The program picks a random number
             between 1 and 100 (inclusive) and the user has to guess what it is.
             If it's too big or too small, the program will reprompt.
             When the user has guessed correctly, the program will end... 
             Unless they want to play again, then it will loop until
             They quit or say "No" to playing again. (See PP 5.4)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 3, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package number_guessing_game;

import java.util.Random;
import java.util.Scanner;

public class  Number_Guessing_Game 
{
    public static void main(String[] args) 
    {
        Scanner scnUserInput = new Scanner(System.in);

        String strUserAnswer = "";
        
        System.out.println("Do you want to play a game? (yes or no)");
        strUserAnswer = scnUserInput.nextLine();

        while (strUserAnswer.equals("yes"))
            {   
                System.out.println("I will now pick a random number. Can you guess what it is?.\n");
                Random randGen = new Random();
                
                int intRandInt = randGen.nextInt(100) + 1;
                int intGuessCounter = 0;

                System.out.println("Enter your first guess (enter 0 to quit): ");
                int intGuess1 = scnUserInput.nextInt();

                if (intGuess1 == 0)
                {System.out.println("You've quit!");
                 break;}

                    while (intGuess1 !=0)
                        {
                        intGuessCounter ++;

                        if (intGuess1 == intRandInt)
                            {System.out.println("You guessed correctly! My number was " + intRandInt + ".\n"
                                                 + "It took you " + intGuessCounter + " guesses.\n");
                            break;}
                        else if (intGuess1 > intRandInt)
                            {System.out.println("Too high! Guess again: ");}
                        else
                            {System.out.println("Too low! Guess again: ");}

                        intGuess1 = scnUserInput.nextInt();  
                        }

            System.out.print("Do you want to continue playing? (yes or no) \n");
            strUserAnswer = scnUserInput.next();
            }
        if (strUserAnswer.equals("no") )
        {
            System.out.println("Maybe later!");
        }
        
    }

}
