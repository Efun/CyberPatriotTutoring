public class Main {
  public static void main(String[] args) {
    //loops
    //while, for
    //while(<condition>) { some code }

    //using a while loop print out banana 3 times
    //you may need other variables to accomplish this
    //==, <, >, <=, >=, !=
    
    int x = 0;

    while (x < 3)
    {
        x += 1;
        System.out.println("banana");
    } 

    //lina: write a while loop that continues infinitely

    while (true)
    {
      
    }

    //hanna: write a while loop that just exits
    while (false)
    {
      
    }


    //for (<type> <name> = <value>; <condition>; <increment>) {}
    for (int i = 0; i < 3; i += 1) {
      System.out.println("banana");
    }
    //for () - another loop
    //type - usually int, type of the variable that you're incrementing
    //name - usually i, the name of the variable that you're incrementing
    //value - usually 0, initial value of the variable that you're incrementing
    //condition - (i < 3), some boolean that is evaluated every time we go through the loop
    //increment - i++/i += 2, this is the operation we do to the variable at each iteration of the loop


    //from python: lists are signified by []
    //in java: lists are called arrays, [] - 0 indexed
    //array declaration in java: <type>[] <name>
    //array has a property called length that tells you how many elements are inside
    int[] intArray = {1, 2, 3, 4};

    //how do you print out the first item of this array?
    System.out.println(intArray[0]);
    System.out.println(intArray.length); //this prints 4

    //how do we use a for loop to print out every single item of the array?
    for (int i = 0; i < intArray.length; i += 1) {
      System.out.println(intArray[i]);
    }
  }
}

