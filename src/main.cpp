#include "Image.h"



// Pour compiler 
// >> cd Répertoire du projet 
// >> make 
// >> make r
// Merci de vérifier si les images ont été bien chargées (Read Image.###)
int main(int argc, char** argv){
    
    
    Image test("frame.jpg",4); 
    Image logo("fitedMoustache1.png",4);
    // I recuperate the coordinates where I have to add 
    test.overlay(logo, 188 ,272); 
    // (188,272)
    test.write("Output.png");
    return 0; 
}



