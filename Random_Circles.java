/*
------------------------------------------------------------------------------
   Name:     Random_Circles
   Author:   Bushra Ibrahim
   Date:     Mar 10, 2022
   Language: Java
   Purpose:  The purpose of this program is to draw 100 circles of random size,
             color, and radius all over the window. They have to be within the
             window, can't have a piece of it outside the bounds of the scene.
             (See PP 6.14)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 10, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package random_circles;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import java.util.Random;

public class Random_Circles extends Application
{
    public void start (Stage stgMyStage)
    {
        Random rndGen = new Random();
        Group grpMyGroup = new Group ();
        
        double dblNewX, dblNewY, dblNewRadius;
        int intRed, intGreen, intBlue;
        
        for (int count = 1; count <= 100; count++) 
        {
            dblNewX = rndGen.nextDouble(450) + 50;
            dblNewY = rndGen.nextDouble(450) + 50;
            dblNewRadius = rndGen.nextDouble(40) + 10;
            
            intRed = rndGen.nextInt(255) + 1;
            intGreen = rndGen.nextInt(255) + 1;
            intBlue = rndGen.nextInt(255) + 1;
            
            Circle crcRandCirc = new Circle();
            crcRandCirc.setCenterX(dblNewX);
            crcRandCirc.setCenterY(dblNewY);
            crcRandCirc.setFill(Color.rgb(intRed, intGreen, intBlue));
            crcRandCirc.setRadius(dblNewRadius);
            
            grpMyGroup.getChildren().add(crcRandCirc);
        }
        
        Scene scnMyScene = new Scene (grpMyGroup, 550, 550, Color.BLACK);
        stgMyStage.setTitle("Random Circles");
        stgMyStage.setScene(scnMyScene);
        stgMyStage.show();
        
    }
            

    public static void main(String[] args) 
    {
        launch(args);
    }

}
