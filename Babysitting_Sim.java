/*
------------------------------------------------------------------------------
   Name:     Babysitting_Sim
   Author:   Bushra Ibrahim
   Date:     Mar 28, 2022
   Language: Java
   Purpose:  The purpose of this program is to demonstrate the value of modular
            coding by simulating a babysitting experience.  This will also
            introduce the concept of Arrays.
            Main Program Functions
                1. Do Introductions
                2. Do Fun Things
                3. Eat Dinner
                4. Do Fun Things
                5. Get Ready for Bed
                6. Send to Bed
                7. Get Paid and Go Home
            Sub-Functions
                1. Get Something to Drink
                2. Eat Something (Snack or Dinner)
                3. Go to Bathroom
                4. Read to Child
            Utility-Functions
                1. Speak to Child
                2. Get Child Response
                3. Count *at* Child
                4. Check the Time
------------------------------------------------------------------------------
   ChangeLog:
   ***********************************************************************************
    Who:        Bushra Ibrahim    Date: Mar 28, 2022
    Desc.:      Add missing functions
    ***********************************************************************************
    Who:        Ed Weber                    Date: Mar 27, 2022
    Desc.:      Updated do_introductions method to remove language that some may
                receive as being inappropriate or inuendos.
    ***********************************************************************************
    Who:        Ed Weber                    Date: Mar 26, 2022
    Desc.:      This is the original file.    
    ***********************************************************************************
------------------------------------------------------------------------------
*/

package babysitting_sim;

import java.util.Scanner;
import java.util.Random;

public class Babysitting_Sim 
{
    // Create public objects and variables used anywhere in this class
    public static final String MYNAME = "Bushra";
    public static Scanner scnKbd = new Scanner(System.in);
    public static Random rndGenerator = new Random();
    public static String strChildName = "";
    public static int intNumberOfDrinks = 0;
    public static boolean blnHasHadSnack = false;
    public static boolean blnHasHadDinner = false;

    public static void main(String[] args) 
    {
        do_introductions();
        do_fun_things();
        eat_dinner();
        speak_to_child("Now that dinner is done, what should we do now?");
        do_fun_things();
        if(check_the_time()){
            speak_to_child("Well, we have time for another activity before bed!");
            do_fun_things();
        } else {
            speak_to_child("Well, it's getting pretty late now... Time to get ready for bed.");
        }
        get_ready_for_bed();
        send_to_bed();
        get_paid_and_go_home();
    }
    
    public static void do_introductions() {
        speak_to_child("Hi! My name is " + MYNAME + " and "
                + "\n\tI'm going to be your baybsitter tonight!\n\tWhat is your name?");
        strChildName = get_child_response();
        speak_to_child("Well hello there " + strChildName + "!"
                + "\n\tBefore dinner, you will have some play time"
                + "\n\tand then maybe a little more play time after dinner."
                + "\n\tThen, you'll get ready for bed and have your bedtime story.");
    }

     public static void do_fun_things() {
        // an array of fun things to be chosen by child or randomly
        String[] arrstrFunThings = {"Play with Action Toys", "Play with Dolls",
            "Play a Board Game", "Play a Card Game", "Play a Video Game",
            "Plan for World Domination"
        };
        String strChildSays = "";
        do {
            int intIndex = rndGenerator.nextInt(arrstrFunThings.length);
            speak_to_child("Would you like to " + arrstrFunThings[intIndex] + "?");
            strChildSays = translateChildResponse(get_child_response());
            if (strChildSays.equals("POTTY")) {
                String strPottyAnswer = go_to_bathroom();
                switch (strPottyAnswer) {
                    case "Going to the bathroom":
                    case "Washing hands":
                    case "Combing hair":
                        speak_to_child("OK - Finish up!");
                        break;
                    case "Taking a bath":
                    case "Brushing teeth":
                        speak_to_child("No - you can do that after dinner and before bedtime.");
                        break;
                    case "Playing":
                        speak_to_child("That's what I thought!  Come back out here!");
                        break;
                }
            } else if (strChildSays.equals("FOOD")) {
                if (!blnHasHadDinner) {
                    speak_to_child("No snacks right now... We'll have dinner in a little bit.");
                } else {
                    if (blnHasHadSnack) {
                        speak_to_child("No, you've already had a snack tonight.");
                    } else {
                        if (!check_the_time()) {
                            speak_to_child("No, it's too soon for a snack.  Maybe later...");
                        } else {
                            speak_to_child("I suppose you can have a snack now.");
                            eat_something();
                            blnHasHadSnack = true;
                        }
                    }
                }
            } else if (strChildSays.equals("DRINK")) {
                if (intNumberOfDrinks <= 4) {
                    get_something_to_drink();
                } else {
                    speak_to_child("You've had enough to drink for now...");
                }
            }
        } while (!strChildSays.equalsIgnoreCase("OK"));
        speak_to_child("Well - that was fun!");
    }

