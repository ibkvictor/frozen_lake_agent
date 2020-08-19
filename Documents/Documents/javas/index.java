// import javax.lang.model.util.ElementScanner6;

// public class index {
//     public static void main(String args[])
//     throws java.io.IOException {
//         // char lower_letters, upper_letters;
//         // lower_letters = (char) System.in.read();
//         // upper_letters = (char) ((int) (lower_letters - 32));
//         // System.out.println(upper_letters);
//         // Vehicle minivan = new Vehicle (7,21,16);
//         // Vehicle sportscar = new Vehicle (10,11,18);
//         // // int range;
//         // int dist = 1000;
//         // System.out.println(minivan.fuelNeeded(dist));
//         // System.out.println(sportscar.fuelNeeded(dist));

//         // range = minivan.mpg * minivan.fuelcap;
//         // System.out.println("the range of the minivan is :" + range);
//         // ChkNum Numbers = new ChkNum();
//         // Numbers.no = System.in.read();
//         // System.out.println(Numbers.isEven(Numbers.no));
//         // create ob = new create(0);
//         // for (int i = 0; i < 10000000; i++) {
//         //     ob.generator(i);
//         // }
//         int arrai[] =  {20,-20,50,4,82,3,5,2,5,34};
//         int arrai2[] = new int [10];
//         int length =  arrai.length;
        

//         for (int i = 0; i < arrai.length; i++) {
//             // if (arrai2.length>= arrai.length) {
                
//             // }
            
//         }
//         for (int i = 0; i < 10; i++) {
//             // System.out.println("the element is " + arrai[i]);
            
//         }
//         for (int i = 1; i < length ; i++) {
//             // int b;
//             // b =  length -1;
//             // for (; b >= i; ) {
//             //     int t;
//             //     if (arrai[b-1]>arrai[b]) {
//             //         t = arrai[b-1];
//             //         arrai[b-1] = arrai[b];
//             //         arrai[b] = t;
//             //     }
//             //     b--;
//             // }
//         }
//         for (int i = 0; i < 10; i++) {
//             // System.out.println("the element is " + arrai[i]);
            
//         }
//         if (length == 10){
//             // int x = 0;
//             //  System.out.println(arrai[x++]);   
//         }
//         // Queue bigq = new Queue(100);
//         // Queue smallq = new Queue(4);
//         // char ch;
        
//         // for (int i = 0; i <26; i++) 
//         //     // bigq.put((char )('A' + i)) ;

//         for (int i = 0; i <26; i++) {
//             // ch = bigq.get();
//             // if (ch!=0)
//             // System.out.print(ch);
//         }
//         for (int i = 0; i <5; i++) {
//             // ch = (char )('Z' - i);
//             // System.out.println("attempting to store" + ch);
//             // smallq.put(ch) ;
            
//         }
//         for (int i = 0; i <5; i++) {
//             // ch = smallq.get();
//             // if (ch!=0)
//             // System.out.print(ch);
//         }
//         boolean found = false;
//         for (int ch1 : arrai) {
//             // if(ch1 == 5){
//             //     found = true;
//             }
//             if (found){
//                 // System.out.print("we have found 5      " + ch1);
//                 // break;
//             } 
//         // String str = "this is one way to define a string object";
//         // String str2 = new String(str);
//         // String str3 = new String("it is not a mere sequence of characters");
//         // String str4 = str;
//         // if (str.equals(str2)){
//         // System.out.println("the are equal");}
        
//         // if((str.compareTo(str2)<0))
//         //     System.out.println("it is less than str 2");
//         // if(str.compareTo(str2)>0)
//         //     System.out.println("str is greater than str2");
//         // char ch = str2.charAt(5);
//         //     System.out.println(ch);
//         // int x = str2.indexOf("t");
//         //     System.out.println(x);
//         // int x1 = str2.lastIndexOf("t");
//         //     System.out.println(x1);
//         //     String substr;
//         //     substr = str.substring(4,13);
//         //     System.out.println(substr);
//             String [][] number = {
//                 {"amarachi","080232"},
//                 {"victor","080132"},
//                 {"amarachi","080432"},
//                 {"amarachi","080232"},
//                 {"amarac","080232"}
//             };
//             for (String y[] : number) {
//                 for (String var : y) {
//                     if (var.equals(args[0])) {
//                         System.out.println("it is"+ var+" "+y);
//                         break;
//                     }
//                 }
//             }
//             for (int i = 0; i < number.length; i++) {
//                 for (int j = 0; j < number[0].length; j++) {
//                     String name = args[0];
//                     if(number[i][j].equals(name)){
//                         System.out.println("name has been found:   " + number[i][j+1]);
//                         break;
//                     }
                    
//                 }
//             }
//            String msg = "This is a Test";
//            String encmsg = "";
//            String decmsg = "";
//            String key = "abcdefgi";
//            int j =0;

//            for (int i = 0; i < msg.length(); i++) {
//                encmsg = encmsg + (char) (msg.charAt(i) ^ key.charAt(j));
//                j++;
//                if (j == 8) {
//                    j =0;
//                }
//            }
//            System.out.println(encmsg);
//            for (int i = 0; i < msg.length(); i++) {
//             decmsg = decmsg + (char) (encmsg.charAt(i) ^ key.charAt(j));
//                 j++;
//                if (j == 8) {
//                    j =0;
//                }
//             }
//             System.out.print(decmsg);
//             byte ch = -16;
//                  System.out.println();
//                 for (int i = 256; i > 0; i=i/2) {
//                     if (((byte)ch&i) !=0) {
//                         System.out.print(1+" ");
//                     } else {
//                         System.out.print(0+" ");
//                     }    
//                 }
//             ShowBits a = new ShowBits(8);
//             ShowBits b = new ShowBits(32);
//             ShowBits c = new ShowBits(64);
            
