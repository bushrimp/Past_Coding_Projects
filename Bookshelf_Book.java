
/*
------------------------------------------------------------------------------
   Name:     Bookshelf_Book
   Author:   Bushra Ibrahim
   Date:     Feb 24, 2022
   Language: Java
   Purpose:  The purpose of this program is to establish the Books class
             for the driver code to run and make/update some book records.
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 24, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package bookshelf;

public class Bookshelf_Book //establishing the "Book" class
{
    String strTitle = "";
    String strAuthor = "";
    String strPublisher = "";
    String strCopyrightYear = "";

//constructor
public Books(String strNewTitle, String strNewAuthor,
             String strNewPublisher, String strNewCopyrightYear)
    {
        strTitle = strNewTitle;
        strAuthor = strNewAuthor;
        strPublisher = strNewPublisher;
        strCopyrightYear = strNewCopyrightYear;
    }

public Books(String strNewTitle)
    {
        strTitle = strNewTitle;
        strAuthor = "unknown";
        strPublisher = "n/a";
        strCopyrightYear = "unknown";
    }

//toString method
public String toString()
    {
        System.out.println("The book titled " + strTitle + ",");
        System.out.println("authored by " + strAuthor + ",");
        System.out.println("was published by " + strPublisher + ",");
        System.out.println("and copyrighted in the year " 
                           + strCopyrightYear + ".");
        return "";
    }

//mutators
public void setBookTitle (String strNewTitle)
    {
        strTitle = strNewTitle;
    }
public void setBookCopyrightYear(String strNewCopyrightYear)
    {
        strCopyrightYear = strNewCopyrightYear;
    }
public void setBookAuthor (String strNewAuthor)
    {
        strAuthor = strNewAuthor;
    }
public void setBookPublisher (String strNewPublisher)
    {
        strPublisher = strNewPublisher;
    }
    
    //accessors
public String getBookTitle()
    {
        return strTitle;
    }
public String getCopyrightYear()
    {
        return strCopyrightYear;
    }
public String getBookPublisher()
    {
        return strPublisher;
    }
public String getBookAuthor()
    {
        return strAuthor;
    }
}

