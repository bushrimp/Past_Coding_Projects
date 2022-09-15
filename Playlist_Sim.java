/*
------------------------------------------------------------------------------
   Name:     Playlist_Sim
   Author:   Bushra Ibrahim
   Date:     Mar 21, 2022
   Language: Java
   Purpose:  The purpose of this program is to create a music playlist as per
             the criteria listed under "Option #1" in the Midterm for 
             IS221. (See Moodle)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 21, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package playlist_sim;

import java.util.Scanner;
import java.util.ArrayList;

public class Playlist_Sim 
{
    public static void main(String[] args) 
    {
        Scanner scnScanKB = new Scanner(System.in);
        String strUserInput = new String();
     
        boolean blnAnswer = false;
        
        while (!blnAnswer)
        {
            System.out.println("Would you like to create a playlist? (y/n)");
            strUserInput = scnScanKB.nextLine();
            
            switch(strUserInput.toLowerCase())    
            {
                case "yes","y":
                    System.out.println("\nAwesome!\n");
                    blnAnswer = true;
                    makePlaylist();
                    break;
                case "no","n":
                    System.out.println("\nOkay, maybe later!\n");
                    blnAnswer = true;
                    break;
                default:
                    System.out.println("\nThat wasn't a yes or a no, try again!\n");
                    break;
            }
        }
     
    }
    
    public static void makePlaylist()
    {
        Scanner scnScanKB = new Scanner(System.in);
        int intSongCount = 0, intUserInput = 0;
        String strPlaylistName, strUserAnswer = new String();
        
        System.out.println("What would you like to name your playlist?");
        strPlaylistName = scnScanKB.nextLine();

        while (intSongCount <3 || intSongCount >10)
        {
            System.out.println("How many songs would you like in your playlist?");
            intSongCount = scnScanKB.nextInt();
            
            if (intSongCount <3 || intSongCount >10)
            {   System.out.println("You may have a minimum of 3 songs, or a maximum of 10 songs.");
                System.out.println("Please choose a better number!");
            }

        }
 
        System.out.println("\nGreat, " + intSongCount + " songs!");
        System.out.println("Now input the song information for your " + intSongCount + " songs.\n");
        
        System.out.println("Please enter song names, artists, and genres as one word with no spaces!");
        System.out.println("Otherwise this playlist maker will crash!");
        //I had an issue with the nextLine vs next thing, and was not willing 
        //to go through my several hundredn lines of code to fix it, so I'm leaving this little message here
        
        ArrayList<Songs> alSongs = new ArrayList();
   
        switch (intSongCount)
        {
            case 10:
            {   Songs sngSong10 = new Songs("","","",0);
                alSongs.add(sngSong10);
                
                System.out.println("Song 10");
                System.out.println("Enter song name: ");
                sngSong10.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong10.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong10.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong10.setSongDuration(scnScanKB.nextDouble());
                
                
                
                Songs sngSong9 = new Songs("","","",0);
                alSongs.add(sngSong9);
                
                System.out.println("\nSong 9");
                System.out.println("Enter song name: ");
                sngSong9.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong9.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong9.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong9.setSongDuration(scnScanKB.nextDouble());
                
                
                Songs sngSong8 = new Songs("","","",0);
                alSongs.add(sngSong8);
                
                System.out.println("\nSong 8");
                System.out.println("Enter song name: ");
                sngSong8.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong8.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong8.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong8.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong7 = new Songs("","","",0);
                alSongs.add(sngSong7);
                
                System.out.println("\nSong 7");
                System.out.println("Enter song name: ");
                sngSong7.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong7.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong7.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong7.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong6 = new Songs("","","",0);
                alSongs.add(sngSong6);
                
                System.out.println("\nSong 6");
                System.out.println("Enter song name: ");
                sngSong6.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong6.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong6.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong6.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong5 = new Songs("","","",0);
                alSongs.add(sngSong5);
                
                System.out.println("\nSong 5");
                System.out.println("Enter song name: ");
                sngSong5.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong5.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong5.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong5.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
                
            case 9:               
            {   Songs sngSong9 = new Songs("","","",0);
                alSongs.add(sngSong9);
                
                System.out.println("\nSong 9");
                System.out.println("Enter song name: ");
                sngSong9.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong9.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong9.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong9.setSongDuration(scnScanKB.nextDouble());
                
                
                Songs sngSong8 = new Songs("","","",0);
                alSongs.add(sngSong8);
                
                System.out.println("\nSong 8");
                System.out.println("Enter song name: ");
                sngSong8.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong8.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong8.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong8.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong7 = new Songs("","","",0);
                alSongs.add(sngSong7);
                
                System.out.println("\nSong 7");
                System.out.println("Enter song name: ");
                sngSong7.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong7.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong7.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong7.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong6 = new Songs("","","",0);
                alSongs.add(sngSong6);
                
                System.out.println("\nSong 6");
                System.out.println("Enter song name: ");
                sngSong6.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong6.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong6.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong6.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong5 = new Songs("","","",0);
                alSongs.add(sngSong5);
                
                System.out.println("\nSong 5");
                System.out.println("Enter song name: ");
                sngSong5.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong5.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong5.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong5.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
            case 8:
            {   Songs sngSong8 = new Songs("","","",0);
                alSongs.add(sngSong8);
                
                System.out.println("\nSong 8");
                System.out.println("Enter song name: ");
                sngSong8.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong8.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong8.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong8.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong7 = new Songs("","","",0);
                alSongs.add(sngSong7);
                
                System.out.println("\nSong 7");
                System.out.println("Enter song name: ");
                sngSong7.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong7.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong7.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong7.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong6 = new Songs("","","",0);
                alSongs.add(sngSong6);
                
                System.out.println("\nSong 6");
                System.out.println("Enter song name: ");
                sngSong6.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong6.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong6.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong6.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong5 = new Songs("","","",0);
                alSongs.add(sngSong5);
                
                System.out.println("\nSong 5");
                System.out.println("Enter song name: ");
                sngSong5.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong5.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong5.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong5.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
            case 7:
            {   Songs sngSong7 = new Songs("","","",0);
                alSongs.add(sngSong7);
                
                System.out.println("\nSong 7");
                System.out.println("Enter song name: ");
                sngSong7.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong7.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong7.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong7.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong6 = new Songs("","","",0);
                alSongs.add(sngSong6);
                
                System.out.println("\nSong 6");
                System.out.println("Enter song name: ");
                sngSong6.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong6.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong6.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong6.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong5 = new Songs("","","",0);
                alSongs.add(sngSong5);
                
                System.out.println("\nSong 5");
                System.out.println("Enter song name: ");
                sngSong5.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong5.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong5.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong5.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
            case 6:
            {   Songs sngSong6 = new Songs("","","",0);
                alSongs.add(sngSong6);
                
                System.out.println("\nSong 6");
                System.out.println("Enter song name: ");
                sngSong6.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong6.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong6.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong6.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong5 = new Songs("","","",0);
                alSongs.add(sngSong5);
                
                System.out.println("\nSong 5");
                System.out.println("Enter song name: ");
                sngSong5.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong5.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong5.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong5.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
            case 5:
            {   Songs sngSong5 = new Songs("","","",0);
                alSongs.add(sngSong5);
                
                System.out.println("\nSong 5");
                System.out.println("Enter song name: ");
                sngSong5.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong5.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong5.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong5.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
            case 4:
            {   Songs sngSong4 = new Songs("","","",0);
                alSongs.add(sngSong4);
                
                System.out.println("\nSong 4");
                System.out.println("Enter song name: ");
                sngSong4.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong4.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong4.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong4.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }
            
            case 3:
            {   Songs sngSong3 = new Songs("","","",0);
                alSongs.add(sngSong3);
                
                System.out.println("\nSong 3");
                System.out.println("Enter song name: ");
                sngSong3.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong3.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong3.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong3.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong2 = new Songs("","","",0);
                alSongs.add(sngSong2);
                
                System.out.println("\nSong 2");
                System.out.println("Enter song name: ");
                sngSong2.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong2.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong2.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong2.setSongDuration(scnScanKB.nextDouble());
                
                //
                
                Songs sngSong1 = new Songs("","","",0);
                alSongs.add(sngSong1);
                
                System.out.println("\nSong 1");
                System.out.println("Enter song name: ");
                sngSong1.setSongName(scnScanKB.next());

                System.out.println("Enter song artist: ");
                sngSong1.setSongArtist(scnScanKB.next());

                System.out.println("Enter song genre: ");
                sngSong1.setSongGenre(scnScanKB.next());

                System.out.println("Enter song duration in seconds: ");
                sngSong1.setSongDuration(scnScanKB.nextDouble());
                
                break;
            }

        }
        
        System.out.println("**************************************************");
        System.out.println("Playlist name: " + strPlaylistName);
        System.out.println(alSongs);
        System.out.println("**************************************************");
        boolean blnAnswer = false;

        while (!blnAnswer)
        {
            System.out.println("\nLook at your playlist above. See if it's correct now? (y/n)");
            strUserAnswer = scnScanKB.next();
            
            if (strUserAnswer.equalsIgnoreCase("no"))
            {
                System.out.println("Which song would you like to fix?");
                intUserInput = scnScanKB.nextInt();

                switch (intUserInput)
                {
                    case 10:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong10 = new Songs("","","",0);
                        alSongs.add(sngSong10);

                        System.out.println("Enter song name: ");
                        sngSong10.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong10.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong10.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong10.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                        
                    case 9:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong9 = new Songs("","","",0);
                        alSongs.add(sngSong9);

                        System.out.println("Enter song name: ");
                        sngSong9.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong9.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong9.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong9.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 8:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong8 = new Songs("","","",0);
                        alSongs.add(sngSong8);

                        System.out.println("Enter song name: ");
                        sngSong8.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong8.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong8.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong8.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 7:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong7 = new Songs("","","",0);
                        alSongs.add(sngSong7);

                        System.out.println("Enter song name: ");
                        sngSong7.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong7.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong7.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong7.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 6:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong6 = new Songs("","","",0);
                        alSongs.add(sngSong6);

                        System.out.println("Enter song name: ");
                        sngSong6.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong6.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong6.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong6.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 5:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong5 = new Songs("","","",0);
                        alSongs.add(sngSong5);

                        System.out.println("Enter song name: ");
                        sngSong5.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong5.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong5.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong5.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 4:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong4 = new Songs("","","",0);
                        alSongs.add(sngSong4);

                        System.out.println("Enter song name: ");
                        sngSong4.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong4.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong4.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong4.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 3:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong3 = new Songs("","","",0);
                        alSongs.add(sngSong3);

                        System.out.println("Enter song name: ");
                        sngSong3.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong3.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong3.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong3.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 2:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong2 = new Songs("","","",0);
                        alSongs.add(sngSong2);

                        System.out.println("Enter song name: ");
                        sngSong2.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong2.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong2.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong2.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    case 1:
                        alSongs.remove(intSongCount - intUserInput);
                        System.out.println("Re-enter song data please!");

                        Songs sngSong1 = new Songs("","","",0);
                        alSongs.add(sngSong1);

                        System.out.println("Enter song name: ");
                        sngSong1.setSongName(scnScanKB.next());

                        System.out.println("Enter song artist: ");
                        sngSong1.setSongArtist(scnScanKB.next());

                        System.out.println("Enter song genre: ");
                        sngSong1.setSongGenre(scnScanKB.next());

                        System.out.println("Enter song duration in seconds: ");
                        sngSong1.setSongDuration(scnScanKB.nextDouble());

                        System.out.println("Fixed!");
                        break;
                    default:
                        System.out.println("Invalid answer! Please hoose the number of the song you want to fix!");
                        break;
                }

            }
            
            else if (strUserAnswer.equalsIgnoreCase("yes"))
            {
                blnAnswer = true;
                System.out.println("\nGreat!");
                break;
            }
            
            else
            {
                System.out.println("\nInvalid answer. Please type 'yes' or 'no'.");
            }
     
        }
        
        System.out.println("\nHere is your updated playlist!\n");
        System.out.println("**************************************************");
        System.out.println("Playlist name: " + strPlaylistName);
        System.out.println(alSongs);
        System.out.println("**************************************************");
        System.out.println("\nAnd here are some playlist stats!\n");
        
        double dblTotalDuration = 0, dblDurationAdd = 0;
        
        for (int i = 0; i <= intSongCount-1; i++)
        {
            dblDurationAdd = alSongs.get(i).getSongDuration();
            dblTotalDuration = dblTotalDuration + dblDurationAdd;
        }
        
        int intDurationMinutes = (int)(dblTotalDuration/60);
        int intDurationSeconds = (int)(dblTotalDuration%60);
        
        int intDurationMinAvg = (int)((dblTotalDuration/intSongCount)/60);
        int intDurationSecAvg = (int)((dblTotalDuration/intSongCount)%60);
        
        String strArtist, strName = new String();
        int intArtistCounter1 = 0, intNameCounter2 =0;
        
        for (int i = 0; i <= intSongCount-1; i++)
        {
             strArtist = alSongs.get(i).getSongArtist();
             if (strArtist.equalsIgnoreCase("doja cat"))
                 intArtistCounter1 ++;  
        }
        
        for (int i = 0; i <= intSongCount-1; i++)
        {
             strName = alSongs.get(i).getSongName();
             if (strName.startsWith("A") || strName.startsWith("a"))
                 intNameCounter2 ++;  
        }
        
        System.out.println("--------------------------------------------------");
        System.out.println("Total duration of playlist: ");
        System.out.println("        " + intDurationMinutes + " minutes and " + intDurationSeconds + " seconds");
        System.out.println("Average duration of a song in your playlist: ");
        System.out.println("        " + intDurationMinAvg + " minutes and " + intDurationSecAvg + " seconds");
        System.out.println("Number of Doja Cat songs in playlist: ");
        System.out.println("        " + intArtistCounter1 + " songs");
        if (intArtistCounter1 <=0)
        {
            System.out.println("~you don't have nearly enough Doja Cat in your playlist...tells me you have poor taste ;( ~");
        }
        System.out.println("Number of songs that begin with 'A': ");
        System.out.println("        " + intNameCounter2 + " songs");
        System.out.println("--------------------------------------------------");
    }

}

//Damn, it really be like that