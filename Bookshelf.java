/*
------------------------------------------------------------------------------
   Name:     Bookshelf
   Author:   Bushra Ibrahim
   Date:     Feb 24, 2022
   Language: Java
   Purpose:  The purpose of this program is to establish a class called Books
             and create a few Books objects, and update one. (see PP 4.7)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 24, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package bookshelf;

public class Bookshelf //acts as the "Bookshelf" driver class that PP 4.7 asks for
{
    public static void main(String[] args) 
    {
        System.out.println("Welcome to IS221 Bookshelf!\n");
        
        Books bookBook1 = new Books("Atomic Habits","James Clear","Penguin Random House", "2018");
        System.out.println(bookBook1);
        
        Books bookBook2 = new Books("Math Through the Ages","William P. Berlinghoff & "
                                    + "Fernando Q. Gouvea","Dover Publication", "2002");
        System.out.println(bookBook2);
        
        Books bookBook3 = new Books("The Epic of Gilgamesh","unknown","unknown", "2100 B.C.E");
        System.out.println(bookBook3);
        
        bookBook3.setBookAuthor("Sin-Liqi-Unninni");
        bookBook3.setBookPublisher("The Babylonian civilization");
        System.out.println("The Epic of Gilgamesh has unclear origins, and so the author and "
                + "publisher had to be updated.");
        System.out.println("Here is the updated record: \n");
        System.out.println(bookBook3);
        
        bookBook2.setBookCopyrightYear("2014");
        System.out.println("Math Through the Ages was copyrighted a second time for its"
                + " second edition in the year 2014");
        System.out.println("and so that record has been updated. Here is the updated record: \n");
        System.out.println(bookBook2);
       
    }

}
