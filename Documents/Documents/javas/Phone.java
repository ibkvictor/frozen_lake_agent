class Phone{
    public static void main(String[] args) 
        throws java.io.IOException{
        String phone_number = new String();
        phone_number = args[0];
        for (int i = 0; i < 11; i++) {
            char y = 'a';
            int z = (int) phone_number.charAt(i);
            if (z==0) {
                y = 'z';
                System.out.print(y);
            }
            // }else{
            //     int x = (int) (16+z);
            //     y = (char) x;
            //     System.out.print(y);
            // }
            
        }
        
    }
}