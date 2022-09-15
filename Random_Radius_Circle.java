/*
------------------------------------------------------------------------------
   Name:     Random_Radius_Circle
   Author:   Bushra Ibrahim
   Date:     Feb 18, 2022
   Language: Java
   Purpose:  The purpose of this program is to draw a circle of a random 
             radius every time it runs. Radii are chosen from a range of 
             50-150 (see PP 3.13)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 18, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package random_radius_circle;

import java.util.Random;
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.*;

public class Random_Radius_Circle extends Application
        
{        
    public void start(Stage primaryStage)
            
 {
    Random gen = new Random();
    
    int radius;
    radius = gen.nextInt(100) + 51;
    
    Circle sun = new Circle(200, 200, radius);
    sun.setFill(Color.CRIMSON);
    
    Group root = new Group(sun);
    Scene scene = new Scene(root, 500, 500, Color.BLACK);
    
    primaryStage.setTitle("Random Radius Circle");
    primaryStage.setScene(scene);
    primaryStage.show(); 
    
    System.out.println("Radius: " + radius);
}
    public static void main(String[] args)
            
    {
        launch(args);
    }
}
