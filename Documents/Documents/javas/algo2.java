

/**
 * algo2
 */
public class algo2 {

    public static void main(String[] args) 
    throws java.io.IOException    
    {
        int x=System.in.read();
        if (x%2==0) {
            System.out.println("this is cleary an even number");
        } else {
            System.out.println("this is cleary an odd number");
            if (x%3==0) {
                System.out.println("this is a number that can be divided by three");
            }
        }
        

    }
}