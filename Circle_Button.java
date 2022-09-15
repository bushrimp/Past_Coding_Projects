/*
------------------------------------------------------------------------------
   Name:     Circle_Button
   Author:   Bushra Ibrahim
   Date:     Feb 28, 2022
   Language: Java
   Purpose:  The purpose of this program is to generate circles of random
             radius in random locations within the window, and also change
             their color to random colors using different rgb combinations.
             Each change occurs when user clicks the button.
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Feb 28, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package circle_button;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.event.ActionEvent;
import java.util.Random;

public class Circle_Button extends Application
{
    Circle randCirc = new Circle(250, 250, 50, Color.rgb(0,0,0));
    Random gen = new Random();
    
    @Override
    public void start(Stage stgmyStage)
            
    {
        Button myButton = new Button("Click me!");
        myButton.setTranslateX(200);
        myButton.setTranslateY(200);
        myButton.setOnAction(this::buttonClick);
        
        Group myGroup = new Group(randCirc, myButton);
        Scene myScene = new Scene (myGroup, 550, 550);
        stgmyStage.setTitle("Random Circle");
        stgmyStage.setScene(myScene);
        stgmyStage.show();
    }
    
    public void buttonClick(ActionEvent event)
    {
        // setting up a new x,y center for every button push
        double newX = gen.nextDouble(450)+50;
        double newY = gen.nextDouble(450)+50;
        System.out.println("New center = " + newX + " x " + newY + "\n");
        
        // setting a new radius every time button is pushed
        double newRad = gen.nextDouble(40) + 10;
        System.out.println("New radius = " + newRad + "\n");
        
        // setting up so color changes randomly on every button push
        int r1, r2, r3;
        r1 = gen.nextInt(255);
        r2 = gen.nextInt(255);
        r3 = gen.nextInt(255);
        System.out.println("New color (rgb) = " + r1 + ", " + r2 + ", " + r3 + "\n");
        
        // some conditionals using the rgb colors
        if (r3 >= 150 && r1 < 150 && r2 < 200) 
            System.out.println("Bluish");
        else if (r3 < 150)
            System.out.println("Not quite so blue");
        else if (r3 == 0)
            System.out.println("Not blue at all");
        else
            System.out.println("Not sure");
        
        //changing the center, fill color, and radius of the circle
        randCirc.setCenterX(newX);
        randCirc.setCenterY(newY);
        randCirc.setFill(Color.rgb(r1, r2, r3));
        randCirc.setRadius(newRad);
        
        System.out.println();
    }
    
    public static void main(String[] args) 
    {
        launch(args);
    }

}
