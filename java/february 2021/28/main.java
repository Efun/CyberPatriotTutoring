class Main {  
  public static void main(String args[]) { 
    System.out.println("Hello, world!");
    printOnePlusOne();
    ifStatementTest();

    //use the alwaysReturnsFalse function in an if statement that prints "Pomegranate".
  if (alwaysReturnsFalse()) {

    System.out.println("Pomegranate");

  }

  }

  public static void printOnePlusOne() {
    //make an integer variable x with the initial value 1
    //add one to x
    //print out x
    //call this function from main
    //https://repl.it/languages/java10

    //python
    // x = 1
    // x += 1
    // print(str(x))

    //java variable format: <type> <name> = <value>;
    int x = 1;
    x++;
    System.out.println(x);
  }

  //write a function that is going to use if statements called ifStatementTest

  public static void ifStatementTest() {
    boolean x = true;
    boolean y = false;
    //challenge: don't change any existing code, add one line to make it so that we print out Tangerine instead of potato

    //python - if <condition>:
    //java - if (<condition>) {} - parentheses are important!
    if (x) {
        System.out.println("X is true!");
    }

    y = true;
    x = "potato";

    //if y is not true then print "Potato"
    //write an else block that prints "Tangerine"
    if (!y) {
      System.out.println("Potato.");
    }
    else {
      System.out.println("Tangerine");
    }
  }

  //write a function that returns false: alwaysReturnsFalse
  public static boolean alwaysReturnsFalse() {
    return(false); 
  }


  //public - you can access this item outside of the class that it's in
  //private - you can only access this item inside of the class that it's in
  //static - you do not have to instantiate a class to call a function
  //void - there's no return
  //return(type) - pass some value back
  //; - every line in java ends with one of these
  //{} - shows scope
  //++ - increment operator adds 1 to whatever you use it on;
  //-- - decrement operator subtracts 1 to whatever you use it on;
  //! - not operator for booleans
  //once we declare a variable, if we want to reassign it later, we do not have to put the type.
  //function syntax: <access control> <?static> <return TYPE> <name>() { }
}

class Test {
    public void printOnePlusOne() {
        //do some code here
    }

    public static void printTwoPlusTwo() {
        //do some other code here
    }
}