    public static void eat_dinner() {
        speak_to_child("It is now time for dinner.");
        String strDinnerOption = "";
        boolean blnDinnerIsSelected = false;
        int intListRepeated = 0;
        // an array of dinner items to be chosen by child or by you or randomly
        String[] arrstrDinnerOptions = {"Veggie Pizzas", "Stir Fry's", "P, B, & J Sandwiches",
            "Mac & Cheese's", "Veggie Burgers", "Bowls of Oatmeal", "Bean Burritos"};
        String strChildSays = "";
        do {
            if (intListRepeated > 2) {    // repeat the list two times only
                strDinnerOption = arrstrDinnerOptions[rndGenerator.nextInt(arrstrDinnerOptions.length)];
                speak_to_child("Well, since you can't decide, I'll pick.  We'll have "
                        + "\n\t" + strDinnerOption + " for dinner tonight.");
                blnDinnerIsSelected = true;
            } else {
                do {
                    for (int i = 0; i < arrstrDinnerOptions.length; i++) {
                        if (i == 0) {
                            intListRepeated++;
                        }
                        strDinnerOption = arrstrDinnerOptions[i];
                        speak_to_child("Would you like to have " + strDinnerOption + " for dinner?");
                        strChildSays = translateChildResponse(get_child_response());
                        if (strChildSays.equals("POTTY")) {
                            go_to_bathroom();
                        } else if (strChildSays.equals("FOOD")) {
                            speak_to_child("Yes, that's what we're trying to decide on right now...");
                        } else if (strChildSays.equals("DRINK")) {
                            if (intNumberOfDrinks <= 4) {
                                get_something_to_drink();
                            } else {
                                speak_to_child("You've had enough to drink for now...");
                            }
                        }
                        if (strChildSays.equalsIgnoreCase("OK")) {
                            blnDinnerIsSelected = true;
                            break;
                        }
                    }
                } while ((!strChildSays.equalsIgnoreCase("OK")) && (intListRepeated < 3));
                if (strChildSays.equalsIgnoreCase("OK")) {
                    blnDinnerIsSelected = true;
                }
            }
        } while (!blnDinnerIsSelected);
        speak_to_child(strDinnerOption + " won't take too long to get ready!"
                + "\n\t...".repeat(5)
                + "\n\tLet's Eat!!!");
        speak_to_child("\n\t...".repeat(5) + "\n\tWell!  That was delicious!"
                + "\n\tI'll clean up the dishes after you go to bed!");
        blnHasHadDinner = true;
    }

    public static void get_ready_for_bed() {
        // an array of bed preparation activities to be performed
        speak_to_child("(Get Ready for Bed here... this code to be replaced...)");
    }

    public static void send_to_bed() {
        // an array of bed activities to be performed (or avoided)!
        speak_to_child("(Send to Bed here... this code to be replaced...)");
    }

    public static void get_paid_and_go_home() {
        // an array of activities to end the night
        speak_to_child("(Get Paid and Go Home here... this code to be replaced...)");
    }

