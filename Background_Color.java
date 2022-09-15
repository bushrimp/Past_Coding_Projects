/*
------------------------------------------------------------------------------
   Name:     Background_Color
   Author:   Bushra Ibrahim
   Date:     Mar 2, 2022
   Language: Java
   Purpose:  The purpose of this program is to create a window with some 
             checkboxes that allow user to change the background color
             using the given options.
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 2, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package background_color;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.event.ActionEvent;
import javafx.scene.control.CheckBox;

public class Background_Color extends Application
{
    CheckBox myRedBox = new CheckBox("Red");
    CheckBox myGreenBox = new CheckBox("Green");
    CheckBox myBlueBox = new CheckBox("Blue");
    
    Text myText = new Text("Click checkbox to change BG color");
    
    Group myGroup = new Group(myText, myRedBox, myGreenBox, myBlueBox);
    
    Scene myScene = new Scene(myGroup, 300, 300);
    
    @Override
    public void start(Stage myStage)
    {
        
        myText.setX(70);
        myText.setY(30);

        myRedBox.setLayoutX(50);
        myRedBox.setLayoutY(50);
        myRedBox.setOnAction(this::checkBoxClick);

        myGreenBox.setLayoutX(50);
        myGreenBox.setLayoutY(100);
        myGreenBox.setOnAction(this::checkBoxClick);
      
        myBlueBox.setLayoutX(50);
        myBlueBox.setLayoutY(150);
        myBlueBox.setOnAction(this::checkBoxClick);
        
        
        myScene.setRoot(myGroup); 
        
        myStage.setTitle("Checkboxes");
        myStage.setScene(myScene);
        myStage.show();
    }
    
    public void checkBoxClick(ActionEvent event)
    {
        if((myRedBox.isSelected()) && (myGreenBox.isSelected()) && (myBlueBox.isSelected()))
            {
                myText.setText("All colors checked\n" + "Setting color to WHITE.");
                myScene.setFill(Color.WHITE);
            }
        else if((myRedBox.isSelected()) && (myGreenBox.isSelected()) && (!myBlueBox.isSelected()))
            {
                myText.setText("Red and green checked\n" + "Setting color to BROWN.");
                myScene.setFill(Color.BROWN);
            }
        else if((myRedBox.isSelected()) && (!myGreenBox.isSelected()) && (myBlueBox.isSelected()))
            {
                myText.setText("Red and blue checked\n" + "Setting color to VIOLET.");
                myScene.setFill(Color.VIOLET);
            }
        else if((!myRedBox.isSelected()) && (myGreenBox.isSelected()) && (myBlueBox.isSelected()))
            {
                myText.setText("Blue and green checked\n" + "Setting color to TEAL.");
                myScene.setFill(Color.TEAL);
            }
        else if((myRedBox.isSelected()) && (!myGreenBox.isSelected()) && (!myBlueBox.isSelected()))
            {
                myText.setText("Red was checked\n" + "Setting color to RED.");
                myScene.setFill(Color.RED);
            }
        else if((!myRedBox.isSelected()) && (!myGreenBox.isSelected()) && (myBlueBox.isSelected()))
            {
                myText.setText("Blue checked\n" + "Setting color to BLUE.");
                myScene.setFill(Color.BLUE);
            }
        else if((!myRedBox.isSelected()) && (myGreenBox.isSelected()) && (!myBlueBox.isSelected()))
            {
                myText.setText("Green checked\n" + "Setting color to GREEN.");
                myScene.setFill(Color.GREEN);
            }
        else if((!myRedBox.isSelected()) && (!myGreenBox.isSelected()) && (!myBlueBox.isSelected()))
            {
                myText.setText("None checked\n" + "Setting color to LIGHT GREY.");
                myScene.setFill(Color.LIGHTGREY);
            }
    }
    
    public static void main(String[] args) 
    {
        launch(args);
    }

}
