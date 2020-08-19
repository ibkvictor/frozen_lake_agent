package adult;
/**
 * Baby
 */
public class Baby {
    double weight;
    String name;
    String [] siblings;
    boolean isMale;
    static int numberBabiesMade =0;


    static double rootof2;
    static double rootof3;

    // STATIC BLOCK THAT IS IMPLEMENTED BEFORE ANYTHING

    static{
        rootof2 = Math.sqrt(2.0);
        rootof3 = Math.sqrt(3.0);
    }
// final prevents overridding of a super class varible or method by a subclass
// private protects class data from being altered making it accessible only by using a proxy variable
// the abstract class is used to create a dummy method or super class such to ensure that all the subclasses override it
// by the way a sub class is defined class victor extends man
    Baby(final double weight, final String name, final String[] siblings, final boolean isMale) {
        numberBabiesMade += 1;
        this.weight = weight;
        this.name = name;
        this.siblings = siblings;
        this.isMale = isMale;

    }

    double babyfood(final int FoodEaten) {
        if ((FoodEaten >= 0) && (FoodEaten < weight)) {
            weight += FoodEaten;
        }
        System.out.println("WE HAVE ACCOUNTED FOR THE FOOD EATEN");
        return weight;
    }

    static void cry(final Baby thebaby) {
        System.out.println(thebaby.name + "cries");
    }

    public static void main(final String[] arguments) throws java.io.IOException {

        final String[] siblings1 = { "chiamaka", "victor", "amarachi" };
        // objects or instances
        Baby.numberBabiesMade = 10;

        final Baby victor = new Baby(29.9D, "victor", siblings1, true);
        Baby.numberBabiesMade = 2; // practising with number of babies made to learn static definition (type) in
                                   // java

        // practicing private access modiifier with test.class
        // test.Babies=5;
        // it says it is not visible for change

        System.out.println(victor.name);
        System.out.println(Baby.numberBabiesMade);
        System.out.println(Baby.numberBabiesMade);

        final int e = 11 / 5;
        System.out.println(e);

        
    }
}
/**
 * test
 */
class test {
    
}
