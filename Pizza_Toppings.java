/*
------------------------------------------------------------------------------
   Name:     Pizza_Toppings
   Author:   Bushra Ibrahim
   Date:     Mar 4, 2022
   Language: Java
   Purpose:  The purpose of this program is to allow user to choose pizza
             toppings using checkboxes, and calculating the cost of their
             pizza with that info. Pizza starts at $10, and $0.50 per
             topping. (See PP 5.16)
------------------------------------------------------------------------------
   ChangeLog:
   Who:      Bushra Ibrahim           Date:     Mar 4, 2022
   Desc.:    This is the original version of the code.
------------------------------------------------------------------------------
*/

package pizza_toppings;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import javafx.event.ActionEvent;
import javafx.scene.control.CheckBox;

public class Pizza_Toppings extends Application
{   
    CheckBox chkbx1 = new CheckBox("Extra Cheese");
    CheckBox chkbx2 = new CheckBox("Bell Peppers");
    CheckBox chkbx3 = new CheckBox("Olives");
    CheckBox chkbx4 = new CheckBox("Onions");
    CheckBox chkbx5 = new CheckBox("Tomatoes");
    CheckBox chkbx6 = new CheckBox("Mushrooms");
    
    Text myText1 = new Text("Pick your pizza toppings!");
    Text myText2 = new Text("Total: $10");
    
    double pizzaCost = 10;
    
    Group myGroup = new Group(myText1, myText2, chkbx1, chkbx2, chkbx3, chkbx4, chkbx5, chkbx6);
    
    Scene myScene = new Scene(myGroup, 300, 400, Color.LIGHTGREEN);
    
    @Override
    public void start(Stage myStage)
    {
        myText1.setX(70);
        myText1.setY(30);
        myText1.setFill(Color.DARKGREEN);
        
        myText2.setX(70);
        myText2.setY(350);
        myText2.setFill(Color.DARKGREEN);

        chkbx1.setLayoutX(50);
        chkbx1.setLayoutY(50);
        chkbx1.setOnAction(this::chkbxClick1);
        
        chkbx2.setLayoutX(50);
        chkbx2.setLayoutY(100);
        chkbx2.setOnAction(this::chkbxClick2);
        
        chkbx3.setLayoutX(50);
        chkbx3.setLayoutY(150);
        chkbx3.setOnAction(this::chkbxClick3);
        
        chkbx4.setLayoutX(50);
        chkbx4.setLayoutY(200);
        chkbx4.setOnAction(this::chkbxClick4);
        
        chkbx5.setLayoutX(50);
        chkbx5.setLayoutY(250);
        chkbx5.setOnAction(this::chkbxClick5);
        
        chkbx6.setLayoutX(50);
        chkbx6.setLayoutY(300);
        chkbx6.setOnAction(this::chkbxClick6);
            
        myScene.setRoot(myGroup); 
        
        myStage.setTitle("Pizza toppings + pizza cost");
        myStage.setScene(myScene);
        myStage.show();
    }
    
    
    public void chkbxClick1(ActionEvent event)
    {   //1
        if (chkbx1.isSelected() )
        {pizzaCost += 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}
        
        else if (!chkbx1.isSelected())
        {pizzaCost -= 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}}
    
    public void chkbxClick2(ActionEvent event)
    {   //2
        if (chkbx2.isSelected())
        {pizzaCost += 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}
        
        else if (!chkbx2.isSelected())
        {pizzaCost -= 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}}
    
    public void chkbxClick3(ActionEvent event)
    {   //3
        if (chkbx3.isSelected())
        {pizzaCost += 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}
        
        else if (!chkbx3.isSelected())
        {pizzaCost -= 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}}

    public void chkbxClick4(ActionEvent event)
    {   //4
        if (chkbx4.isSelected())
        {pizzaCost += 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}
        
        else if (!chkbx4.isSelected())
        {pizzaCost -= 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}}
    
    public void chkbxClick5(ActionEvent event)    
    {    //5
        if (chkbx5.isSelected())
        {pizzaCost += 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}
        
        else if (!chkbx5.isSelected())
        {pizzaCost -= 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}}
    
    public void chkbxClick6(ActionEvent event)
    {   //6
        if (chkbx6.isSelected())
        {pizzaCost += 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}
        
        else if (!chkbx6.isSelected())
        {pizzaCost -= 0.5;
         myText2.setText("Total: " + "$" + pizzaCost);}}

    public static void main(String[] args) 
    {
        launch(args);
    }

}