    public static void get_something_to_drink() {
        if (intNumberOfDrinks >= 4) {
            speak_to_child("You've had too much to drink, let's do something else.");
                }
        else
        {
        speak_to_child("Okay, let's get you a drink!.");
        String strDrinkOption = "";
        boolean blnDrinkIsSelected = false;
        int intListRepeated = 0;
        // an array of drink items to be chosen by child or by you or randomly
        String[] arrstrDrinkOptions = {"water","milk","lemonade","juice","soda","CapriSun"};
        String strChildSays = "";
        do {
            if (intListRepeated >= 2) {    // repeat the list two times only
                strDrinkOption = arrstrDrinkOptions[rndGenerator.nextInt(arrstrDrinkOptions.length)];
                speak_to_child("Well, since you can't decide, I'll pick.  We'll drink some "
                        + "\n\t" + strDrinkOption + ".");
                blnDrinkIsSelected = true;
            } else {
                do {
                    for (int i = 0; i < arrstrDrinkOptions.length; i++) {
                        if (i == 0) {
                            intListRepeated++;
                        }
                        strDrinkOption = arrstrDrinkOptions[i];
                        speak_to_child("Would you like to drink " + strDrinkOption + "?");
                        strChildSays = translateChildResponse(get_child_response());
                        if (strChildSays.equals("POTTY")) {
                            go_to_bathroom();
                        } else if (strChildSays.equals("FOOD")) {
                            speak_to_child("No, we're picking a drink now. You can eat something later.");
                        } else if (strChildSays.equals("DRINK")) {
                            speak_to_child("Yes, that's what we're deciding right now.");
                        } else if (strChildSays.equals("SLEEP")) {
                            speak_to_child("No, it's not bedtime yet.");
                        }           
                        if (strChildSays.equalsIgnoreCase("OK")) {
                            blnDrinkIsSelected = true;
                            break;
                        }
                    }
                } while ((!strChildSays.equalsIgnoreCase("OK")) && (intListRepeated < 3));
                if (strChildSays.equalsIgnoreCase("OK")) {
                    blnDrinkIsSelected = true;
                }
            }
        } while (!blnDrinkIsSelected);
        intNumberOfDrinks ++;
        speak_to_child("Alright, let's get you " + strDrinkOption + " to drink!"
                + "\n\t...".repeat(3) + "\n\t Are you done drinking " + strDrinkOption + "? Great!"
                + "\n\tI'll wash the cups after dinner.");
                }
    }

    public static void eat_something() {
        // an array of snack items (or dinner) to be chosen by child or by you or randomly
        speak_to_child("(Eat Something here... this code to be replaced...)");
    }

    public static String go_to_bathroom() {
        String[] arystrBathroomThings = {
            "Going to the bathroom", "Washing hands", "Taking a bath",
            "Brushing teeth", "Combing hair", "Playing"
        };
        speak_to_child("You've been in there a while... now what are you doing in there?");
        String strWhatChildIsDoing = arystrBathroomThings[rndGenerator.nextInt(arystrBathroomThings.length)];
        System.out.println(strWhatChildIsDoing);
        return strWhatChildIsDoing;
    }

    public static void read_to_child() {
        // an array of types of reading to be chosen by child or by you or randomly
        speak_to_child("(Read to Child here... this code to be replaced...)");
    }

    public static void speak_to_child(String strWhatToSay) {
        // more code can go here to handle different *ways* to say something!
        System.out.println(">>>\t" + strWhatToSay);
    }

    public static String get_child_response() {
        // more code goes here to simulate possible child responses!
        String strTheReply = scnKbd.nextLine();
        return strTheReply;
    }

    public static void count_at_child() {
        // an array of *consequences* that might happen for bad behavior and the 
        // typical counting that one does with a child until the counting reaches 3!
    }

    public static boolean check_the_time() {
        // normally - this would check the *actual* time and return the time value
        // for this, we will consider it a random test to answer the question
        // '... is now the right time for ... (whatever we may be asking)
        // so we just return a random true or false
        return rndGenerator.nextBoolean();
    }
    
    public static String translateChildResponse(String strWhatTheySaid) {
        String strWhatTheyMeant = "";
        switch (strWhatTheySaid.trim().toLowerCase()) {
            case "yes", "y", "yeah", "yay", "ok", "sure", "duh", "whatever", "whatev", "why not",
                    "please", "yes please", "goody", "goody goody" ->
                strWhatTheyMeant = "OK";
            case "no", "n", "no way", "uh-uh", "eww", "really?", "blech", "pff",
                    "no thank you" ->
                strWhatTheyMeant = "NO";
            case "potty", "bathroom", "tinkle", "pee-pee", "poop", "poo-poo" ->
                strWhatTheyMeant = "POTTY";
            case "hungry", "food", "dinner", "snack", "cookies", "fruit" ->
                strWhatTheyMeant = "FOOD";
            case "thirsty", "drink", "milk", "water", "juice", "lemonade" ->
                strWhatTheyMeant = "DRINK";
            case "tired", "sleepy", "bored" ->
                strWhatTheyMeant = "SLEEP";
            default ->
                strWhatTheyMeant = "UNCLEAR";
        }
        return strWhatTheyMeant;
    }

}
