
/*
------------------------------------------------------------------------------
   Name:     Songs
   Author:   Bushra Ibrahim
   Date:     Mar 21, 2022
   Language: Java
   Purpose:  The purpose of this program is to define the song class and 
             have constructors, accessors, and mutators to edit song
             objects. (will be used in driver code)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 21, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package playlist_sim;

public class Playlist_Songs 
{
    String strSongName = "";
    String strSongArtist = "";
    String strSongGenre = "";
    double dblSongDuration = 0; // in seconds
    
    //constructor
    public Songs(String strNewSongName, String strNewSongArtist,
             String strNewSongGenre, double dblNewSongDuration)
        {
            strSongName = strNewSongName;
            strSongArtist = strNewSongArtist;
            strSongGenre = strNewSongGenre;
            dblSongDuration = dblNewSongDuration;
        }

    //toString method
    public String toString()
        {
            System.out.println("\nSong: " + strSongName);
            System.out.println("Artist: " + strSongArtist);
            System.out.println("Genre: " + strSongGenre);
            System.out.println("Duration: " + dblSongDuration);
            return "";
        }
    
    //mutators
    public void setSongName (String strNewSongName)
        {
            strSongName = strNewSongName;
        }
    public void setSongArtist(String strNewSongArtist)
        {
            strSongArtist = strNewSongArtist;
        }
    public void setSongGenre (String strNewSongGenre)
        {
            strSongGenre = strNewSongGenre;
        }
    public void setSongDuration (double dblNewSongDuration)
        {
            dblSongDuration = dblNewSongDuration;
        }
    
    //accessors
    public String getSongName()
        {
            return strSongName;
        }
    public String getSongArtist()
        {
            return strSongArtist;
        }
    public String getSongGenre()
        {
            return strSongGenre;
        }
    public double getSongDuration()
        {
            return dblSongDuration;
        }

}