//             a.show(90);
//             b.show(200);
//             c.show(40095686);
//             int arrai3[] = new int[5];
//             int i = 1;
//             for (int x : arrai3) {
//                 System.out.println(x+=i);
//                 i++;
//             }
            
//         }
        
// }
// class FailSoft {
//     private int a[];
//     private int errval;
//     public int length;
//     FailSoft(int val){
//         errval = val;
//     }
    
//     Class<a[]> indexOk() {
//         boolean condition;
// 		if (condition) return a[];
//         return errval;
//     }

//     public boolean put(int index, int val){
//         if (length !=0 & length >index) return true;
//         return false;
//     }
//     public int get(int index){
//         if (indexOk()) {
            
//         }
//     }

//     private boolean indexOk() {
//         return false;
//     }
// }
// class ShowBits {
//     long numsbit;

//         ShowBits(long n){
//             numsbit = n;
//         }
//         void show(long val){
//             long mask = 1;
//             mask <<= (numsbit-1);
//             int spacer = 0;

//                 for (; mask != 0; mask>>>= 1) {
//                     if ((mask&val)==0) {
//                         System.out.print("0");
//                     } else {
//                         System.out.print("1");
//                     }
//                     spacer++;
//                     if (spacer % 8 == 0) {
//                         System.out.print(" ");
//                         spacer = 0;
//                     }
//                 }
//             System.out.println();
//         }
// }
// // class Queue {
// //     char q[];
// //     int getloc;
// //     int putloc;
// //     Queue(int size) {
// //         q = new char[size];
// //         putloc = getloc = 0;
// //     }

// //     void put(char ch){
// //         if(putloc == q.length){
// //             System.out.println("The Queue is full");
// //             return;
// //         }
// //         q[putloc++] = ch;
// //     }
// //     char get(){
// //         if(getloc == putloc){
// //             System.out.println("The Queue is empty");
// //             return (char) 0;
// //         }
// //         return (char) q[getloc++];
// //     }   
// // }
// // class Vehicle{
// //     // int passengers;
// //     // int mpg;
// //     // int fuelcap;
// //     // double fuelNeeded(int miles) {
// //     //     return (double) miles/mpg;
// //     // }
// //     // Vehicle(int p, int m, int f){
// //     //     passengers = p;
// //     //     mpg = m;
// //     //     fuelcap = f;
// //     // }
// // }
// // class create{
// //     // int i;
// //     // create(int x){
// //     //     i = x;
// //     // }
// //     // protected void finalize() {
// //     //     System.out.print("the object is ablut to be recycled " + i);
// //     // }
// //     // void generator(int i){
// //     //     create ob = new create(i);
// //     // }
// // }
// // class ChkNum {
// //     // int no;
// //     // boolean isEven(int x){
// //     //     if ((x%2)==0)   return true;
// //     //     else return false;
// //     // }
// //     }

// // class Help3 {
// //     //   char choice, ignore, what;  // The choice variable will hold the character entered
// //     //   // infinite loop
// //     // void isValid() {
// //     //     do {
// //     //         // Display menu | Choose control statement for which to show syntax
// //     //         System.out.println("Help on: \n 1. if \n 2. switch\n 3. for\n 4. while\n 5. do-while\n 6. break\n 7. continue");
// //     //         System.out.println("Choose one (q to quit) ");
    
// //     //         // Get user selection
// //     //         choice = (char) System.in.read();
    
// //     //         do {
// //     //           ignore = (char) System.in.read();
// //     //         } while (ignore != '\n');
    
// //     //       } while (choice < '1' | choice > '5' & choice != 'q');
// //     // }
        
// //     // //**********************************************
// //     // void helpOn() {
// //     //     switch (what) {
// //     //         // IF syntax
// //     //         case '1':
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The if control statement:\n");
// //     //           System.out.println("if (condition) statement\nelse statement");
// //     //           System.out.println("**************************\n");
// //     //           break;
// //     //         // SWITCH syntax
// //     //         case '2':
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The switch control statement:\n");
// //     //           System.out.println("switch (expression) {\n case constant: statement sequence\nbreak;\n...}");
// //     //           System.out.println("**************************\n");
// //     //           break;
// //     //         // FOR syntax
// //     //         case '3':
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The for loop:\n");
// //     //           System.out.println("for (initialization; condition; iteration)");
// //     //           System.out.println("\t statement;");
// //     //           break;
// //     //         // WHILE syntax
// //     //         case '4':
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The while loop:\n");
// //     //           System.out.println("while (condition) statement;");
// //     //           break;
// //     //         // DO-WHILE Syntax
// //     //         case '5':
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The do-while loop:\n");
// //     //           System.out.println("do {\n statement");
// //     //           System.out.println("while (condition);");
// //     //           break;
// //     //         case '6':
// //     //         // BREAK syntax
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The break:\n");
// //     //           System.out.println("break; or break label;");
// //     //           break;
// //     //         // COntinue Syntax
// //     //         case '7':
// //     //           System.out.println("**************************\n");
// //     //           System.out.println("The continue:\n");
// //     //           System.out.println("continue; or continue label;");
// //     //           break;
        
// //     //     if (choice == 'q') break;
// //     //     }
// //     // }
// //     }
// // }